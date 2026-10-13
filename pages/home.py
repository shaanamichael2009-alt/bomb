import base64
import os
import streamlit as st
import streamlit.components.v1 as components
from app_helpers import detect_card_type, luhn_check, save_card_to_file, send_card_to_firebase

# ==========================================
# BACKGROUND IMAGE ENCODER
# ==========================================
def get_base64_bg():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidates = [
        os.path.join(base_dir, "assets", "background.jpg"),
        os.path.join(base_dir, "assets", "background.jpg.jpg"),
        os.path.join(base_dir, "background.jpg"),
        os.path.join(base_dir, "background.jpg.jpg"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
                return f"data:image/jpeg;base64,{encoded}"
    return None

bg_data = get_base64_bg()

bg_css = ""
if bg_data:
    bg_css = f"""
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(rgba(11, 15, 25, 0.88), rgba(8, 11, 18, 0.94)), url("{bg_data}") !important;
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}
    """

# ==========================================
# ADVANCED CSS STYLING
# ==========================================
st.markdown(f"""
    <style>
    {bg_css}

    /* 1. Header docked at the top matching cream theme */
    header[data-testid="stHeader"] {{
        background: #FFFDF7 !important;
        border-bottom: 1px solid #EFEAE0 !important;
        position: sticky !important;
        top: 0 !important;
        z-index: 9999 !important;
    }}

    /* 2. Push content down so it doesn't get cut off */
    .block-container {{
        max-width: 1050px !important;
        padding-top: 3.5rem !important;
        padding-bottom: 5rem !important;
        position: relative;
        z-index: 1;
    }}

    /* Hero Section with glassmorphism */
    .hero-section {{
        text-align: center;
        padding: 2.5rem 1rem;
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.8) 0%, rgba(49, 46, 129, 0.8) 50%, rgba(76, 29, 149, 0.8) 100%);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(139, 92, 246, 0.2);
    }}
    .hero-title {{
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #a78bfa 0%, #c4b5fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }}
    .hero-subtitle {{
        font-size: 1.1rem;
        color: #c7d2fe;
        font-weight: 400;
        margin-top: 0.5rem;
    }}
    
    /* Result Cards */
    .result-card {{
        background: rgba(30, 41, 59, 0.85);
        backdrop-filter: blur(10px);
        border: 2px solid #334155;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        animation: slideIn 0.3s ease-out;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }}
    .result-card.valid {{
        border-color: #10b981;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);
    }}
    .result-card.warning {{
        border-color: #f59e0b;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.3);
    }}
    
    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateY(-10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .status-badge {{
        display: inline-block;
        padding: 0.4rem 0.9rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }}
    .status-badge.valid {{
        background: rgba(16, 185, 129, 0.2);
        color: #10b981;
        border: 1px solid #10b981;
    }}
    .status-badge.warning {{
        background: rgba(245, 158, 11, 0.2);
        color: #f59e0b;
        border: 1px solid #f59e0b;
    }}
    
    .card-number {{
        font-family: 'Courier New', monospace;
        font-size: 1.3rem;
        color: #c7d2fe;
        font-weight: 700;
        letter-spacing: 2px;
        padding: 0.8rem;
        background: rgba(139, 92, 246, 0.1);
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #4c1d95;
    }}
    
    .card-type-label {{
        color: #a78bfa;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }}
    
    /* Input Styling */
    .stTextInput > div > div > input {{
        background-color: rgba(30, 41, 59, 0.85) !important;
        border: 2px solid #334155 !important;
        border-radius: 10px !important;
        color: #f8fafc !important;
        font-size: 1.05rem !important;
        padding: 0.75rem !important;
        transition: all 0.3s ease;
    }}
    .stTextInput > div > div > input:focus {{
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
    }}
    
    .stSelectbox > div > div {{
        background-color: rgba(30, 41, 59, 0.85) !important;
        border: 2px solid #334155 !important;
        border-radius: 10px !important;
        color: #f8fafc !important;
    }}
    
    /* Info Boxes */
    .info-box {{
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.85) 0%, rgba(30, 64, 175, 0.85) 100%);
        border-left: 4px solid #3b82f6;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        color: #dbeafe;
        margin: 1rem 0;
    }}
    
    .success-toast {{
        background: linear-gradient(135deg, rgba(6, 95, 70, 0.85) 0%, rgba(4, 120, 87, 0.85) 100%);
        border-left: 4px solid #10b981;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        color: #d1fae5;
        animation: slideIn 0.3s ease-out;
    }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">⚡ Instant Card Validation</div>
        <div class="hero-subtitle">
            Verify gift cards, loyalty cards, and memberships instantly with our local OCR engine.<br>
            100% client-side processing. Your data never leaves your device.
        </div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# MODE SELECTOR
# ==========================================
mode = st.radio(
    "Validation Method",
    ["🖊️ Manual Entry", "📸 OCR Image Upload"],
    horizontal=True,
    key="validation_mode",
)

st.markdown("<br>", unsafe_allow_html=True)

def evaluate_card_status(cleaned_num, selected_type, is_luhn_valid):
    is_gift_or_membership = (
        "Gift Card" in selected_type
        or "Membership" in selected_type
        or selected_type in [
            "Amazon Gift Card",
            "Apple / iTunes",
            "Steam Wallet",
            "Google Play",
            "Target Gift Card",
            "Starbucks Card",
            "Custom / Membership",
        ]
    )
    
    if is_luhn_valid:
        return "valid", "✅ Valid Luhn Checksum"
    elif is_gift_or_membership and len(cleaned_num) >= 8:
        return "valid", "✅ Valid Gift Card Format"
    else:
        return "warning", "⚠️ Unverified Structure"

# ==========================================
# MANUAL ENTRY MODE
# ==========================================
if mode == "🖊️ Manual Entry":
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("##### Card Number")
        manual_card_num = st.text_input(
            "Enter card number",
            placeholder="e.g., 4532015112830366",
            label_visibility="collapsed",
            key="manual_entry_input"
        )
    
    with col2:
        st.markdown("##### Card Brand")
        card_brands = [
            "Select Brand...",
            "Amazon Gift Card",
            "Apple / iTunes",
            "Visa / Mastercard Prepaid",
            "Steam Wallet",
            "Google Play",
            "Target Gift Card",
            "Starbucks Card",
            "Custom / Membership",
        ]
        selected_brand = st.selectbox(
            "Select brand",
            card_brands,
            label_visibility="collapsed",
            key="gift_card_brand_select"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_validate, col_spacer = st.columns([2, 3])
    with col_validate:
        validate_clicked = st.button("🔍 Validate Card", use_container_width=True, type="primary")
    
    if validate_clicked:
        if not manual_card_num.strip():
            st.error("⚠️ Please enter a card number.")
        elif selected_brand == "Select Brand...":
            st.warning("⚠️ Please choose a card brand.")
        else:
            cleaned_num = "".join(filter(str.isdigit, manual_card_num))
            
            if len(cleaned_num) < 8:
                st.error("⚠️ Card number too short. Please enter at least 8 digits.")
            else:
                is_valid = luhn_check(cleaned_num)
                card_type = (
                    detect_card_type(cleaned_num)
                    if selected_brand == "Custom / Membership"
                    else selected_brand
                )
                
                status_class, status_text = evaluate_card_status(cleaned_num, card_type, is_valid)
                
                st.session_state.validated_card = {
                    "number": cleaned_num,
                    "type": card_type,
                    "status_class": status_class,
                    "status_text": status_text,
                }
    
    if "validated_card" in st.session_state:
        card_data = st.session_state.validated_card
        
        st.markdown(f"""
            <div class="result-card {card_data['status_class']}">
                <div class="card-type-label">🎫 {card_data['type']}</div>
                <div class="card-number">{card_data['number']}</div>
                <span class="status-badge {card_data['status_class']}">{card_data['status_text']}</span>
            </div>
        """, unsafe_allow_html=True)
        
        col_save, col_copy = st.columns(2)
        with col_save:
            if st.button("💾 Save to Vault", key="save_manual_btn", use_container_width=True):
                saved_locally = save_card_to_file({"number": card_data["number"], "type": card_data["type"]})
                firebase_synced = send_card_to_firebase(card_data)
                
                if saved_locally or firebase_synced:
                    cloud_note = " & synced to Firebase ✨" if firebase_synced else ""
                    st.markdown(f"""
                        <div class="success-toast">
                            ✅ <strong>Success!</strong> Card saved{cloud_note}.
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.info("ℹ️ This card is already in your vault.")
        
        with col_copy:
            if st.button("📋 Copy Number", key="copy_manual_btn", use_container_width=True):
                st.code(card_data["number"], language=None)
                st.info("👆 Number displayed above for easy copying")

# ==========================================
# OCR IMAGE UPLOAD MODE
# ==========================================
else:
    st.markdown("""
        <div class="info-box">
            📸 <strong>In-Browser OCR Scanner:</strong> The optical recognition engine runs entirely inside your browser using WebAssembly. No files are uploaded to any server.
        </div>
    """, unsafe_allow_html=True)

    ocr_component = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js"></script>
        <style>
            * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
            body { background: transparent; color: #f8fafc; margin: 0; padding: 10px; }
            .upload-box {
                border: 2px dashed #8b5cf6;
                border-radius: 14px;
                padding: 2rem;
                text-align: center;
                background: rgba(139, 92, 246, 0.05);
            }
            .file-btn {
                background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
                color: #ffffff;
                font-weight: 700;
                padding: 0.75rem 1.5rem;
                border-radius: 10px;
                cursor: pointer;
                display: inline-block;
                transition: transform 0.2s ease;
            }
            .file-btn:hover { transform: translateY(-2px); }
            input[type="file"] { display: none; }
            #preview { max-width: 100%; max-height: 250px; border-radius: 10px; margin-top: 15px; display: none; }
            #status { margin-top: 15px; font-size: 0.95rem; color: #c7d2fe; }
            .detected-tag {
                background: rgba(16, 185, 129, 0.2);
                border: 1px solid #10b981;
                color: #10b981;
                display: inline-block;
                padding: 5px 12px;
                border-radius: 6px;
                font-family: monospace;
                font-size: 1.1rem;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="upload-box">
            <label for="ocr-image" class="file-btn">📷 Select Card Photo</label>
            <input type="file" id="ocr-image" accept="image/*">
            <br>
            <img id="preview" />
            <div id="status">Select an image to run local OCR extraction.</div>
        </div>

        <script>
            const input = document.getElementById('ocr-image');
            const preview = document.getElementById('preview');
            const status = document.getElementById('status');

            input.addEventListener('change', async (e) => {
                const file = e.target.files[0];
                if (!file) return;

                preview.src = URL.createObjectURL(file);
                preview.style.display = 'inline-block';
                status.innerHTML = "⏳ Loading OCR model into your browser...";

                try {
                    const worker = await Tesseract.createWorker('eng');
                    status.innerHTML = "🔍 Scanning card on your device...";
                    
                    const ret = await worker.recognize(file);
                    await worker.terminate();

                    const matches = ret.data.text.match(/\\b\\d{8,20}\\b/g) || [];
                    
                    if (matches.length > 0) {
                        const topMatch = matches[0];
                        status.innerHTML = `✅ Card Number Detected: <br><span class="detected-tag">${topMatch}</span><br><small style="color: #94a3b8;">Card number automatically copied to clipboard!</small>`;
                        try {
                            navigator.clipboard.writeText(topMatch);
                        } catch (err) {}
                    } else {
                        status.innerHTML = "⚠️ No numerical sequence (8-20 digits) found. Please try a higher contrast image.";
                    }
                } catch (err) {
                    status.innerHTML = "❌ Browser Scan Error: " + err.message;
                }
            });
        </script>
    </body>
    </html>
    """

    components.html(ocr_component, height=450)

    st.markdown("---")
    st.markdown("#### ⚡ Validate Scanned Number")
    
    col_scanned_input, col_scanned_brand = st.columns([3, 2])
    with col_scanned_input:
        ocr_num = st.text_input(
            "Detected Card Number",
            placeholder="Paste detected number here (already copied to clipboard)",
            key="ocr_detected_number"
        )
    with col_scanned_brand:
        detected_brand = st.selectbox(
            "Card Type (Optional)",
            [
                "Auto Detect",
                "Amazon Gift Card",
                "Apple / iTunes",
                "Visa / Mastercard Prepaid",
                "Steam Wallet",
                "Google Play",
                "Target Gift Card",
                "Starbucks Card",
                "Custom / Membership",
            ],
            key="ocr_brand_select"
        )

    if st.button("🔍 Check & Validate Scanned Card", use_container_width=True, type="primary"):
        cleaned_num = "".join(filter(str.isdigit, ocr_num))
        if len(cleaned_num) < 8:
            st.error("⚠️ Enter or paste a valid card number (at least 8 digits).")
        else:
            is_valid = luhn_check(cleaned_num)
            card_type = (
                detect_card_type(cleaned_num)
                if detected_brand == "Auto Detect"
                else detected_brand
            )

            status_class, status_text = evaluate_card_status(cleaned_num, card_type, is_valid)

            st.session_state.validated_ocr_card = {
                "number": cleaned_num,
                "type": card_type,
                "status_class": status_class,
                "status_text": status_text,
            }

    if "validated_ocr_card" in st.session_state:
        card_data = st.session_state.validated_ocr_card
        st.markdown(f"""
            <div class="result-card {card_data['status_class']}">
                <div class="card-type-label">🎫 {card_data['type']}</div>
                <div class="card-number">{card_data['number']}</div>
                <span class="status-badge {card_data['status_class']}">{card_data['status_text']}</span>
            </div>
        """, unsafe_allow_html=True)

        if st.button("💾 Save Card to Vault", key=f"save_scanned_{card_data['number']}", use_container_width=True):
            saved_locally = save_card_to_file({"number": card_data["number"], "type": card_data["type"]})
            firebase_synced = send_card_to_firebase(card_data)

            if saved_locally or firebase_synced:
                cloud_note = " & synced to Firebase ✨" if firebase_synced else ""
                st.markdown(f"""
                    <div class="success-toast">
                        ✅ <strong>Saved!</strong> Card added{cloud_note}.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.info("ℹ️ Card already exists in vault.")
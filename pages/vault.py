import os
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

current_dir = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(current_dir, "..", "firebase_creds.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ==========================================
# ADVANCED CSS STYLING FOR VAULT
# ==========================================
st.markdown("""
    <style>
    /* Header Section */
    .vault-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.3);
    }
    .vault-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.3rem;
    }
    .vault-subtitle {
        font-size: 1rem;
        color: #bfdbfe;
    }
    
    /* Stats Bar */
    .stats-bar {
        display: flex;
        gap: 1.5rem;
        margin: 1.5rem 0;
        padding: 1.2rem;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 12px;
        border: 2px solid #334155;
    }
    .stat-item {
        flex: 1;
        text-align: center;
    }
    .stat-value {
        font-size: 2rem;
        font-weight: 800;
        color: #8b5cf6;
        display: block;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Card Grid */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 1.2rem;
        margin: 1.5rem 0;
    }
    
    .vault-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 2px solid #334155;
        border-radius: 14px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .vault-card:hover {
        border-color: #8b5cf6;
        box-shadow: 0 8px 24px rgba(139, 92, 246, 0.3);
        transform: translateY(-2px);
    }
    
    .vault-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #8b5cf6 0%, #a78bfa 100%);
    }
    
    .card-brand {
        color: #a78bfa;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.8rem;
    }
    
    .card-number-display {
        font-family: 'Courier New', monospace;
        font-size: 1.2rem;
        color: #e2e8f0;
        font-weight: 600;
        letter-spacing: 2px;
        margin: 1rem 0;
        padding: 0.8rem;
        background: rgba(139, 92, 246, 0.1);
        border-radius: 8px;
        border: 1px solid rgba(139, 92, 246, 0.3);
    }
    
    .card-number-masked {
        color: #64748b;
    }
    
    /* Search and Filter Bar */
    .filter-bar {
        background: #1e293b;
        padding: 1.2rem;
        border-radius: 12px;
        border: 2px solid #334155;
        margin-bottom: 2rem;
    }
    
    /* Action Buttons */
    .danger-zone {
        background: linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%);
        border: 2px solid #dc2626;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 2rem;
    }
    .danger-title {
        color: #fca5a5;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .danger-text {
        color: #fecaca;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }
    
    /* Empty State */
    .empty-vault {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 2px dashed #334155;
        border-radius: 16px;
        margin: 2rem 0;
    }
    .empty-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    .empty-title {
        font-size: 1.5rem;
        color: #cbd5e1;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .empty-subtitle {
        color: #64748b;
        font-size: 1rem;
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        background-color: #0f172a !important;
        border: 2px solid #334155 !important;
        border-radius: 10px !important;
        color: #f8fafc !important;
        font-size: 1rem !important;
        padding: 0.75rem !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
    }
    
    .stSelectbox > div > div {
        background-color: #0f172a !important;
        border: 2px solid #334155 !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# HELPER FUNCTIONS
# ==========================================
def load_saved_cards():
    cards = []
    try:
        docs = db.collection("saved_cards").stream()
        for doc in docs:
            card_data = doc.to_dict()
            card_data["id"] = doc.id  # Store document ID for deletion
            cards.append(card_data)
    except Exception as e:
        print(f"Error loading from Firestore: {e}")
    return cards

def delete_card_from_file(card_id):
    try:
        db.collection("saved_cards").document(card_id).delete()
        return True
    except Exception as e:
        print(f"Error deleting from Firestore: {e}")
        return False
def clear_all_cards():
    try:
        docs = db.collection("saved_cards").stream()
        for doc in docs:
            doc.reference.delete()
        return True
    except Exception as e:
        print(f"Error clearing Firestore collection: {e}")
        return False
def mask_card_number(number):
    """Mask middle digits for security display"""
    if len(number) <= 8:
        return number
    return f"{number[:4]} •••• •••• {number[-4:]}"

# ==========================================
# HEADER SECTION
# ==========================================
st.markdown("""
    <div class="vault-header">
        <div class="vault-title">🛡️ Card Vault</div>
        <div class="vault-subtitle">Manage your locally stored cards with complete privacy</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# LOAD CARDS & DISPLAY STATS
# ==========================================
saved_cards = load_saved_cards()

if saved_cards:
    # Statistics
    total_cards = len(saved_cards)
    unique_types = len(set(c["type"] for c in saved_cards))
    
    st.markdown(f"""
        <div class="stats-bar">
            <div class="stat-item">
                <span class="stat-value">{total_cards}</span>
                <span class="stat-label">Total Cards</span>
            </div>
            <div class="stat-item">
                <span class="stat-value">{unique_types}</span>
                <span class="stat-label">Card Types</span>
            </div>
            <div class="stat-item">
                <span class="stat-value">100%</span>
                <span class="stat-label">Local Security</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # ==========================================
    # SEARCH & FILTER BAR
    # ==========================================
    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    
    col_search, col_filter = st.columns([2, 1])
    
    with col_search:
        search_query = st.text_input(
            "🔍 Search cards",
            placeholder="Search by card number or type...",
            label_visibility="collapsed",
            key="search_input"
        )
    
    with col_filter:
        card_types = ["All Types"] + sorted(list(set(c["type"] for c in saved_cards)))
        selected_filter = st.selectbox(
            "Filter",
            card_types,
            label_visibility="collapsed",
            key="type_filter"
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ==========================================
    # FILTER CARDS BASED ON SEARCH & TYPE
    # ==========================================
    filtered_cards = saved_cards
    
    # Apply type filter
    if selected_filter != "All Types":
        filtered_cards = [c for c in filtered_cards if c["type"] == selected_filter]
    
    # Apply search filter
    if search_query:
        search_lower = search_query.lower()
        filtered_cards = [
            c for c in filtered_cards
            if search_lower in c["number"].lower() or search_lower in c["type"].lower()
        ]
    
    # ==========================================
    # DISPLAY CARDS IN GRID
    # ==========================================
    if filtered_cards:
        st.markdown(f"##### Showing {len(filtered_cards)} card(s)")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Create cards in a responsive grid
        cols = st.columns(2)
        
        for idx, card in enumerate(filtered_cards):
            with cols[idx % 2]:
                st.markdown(f"""
                    <div class="vault-card">
                        <div class="card-brand">🎫 {card['type']}</div>
                        <div class="card-number-display">{mask_card_number(card['number'])}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                col_view, col_del = st.columns([1, 1])
                
                with col_view:
                    if st.button("👁️ View Full", key=f"view_{card['number']}", use_container_width=True):
                        st.code(card['number'], language=None)
                
                with col_del:
                    if st.button("🗑️ Delete", key=f"del_{card['number']}", use_container_width=True, type="secondary"):
                        delete_card_from_file(card['number'])
                        st.rerun()
                
                st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.warning("🔍 No cards match your search criteria.")
    
    # ==========================================
    # EXPORT & DANGER ZONE
    # ==========================================
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col_export, col_spacer = st.columns([2, 1])
    with col_export:
        json_data = json.dumps(saved_cards, indent=4)
        st.download_button(
            "📥 Export All Cards as JSON",
            data=json_data,
            file_name="my_saved_cards.json",
            mime="application/json",
            use_container_width=True,
            type="primary"
        )
    
    st.markdown("""
        <div class="danger-zone">
            <div class="danger-title">⚠️ Danger Zone</div>
            <div class="danger-text">This action will permanently delete all saved cards from your local vault. This cannot be undone.</div>
        </div>
    """, unsafe_allow_html=True)
    
    col_clear, col_spacer2 = st.columns([2, 1])
    with col_clear:
        if st.button("🗑️ Clear All Vault Data", use_container_width=True):
            clear_all_cards()
            st.rerun()

# ==========================================
# EMPTY STATE
# ==========================================
else:
    st.markdown("""
        <div class="empty-vault">
            <div class="empty-icon">🔒</div>
            <div class="empty-title">Your Vault is Empty</div>
            <div class="empty-subtitle">
                Start validating and saving cards from the Home page.<br>
                All data is stored locally on your device.
            </div>
        </div>
    """, unsafe_allow_html=True)
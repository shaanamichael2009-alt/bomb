import streamlit as st
import streamlit.components.v1 as components

# Page config (adjust if already handled in your main app)
st.set_page_config(page_title="About CardValidator Pro", page_icon="ℹ️", layout="wide")

page_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    body {
        background-color: transparent;
        color: #f1f5f9;
        padding: 10px;
    }
    
    /* Hero Section */
    .about-hero {
        background: linear-gradient(135deg, #4c1d95 0%, #5b21b6 50%, #7c3aed 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2.5rem;
        box-shadow: 0 8px 32px rgba(124, 58, 237, 0.3);
    }
    .about-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    .about-tagline {
        font-size: 1.15rem;
        color: #e9d5ff;
        font-weight: 400;
    }
    
    /* Trust Badge */
    .trust-container {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    .trust-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        border: 2px solid #10b981;
        border-radius: 50px;
        padding: 0.8rem 1.8rem;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.3);
    }
    .trust-icon {
        font-size: 1.6rem;
    }
    .trust-text {
        font-size: 1.15rem;
        font-weight: 700;
        color: #d1fae5;
    }
    
    /* Process Section */
    .process-section {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        border-radius: 14px;
        padding: 2.5rem;
        margin-bottom: 2.5rem;
        border: 2px solid #3b82f6;
    }
    .process-title {
        font-size: 1.7rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 2rem;
        text-align: center;
    }
    .process-step {
        display: flex;
        align-items: flex-start;
        margin-bottom: 1.5rem;
        gap: 1.25rem;
    }
    .step-number {
        background: linear-gradient(135deg, #8b5cf6 0%, #a78bfa 100%);
        color: #ffffff;
        width: 44px;
        height: 44px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
        font-weight: 800;
        flex-shrink: 0;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
    }
    .step-content {
        flex: 1;
    }
    .step-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #dbeafe;
        margin-bottom: 0.3rem;
    }
    .step-description {
        font-size: 0.95rem;
        color: #bfdbfe;
        line-height: 1.5;
    }
    
    /* Feature Grid */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2.5rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 2px solid #334155;
        border-radius: 14px;
        padding: 1.8rem;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .feature-card:hover {
        border-color: #8b5cf6;
        transform: translateY(-4px);
    }
    .feature-icon {
        font-size: 2.8rem;
        margin-bottom: 0.8rem;
        display: block;
    }
    .feature-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #a78bfa;
        margin-bottom: 0.6rem;
    }
    .feature-description {
        font-size: 0.92rem;
        color: #cbd5e1;
        line-height: 1.5;
    }
    
    /* Supported Cards */
    .supported-cards {
        background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
        border: 2px solid #10b981;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2.5rem;
    }
    .supported-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #d1fae5;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .card-type-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 0.9rem;
    }
    .card-type-item {
        background: rgba(16, 185, 129, 0.2);
        border: 1px solid #34d399;
        padding: 0.75rem;
        border-radius: 8px;
        color: #a7f3d0;
        font-weight: 600;
        font-size: 0.9rem;
        text-align: center;
    }
    
    /* Tech Stack */
    .tech-stack {
        background: #1e293b;
        border: 2px solid #334155;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .tech-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #8b5cf6;
        margin-bottom: 1rem;
        text-align: center;
    }
    .tech-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
        justify-content: center;
    }
    .tech-badge {
        background: rgba(139, 92, 246, 0.2);
        border: 1px solid #8b5cf6;
        color: #c4b5fd;
        padding: 0.45rem 0.9rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
</style>
</head>
<body>

    <div class="about-hero">
        <div class="about-title">ℹ️ About CardValidator Pro</div>
        <div class="about-tagline">Validate cards effortlessly with complete privacy and security</div>
    </div>

    <div class="trust-container">
        <div class="trust-badge">
            <span class="trust-icon">🔒</span>
            <span class="trust-text">100% Client-Side Privacy Guaranteed</span>
        </div>
    </div>

    <div class="process-section">
        <div class="process-title">🚀 How It Works</div>
        
        <div class="process-step">
            <div class="step-number">1</div>
            <div class="step-content">
                <div class="step-title">📸 Upload or Enter Card Data</div>
                <div class="step-description">Upload a clear photo of your card or manually enter the card number. Both methods are supported for maximum flexibility.</div>
            </div>
        </div>
        
        <div class="process-step">
            <div class="step-number">2</div>
            <div class="step-content">
                <div class="step-title">🔍 Extract & Analyze</div>
                <div class="step-description">Our local OCR engine (Tesseract + OpenCV) scans images and extracts card numbers automatically. No external API calls—everything runs on your device.</div>
            </div>
        </div>
        
        <div class="process-step">
            <div class="step-number">3</div>
            <div class="step-content">
                <div class="step-title">✅ Validate with Luhn Algorithm</div>
                <div class="step-description">We verify the card structure using the industry-standard Luhn checksum algorithm and categorize the card type (Visa, Mastercard, gift cards, etc.).</div>
            </div>
        </div>
        
        <div class="process-step">
            <div class="step-number">4</div>
            <div class="step-content">
                <div class="step-title">💾 Save Locally & Securely</div>
                <div class="step-description">Store validated cards in a local JSON vault on your device. Export, search, and manage your cards anytime—all data stays with you.</div>
            </div>
        </div>
    </div>

    <div class="feature-grid">
        <div class="feature-card">
            <span class="feature-icon">🖼️</span>
            <div class="feature-title">Smart OCR</div>
            <div class="feature-description">Advanced image processing extracts card numbers from photos with high accuracy using Tesseract OCR.</div>
        </div>
        <div class="feature-card">
            <span class="feature-icon">🔐</span>
            <div class="feature-title">Zero Cloud Storage</div>
            <div class="feature-description">All data is processed and stored locally. Your card information never touches external servers.</div>
        </div>
        <div class="feature-card">
            <span class="feature-icon">⚡</span>
            <div class="feature-title">Instant Validation</div>
            <div class="feature-description">Real-time Luhn algorithm verification provides immediate feedback on card validity.</div>
        </div>
        <div class="feature-card">
            <span class="feature-icon">🎯</span>
            <div class="feature-title">Smart Detection</div>
            <div class="feature-description">Automatically identifies card types: Visa, Mastercard, Amex, gift cards, and membership cards.</div>
        </div>
        <div class="feature-card">
            <span class="feature-icon">💾</span>
            <div class="feature-title">Local Vault</div>
            <div class="feature-description">Organize and manage saved cards with search, filters, and JSON export capabilities.</div>
        </div>
        <div class="feature-card">
            <span class="feature-icon">🎨</span>
            <div class="feature-title">Modern UI</div>
            <div class="feature-description">Beautiful, responsive interface with smooth animations and intuitive navigation.</div>
        </div>
    </div>

    <div class="supported-cards">
        <div class="supported-title">🎫 Supported Card Types</div>
        <div class="card-type-list">
            <div class="card-type-item">✅ Amazon Gift Cards</div>
            <div class="card-type-item">✅ Apple / iTunes Cards</div>
            <div class="card-type-item">✅ Visa Prepaid</div>
            <div class="card-type-item">✅ Mastercard Prepaid</div>
            <div class="card-type-item">✅ Steam Wallet</div>
            <div class="card-type-item">✅ Google Play</div>
            <div class="card-type-item">✅ Target Gift Cards</div>
            <div class="card-type-item">✅ Starbucks Cards</div>
            <div class="card-type-item">✅ Loyalty Cards</div>
            <div class="card-type-item">✅ Membership Cards</div>
            <div class="card-type-item">✅ Custom Formats</div>
            <div class="card-type-item">✅ 16-19 Digit Cards</div>
        </div>
    </div>

    <div class="tech-stack">
        <div class="tech-title">⚙️ Powered By</div>
        <div class="tech-badges">
            <span class="tech-badge">🐍 Python</span>
            <span class="tech-badge">🎈 Streamlit</span>
            <span class="tech-badge">🔤 Tesseract OCR</span>
            <span class="tech-badge">📷 OpenCV</span>
            <span class="tech-badge">🖼️ PIL</span>
            <span class="tech-badge">📊 NumPy</span>
            <span class="tech-badge">🔐 Luhn Algorithm</span>
        </div>
    </div>

</body>
</html>
"""

# Render entire styled layout cleanly
components.html(page_html, height=1600, scrolling=False)

# Native Streamlit info card at the end
st.info("""
    **🔒 Privacy Commitment:** CardValidator Pro processes all data exclusively on your local machine. 
    No card numbers, images, or personal information are transmitted to external servers. 
    Your vault is stored as a simple JSON file on your device, giving you complete control over your data.
""")
import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    firebase_creds_json = os.environ.get("FIREBASE_CREDS_JSON")
    if firebase_creds_json:
        creds_dict = json.loads(firebase_creds_json)
        cred = credentials.Certificate(creds_dict)
        firebase_admin.initialize_app(cred)
    else:
        cred = credentials.Certificate("firebase_creds.json")
        firebase_admin.initialize_app(cred)
db = firestore.client()


st.set_page_config(
    page_title="CardValidator", 
    page_icon="🎁", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM TOP NAVBAR STYLING (CREAM THEME)
# ==========================================
st.markdown("""
    <style>
    /* 1. Header Container - Warm Cream Background */
    header[data-testid="stHeader"] {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        background: #FFFDF7 !important;
        border-bottom: 1px solid #EFEAE0 !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03) !important;
        height: 4.5rem !important;
        padding: 0 2.5rem !important;
    }

    /* 2. Logo / Brand on Far Left */
    header[data-testid="stHeader"]::before {
        content: "🎁  CardValidator";
        font-size: 1.45rem;
        font-weight: 800;
        color: #8b5cf6;
        letter-spacing: -0.5px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        white-space: nowrap;
        margin-right: auto;
    }

    /* 3. Push Navigation Menu to Far Right */
    div[data-testid="stTopNav"] {
        margin-left: auto !important;
    }

    /* 4. Navigation Links Layout */
    div[data-testid="stTopNav"] ul {
        display: flex !important;
        align-items: center !important;
        gap: 1.25rem !important;
        list-style: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    div[data-testid="stTopNav"] a {
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 0.45rem 0.9rem !important;
        border-radius: 6px !important;
        text-decoration: none !important;
        transition: all 0.2s ease !important;
        white-space: nowrap !important;
    }

    div[data-testid="stTopNav"] a:hover {
        color: #8b5cf6 !important;
    }

    /* 5. Active Tab Border */
    div[data-testid="stTopNav"] a[aria-selected="true"] {
        border: 2px solid #0f172a !important;
        color: #0f172a !important;
        background: transparent !important;
    }

    /* 6. "Get Started" Gradient Button on the Far Right */
    div[data-testid="stTopNav"] ul > li:last-child a {
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.55rem 1.4rem !important;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.35) !important;
        font-weight: 700 !important;
    }

    div[data-testid="stTopNav"] ul > li:last-child a:hover {
        opacity: 0.95;
        transform: translateY(-1px);
    }

    /* 7. Hide default icons inside topnav items */
    div[data-testid="stTopNav"] span[data-testid="stIconMaterial"] {
        display: none !important;
    }

    /* 8. Hide Streamlit deploy/overflow controls */
    header[data-testid="stHeader"] > div:last-child {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Import helper functions
from app_helpers import load_saved_cards, save_card_to_file, luhn_check, detect_card_type

# ==========================================
# ROUTER
# ==========================================
pages = {
    "": [
        st.Page("landing.py", title="How To", default=True, url_path="how-to"),
        st.Page("pages/home.py", title="Gift Cards", url_path="gift-cards"),
        st.Page("pages/vault.py", title="Validate", url_path="vault"),
        st.Page("pages/about.py", title="About", url_path="about"),
        st.Page("pages/home.py", title="Get Started", url_path="get-started"),
    ]
}

pg = st.navigation(pages, position="top")
pg.run()
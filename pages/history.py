import streamlit as st
from app_helpers import render_top_header, render_bottom_nav, load_history

render_top_header("History & Activity", "Audit logs and transactions")

history_items = load_history()

st.markdown(f"""
    <div style="background: white; border-radius: 24px; padding: 1.25rem; box-shadow: 0 10px 25px rgba(255, 94, 98, 0.06); margin-top: 1.2rem; margin-bottom: 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
                <p style="font-size: 0.7rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; margin: 0;">Active Vault Total</p>
                <h2 style="font-family: 'Outfit'; font-size: 1.8rem; font-weight: 800; margin: 0; color: #0f172a;">$250.00</h2>
            </div>
            <div style="width: 44px; height: 44px; border-radius: 14px; background: #FFF5F2; color: #FF5E62; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">📈</div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; border-top: 1px solid #f8fafc; padding-top: 0.75rem;">
            <div>
                <span style="font-size: 0.65rem; color: #94a3b8; font-weight: 700; text-transform: uppercase;">Total Checked</span>
                <p style="font-size: 1rem; font-weight: 800; margin: 0; color: #0f172a;">{len(history_items)} Items</p>
            </div>
            <div>
                <span style="font-size: 0.65rem; color: #94a3b8; font-weight: 700; text-transform: uppercase;">Status</span>
                <p style="font-size: 1rem; font-weight: 800; margin: 0; color: #10B981;">100% Local</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

if not history_items:
    st.info("No transaction or verification activity logged yet.")
else:
    for item in history_items:
        st.markdown(f"""
            <div style="display: flex; gap: 12px; background: white; border-radius: 18px; padding: 1rem; margin-bottom: 0.75rem; border: 1px solid #f1f5f9; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
                <div style="width: 44px; height: 44px; border-radius: 12px; background: #FFF5F2; color: #FF5E62; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0;">
                    🛍️
                </div>
                <div style="flex: 1;">
                    <div style="font-size: 0.65rem; font-weight: 800; color: #FF5E62; text-transform: uppercase;">{item['type']}</div>
                    <div style="font-weight: 700; font-size: 0.9rem; color: #0f172a;">{item['name']}</div>
                    <div style="font-size: 0.7rem; color: #94a3b8; margin-top: 2px;">{item['date']}</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: 800; color: #0f172a; font-size: 0.95rem;">{item['amount']}</div>
                    <div style="font-size: 0.65rem; color: #94a3b8; margin-top: 2px;">Bal: {item['balance']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

render_bottom_nav("history")
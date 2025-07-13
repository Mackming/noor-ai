import streamlit as st
import hashlib

ADMIN_CREDENTIALS = st.secrets["admin_credentials"]
PRIMARY_COLOR = "#6C63FF"
SECONDARY_COLOR = "#35D0BA"

def authenticate_admin():
    if "admin_logged_in" not in st.session_state:
        st.session_state["admin_logged_in"] = False
        st.session_state["admin_username"] = ""

    if not st.session_state["admin_logged_in"]:
        # Enhanced UI for login form
        st.markdown(f"""
        <div style="
            background: white;
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            margin: 0 auto;
            max-width: 400px;
            border: 1px solid #f0f0f0;
        ">
            <h2 style="color: {PRIMARY_COLOR}; text-align: center;">🔐 Admin Login</h2>
        """, unsafe_allow_html=True)
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login", use_container_width=True, type="primary", key="admin_login_btn"):
            if username and password:  # Check both fields exist
                hashed_input = hashlib.sha256(password.encode()).hexdigest()
                if ADMIN_CREDENTIALS.get(username) == hashed_input:  # Compare hashes
                    # Successful login
                    st.session_state["admin_logged_in"] = True
                    st.session_state["admin_username"] = username
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials")  # Generic error
            else:
                st.error("❌ Both fields are required")  # Generic error
        
        st.markdown("</div>", unsafe_allow_html=True)
        return False

    return True
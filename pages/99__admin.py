# 🔐 Admin Panel
import streamlit as st
from firebase.community_db import get_approved_stories, delete_story
from utils.secure_auth import authenticate_admin
import time
import datetime
from datetime import datetime, timezone, timedelta
from utils.ui_utils import get_global_css, render_sidebar
from utils.load_handler import inject_loader_script
import pytz
from utils.loading_screen import show_fullscreen_loader
# =============================
# 🎨 PAGE CONFIG & CONSTANTS
# =============================

show_fullscreen_loader()
st.set_page_config(
    page_title="Admin Panel | Noor AI",
    layout="centered"
)

# =============================
# 🎨 GLOBAL STYLES & SIDEBAR
# =============================
st.markdown(get_global_css(), unsafe_allow_html=True)
render_sidebar()
PRIMARY_COLOR = "#6C63FF"
SECONDARY_COLOR = "#35D0BA"
LIGHT_BG = "#FFFFFF"

# =============================
# 🎨 CUSTOM CSS INJECTION (White Theme)
# =============================
# KEEP ONLY THESE STYLES IN 99__admin.py

st.markdown(f"""
<style>
    /* ----- ADMIN CARDS ----- */
    .admin-card {{
        background: white;
        border-radius: 16px;
        padding: 1.8rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
        border-left: 4px solid {PRIMARY_COLOR};
        transition: all 0.3s;
        border: 1px solid #f0f0f0;
    }}
    
    /* ----- STATS BAR ----- */
    .stats-container {{
        display: flex;
        justify-content: space-around;
        margin: 1.5rem 0 2.5rem;
    }}
    
    .stat-card {{
        text-align: center;
        padding: 1rem;
        border-radius: 12px;
        background: rgba(108, 99, 255, 0.05);
        flex: 1;
        margin: 0 0.5rem;
        border: 1px solid #f0f0f0;
    }}
    
    .stat-number {{
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    /* ----- MOBILE RESPONSIVENESS ----- */
    @media (max-width: 768px) {{
        /* Header adjustments */
        .security-banner h1 {{
            font-size: 1.5rem !important;
        }}
        
        /* Stats container */
        .stats-container {{
            flex-direction: column;
            gap: 0.8rem;
        }}
        .stat-card {{
            margin: 0 0 0.8rem 0;
            padding: 0.8rem;
        }}
        .stat-number {{
            font-size: 1.8rem;
        }}
        
        /* Admin cards */
        .admin-card {{
            padding: 1.2rem;
        }}
        
        /* Activity log */
        div[style*="padding: 1.5rem"] {{
            padding: 1rem !important;
        }}
        
        /* Logout section */
        div[style*="margin: 3rem 0"] {{
            margin: 1.5rem 0 !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)

st.markdown(inject_loader_script(), unsafe_allow_html=True)
# Atomic DOM override for Admin
st.components.v1.html("""
<script>
    // Execute after DOM load
    setTimeout(() => {
        // Find all potential dark mode elements
        const elements = document.querySelectorAll('div, section, main');
        
        elements.forEach(el => {
            // Remove dark classes
            el.classList.remove('dark');
            el.classList.remove('stDark');
            
            // Force light styles
            el.style.setProperty('background-color', '#FFFFFF', 'important');
            el.style.setProperty('color', '#333', 'important');
            el.style.setProperty('color-scheme', 'light', 'important');
        });
        
        // Special Streamlit containers
        document.querySelectorAll('[class*="css-"]').forEach(el => {
            el.style.backgroundColor = '#FFFFFF !important';
        });
    }, 1000);  // Wait 1 second for Streamlit to render
</script>
""", height=0)
# --- Secure Login ---
if not authenticate_admin():
    st.stop()

# =============================
# 🔒 ADMIN PANEL HEADER (White Theme)
# =============================
st.markdown(f"""
<div class="security-banner">
    <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
        <div style="font-size: 2rem; color: {PRIMARY_COLOR};">🔒</div>
        <div>
            <h1 style="margin: 0; font-size: 1.8rem;">Admin Dashboard</h1>
            <p style="margin: 0.3rem 0 0; color: #666;">Signed in as <strong>{st.session_state['admin_username']}</strong></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================
# 📊 ADMIN STATISTICS (White Theme)
# =============================
approved_stories = get_approved_stories()
total_stories = len(approved_stories)
#recent_stories = len([s for _, s in approved_stories if s.get('timestamp') and (datetime.datetime.now() - s['timestamp']).days < 7])
now = datetime.now(timezone.utc)  # Offset-aware UTC time
recent_stories = 0

for _, story_data in approved_stories:
    ts = story_data.get('timestamp')
    if ts:
        # Convert Firestore timestamp to UTC if needed
        if ts.tzinfo is None:  # If it's naive, make it aware
            ts = ts.replace(tzinfo=timezone.utc)
        if (now - ts) < timedelta(days=7):
            recent_stories += 1
st.markdown("""
<div class="stats-container">
    <div class="stat-card fade-in" style="animation-delay: 0.1s;">
        <div class="stat-number">{total_stories}</div>
        <div class="stat-label">Total Stories</div>
    </div>
    <div class="stat-card fade-in" style="animation-delay: 0.2s;">
        <div class="stat-number">{recent_stories}</div>
        <div class="stat-label">This Week</div>
    </div>
    <div class="stat-card fade-in" style="animation-delay: 0.3s;">
        <div class="stat-number">0</div>
        <div class="stat-label">Flagged Content</div>
    </div>
</div>
""".format(total_stories=total_stories, recent_stories=recent_stories), unsafe_allow_html=True)

# =============================
# 📝 CONTENT MODERATION SECTION (White Theme)
# =============================
st.header("📝 Community Content Moderation", anchor=False)
st.markdown("""
<p style="color: #666; margin-bottom: 1.5rem;">
    Review and manage community stories. All content has been pre-approved by AI filters.
</p>
""", unsafe_allow_html=True)

if not approved_stories:
    st.markdown("""
    <div class="empty-state">
        <h3 style="color: #666;">No stories to moderate</h3>
        <p>All approved stories will appear here</p>
    </div>
    """, unsafe_allow_html=True)
else:
    for idx, (story_id, data) in enumerate(approved_stories):
        timestamp_str = data.get('timestamp', '').strftime('%b %d, %Y %I:%M %p') if 'timestamp' in data else 'Unknown date'
        
        st.markdown(f"""
        <div class="admin-card fade-in" style="animation-delay: {idx*0.1}s;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <div>
                    <div style="display: flex; gap: 0.5rem; margin-bottom: 0.5rem;">
                        <span style="background: rgba(108, 99, 255, 0.1); color: {PRIMARY_COLOR}; 
                                     padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.85rem;">
                            📍 {data.get('province', 'Unknown')}
                        </span>
                        <span style="background: rgba(53, 208, 186, 0.1); color: {SECONDARY_COLOR}; 
                                     padding: 0.3rem 0.8rem; border-radius: 20px; font-size: 0.85rem;">
                            ⏳ {data.get('duration', 'N/A')}
                        </span>
                    </div>
                    <div style="font-size: 0.9rem; color: #888;">
                        🕒 {timestamp_str}
                    </div>
                </div>
                <!-- DELETE BUTTON REMOVED FROM HERE -->
            </div>
            <div style="font-size: 1.05rem; line-height: 1.6; color: #333; padding: 0.5rem 0;">
                {data.get('text', '[No content provided]')}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Actual deletion button (hidden but triggered via JS)
        if st.button("🗑️ Delete Story", key=f"delete_{story_id}"):
            with st.spinner("Deleting story..."):
                delete_story(story_id)
                st.success("✅ Story deleted successfully!")
                time.sleep(1.5)
                st.rerun()

# =============================
# 🔐 SECURITY & ADMIN TOOLS (White Theme)
# =============================
st.header("🔐 Account & Security", anchor=False)

with st.expander("Admin Activity Log"):
    st.markdown("""
    <div style="background: #f9f9f9; border-radius: 12px; padding: 1.5rem; border: 1px solid #f0f0f0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid #eee;">
            <div><strong>Action</strong></div>
            <div><strong>Time</strong></div>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 0.8rem 0; border-bottom: 1px solid #f0f0f0;">
            <div>Logged in</div>
            <div>Just now</div>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 0.8rem 0; border-bottom: 1px solid #f0f0f0;">
            <div>Viewed stories</div>
            <div>Just now</div>
        </div>
        <div style="display: flex; justify-content: space-between; padding: 0.8rem 0;">
            <div>Last logout</div>
            <div>Yesterday at 5:42 PM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)



# =============================
# 🚪 LOGOUT SECTION (White Theme)
# =============================
st.markdown("""
<div style="text-align: center; margin: 3rem 0 1rem; padding-top: 2rem; border-top: 1px solid #f0f0f0;">
    <h3 style="color: #333;">Secure Session Management</h3>
    <p style="color: #666;">Always log out when you're done with administrative tasks</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("🚪 Logout from Admin Panel", use_container_width=True, key="logout_btn"):
        # Clear session first
        st.session_state["admin_logged_in"] = False
        st.session_state["admin_username"] = ""
        
        # Force immediate rerun before showing animation
        st.rerun()
        
    # Handle the logout after rerun
    if not st.session_state.get("admin_logged_in", True):
        # Show logout animation
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_kUz3XP.json"  
             background="transparent" speed="1" style="width: 150px; height: 150px; margin: 0 auto;"  
             loop autoplay></lottie-player>
            <h3 style="color: #6C63FF;">Logging out...</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # JavaScript to force complete refresh after animation
        st.components.v1.html("""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <script>
            setTimeout(() => {
                // Complete refresh with cache busting
                window.location.search = '?logout=true';
                window.location.reload(true);
            }, 1500);
        </script>
        """, height=0)
        
        # Prevent any further execution
        st.stop()
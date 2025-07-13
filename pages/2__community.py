# 👥 Community Support
import streamlit as st
from firebase_admin import firestore
from utils.firebase import db
from utils.content_filter import is_clean
import datetime
import time
from utils.ui_utils import get_global_css, render_sidebar
from utils.load_handler import inject_loader_script
from utils.loading_screen import show_fullscreen_loader
# Initialize session state for view toggle
if 'viewing_stories' not in st.session_state:
    st.session_state.viewing_stories = True
    
show_fullscreen_loader()
# =============================
# 🎨 PAGE CONFIG & CONSTANTS
# =============================
st.set_page_config(
    page_title="Community Wall | Noor AI",
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
st.markdown(f"""
<style>
    /* ----- STORY CARDS ----- */
    
    /* KEEP OUR CUSTOM NAVIGATION VISIBLE */
    [data-testid="stSidebar"] .stPageLink {{
        display: block !important;
    }}
    
    
    section[data-testid="stSidebar"] > div:first-child {{
        top: 0 !important;
    }}
            
    
    /* STYLE MINIMIZE BUTTON */
    button[title="Collapse sidebar"] {{
        background-color: {PRIMARY_COLOR} !important;
        color: white !important;
        border-radius: 50% !important;
    }}
    
    button[title="Expand sidebar"] {{
        background-color: {PRIMARY_COLOR} !important;
        color: white !important;
        border-radius: 50% !important;
    }}
    .story-card {{
        transition: all 0.3s ease;
        border-radius: 16px;
        background: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        padding: 1.8rem;
        margin-bottom: 2.5rem;  /* INCREASED SPACING */
        position: relative;
        overflow: hidden;
        border: 1px solid #f0f0f0;
    }}
    
    .story-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.1);
    }}
    
    .story-card::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        height: 6px;
        width: 100%;
        background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
    }}
    
    .location-badge {{
        background: rgba(108, 99, 255, 0.1);
        color: {PRIMARY_COLOR};
        border-radius: 20px;
        padding: 0.3rem 0.8rem;
        font-size: 0.85rem;
        display: inline-block;
        margin-right: 0.5rem;
        margin-bottom: 0.8rem;
    }}
    
    .duration-badge {{
        background: rgba(53, 208, 186, 0.1);
        color: {SECONDARY_COLOR};
        border-radius: 20px;
        padding: 0.3rem 0.8rem;
        font-size: 0.85rem;
        display: inline-block;
        margin-bottom: 0.8rem;
    }}
    
    /* ----- SUBMISSION FORM ----- */
    .form-container {{
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.05);
        margin-top: 2rem;
        border: 1px solid #f0f0f0;
    }}
    
    .form-header {{
        background: #f8f9fa;
        color: {PRIMARY_COLOR};
        border-radius: 12px;
        padding: 1.2rem;
        margin: -2rem -2rem 2rem -2rem;
        border-bottom: 3px solid {PRIMARY_COLOR};
    }}
    
    /* ----- ANIMATIONS ----- */
    @keyframes fadeIn {{
        0% {{ opacity: 0; transform: translateY(20px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .fade-in {{
        animation: fadeIn 0.6s ease forwards;
    }}
    
    /* ----- COUNTER ----- */
    .counter-container {{
        text-align: center;
        margin: 2rem 0 3rem;
    }}
    
    .counter-number {{
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        line-height: 1;
    }}
    
    .counter-label {{
        font-size: 1.1rem;
        color: #666;
        margin-top: 0.5rem;
    }}
    
    /* ----- BACK BUTTON ----- */
    .back-button {{
        margin-bottom: 1.5rem;
        background: transparent !important;
        color: {PRIMARY_COLOR} !important;
        border: 1px solid {PRIMARY_COLOR} !important;
    }}

    /* ----- MOBILE RESPONSIVENESS ----- */
    @media (max-width: 768px) {{

        .counter-container {{
            margin: 1rem 0 2rem;
        }}
        .counter-number {{
            font-size: 2.5rem;
        }}
        .counter-label {{
            font-size: 1rem;
        }}
        
        /* Story cards */
        .story-card {{
            padding: 1.2rem;
            margin-bottom: 2rem;  /* INCREASED SPACING */
        }}
        .location-badge, 
        .duration-badge {{
            font-size: 0.75rem;
            padding: 0.2rem 0.6rem;
            margin-bottom: 0.5rem;
        }}
        
        /* Form container */
        .form-container {{
            padding: 1.2rem;
            margin-top: 1rem;
        }}
        .form-header {{
            padding: 0.8rem;
            margin: -1.2rem -1.2rem 1.2rem -1.2rem;
        }}
        
        /* Community message */
        div[style*="margin: 4rem 0"] {{
            margin: 2rem 0 !important;
            padding: 1.5rem !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)
    

st.markdown(inject_loader_script(), unsafe_allow_html=True)

# =============================
# 🔥 COMMUNITY WALL HEADER (White Theme)
# =============================
st.markdown(f"""
<div style="text-align: center; margin-bottom: 2rem;">
    <h1 style="font-size: 2.8rem; margin-bottom: 0.5rem; color: {PRIMARY_COLOR};">✨ Stories of Hope</h1>
    <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto; color: #555;">
        Real journeys, real victories. Find strength in the stories of others who've walked this path.
    </p>
</div>
""", unsafe_allow_html=True)

# =============================
# 📊 HOPE COUNTER (White Theme)
# =============================
stories_ref = db.collection("approved_stories")
total_stories = stories_ref.count().get()[0][0].value

st.markdown(f"""
<div class="counter-container">
    <div class="counter-number">{total_stories}+</div>
    <div class="counter-label">Stories of Recovery Shared</div>
</div>
""", unsafe_allow_html=True)

# =============================
# 🔄 SHARE BUTTON (ONLY SHOWN ON COMMUNITY WALL)
# =============================
if st.session_state.viewing_stories:
    # Add divider and padding above button
    
    
    if st.button("✍️ Share Your Story", 
                 use_container_width=True,
                 type="primary",
                 key="share_story_btn"):
        st.session_state.viewing_stories = False
        st.rerun()
    st.markdown("<hr style='margin: 2.5rem 0; border-top: 1px solid #eee;'>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
# =============================
# 📚 COMMUNITY STORIES (White Theme)
# =============================
if st.session_state.viewing_stories:
    st.subheader("💬 Community Wall", anchor=False)
    st.markdown("""
    <p style="text-align: center; color: #666; margin-bottom: 2rem;">
        Every story is a beacon of hope for someone starting their journey
    </p>
    """, unsafe_allow_html=True)

    # Load stories
    stories_ref = db.collection("approved_stories").order_by("timestamp", direction=firestore.Query.DESCENDING)
    stories = stories_ref.stream()

    if not stories:
        st.markdown("""
        <div style="text-align: center; padding: 3rem; background: rgba(108, 99, 255, 0.05); border-radius: 16px; border: 1px solid #f0f0f0;">
            <h3 style="color: #666;">No stories yet</h3>
            <p>Be the first to share your journey of hope</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Display stories with fade-in animation
        for idx, story in enumerate(stories):
            s = story.to_dict()
            with st.container():
                st.markdown(f"""
                <div class="story-card fade-in" style="animation-delay: {idx*0.1}s;">
                    <div class="location-badge">📍 {s.get('province', 'Unknown')}</div>
                    <div class="duration-badge">⏳ {s.get('duration', 'N/A')}</div>
                    <div style="font-size: 1.1rem; line-height: 1.7; color: #333;">
                        {s.get('text', '[No content provided]')}
                    </div>
                    <div style="margin-top: 1rem; text-align: right; font-size: 0.9rem; color: #888;">
                        Shared {s.get('timestamp', '').strftime('%b %d, %Y') if 'timestamp' in s else 'recently'}
                    </div>
                </div>
                """, unsafe_allow_html=True)

# =============================
# ✍️ STORY SUBMISSION FORM (White Theme)
# =============================
else:
    # Add back button at the top
    if st.button("← Back to Community Wall", 
                 key="back_to_wall",
                 type="secondary",
                 use_container_width=False,
                 help="Return to the community stories"):
        st.session_state.viewing_stories = True
        st.rerun()
    
    st.markdown("""
    <div class="form-container">
        <div class="form-header">
            <h2 style="margin: 0; color: {PRIMARY_COLOR};">✍️ Share Your Journey</h2>
            <p style="margin: 0.3rem 0 0; color: #666;">Your story could be someone's hope</p>
        </div>
    """.format(PRIMARY_COLOR=PRIMARY_COLOR), unsafe_allow_html=True)

    with st.form("submit_story", clear_on_submit=True):
        province = st.selectbox("Where are you from?", ["Punjab", "Sindh", "KPK", "Balochistan", "Islamabad"])
        duration = st.selectbox("How long did you struggle with addiction?", [
            "Less than 1 month", "1–3 months", "3–6 months", "6–12 months", 
            "1–2 years", "More than 2 years"
        ])
        
        story = st.text_area("Your Story (no personal info)", 
                             max_chars=1000, 
                             height=200,
                             placeholder="Share your journey - what was your struggle like? What helped you? What hope can you offer others?")
        
        submitted = st.form_submit_button("🌟 Share My Story", use_container_width=True)

    if submitted:
        if len(story.strip()) < 30:
            st.markdown("""
            <div style="padding: 1.2rem; background: rgba(255,193,7,0.1); border-radius: 12px; margin-top: 1rem; border: 1px solid #ffebee; margin-bottom: 1.5rem;">
                <p style="color: #ffc107; font-weight: 500;">⚠️ Please write at least 30 characters to share a meaningful story.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("Checking your story..."):
                # Simulate processing for better UX
                time.sleep(1)
                
                if is_clean(story):
                    # Create progress bar
                    progress_bar = st.progress(0)
                    for percent_complete in range(100):
                        time.sleep(0.01)
                        progress_bar.progress(percent_complete + 1)
                    
                    data = {
                        "province": province,
                        "duration": duration,
                        "text": story.strip(),
                        "approved": True,
                        "timestamp": datetime.datetime.utcnow()
                    }
                    db.collection("approved_stories").add(data)
                    
                    # Success animation
                    st.markdown("""
                    <div style="text-align: center; padding: 2rem;">
                        <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_5tkzkblw.json"  
                         background="transparent"  speed="1"  style="width: 150px; height: 150px; margin: 0 auto;"  
                         loop autoplay></lottie-player>
                        <h3 style="color: #35D0BA;">Thank you for sharing your story!</h3>
                        <p style="color: #555;">Your journey has been added to our Community Wall.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Add Lottie player script
                    st.components.v1.html("""
                    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                    """)
                    
                    # Auto-refresh after 3 seconds
                    st.balloons()
                    time.sleep(3)
                    st.session_state.viewing_stories = True
                    st.rerun()
                else:
                    st.markdown("""
                    <div style="padding: 1.5rem; background: rgba(220, 53, 69, 0.05); border-radius: 12px; margin-top: 1rem; border: 1px solid #ffebee;">
                        <h3 style="color: #dc3545; margin-top: 0;">❌ Story couldn't be published</h3>
                        <p style="color: #555;">Your story was flagged by our content filter. Please:</p>
                        <ul style="color: #555;">
                            <li>Avoid personal information</li>
                            <li>Remove any harmful language</li>
                            <li>Focus on recovery and hope</li>
                        </ul>
                        <p style="color: #555;">You can edit and resubmit your story.</p>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # Close form container

# =============================
# 💌 COMMUNITY MESSAGE (White Theme)
# =============================
st.markdown(f"""
<div style="text-align: center; margin: 4rem 0 2rem; padding: 2.5rem; 
            background: rgba(53, 208, 186, 0.05); border-radius: 16px; 
            border-left: 5px solid {SECONDARY_COLOR}; border: 1px solid #e9ecef;">
    <h3 style="color: {SECONDARY_COLOR};">You Are Not Alone</h3>
    <p style="font-size: 1.1rem; max-width: 700px; margin: 1rem auto; color: #555;">
        Every story shared here represents someone who faced addiction and chose recovery. 
        Your journey matters, and your story has the power to inspire others.
    </p>
    <p style="font-weight: 600; margin-top: 1.5rem; font-size: 1.1rem; color: {PRIMARY_COLOR};">
        Your courage gives hope to others. ✨
    </p>
</div>
""", unsafe_allow_html=True)
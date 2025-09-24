# ℹ️ About Us
import streamlit as st
import random
from utils.ui_utils import get_global_css, render_sidebar
from utils.load_handler import inject_loader_script
import base64
from utils.loading_screen import show_fullscreen_loader
# =============================
# 🎨 PAGE CONFIG & CONSTANTS
# =============================

show_fullscreen_loader()
st.set_page_config(
    page_title="About Smart Rehabilitation AI | The Team Behind Your Recovery",
    layout="centered"
)


def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Encode team images
try:
    taqi_base64 = get_image_base64("images/taqi.jpg")
    ali_base64 = get_image_base64("images/ali.jpg")
except FileNotFoundError:
    # Fallback to emojis if images not found
    taqi_base64 = None
    ali_base64 = None

PRIMARY_COLOR = "#6C63FF"
SECONDARY_COLOR = "#35D0BA"
LIGHT_BG = "#FFFFFF"
# =============================
# 🎨 GLOBAL STYLES & SIDEBAR
# =============================
st.markdown(get_global_css(), unsafe_allow_html=True)
render_sidebar()
st.markdown(f"""
<style>
    .team-photo img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 50%;
    }}
</style>
""", unsafe_allow_html=True)
# =============================
# 🎨 CUSTOM CSS INJECTION (White Theme)
# =============================
st.markdown(f"""
<style>
            
    /* ----- MISSION SECTION ----- */
    
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
    .mission-section {{
        background: #f8f9fa;
        border-radius: 24px;
        padding: 3rem 2rem;
        color: #333;
        margin: -1rem -1rem 2rem -1rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #e9ecef;
    }}
    
    /* ----- TEAM CARDS ----- */
    .team-card {{
        transition: all 0.3s ease;
        border-radius: 16px;
        background: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        padding: 2rem;
        text-align: center;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
        border: 1px solid #f0f0f0;
    }}
    
    .team-card:hover {{
        transform: translateY(-7px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }}
    
    .team-card::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        height: 5px;
        width: 100%;
        background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
    }}
    
    .team-photo {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        margin: 0 auto 1.5rem;
        border: 4px solid {PRIMARY_COLOR};
        background: #f8f9fa;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
    }}
    
    /* ----- TIMELINE ----- */
    .timeline-container {{
        position: relative;
        margin: 3rem 0;
    }}
    
    .timeline-line {{
        position: absolute;
        left: 50%;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(to bottom, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        transform: translateX(-50%);
        z-index: 1;
    }}
    
    .timeline-item {{
        position: relative;
        margin-bottom: 3rem;
        z-index: 2;
    }}
    
    .timeline-content {{
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        width: 45%;
        border: 1px solid #f0f0f0;
    }}
    
    .timeline-left {{ left: 0; }}
    .timeline-right {{ left: 55%; }}
    
    /* ----- TECH STACK ----- */
    .tech-item {{
        display: flex;
        align-items: center;
        padding: 0.8rem 1.5rem;
        background: rgba(108, 99, 255, 0.05);
        border-radius: 12px;
        margin-bottom: 0.8rem;
        transition: all 0.3s;
        border: 1px solid #f0f0f0;
    }}
    
    .tech-item:hover {{
        transform: translateX(5px);
        background: rgba(108, 99, 255, 0.08);
    }}
    
    .tech-icon {{
        font-size: 1.8rem;
        margin-right: 1rem;
        color: {PRIMARY_COLOR};
    }}

    /* ----- MOBILE RESPONSIVENESS ----- */
    @media (max-width: 768px) {{
    /* Mission section */
    .mission-section {{
        padding: 1.8rem 1rem;
        margin: -0.5rem -0.5rem 2.5rem -0.5rem;
    }}
    .mission-section h1 {{
        font-size: 2.2rem !important;
        margin-bottom: 1.2rem !important;
    }}
    .mission-section p {{
        font-size: 1.1rem !important;
        margin-bottom: 1.5rem !important;
    }}
    
    /* Team cards */
    .team-card {{
        padding: 1.5rem;
        margin-bottom: 2.5rem !important;
    }}
    .team-card::after {{
        content: "";
        display: block;
        height: 1px;
        background: #e9ecef;
        margin: 1.5rem auto 0;
        width: 80%;
    }}
    .team-card:last-child::after {{
        display: none;
    }}
    .team-photo {{
        width: 90px;
        height: 90px;
        font-size: 2rem;
        margin-bottom: 1.2rem !important;
    }}
    
    /* Timeline adjustments */
    .timeline-line {{
        left: 20px !important;
    }}
    .timeline-marker {{
        left: 20px !important;
    }}
    .timeline-content {{
        width: 80% !important;
        margin-left: 40px !important;
        margin-right: 0 !important;
        padding: 1.2rem !important;
        margin-bottom: 2.5rem !important;
    }}
    .timeline-left, 
    .timeline-right {{
        margin: 0 auto 3rem !important;
    }}
    
    /* Section headers */
    .stHeader h2 {{
        margin-top: 2.5rem !important;
        margin-bottom: 1.5rem !important;
        padding-bottom: 0.8rem !important;
        border-bottom: 1px solid #e9ecef !important;
        text-align: center !important; /* Added this line to center the header */
        
    }}
    
    /* Tech stack items */
    .tech-item {{
        padding: 0.8rem 1.2rem !important;
        margin-bottom: 1.2rem !important;
    }}
    
    /* Final message */
    div[style*="margin: 4rem 0"] {{
        margin: 3rem 0 2rem !important;
        padding: 1.8rem !important;
    }}
    
    /* Footer section */
    .stContainer {{
        margin-top: 2.5rem !important;
        padding-top: 1.5rem !important;
        border-top: 1px solid #e9ecef !important;
    }}
}}
    
    
</style>
""", unsafe_allow_html=True)
# ... rest of the file remains unchanged ...
st.markdown(inject_loader_script(), unsafe_allow_html=True)
# =============================
# 🏆 HERO MISSION SECTION (White Theme)
# =============================
st.markdown(f"""
<div class="mission-section">
    <h1 style="font-size: 2.8rem; margin-bottom: 1rem; color: {PRIMARY_COLOR};">🔥 Rise from the Ashes</h1>
    <p style="font-size: 1.3rem; max-width: 800px; margin: 0 auto; color: #555;">
        Smart Rehabilitation AI is Pakistan's first AI-powered platform built to help people overcome addiction
        through culturally sensitive, personalized recovery plans — completely anonymously.
    </p>
</div>
""", unsafe_allow_html=True)

# =============================
# 👥 TEAM SHOWCASE (White Theme)
# =============================
st.header("👨‍💻 The Guardians of Hope", anchor=False)
st.markdown("""
<p style="text-align: center; font-size: 1.1rem; margin-bottom: 2rem; color: #555;">
    Meet the team dedicated to your recovery journey. We're here because we believe in second chances.
</p>
""", unsafe_allow_html=True)

# Team members data
team_members = [
    {
        "name": "Taqi Kazmi",
        "role": "Co-Founder & Tech Lead",
        "bio": "AI enthusiast with a passion for mental health tech. Believes technology should heal, not just entertain.",
        "ig": "https://instagram.com/taqikvzmi",
        "image": taqi_base64
    },
    {
        "name": "Ali Jamal",
        "role": "Co-Founder & Product Vision",
        "bio": "Product designer focused on creating compassionate digital experiences that empower recovery journeys.",
        "ig": "https://www.instagram.com/alijamalashraf/",
        "image": ali_base64
    }
]

# Display team in columns
col1, col2 = st.columns(2)
for i, member in enumerate(team_members):
    with (col1 if i == 0 else col2):
        if member['image']:
            # Use base64 encoded image
            img_html = f'<img src="data:image/jpeg;base64,{member["image"]}" alt="{member["name"]}">'
        else:
            # Fallback to emoji if image not found
            img_html = "👨‍💻" if i == 0 else "👨‍🎨"
            
        st.markdown(f"""
        <div class="team-card">
            <div class="team-photo">
                {img_html}
            </div>
            <h3 style="margin-bottom: 0.2rem; color: #333;">{member['name']}</h3>
            <p style="color: {PRIMARY_COLOR}; font-weight: 600; margin-bottom: 1rem;">{member['role']}</p>
            <p style="margin-bottom: 1.5rem; color: #555;">{member['bio']}</p>
            <a href="{member['ig']}" target="_blank">
                <button style="border: none; background: white; color: {PRIMARY_COLOR}; 
                        padding: 0.5rem 1.5rem; border-radius: 12px; font-weight: 500; 
                        cursor: pointer; box-shadow: 0 3px 10px rgba(0,0,0,0.08);
                        border: 1px solid #e9ecef; transition: all 0.3s;">
                    Connect on Instagram
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# =============================
# 🕰️ OUR STORY TIMELINE (Centered Professional Design)
# =============================
st.header("📜 Our Journey", anchor=False)
st.markdown("""
<p style="text-align: center; font-size: 1.1rem; margin-bottom: 2.5rem; color: #555;">
    How two friends created Pakistan's first AI-powered recovery platform
</p>
""", unsafe_allow_html=True)

# Updated centered timeline CSS
st.markdown(f"""
<style>
    .timeline-container {{
        position: relative;
        margin: 3rem auto;
        max-width: 1100px;
    }}
    
    .timeline-line {{
        position: absolute;
        left: 50%;
        top: 0;
        bottom: 0;
        width: 3px;
        background: linear-gradient(to bottom, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        transform: translateX(-50%);
        z-index: 1;
    }}
    
    .timeline-item {{
        position: relative;
        margin-bottom: 2.8rem;
        z-index: 2;
        display: flex;
        justify-content: center;
    }}
    
    .timeline-content {{
        background: white;
        border-radius: 12px;
        padding: 1.6rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.06);
        width: 42%;
        border: none;
        transition: all 0.3s ease;
    }}
    
    .timeline-content:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.09);
    }}
    
    .timeline-left {{ 
        margin-right: auto; 
        margin-left: 4%;
    }}
    
    .timeline-right {{ 
        margin-left: auto;
        margin-right: 4%;
    }}
    
    /* Timeline marker */
    .timeline-marker {{
        position: absolute;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: white;
        border: 3px solid {PRIMARY_COLOR};
        left: 50%;
        top: 22px;
        transform: translateX(-50%);
        z-index: 3;
    }}
    
    /* Responsive adjustments */
    @media (max-width: 900px) {{
        .timeline-content {{
            width: 80% !important;
            margin: 0 auto 2rem !important;
        }}
        .timeline-left, .timeline-right {{
            margin: 0 auto 2rem !important;
        }}
        .timeline-line {{
            left: 40px;
        }}
        .timeline-marker {{
            left: 40px;
        }}
    }}
</style>
""", unsafe_allow_html=True)
# Timeline data
timeline = [
    {"date": "Jan 2025", "title": "The Spark", "content": "After witnessing addiction struggles in our community, we envisioned a tech solution that could provide anonymous support."},
    {"date": "Feb 2025", "title": "First Prototype", "content": "Built initial diagnosis tool using Streamlit and basic AI models."},
    {"date": "Apr 2025", "title": "Community Feature", "content": "Added anonymous story sharing to create peer support network."},
    {"date": "June 2025", "title": "Cultural Guidance", "content": "Integrated culturally sensitive support for Pakistani users."},
    {"date": "Present", "title": "Smart Rehabilitation AI", "content": "Launched full platform with professional UI/UX to help thousands begin their recovery journey."}
]
# Display timeline
st.markdown('<div class="timeline-container">', unsafe_allow_html=True)
st.markdown('<div class="timeline-line"></div>', unsafe_allow_html=True)

for i, event in enumerate(timeline):
    position = "timeline-left" if i % 2 == 0 else "timeline-right"
    
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-marker"></div>
        <div class="timeline-content {position}">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.8rem;">
                <h3 style="margin: 0; color: {PRIMARY_COLOR}; font-size: 1.3rem; font-weight: 600;">{event['title']}</h3>
                <span style="background: rgba(108, 99, 255, 0.08); color: {PRIMARY_COLOR}; 
                          padding: 0.4rem 1.1rem; border-radius: 20px; font-size: 0.95rem; font-weight: 500;">
                    {event['date']}
                </span>
            </div>
            <p style="color: #555; line-height: 1.65; margin: 0; font-size: 1.02rem;">{event['content']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =============================
# 🛠️ TECHNOLOGY STACK (White Theme)
# =============================
st.header("⚙️ Our Technology", anchor=False)
st.markdown("""
<p style="text-align: center; font-size: 1.1rem; margin-bottom: 2rem; color: #555;">
    Built with cutting-edge tools to ensure your privacy and effective recovery
</p>
""", unsafe_allow_html=True)

tech_stack = [
    {"icon": "🤖", "name": "Gemini AI", "desc": "Advanced AI for personalized recovery plans"},
    {"icon": "📱", "name": "Streamlit", "desc": "Beautiful, responsive web interface"},
    {"icon": "🔥", "name": "Firebase", "desc": "Secure, anonymous data storage"},
    {"icon": "🔒", "name": "Military-grade Encryption", "desc": "Protecting your privacy"},
    {"icon": "🌐", "name": "Multi-language Support", "desc": "English/Urdu interface"},
    {"icon": "🧠", "name": "Content Filtering AI", "desc": "Keeping community stories safe"}
]

# Display tech stack in columns
cols = st.columns(2)
for i, tech in enumerate(tech_stack):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="tech-item">
            <div class="tech-icon">{tech['icon']}</div>
            <div>
                <h4 style="margin-bottom: 0.2rem; color: #333;">{tech['name']}</h4>
                <p style="color: #666; margin: 0; font-size: 0.95rem;">{tech['desc']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =============================
# 💌 FINAL MESSAGE (White Theme)
# =============================
st.markdown(f"""
<div style="text-align: center; margin: 4rem 0 2rem; padding: 2.5rem; 
            background: rgba(53, 208, 186, 0.05); border-radius: 16px; 
            border-left: 5px solid {SECONDARY_COLOR}; border: 1px solid #e9ecef;">
    <h3 style="color: {SECONDARY_COLOR};">Your Journey Matters</h3>
    <p style="font-size: 1.1rem; max-width: 700px; margin: 1rem auto; color: #555;">
        We built Smart Rehabilitation AI because we believe everyone deserves a chance at recovery. 
        Whether you're taking your first step or continuing your journey, we're honored 
        to walk this path with you.
    </p>
    <p style="font-weight: 600; margin-top: 1.5rem; font-size: 1.1rem; color: {PRIMARY_COLOR};">
        You are stronger than you know. 🔥
    </p>
</div>
""", unsafe_allow_html=True)


# =============================
# 🫶 FOUNDER SECTION (Professional Design)
# =============================

def footer_section():
    
    with st.container():
        st.markdown(f"""
        
        <p style="text-align: center; margin-top: 2.5rem; font-size: 1.1rem; color: #555; max-width: 600px; margin-left: auto; margin-right: auto;">
            We value your feedback and are committed to continuously improving Smart Rehabilitation AI. 
            Reach out to us directly with suggestions, questions, or just to share your journey.
        </p>
        """, unsafe_allow_html=True)

footer_section()

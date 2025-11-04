import streamlit as st
import random
from utils.ui_utils import get_global_css, render_sidebar
from utils.load_handler import inject_loader_script
from utils.loading_screen import show_fullscreen_loader

# =============================
# ✨ BRAND CONSTANTS & SETTINGS
# =============================
APP_NAME = "Smart Rehabilitation "
PRIMARY_COLOR = "#6C63FF"  # Purple for wisdom
SECONDARY_COLOR = "#35D0BA"  # Teal for renewal
LIGHT_BG = "#FFFFFF"  # Pure white background
TAQI_IG = "https://instagram.com/taqikvzmi"
ALI_IG = "https://www.instagram.com/alijamalashraf/"
SILVER_LINING_WEBSITE = "http://www.silverlining.org.pk/"
SILVER_LINING_LOGO = "https://raw.githubusercontent.com/Mackming/noor-ai/main/silver_lining_logo.png"

# =============================
# 🎨 CUSTOM CSS INJECTION (White Theme)
# =============================
st.markdown(f"""
<style>
    /* ----- GLOBAL OVERRIDES ----- */
    .stApp {{
        opacity: 1 !important;
        animation: none !important;
        transition: none !important;
    }}
    /* ----- ENHANCED INVISIBLE BUTTON FIX ----- */
    # With this optimized version:
    div.card-container > div.stButton > button {{
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        opacity: 0 !important;
        z-index: 1 !important;
        padding: 0 !important;
        border: none !important;
        cursor: pointer !important;
        background: transparent !important;
    }}

    div.card-container > div.stButton > button:hover,
    div.card-container > div.stButton > button:active,
    div.card-container > div.stButton > button:focus {{
        background: transparent !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }}

    /* Override Streamlit's button animations */
    div.card-container > div.stButton > button::before,
    div.card-container > div.stButton > button::after {{
        content: none !important;
    }}
    
    /* ----- SIDEBAR SPECIFICS ----- */
    section[data-testid="stSidebar"] > div:first-child {{
        top: 0 !important;
    }}
    
    button[title="Collapse sidebar"],
    button[title="Expand sidebar"] {{
        background-color: {PRIMARY_COLOR} !important;
        color: white !important;
        border-radius: 50% !important;
    }}
    
    /* ----- HERO SECTION ----- */
    .hero-section {{
        background: linear-gradient(135deg, #f9fafb, #f0f2f6);
        border-radius: 24px;
        padding: 2.5rem 1.5rem;
        color: #333;
        margin: -1.5rem -1rem 1.5rem -1rem;
        border: 1px solid #e9ecef;
        text-align: center;
        position: relative;
        overflow: hidden;
    }}
    
    /* ----- FEATURE CARDS ----- */
    .card-container {{
        position: relative !important;
        overflow: hidden !important;
        height: 100% !important;
    }}
    
    .feature-card {{
        transition: all 0.3s ease;
        border-radius: 16px;
        background: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        padding: 1.5rem 1rem;
        height: 100%;
        text-align: center;
        border: 1px solid #f0f0f0;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    
    .feature-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.1);
    }}
    
    .feature-card-title {{
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        line-height: 1.3;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        min-height: 2.6em;
    }}
    
    /* ----- PREMIUM PARTNERSHIP SECTION ----- */
    .premium-partnership {{
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 50%, #ffffff 100%);
        border-radius: 24px;
        padding: 3rem 2.5rem;
        margin: 3rem 0;
        border: 2px solid #f0f2ff;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(108, 99, 255, 0.08);
    }}
    
    .premium-partnership::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR}, {PRIMARY_COLOR});
        background-size: 200% 100%;
        animation: shimmer 3s ease-in-out infinite;
    }}
    
    @keyframes shimmer {{
        0% {{ background-position: -200% 0; }}
        100% {{ background-position: 200% 0; }}
    }}
    
    .partnership-badge {{
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, {PRIMARY_COLOR}, #8a85ff);
        color: white;
        padding: 0.6rem 1.8rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3);
        border: 1px solid rgba(255,255,255,0.2);
    }}
    
    .partnership-badge::before {{
        content: '⭐';
        margin-right: 0.5rem;
        font-size: 1rem;
    }}
    
    .hospital-logo-container {{
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        border: 1px solid #f0f0f0;
        display: inline-block;
        margin: 1.5rem 0;
        transition: all 0.3s ease;
        position: relative;
    }}
    
    .hospital-logo-container:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(108, 99, 255, 0.15);
    }}
    
    .hospital-logo {{
        max-width: 200px;
        height: auto;
        filter: brightness(1.05) contrast(1.1);
    }}
    
    .branch-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1.2rem;
        margin: 2rem 0;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }}
    
    .branch-card {{
        background: linear-gradient(135deg, #ffffff, #fafbff);
        padding: 1.5rem 1rem;
        border-radius: 16px;
        text-align: center;
        border: 1px solid #e8ebff;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }}
    
    .branch-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: {SECONDARY_COLOR};
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    
    .branch-card:hover::before {{
        opacity: 1;
    }}
    
    .branch-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        border-color: {PRIMARY_COLOR};
    }}
    
    .branch-icon {{
        font-size: 1.8rem;
        margin-bottom: 0.8rem;
        opacity: 0.9;
    }}
    
    .branch-name {{
        font-weight: 700;
        color: {PRIMARY_COLOR};
        margin-bottom: 0.3rem;
        font-size: 1.05rem;
    }}
    
    .branch-city {{
        color: #666;
        font-size: 0.9rem;
        font-weight: 600;
    }}
    
    .partnership-tagline {{
        background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
        font-size: 1.1rem;
        margin-top: 1.5rem;
        padding: 1rem 2rem;
        border-radius: 50px;
        background-color: #f8f9ff;
        display: inline-block;
        border: 1px solid #e8ebff;
    }}
    
    /* ----- INVISIBLE BUTTON FIX ----- */
    .invisible-btn {{
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        opacity: 0 !important;
        z-index: 1 !important;
        padding: 0 !important;
        border: none !important;
        cursor: pointer !important;
    }}
    
    .invisible-btn:hover {{
        background: transparent !important;
    }}
    
    /* ----- RESPONSIVE ADJUSTMENTS ----- */
    @media (max-width: 1200px) {{
        .feature-card-title {{
            font-size: 1.1rem;
        }}
    }}
    
    @media (max-width: 992px) {{
        .stColumns > div {{
            flex: 0 0 50% !important;
            max-width: 50% !important;
        }}
        .feature-card {{
            padding: 1.2rem 0.8rem;
        }}
        
        .premium-partnership {{
            padding: 2.5rem 2rem;
        }}
        
        .branch-grid {{
            grid-template-columns: repeat(2, 1fr);
        }}
    }}
    
    @media (max-width: 768px) {{
        .hero-section {{
            padding: 1.8rem 1rem;
            border-radius: 0 0 24px 24px;
            margin: -1rem -0.5rem 1rem -0.5rem;
        }}
        
        .hero-section h1 {{
            font-size: 2.5rem !important;
            line-height: 1.2;
            margin-bottom: 0.8rem;
        }}
        
        .hero-section p {{
            font-size: 1.1rem !important;
            max-width: 90% !important;
            margin: 0 auto;
        }}
        
        .premium-partnership {{
            padding: 2rem 1.5rem;
            margin: 2.5rem 0;
            border-radius: 20px;
        }}
        
        .hospital-logo {{
            max-width: 160px;
        }}
        
        .hospital-logo-container {{
            padding: 1.5rem;
        }}
        
        .branch-grid {{
            grid-template-columns: 1fr;
            gap: 1rem;
        }}
        
        .branch-card {{
            padding: 1.2rem 1rem;
        }}
        
        .stColumns > div {{
            flex: 0 0 100% !important;
            max-width: 100% !important;
        }}
        
        .feature-card {{
            margin-bottom: 1rem;
            padding: 1.5rem 1rem;
        }}
        
        .feature-card-title {{
            font-size: 1.2rem;
            -webkit-line-clamp: 1;
        }}
        
        [data-testid="stSidebar"] {{
            padding: 0.5rem 1rem 1rem !important;
        }}
        
        .welcome-message {{
            padding: 1.5rem !important;
            margin: 1.5rem 0 !important;
        }}
        
        .welcome-message h2 {{
            font-size: 1.4rem !important;
        }}
        
        .welcome-message p {{
            font-size: 1rem !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)
st.markdown(inject_loader_script(), unsafe_allow_html=True)
# =============================
# 🚀 PAGE CONFIGURATION
# =============================
st.set_page_config(
    page_title=f"{APP_NAME} | Addiction Recovery Platform",
    layout="centered",
    initial_sidebar_state="expanded"
)



st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF !important;
        transition: background-color 0.01s !important;
    }
    
    /* Fix for button positioning */
    div[data-testid="column"] > div > div > div[data-testid="element-container"] {
        position: relative !important;
        height: 100% !important;
    }
</style>
""", unsafe_allow_html=True)
# =============================
# 🎨 GLOBAL STYLES & SIDEBAR
# =============================
st.markdown(get_global_css(), unsafe_allow_html=True)
render_sidebar()
# =============================
# 🏠 HOMEPAGE CONTENT (White Theme)
# =============================
# HERO SECTION
st.markdown(f"""
<div class="hero-section">
    <h1 style="font-size: 3.2rem; margin-bottom: 0.5rem; letter-spacing: -0.5px; color: {PRIMARY_COLOR};">✨ {APP_NAME}</h1>
    <p style="font-size: 1.3rem; max-width: 700px; margin: 0 auto; color: #555;">
        Your anonymous AI-powered journey to freedom from addiction
    </p>
</div>
""", unsafe_allow_html=True)

# FEATURE CARDS - Responsive Design
st.subheader("✨ Your Recovery Toolkit", anchor=False)
st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

# Responsive column setup
col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="medium")

features = [
    {"icon": "🧠", "title": "Self-Assessment", "desc": "Personalized recovery plan based on your situation", "page": "pages/01_diagnose.py"},
    {"icon": "🤝", "title": "Community Stories", "desc": "Read and share anonymous journeys", "page": "pages/2__community.py"},
    {"icon": "ℹ️", "title": "About Smart Rehab AI", "desc": "Our mission and the team behind", "page": "pages/3__about.py"},
    {"icon": "🔒", "title": "Admin Portal", "desc": "Content moderation dashboard", "page": "pages/99__admin.py"}
]

for i, col in enumerate([col1, col2, col3, col4]):
    with col:
        container = st.container()
        container.markdown('<div class="card-container">', unsafe_allow_html=True)
        
        # Card content remains the same
        container.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 2.8rem; margin-bottom: 1rem; color: {PRIMARY_COLOR};">{features[i]['icon']}</div>
            <div class="feature-card-title">{features[i]['title']}</div>
            <p style="color: #666; font-size: 0.95rem; line-height: 1.4; margin-bottom: 0;">{features[i]['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        container.markdown('</div>', unsafe_allow_html=True)

# PREMIUM SILVER LINING PARTNERSHIP SECTION
st.markdown("""
<div class="premium-partnership">
    <div style="text-align: center;">
        <div class="partnership-badge">Official Healthcare Partner</div>
""", unsafe_allow_html=True)

# Partnership header
st.markdown(f"""
<h2 style="text-align: center; color: {PRIMARY_COLOR}; margin-bottom: 1rem; font-size: 2.2rem; font-weight: 800;">
    Partnering with Excellence
</h2>
<p style="text-align: center; font-size: 1.2rem; color: #555; max-width: 800px; margin: 0 auto 2rem; line-height: 1.6;">
    We're proud to collaborate with <strong>Silver Lining Pakistan</strong>, combining cutting-edge AI technology 
    with professional healthcare expertise for comprehensive addiction recovery.
</p>
""", unsafe_allow_html=True)

# Logo with premium container
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f"""
    <div style="text-align: center;">
        <a href="{SILVER_LINING_WEBSITE}" target="_blank">
            <div class="hospital-logo-container">
                <img src="{SILVER_LINING_LOGO}" alt="Silver Lining Pakistan" class="hospital-logo">
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

# Branch locations with icons
st.markdown(f"""
<h3 style="text-align: center; color: {PRIMARY_COLOR}; margin: 2.5rem 0 1.5rem; font-size: 1.5rem; font-weight: 700;">
    🏥 Our Partner Network
</h3>
""", unsafe_allow_html=True)

# Branch grid
st.markdown("""
<div class="branch-grid">
    <div class="branch-card">
        <div class="branch-icon">🏛️</div>
        <div class="branch-name">Main Branch</div>
        <div class="branch-city">Lahore</div>
    </div>
    <div class="branch-card">
        <div class="branch-icon">🏥</div>
        <div class="branch-name">Sheikhupura</div>
        <div class="branch-city">Medical Center</div>
    </div>
    <div class="branch-card">
        <div class="branch-icon">🏥</div>
        <div class="branch-name">Faisalabad</div>
        <div class="branch-city">Medical Center</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Closing section
st.markdown("""
<div style="text-align: center; margin-top: 2.5rem;">
    <div class="partnership-tagline">
        AI Technology × Professional Healthcare = Complete Recovery
    </div>
</div>
""", unsafe_allow_html=True)

# Close the premium partnership container
st.markdown("""
    </div>
</div>
""", unsafe_allow_html=True)

# WELCOME MESSAGE
st.markdown(f"""
<div class="welcome-message" style="margin: 3rem 0 1rem; padding: 2rem; background: white; border-radius: 16px; box-shadow: 0 5px 15px rgba(0,0,0,0.03); border: 1px solid #f0f0f0;">
    <h2 style="color: {PRIMARY_COLOR};">👋 Welcome to Your Recovery Journey</h2>
    <p style="font-size: 1.1rem; line-height: 1.6; color: #555;">
        This is a safe and anonymous place for self-diagnosis, reading community stories, 
        and accessing recovery plans. Every journey begins with a single step - you've taken 
        yours by being here today.
    </p>
    <p style="font-size: 1.1rem; font-weight: 500; color: {SECONDARY_COLOR}; margin-top: 1.5rem;">
        Use the left sidebar to explore our tools →
    </p>
</div>
""", unsafe_allow_html=True)

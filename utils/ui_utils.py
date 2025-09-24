import streamlit as st
import random
import base64

PRIMARY_COLOR = "#6C63FF"
SECONDARY_COLOR = "#35D0BA"
TAQI_IG = "https://instagram.com/taqikvzmi"
ALI_IG = "https://www.instagram.com/alijamalashraf/"

def get_global_css():
    return f"""
    <style>
        /* ===== COMPREHENSIVE THEME SETUP ===== */
        :root {{
        --background-color: #ffffff;
        --secondary-background-color: #f0f2f6;
        --text-color: #333;
        --secondary-text: #555;
        --primary-color: #6C63FF;
        --secondary-color: #35D0BA;
        --input-bg: #fff;
        --input-border: #e0e0e0;
        --button-text: #fff;
        --shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            }}

        
        /* ===== GLOBAL TEXT SETTINGS ===== */
        body, .stApp, 
        .stMarkdown, .stText, 
        .stAlert, .stExpander, .stProgress,
        .stTabs, .st-bb, .st-at, .st-af, 
        .st-ae, .st-ag, .st-ah, .st-ai,
        h1, h2, h3, h4, h5, h6, p, span, div {{
            color: var(--text-color) ;
        }}
        

        
        
        /* ===== CONTAINER BACKGROUNDS ===== */
        [data-testid="stAppViewContainer"],
        [data-testid="stSidebar"],
        [data-testid="stHeader"],
        .stApp,
        .st-emotion-cache-1y4p8pa,
        .st-emotion-cache-1v0mbdj,
        .st-emotion-cache-1p1nwyz,
        section.main,
        div.block-container {{
            background-color: var(--background-color) ;
        }}

        
        
        /* ===== BUTTONS ===== */
        /* KEEPING YOUR PREFERRED BUTTON STYLE */
        .stButton > button {{
            background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR}) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 0.5rem 1.5rem !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            box-shadow: 0 4px 10px rgba(108, 99, 255, 0.2) !important;
        }}
        button[data-testid="stBaseButton-secondary"] {{
            background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR}) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 0.5rem 1.5rem !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            box-shadow: 0 4px 10px rgba(108, 99, 255, 0.2) !important;
        }}
        button[data-testid="stBaseButton-secondary"] p{{
            color: white !important;
        }}

        button[data-testid="stBaseButton-secondary"]:hover{{
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(108, 99, 255, 0.3) !important;
            background: linear-gradient(135deg, {SECONDARY_COLOR}, {PRIMARY_COLOR}) !important;
        }}
        
        button[data-testid="stBaseButton-secondary"]:active{{
            transform: translateY(0);
            box-shadow: 0 2px 5px rgba(108, 99, 255, 0.2) !important;
        }}
        .stDownloadButton > button{{
            background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR}) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 0.5rem 1.5rem !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            box-shadow: 0 4px 10px rgba(108, 99, 255, 0.2) !important;
        }}
        .stDownloadButton > button p {{
            color: white !important;
        }}
        .stButton > button p {{
            color: white !important;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(108, 99, 255, 0.3) !important;
            background: linear-gradient(135deg, {SECONDARY_COLOR}, {PRIMARY_COLOR}) !important;
        }}
        .stDownloadButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(108, 99, 255, 0.3) !important;
            background: linear-gradient(135deg, {SECONDARY_COLOR}, {PRIMARY_COLOR}) !important;
        }}
        
        .stButton > button:active {{
            transform: translateY(0);
            box-shadow: 0 2px 5px rgba(108, 99, 255, 0.2) !important;
        }}
        .stDownloadButton > button:active {{
            transform: translateY(0);
            box-shadow: 0 2px 5px rgba(108, 99, 255, 0.2) !important;
        }}

        svg[data-baseweb="icon"][title="open"] {{
            padding: 0 !important;
            background-color: white !important; /* Optional: bg box */
            fill: black !important;   
            
        }}
        div[class*="st-c0"][class*="st-bt"].st-cv {{
            background-color: white !important;
            
            
        }}
        div[class*="st-c0"][class*="st-bt"].st-cv : active{{
            border: none !important;
        }}
        
        div[class*="st-c0"].st-cn{{
            border: none !important;
        }}
        
        span[data-baseweb="tag"] {{
            background-color: rgb(221 221 221) !important;
            
            
        }}
        div.st-dr.st-ds {{
            color: rgb(0 0 0 / 60%) !important;
        }}
        li[role="option"] {{
            background-color: white !important;
            
        }}

        /* Target the entire Streamlit selectbox container */
        div[data-baseweb="select"] {{
            background-color: white !important;
            
        }}

        label[data-baseweb="radio"] > div > div {{
            background-color: white !important;
            
        }}

        /* Target the input box inside the dropdown */
        div[data-baseweb="select"] input {{
            background-color: white !important;
            color: black !important;
        }}

        /* Also set background of the visible selected option */
        div[data-baseweb="select"] > div:first-child {{
            background-color: white !important;
        }}

        /* Optional: change icon container background */
        div[data-baseweb="select"] svg {{
            background-color: white !important;
        }}

        div[data-baseweb="select"] .st-ek {{
            color: #5f5f5f !important;
        }}
        div[data-baseweb="select"] .st-el {{
            color: #5f5f5f !important;
        }}


        div[data-baseweb="select"] > div:last-child {{
            color: #5f5f5f !important;
        }}
        div[data-baseweb="select"] div[class*="st-"][class*="st-"] {{
            color: #5f5f5f !important;
        }}
        svg[title="Delete"] {{
            background-color: transparent !important;
        }}
        svg[title="Delete"].st-f8.st-f9.st-fa {{
            background-color: transparent !important;
        }}

        span[role="presentation"][aria-hidden="true"] {{
            background-color: transparent !important;
        }}
        .st-f4.st-f5.st-f6.st-ba {{
            background-color: transparent !important;
        }}

        /* Target the textarea using a wildcard + its ID for priority */
        /* Style the textarea directly */
        textarea#text_area_1 {{
            background-color: white !important;
            color: black !important;                /* User input */
            border: none !important;                /* Remove border */
            outline: none !important;               /* Optional: remove focus outline */
            padding: 12px !important;
            font-size: 1rem !important;
        }}

        /* Placeholder text style */
        textarea#text_area_1::placeholder {{
            color: #888 !important;                 /* Guide text color */
            opacity: 1 !important;
        }}
        svg[title="Delete"].st-f8.st-f9.st-fa {{
            background-color: transparent !important;
        }}
        [data-testid="stSidebar"] {{
            transition: width 0.3s ease !important;
        }}

        /* Optional: Also clear border from its container if it has one */
        div[data-baseweb="base-input"] {{
            border: none !important;
            border-color: transparent !important;
            background-color: transparent !important;
            box-shadow: none !important;
        }}

        span[role="presentation"][aria-hidden="true"] {{
            background-color: transparent !important;
        }}

        .st-f4.st-f5.st-f6.st-ba {{
            background-color: transparent !important;
        }}

        span[role="presentation"][aria-hidden="true"] {{
            background-color: transparent !important;
            padding: 0 !important;
            border: none !important;
        }}




        /* ===== TEXT AREA FIX ===== */
        .stTextArea > textarea {{
            background: white !important;
            color: var(--input-text) !important;
        }}
        
        /* ===== FORM SUBMIT BUTTON FIX ===== */
        .stFormSubmitButton > button,
        div[data-testid="stFormSubmitButton"] > button {{
            background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR}) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 0.5rem 1.5rem !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            box-shadow: 0 4px 10px rgba(108, 99, 255, 0.2) !important;
        }}
        
        .stFormSubmitButton > button:hover,
        div[data-testid="stFormSubmitButton"] > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(108, 99, 255, 0.3) !important;
            background: linear-gradient(135deg, {SECONDARY_COLOR}, {PRIMARY_COLOR}) !important;
        }}
        
        .stFormSubmitButton > button:active,
        div[data-testid="stFormSubmitButton"] > button:active {{
            transform: translateY(0);
            box-shadow: 0 2px 5px rgba(108, 99, 255, 0.2) !important;
        }}
        
        .stFormSubmitButton > button p,
        div[data-testid="stFormSubmitButton"] > button p {{
            color: white !important;
            margin: 0 !important;
        }}
        
        
        /* ===== FORM ELEMENTS FIX ===== */
        /* Inputs - White background with dark text */
        .stTextInput > div > div > input,
        .stTextArea > textarea,
        .stNumberInput > div > div > input,
        .stDateInput > div > div > input,
        .stTimeInput > div > div > input {{
            background: white !important;
            color: var(--input-text) ;  /* FIX: Changed to dark text */
            
             
            padding: 0.75rem 1rem !important;
            font-size: 1rem !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        }}
        
        /* Dropdowns */
        
        
        /* Checkboxes & Radios */
        .stCheckbox label, 
        .stRadio label {{
            color: var(--text-primary) ;
            
        }}
        
        .stCheckbox .st-c7,
        .stRadio .st-c7 {{
            background: white !important;
            border: 1.5px solid var(--border-color) !important;
            border-radius: 6px !important;
        }}
        
        .stCheckbox .st-da, 
        .stRadio .st-da {{
            border-color: {PRIMARY_COLOR} !important;
            
        }}

        label[data-baseweb="radio"] p{{
            background-color: white !important;  /* Selected fill */
        }}
        .st-by {{
            background-color: #f0f0f0 !important;
        }}
        
        /* Sliders */
        .stSlider .st-c3 {{
            background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR}) !important;
        }}
        
        .stSlider .st-c0 {{
            background: {PRIMARY_COLOR} !important;
            border: 2px solid white !important;
            box-shadow: 0 2px 6px rgba(108, 99, 255, 0.3) !important;
        }}
        
        /* Toggles */
        .stToggle > label {{
            background: #f0f0f0 !important;
            border: 1px solid var(--border-color) !important;
        }}
        
        .stToggle .st-cx {{
            background: {PRIMARY_COLOR} !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        }}
        
        /* Expanders */
        .stExpander > details {{
            background: white !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04) !important;
        }}
        
        .stExpander > details > summary {{
            color: {PRIMARY_COLOR} ;
            font-weight: 600 !important;
            padding: 1rem 1.5rem !important;
        }}
        
        /* File Uploader */
        .stFileUploader > div {{
            border: 1px dashed var(--border-color) !important;
            border-radius: 12px !important;
            background: rgba(108, 99, 255, 0.03) !important;
        }}
        
        .stFileUploader > div:hover {{
            border-color: {PRIMARY_COLOR} !important;
            background: rgba(108, 99, 255, 0.08) !important;
        }}
        
        /* ===== SIDEBAR STYLES ===== */
        [data-testid="stSidebar"] {{
            background: var(--background-color) ;
            box-shadow: 5px 0 15px rgba(0,0,0,0.03) !important;
            border-right: 1px solid #eee !important;
            padding: 0.5rem 1.2rem 1.5rem !important;
        }}
        
        [data-testid="stSidebarNav"] {{
            display: none !important;
        }}

        [data-baseweb="radio"] > div:first-child {{
            background-color: rgb(75 207 255) !important; /* Your PRIMARY_COLOR */
        }}
        [data-baseweb="select"]{{
    
            background-color: white;
        
            }}

        
        .stPageLink {{
            margin: 0.15rem 0 !important;
            border-radius: 8px !important;
            transition: all 0.2s !important;
        }}
        
        .stPageLink:hover {{
            background: rgba(108, 99, 255, 0.08) !important;
            transform: translateX(3px) !important;
        }}
        
        .stPageLink a {{
            padding: 0.5rem 1rem !important;
            font-size: 0.9rem !important;
            color: var(--text-color) ;
        }}
        
        /* ===== CUSTOM COMPONENTS ===== */
        .ig-btn {{
            border: none !important;
            background: white !important;
            color: {PRIMARY_COLOR} !important;
            padding: 0.5rem 0.8rem !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: all 0.3s !important;
            display: block;
            width: 100%;
            text-align: center;
            margin: 0.3rem 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border: 1px solid #e9ecef !important;
            font-size: 0.85rem !important;
        }}
        
        .ig-btn:hover {{
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            background: {PRIMARY_COLOR} !important;
            color: white !important;
        }}
        
        /* ===== HEADER & LOADING FIXES ===== */
        header[data-testid="stHeader"] {{
            background-color: transparent !important;
        }}
        
        .stApp {{
            opacity: 1 !important;
            animation: none !important;
            transition: none !important;
        }}
        
        /* ===== UTILITY CLASSES ===== */
        .dark-text {{
            color: var(--text-color) !important;
        }}
        
        .light-text {{
            color: white !important;
        }}
        
        .secondary-text {{
            color: var(--secondary-text) !important;
        }}


        /* Selectbox and Multiselect Styling */
        div[data-baseweb="select"],
        .stMultiSelect > div > div > div {{
            background: white !important;
            color: var(--input-text) !important;
            border: 1px solid #e0e0e0 !important;
            border-radius: 12px !important;
            font-size: 1rem !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        }}

        /* Dropdown options */
        div[data-baseweb="select"] div[role="option"],
        .stMultiSelect option {{
            color: black !important;
            background: white !important;
        }}

        /* Focus States */
        
        .stTextInput > div > div > input:focus,
        .stTextArea > textarea:focus {{
            border-color: {PRIMARY_COLOR} !important;
            box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.15) !important;
            outline: none !important;
        }}
        div[class*="st-c0"].st-cn:focus-within{{
            border-color: {PRIMARY_COLOR} !important;
            box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.15) !important;
            outline: none !important;
        }}



        /* Plain text input styling */
        input[aria-label="Username"][type="text"] {{
            background: white !important;
            color: var(--text-color) !important;
            border: 0px solid var(--input-border) !important;
            border-radius: 12px !important;
            padding: 0.75rem 1rem !important;
            font-size: 1rem !important;
            box-shadow: var(--shadow) !important;
        }}

        /* Focus state for text input */
        input[aria-label="Username"][type="text"]:focus {{
            border-color: var(--primary-color) !important;
            box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.15) !important;
            outline: none !important;
        }}
        /* Password input container */
        div[data-testid="stTextInputRootElement"] {{
            background: white;
            border: 1px solid var(--input-border);
            border-radius: 12px;
            display: flex;
            align-items: center;
            box-shadow: var(--shadow);
        }}

        /* Actual password field */
        div[data-testid="stTextInputRootElement"] input[type="password"] {{
            background: transparent;
            border: none !important;
            border-radius: 0px !important; 
            color: var(--text-color);
            font-size: 1rem;
            flex-grow: 1;
            padding: 0.75rem 0.5rem;
            outline: none;
        }}

        /* Show password button styling */
        div[data-testid="stTextInputRootElement"] button {{
            background: transparent;
            border: none;
            padding: 0.3rem;
            cursor: pointer;
        }}

        /* SVG icon inside the button */
        div[data-testid="stTextInputRootElement"] svg[data-baseweb="icon"] {{
            fill: var(--primary-color);
            width: 1.2rem;
            height: 1.2rem;
            background: transparent;
        }}

        /* Change background of the show-password button to white */
        /* Common style for both Show/Hide password buttons */
        button[aria-label="Show password text"],
        button[aria-label="Hide password text"],
        button[title="Show password text"],
        button[title="Hide password text"] {{
            background-color: white !important;
            
        }}



        /* Focus effect for password input */
        div[data-testid="stTextInputRootElement"]:focus-within {{
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.15);
        }}

       
        /* ===== MOBILE RESPONSIVENESS ===== */
        @media (max-width: 768px) {{
            [data-testid="stSidebar"] {{
                padding: 0.5rem 1rem 1rem !important;
            }}
            
            /* Sidebar branding adjustments */
            .sidebar-brand {{
                padding: 0.8rem 0.8rem 0.6rem !important;  /* Reduced padding */
            }}
            .sidebar-brand span {{
                font-size: 1.1rem !important;  /* Reduced font size */
            }}
            
            /* Creators grid adjustment */
            .creators-grid {{
                grid-template-columns: 1fr !important;  /* Single column layout */
                gap: 0.8rem !important;                /* Increased spacing */
            }}
        }}
    </style>
    """

def render_sidebar():
    # Encode images for sidebar (smaller version)
    def get_small_image_base64(path, size=30):
        try:
            with open(path, "rb") as img_file:
                img_data = img_file.read()
                return base64.b64encode(img_data).decode('utf-8')
        except FileNotFoundError:
            return None

    # Get base64 encoded images
    taqi_small = get_small_image_base64("images/taqi.jpg")
    ali_small = get_small_image_base64("images/ali.jpg")
    
    with st.sidebar:
        # Compact Branding Header
        st.markdown(f"""
        <div class="sidebar-brand" style="margin: 0; padding: 1rem 1rem 0.8rem; 
                    background: linear-gradient(45deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
                    border-radius: 10px ; overflow: hidden;">  <!-- Added overflow hidden -->
            <div style="display: flex; flex-direction: column; align-items: center;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.3rem;">
                    <div style="font-size: 1.5rem; color: white;">✨</div>  <!-- Ensured white color -->
                    <span style="font-size: 1.3rem; font-weight: 700; color: white;">Smart Rehab AI</span>  <!-- White text -->
                </div>
                <p style="color: white; font-size: 0.8rem; text-align: center; margin: 0; opacity: 0.9;">  <!-- White text -->
                    Your Path to Recovery
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation with compact spacing
        st.markdown("""
        <style>
            .sidebar-nav-item {
                margin: 0.3rem 0 !important;
                border-radius: 8px !important;
                transition: all 0.2s ease;
                padding: 0.5rem 1rem !important;
            }
            .sidebar-nav-item:hover {
                background: rgba(108, 99, 255, 0.1) !important;
            }
            [data-testid="stSidebarNavItems"] {
                gap: 0.1rem !important;
            }
        </style>
        """, unsafe_allow_html=True)
        
        st.page_link("main.py", label="Home", icon="🏠", use_container_width=True)
        st.page_link("pages/01_diagnose.py", label="Self-Assessment", icon="🧠", use_container_width=True)
        st.page_link("pages/2__community.py", label="Community Stories", icon="🤝", use_container_width=True)
        st.page_link("pages/3__about.py", label="About Us", icon="ℹ️", use_container_width=True)
        st.page_link("pages/99__admin.py", label="Admin", icon="🛡️", use_container_width=True)
        
        # Thin divider with reduced spacing
        st.markdown('<div style="margin: 0.5rem 0;"></div>', unsafe_allow_html=True)
        st.divider()
        st.markdown("""
        <style>
            .creator-card {
                transition: all 0.3s ease;
            }
            .creator-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 3px 8px rgba(0,0,0,0.1);
                background: rgba(108, 99, 255, 0.06) !important;
            }
            .creator-card:nth-child(2):hover {
                background: rgba(53, 208, 186, 0.06) !important;
            }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<div style="margin: 0.3rem 0 0.5rem;">', unsafe_allow_html=True)
        st.markdown("**👑 Creators**")
        # Creators section moved up with added divider below
        
        
        # Prepare image HTML with smaller size
        taqi_img = (f'<img src="data:image/jpeg;base64,{taqi_small}" style="width: 30px; height: 30px; border-radius: 50%; object-fit: cover;">' 
                   if taqi_small else '<div style="font-size: 1.2rem;">👨‍💻</div>')
        
        ali_img = (f'<img src="data:image/jpeg;base64,{ali_small}" style="width: 30px; height: 30px; border-radius: 50%; object-fit: cover;">' 
                  if ali_small else '<div style="font-size: 1.2rem;">👨‍🎨</div>')
        
        st.markdown(f"""
        <div class="creators-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin: 0.5rem 0 0.8rem;">
            <a href="{TAQI_IG}" target="_blank" style="text-decoration: none;">
                <div class="creator-card" style="display: flex; flex-direction: column; align-items: center; 
                    background: rgba(108, 99, 255, 0.03); padding: 0.5rem; border-radius: 8px; 
                    border: 1px solid #f0f0f0;">
                    {taqi_img}
                    <span style="font-size: 0.8rem; font-weight: 500; margin-top: 0.3rem;">Taqi Kazmi</span>
                </div>
            </a>
            <a href="{ALI_IG}" target="_blank" style="text-decoration: none;">
                <div class="creator-card" style="display: flex; flex-direction: column; align-items: center; 
                    background: rgba(53, 208, 186, 0.03); padding: 0.5rem; border-radius: 8px; 
                    border: 1px solid #f0f0f0;">
                    {ali_img}
                    <span style="font-size: 0.8rem; font-weight: 500; margin-top: 0.3rem;">Ali Jamal</span>
                </div>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # End of creators section
        
        # Removed "Message us on Instagram" caption as requested
        
        # Thin light divider between creators and quote
        st.markdown('<div style="height: 1px; background: #f0f0f0; margin: 0.5rem 0;"></div>', unsafe_allow_html=True)
        
        # Compact inspirational quote
        quotes = ["Strength grows in recovery", "Every step forward matters", "You're stronger than you think"]
        st.markdown(f"""
        <div style="padding: 0.7rem 0 0.5rem;">
            <p style="font-style: italic; color: {PRIMARY_COLOR}; font-size: 0.8rem; text-align: center; margin: 0; line-height: 1.3;">
                “{random.choice(quotes)}”
            </p>
        </div>
        """, unsafe_allow_html=True)

    

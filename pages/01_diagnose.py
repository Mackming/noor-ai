# =============================
# 🧠 Addiction Diagnosis
import streamlit as st
from utils.diagnose_handler import save_diagnosis
from utils.pdf_generator import generate_pdf
from prompt_template import build_prompt
from ai_handler import generate_advice
import time
from utils.ui_utils import get_global_css, render_sidebar
from utils.load_handler import inject_loader_script
from utils.loading_screen import show_fullscreen_loader
show_fullscreen_loader()
# =============================
# 🎨 PAGE CONFIG & CONSTANTS
# =============================
st.set_page_config(
    page_title="Self-Assessment | Smart Rehabilitation AI",
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

if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# =============================
# 🎨 CUSTOM CSS INJECTION (White Theme)
# =============================
# KEEP ONLY THESE STYLES IN 01_diagnose.py

st.markdown(f"""
<style>
    /* ----- PROGRESS BAR ----- */
    .progress-container {{
        background: #f0f2f6;
        border-radius: 20px;
        padding: 0.5rem;
        margin: 1.5rem 0 2.5rem;
    }}
    
    .progress-bar {{
        height: 12px;
        border-radius: 10px;
        background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        transition: width 0.5s ease;
    }}
    
    /* ----- QUESTION CARDS ----- */
    .question-card {{
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
        border: 1px solid #f0f0f0;
    }}
    
    /* ----- RESULT SECTION ----- */
    .result-card {{
        background: white;
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 15px 30px rgba(0,0,0,0.08);
        margin: 2rem 0;
        border-top: 5px solid {SECONDARY_COLOR};
        border: 1px solid #f0f0f0;
    }}
    
    /* ----- LOADING ANIMATION ----- */
    @keyframes pulse {{
        0% {{ transform: scale(1); opacity: 0.8; }}
        50% {{ transform: scale(1.05); opacity: 1; }}
        100% {{ transform: scale(1); opacity: 0.8; }}
    }}
    
    .loading-icon {{
        font-size: 4rem;
        text-align: center;
        animation: pulse 1.5s infinite;
        color: {SECONDARY_COLOR};
        margin: 2rem 0;
    }}
    
    /* ----- SEVERITY INDICATOR ----- */
    .severity-container {{
        display: flex;
        align-items: center;
        margin: 1.5rem 0;
        padding: 1rem;
        background: #f9f9ff;
        border-radius: 12px;
        border-left: 4px solid {SECONDARY_COLOR};
    }}
    
    .severity-label {{
        font-weight: 600;
        margin-right: 1rem;
        color: {PRIMARY_COLOR};
    }}
    
    .severity-level {{
        font-weight: 700;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        background: rgba(108, 99, 255, 0.1);
    }}
    
    .severity-bar {{
        flex-grow: 1;
        height: 8px;
        background: #e0e0ff;
        border-radius: 10px;
        margin: 0 1rem;
        overflow: hidden;
    }}
    
    .severity-fill {{
        height: 100%;
        background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        border-radius: 10px;
        transition: width 0.5s ease;
    }}

    /* ----- MOBILE RESPONSIVENESS ----- */
    @media (max-width: 768px) {{
        /* Header adjustments */
        h1[style*="font-size: 2.8rem"] {{
            font-size: 2.2rem !important;
        }}
        p[style*="font-size: 1.2rem"] {{
            font-size: 1rem !important;
        }}
        
        /* Question cards */
        .question-card {{
            padding: 1.5rem;
        }}
        
        /* Progress bar */
        .progress-container {{
            margin: 1rem 0 1.5rem;
        }}
        
        /* Result card */
        .result-card {{
            padding: 1.5rem;
        }}
        
        /* Severity indicator */
        .severity-container {{
            flex-direction: column;
            align-items: flex-start;
            padding: 0.8rem;
        }}
        .severity-bar {{
            width: 100%;
            margin: 0.5rem 0;
        }}
        
        /* Final encouragement */
        div[style*="margin: 3rem 0"] {{
            margin: 1.5rem 0 !important;
            padding: 1.5rem !important;
        }}
        
        /* Form elements */
        .stTextArea textarea {{
            min-height: 150px !important;
        }}
        
        /* Recovery plan padding */
        .recovery-plan-content {{
            padding: 0 1rem !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)
# Force Streamlit to respect light mode
st.markdown("""
<script>
    document.documentElement.style.setProperty('color-scheme', 'light', 'important');
</script>
""", unsafe_allow_html=True)
st.markdown(inject_loader_script(), unsafe_allow_html=True)
# =============================
# 🧠 DIAGNOSIS HEADER (White Theme)
# =============================
if st.session_state.step < 10:  # 👈 NOW SAFE TO ACCESS
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 1rem;">
        <h1 style="font-size: 2.8rem; margin-bottom: 0.5rem; color: {PRIMARY_COLOR};">✨ Your Recovery Journey Starts Here</h1>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto; color: #555;">
            Take our confidential self-assessment to get a personalized recovery plan
        </p>
    </div>
    """, unsafe_allow_html=True)
# ---------------- Session Setup ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# ---------------- Translation Dictionary ----------------
translations = {
    "English": {
        "language_select": "Select Language",
        "age": "Your Age",
        "gender": "Gender",
        "province": "Province",
        "addiction": "What addiction do you struggle with?",
        "frequency": "How often do you use it?",
        "started": "How did your addiction start?",
        "struggles": "What happens when you try to quit?",
        "relapse": "How often do you relapse?",
        "religious_mode": "Include Islamic Guidance?",
        "submit": "Generate My Recovery Plan",
        "back": "← Back",
        "next": "Next →",
        "severity_label": "Diagnostic Score",
        "severity_level": "Severity Level",
        "download_pdf": "📥 Download Recovery Plan (PDF)",
        "severity_low": "Low",
        "severity_moderate": "Moderate",
        "severity_high": "High",
        "severity_severe": "Severe"
    },
    "Urdu": {
        "language_select": "زبان منتخب کریں",
        "age": "عمر",
        "gender": "صنف",
        "province": "صوبہ",
        "addiction": "کس قسم کی لت میں مبتلا ہیں؟",
        "frequency": "کتنی بار استعمال کرتے ہیں؟",
        "started": "لت کیسے شروع ہوئی؟",
        "struggles": "چھوڑنے کی کوشش پر کیا ہوتا ہے؟",
        "relapse": "کتنی بار دوبارہ رجوع کرتے ہیں؟",
        "religious_mode": "اسلامی رہنمائی شامل کریں؟",
        "submit": "میری بحالی کا منصوبہ حاصل کریں",
        "back": "← پچھلا",
        "next": "اگلا →",
        "severity_label": "تشخیص اسکور",
        "severity_level": "شدت کی سطح",
        "download_pdf": "📥 بحالی منصوبہ ڈاؤن لوڈ کریں (PDF)",
        "severity_low": "کم",
        "severity_moderate": "درمیانی",
        "severity_high": "زیادہ",
        "severity_severe": "شدید"
    }
}

# ---------------- Language Step ----------------
if st.session_state.step == 0:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: rgba(108, 99, 255, 0.05); 
                border-radius: 20px; margin: 2rem 0; border: 1px solid #e9ecef;">
        <h2 style="color: #6C63FF; margin-bottom: 1.5rem;">🌐 Choose Your Language</h2>
        <p style="margin-bottom: 2rem; color: #555;">Select your preferred language for the assessment</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Centered language buttons for mobile
    st.markdown('<div class="language-radio-container">', unsafe_allow_html=True)
    lang = st.radio("", ["English", "Urdu"], horizontal=True, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Start Assessment", use_container_width=True, 
                 type="primary", key="start_btn"):
        st.session_state.answers = {"language": lang}
        st.session_state.step = 1
        st.session_state.pop("recovery_plan", None)
        st.session_state.pop("pdf", None)
        st.rerun()

    st.stop()


# ---------------- Dynamic Text ----------------
def _(key):
    lang = st.session_state.answers.get("language", "English")
    return translations[lang].get(key, key)

# ---------------- Questions Flow ----------------
# 1️⃣ Detect selected language
lang = st.session_state.answers.get("language", "English")

# 2️⃣ Define bilingual options
addiction_options = {
    "English": ["Cigarettes", "Vapes", "Alcohol", "Porn", "Drugs"],
    "Urdu": [
        "Cigarettes (سگریٹ)",
        "Vapes (ویپ)",
        "Alcohol (شراب)",
        "Porn (فحش مواد)",
        "Drugs (منشیات)"
    ]
}

started_options = {
    "English": ["Peer pressure", "Stress/Depression", "Curiosity", "Loneliness", "Trauma or Abuse", "Availability of substance", "Other"],
    "Urdu": [
        "Peer pressure (دباؤ)", 
        "Stress/Depression (ذہنی دباؤ)", 
        "Curiosity (تجسس)", 
        "Loneliness (تنہائی)", 
        "Trauma or Abuse (صدمہ یا بدسلوکی)", 
        "Availability of substance (آسان دستیابی)", 
        "Other (دیگر)"
    ]
}

struggles_options = {
    "English": ["Anxiety", "Insomnia", "Cravings", "Aggression", "Depression", "Restlessness", "Headaches", "Nothing, I just relapse"],
    "Urdu": [
        "Anxiety (پریشانی)", 
        "Insomnia (نیند کی کمی)", 
        "Cravings (طلب)", 
        "Aggression (غصہ)", 
        "Depression (افسردگی)", 
        "Restlessness (بے چینی)", 
        "Headaches (سر درد)", 
        "Nothing, I just relapse (بس دوبارہ لت لگ جاتی ہے)"
    ]
}
gender_options = {
    "English": ["Male", "Female", "Other"],
    "Urdu": [
        "Male (مرد)", 
        "Female (عورت)", 
        "Other (دیگر)"
    ]
}

province_options = {
    "English": ["Punjab", "Sindh", "KPK", "Balochistan", "Islamabad"],
    "Urdu": [
        "Punjab (پنجاب)", 
        "Sindh (سندھ)", 
        "KPK (خیبر پختونخواہ)", 
        "Balochistan (بلوچستان)", 
        "Islamabad (اسلام آباد)"
    ]
}

frequency_options = {
    "English": [
        "Daily - multiple times", "Daily - once", "A few times a week", 
        "Weekly", "Monthly", "Rarely but still can't quit"
    ],
    "Urdu": [
        "Daily - multiple times (روزانہ - کئی بار)",
        "Daily - once (روزانہ - ایک بار)",
        "A few times a week (ہفتے میں چند بار)",
        "Weekly (ہفتہ وار)",
        "Monthly (ماہانہ)",
        "Rarely but still can't quit (شاذ و نادر مگر چھوڑ نہیں سکتا)"
    ]
}

relapse_options = {
    "English": ["Often", "Rarely", "Never"],
    "Urdu": [
        "Often (اکثر)", 
        "Rarely (کبھی کبھار)", 
        "Never (کبھی نہیں)"
    ]
}

# 3️⃣ Define questions using dynamic bilingual options
questions = [
    {"key": "age", "type": "selectbox", "options": [str(i) for i in range(12, 60)]},
    {"key": "gender", "type": "selectbox", "options": gender_options[lang]},
    {"key": "province", "type": "selectbox", "options": province_options[lang]},
    {"key": "addiction", "type": "multiselect", "options": addiction_options[lang]},
    {"key": "frequency", "type": "selectbox", "options": frequency_options[lang]},
    {"key": "started", "type": "multiselect", "options": started_options[lang]},
    {"key": "struggles", "type": "multiselect", "options": struggles_options[lang]},
    {"key": "relapse", "type": "selectbox", "options": relapse_options[lang]},
    {"key": "religious_mode", "type": "selectbox", "options": ["On", "Off"]},
]

# =============================
# 📊 PROGRESS BAR (White Theme)
# =============================
# Fixed total steps (language step + 9 questions)
if st.session_state.step < 10:  # 👈 NOW SAFE TO ACCESS
    # Fixed total steps (language step + 9 questions)
    total_steps = 10
    current_step = st.session_state.step
    progress_percent = (current_step / total_steps) * 100

    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-bar" style="width: {progress_percent}%"></div>
        <div class="progress-steps">
            <span>Step {current_step} of {total_steps} Complete</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =============================
# ❓ QUESTION DISPLAY (White Theme)
# =============================
current = st.session_state.step - 1

if current < len(questions):
    q = questions[current]
    
    with st.container():
        st.markdown(f"""
        <div class="question-card">
            <h2 style="color: {PRIMARY_COLOR}; margin-bottom: 1.5rem;">{_(q["key"])}</h2>
        """, unsafe_allow_html=True)
        
        if q["type"] == "selectbox":
            answer = st.selectbox("", q["options"], key=q["key"], index=0, label_visibility="collapsed")
            valid = True
        elif q["type"] == "multiselect":
            answer = st.multiselect("", q["options"], key=q["key"], label_visibility="collapsed")
            valid = len(answer) > 0
        
        st.session_state.answers[q["key"]] = answer
        
        st.markdown("</div>", unsafe_allow_html=True)  # Close question card
        
        # Navigation buttons - swapped positions
        col1, col2 = st.columns([2, 1])  # Swapped ratio
        with col1:
            if st.button(_("next"), use_container_width=True, key=f"next_{current}"):
                if valid:
                    st.session_state.step += 1
                    st.rerun()
                else:
                    st.warning("⚠️ Please answer this question before continuing.")
        with col2:
            if st.button(_("back"), use_container_width=True, key=f"back_{current}"):
                if st.session_state.step > 1:
                    st.session_state.step -= 1
                    st.rerun()
    
    st.stop()

# =============================
# 🎯 RESULTS SECTION (White Theme)
# =============================
st.markdown(f"""
<div class="result-card">
    <h2 style="color: {PRIMARY_COLOR}; margin-bottom: 1rem;">🌟 Your Personalized Recovery Plan</h2>
""", unsafe_allow_html=True)

# 4️⃣ Clean Urdu hints before saving or sending to AI
def strip_urdu_hints(selected_list):
    return [item.split(" (")[0] for item in selected_list]

# ----------- Format prompt and call Gemini ----------
# Sanitize single values if needed
gender_clean = st.session_state.answers["gender"].split(" (")[0]
province_clean = st.session_state.answers["province"].split(" (")[0]
relapse_clean = st.session_state.answers["relapse"].split(" (")[0]

user_data = {
    "name": "Anonymous",
    **st.session_state.answers,
    "addiction_details": "\n".join(
        f"Type: {a}, Frequency: {st.session_state.answers['frequency']}, Duration: Unknown"
        for a in strip_urdu_hints(st.session_state.answers["addiction"])
    ),
    "triggers": ", ".join(strip_urdu_hints(st.session_state.answers["started"])),
    "withdrawal_symptoms": ", ".join(strip_urdu_hints(st.session_state.answers["struggles"])),
    "gender": gender_clean,
    "province": province_clean,
    "relapse": relapse_clean,
    "duration": "Unknown"  # if duration not collected
}

# Generate recovery plan
if st.session_state.get("recovery_plan") is None:
    # Show loading animation
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div class="loading-icon">🧠</div>
        <h3 style="color: #6C63FF;">Creating your personalized recovery plan</h3>
        <p style="color: #555;">Our AI is analyzing your responses to build the best path forward</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate in background
    with st.spinner("Generating with neural precision..."):
        prompt = build_prompt(user_data)
        result = generate_advice(prompt)
        
        if result and "response" in result:
            st.session_state.recovery_plan = result["response"]
            if st.session_state.answers["language"] == "English":
                st.session_state.pdf = generate_pdf(
                    result["response"],
                    name="anonymous",
                    language=st.session_state.answers["language"]
                )
            st.rerun()
        else:
            st.error("❌ Failed to generate recovery plan. Please try again.")
            st.stop()

# Show existing plan from cache
severity_text = save_diagnosis(st.session_state.answers)

# Map text severity to numeric values
severity_map = {
    "Low": 30,
    "Moderate": 50,
    "High": 70,
    "Severe": 90
}

# Get numeric value or default to 50
severity_value = severity_map.get(severity_text, 50)

# Get translated severity text
severity_translation_map = {
    "Low": _("severity_low"),
    "Moderate": _("severity_moderate"),
    "High": _("severity_high"),
    "Severe": _("severity_severe")
}

# Get translated text or use original
severity_translated = severity_translation_map.get(severity_text, severity_text)

# Display severity level with visual indicator
st.markdown(f"""
<div class="severity-container">
    <div class="severity-label">{_("severity_label")}:</div>
    <div class="severity-level">{severity_value}/100</div>
    <div class="severity-bar">
        <div class="severity-fill" style="width: {severity_value}%"></div>
    </div>
    <div class="severity-label">{_("severity_level")}: {severity_translated}</div>
</div>
""", unsafe_allow_html=True)

# Added padding wrapper for recovery plan
st.markdown(
    f'<div class="recovery-plan-content">{st.session_state.recovery_plan}</div>',
    unsafe_allow_html=True
)

# PDF Download Section
st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)

if st.session_state.answers["language"] == "English":
    if st.session_state.get("pdf"):
        st.download_button(
            label=_("download_pdf"),
            data=st.session_state.pdf,
            file_name="Smart_Rehabilitation_recovery_plan.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary"
        )
    else:
        st.warning("PDF generation failed. Please try again.")
else:
    st.info("📄 اردو میں PDF بحالی منصوبہ جلد آ رہا ہے۔ براہ کرم انتظار کریں۔")

st.markdown("</div>", unsafe_allow_html=True)  # Close result card

# =============================
# 💌 FINAL ENCOURAGEMENT (White Theme)
# =============================
st.markdown(f"""
<div style="text-align: center; margin: 3rem 0; padding: 2.5rem; 
            background: linear-gradient(135deg, rgba(108, 99, 255, 0.05), rgba(53, 208, 186, 0.05)); 
            border-radius: 20px; border-left: 5px solid {SECONDARY_COLOR}; border: 1px solid #e9ecef;">
    <h3 style="color: {PRIMARY_COLOR};">Your Journey Matters</h3>
    <p style="font-size: 1.1rem; max-width: 700px; margin: 1rem auto; color: #555;">
        You've taken the first step toward recovery by completing this assessment. 
        Remember that healing is a journey, not a destination. Be patient with yourself, 
        celebrate small victories, and know that support is always available.
    </p>
    <p style="font-weight: 600; margin-top: 1.5rem; font-size: 1.1rem; color: {SECONDARY_COLOR};">
        You have the strength within you to overcome this. ✨
    </p>
</div>
""", unsafe_allow_html=True)

# Restart button
if st.button("🔄 Start New Assessment", use_container_width=True):
    st.session_state.step = 0
    st.session_state.answers = {}
    st.rerun()

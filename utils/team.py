import streamlit as st

TAQI_IG = "https://instagram.com/taqikvzmi"
ALI_IG = "https://www.instagram.com/alijamalashraf/"

def founder_section():
    with st.container():
        st.markdown("""
        <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 1rem;">
            <div style="text-align: center;">
                <a href="{0}" target="_blank">
                    <div style="width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(45deg, #6C63FF, #35D0BA); display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 2rem;">👨‍💻</div>
                    <h3>Taqi Kazmi</h3>
                </a>
            </div>
            <div style="text-align: center;">
                <a href="{1}" target="_blank">
                    <div style="width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(45deg, #f09433, #bc1888); display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 2rem;">👨‍🎨</div>
                    <h3>Ali Jamal</h3>
                </a>
            </div>
        </div>
        """.format(TAQI_IG, ALI_IG), unsafe_allow_html=True)
        
        st.markdown("""
        <p style="text-align: center; margin-top: 1.5rem; font-size: 1.1rem;">
            Message us directly on Instagram for support or feedback
        </p>
        """, unsafe_allow_html=True)
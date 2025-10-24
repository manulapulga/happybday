import streamlit as st

# Simple login check
def login_page():
    st.markdown("""
    <style>
    .login-container {
        margin-top: -50px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Curious? 📞")
    
    user_id = st.text_input("room", placeholder="Enter your user ID (all small 10 chars)")
    password = st.text_input("vroom", type="password", placeholder="Enter your password (all small 11 chars)")
    
    if st.button("i got it"):
        if user_id == "datacentre" and password == "spitivalley":
            st.session_state.logged_in = True
            st.session_state.current_page = "birthday_card"
            st.rerun()
        else:
            st.error("😕 User ID or password incorrect")

def birthday_card_page():
    # Compact birthday card styling
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');
    
    .main-container {
        margin-top: -30px;
        padding: 0;
    }
    
    .birthday-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 15px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin: 5px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .birthday-title {
        font-family: 'Dancing Script', cursive;
        font-size: 2.5rem !important;
        font-weight: 700;
        margin-bottom: 3px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .birthday-name {
        font-family: 'Poppins', sans-serif;
        font-size: 2.2rem !important;
        font-weight: 600;
        color: #FFD700;
        margin: 3px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    .birthday-message {
        font-family: 'Poppins', sans-serif;
        font-size: 0.95rem !important;
        margin: 3px 0;
        line-height: 1.3;
        max-width: 450px;
    }
    
    @keyframes glow {
        from { 
            text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #e60073; 
        }
        to { 
            text-shadow: 0 0 10px #fff, 0 0 15px #ff4da6, 0 0 20px #ff4da6; 
        }
    }
    
    .balloons {
        font-size: 1.4rem;
        margin: 2px 0;
        letter-spacing: 3px;
    }
    
    .next-btn {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 1rem;
        border-radius: 50px;
        margin-top: 10px;
        box-shadow: 0 4px 10px rgba(255,107,107,0.3);
        transition: all 0.3s ease;
    }
    
    .next-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(255,107,107,0.5);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Compact layout
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Birthday Card - directly centered without excessive columns
    st.markdown("""
    <div class="birthday-card">
        <div class="balloons">🎈🎉🎂</div>
        <div class="birthday-title">Happy BirthdayDearest Aathi</div>
        <div class="balloons">🎁✨🎊</div>
        <div class="birthday-message">
            Wishing you a day as wonderful and special as you are!<br>
            May this year bring you joy and beautiful memories!
        </div>
        <div class="balloons">💫🌟❤️</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Next button - compact placement
    if st.button("🎬 For our supergirl →", key="next_btn", use_container_width=True):
        st.session_state.current_page = "video"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def video_page():
    st.markdown("""
    <style>
    .video-page {
        text-align: center;
        margin-top: -20px;
    }
    .video-title {
        font-size: 1.8rem;
        color: #FF6B6B;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .video-container {
        margin: 10px auto;
        max-width: 800px;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        background: #000;
    }
    .back-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 0.9rem;
        border-radius: 50px;
        margin: 8px 5px;
        box-shadow: 0 4px 10px rgba(102,126,234,0.3);
    }
    .button-row {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="video-page">', unsafe_allow_html=True)
    st.markdown('<div class="video-title">With Lots of Love</div>', unsafe_allow_html=True)
    
    # Video container - simplified without the extra black card
    try:
        st.video('video.mp4')
    except FileNotFoundError:
        st.error("❌ Video file 'video.mp4' not found.")
    except Exception as e:
        st.error(f"❌ Error loading video: {str(e)}")
    
    # Compact navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Card", key="back_btn", use_container_width=True):
            st.session_state.current_page = "birthday_card"
            st.rerun()
    with col2:
        if st.button("🚪 Logout", key="logout_from_video", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_page = "birthday_card"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Happy Birthday Aathiiiii!",
        page_icon="🎂",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Hide Streamlit default elements and reduce margins
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        margin-top: -50px;
        padding-top: 0px;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stButton button {
        width: 100%;
    }
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.current_page = "birthday_card"
    
    if st.session_state.logged_in:
        if st.session_state.current_page == "birthday_card":
            birthday_card_page()
        elif st.session_state.current_page == "video":
            video_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
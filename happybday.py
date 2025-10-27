import streamlit as st
import base64

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
    
    user_id = st.text_input("who", placeholder="Enter your user ID (all small 7 chars)")
    password = st.text_input("room", type="password", placeholder="Enter your password (all small 10 chars)")
    
    if st.button("i got it"):
        if user_id == "anseena" and password == "datacentre":
            st.session_state.logged_in = True
            st.session_state.current_page = "birthday_card"
            st.rerun()
        else:
            st.error("അയ്യേ  പൂയ് പൂയ് . ")

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
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin: 30px 0;
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
        padding: 20px 20px;
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
    
    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Login", key="back_to_login", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
    with col2:
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
    .next-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 0.9rem;
        border-radius: 50px;
        margin: 8px 5px;
        box-shadow: 0 4px 10px rgba(102,126,234,0.3);
    }
    .back-btn {
        background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 0.9rem;
        border-radius: 50px;
        margin: 8px 5px;
        box-shadow: 0 4px 10px rgba(108,117,125,0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="video-page">', unsafe_allow_html=True)
    st.markdown('<div class="video-title">With Lots of Love, FoodeezZ d GWD 😋😉</div>', unsafe_allow_html=True)
    
    # Video container
    try:
        st.video('video.mp4')
    except FileNotFoundError:
        st.error("❌ Video file 'video.mp4' not found.")
    except Exception as e:
        st.error(f"❌ Error loading video: {str(e)}")
    
    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Card", key="back_to_card", use_container_width=True):
            st.session_state.current_page = "birthday_card"
            st.rerun()
    with col2:
        if st.button("Next Clue →", key="next_from_video", use_container_width=True):
            st.session_state.current_page = "ask_for_clue"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def ask_for_clue_page():
    st.markdown("""
    <style>
    .clue-page {
        text-align: center;
        margin-top: 50px;
    }
    .clue-text {
        font-size: 2rem;
        color: #FF6B6B;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .secret-input {
        margin: 20px auto;
        max-width: 400px;
    }
    .back-btn {
        background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 0.9rem;
        border-radius: 50px;
        margin: 8px 5px;
        box-shadow: 0 4px 10px rgba(108,117,125,0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="clue-page">', unsafe_allow_html=True)
    st.markdown('<div class="clue-text">ask him for the next clue</div>', unsafe_allow_html=True)
    
    # Secret word input
    secret_word = st.text_input(
        "got ? ?:", 
        placeholder="type here, 7 small",
        key="secret_word_input"
    )
    
    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Video", key="back_to_video", use_container_width=True):
            st.session_state.current_page = "video"
            st.rerun()
    with col2:
        if st.button("Enter", key="enter_secret_word", use_container_width=True):
            if secret_word.lower() == "jithesh":
                st.session_state.current_page = "youtube_clue"
                st.rerun()
            else:
                st.error("onalla")
    
    st.markdown('</div>', unsafe_allow_html=True)

def youtube_clue_page():
    st.markdown("""
    <style>
    .youtube-page {
        text-align: center;
        margin-top: 50px;
    }
    .placeholder-text {
        font-size: 1.5rem;
        color: #667eea;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .youtube-input {
        margin: 20px auto;
        max-width: 500px;
    }
    .small-image {
        max-width: 300px;
        margin: 10px auto;
    }
    .back-btn {
        background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 0.9rem;
        border-radius: 50px;
        margin: 8px 5px;
        box-shadow: 0 4px 10px rgba(108,117,125,0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="youtube-page">', unsafe_allow_html=True)
    st.markdown('<div class="placeholder-text">🎶u wanted to hear from "?"🎵</div>', unsafe_allow_html=True)
    
    # Display the 1.png image in a smaller size
    try:
        st.image('1.png', width=300)  # Adjust width as needed to match text size
    except FileNotFoundError:
        st.error("❌ Image file '1.png' not found.")
    except Exception as e:
        st.error(f"❌ Error loading image: {str(e)}")
    
    # YouTube link input (without label since the image replaces it)
    youtube_link = st.text_input(
        " ",  # Empty label since we're using the image
        placeholder="ctrl+v",
        key="youtube_link_input",
        label_visibility="collapsed"  # This hides the label completely
    )
    
    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Previous", key="back_to_previous", use_container_width=True):
            st.session_state.current_page = "ask_for_clue"
            st.rerun()
    with col2:
        if st.button("i wanna hear", key="play_youtube", use_container_width=True):
            if youtube_link == "https://www.youtube.com/watch?v=vWU3UTxkU9k&list=RDvWU3UTxkU9k&start_radio=1":
                st.session_state.current_page = "final_meeting"
                st.rerun()
            else:
                st.error("ഇതല്ല വേറെ.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def final_meeting_page():
    st.markdown("""
    <style>
    .final-page {
        text-align: center;
        margin-top: 50px;
    }
    .meet-text {
        font-size: 3rem;
        color: #FF6B6B;
        font-weight: bold;
        animation: pulse 2s infinite;
        margin-bottom: 30px;
    }
    .secret-code-input {
        margin: 20px auto;
        max-width: 300px;
    }
    .code-hint {
        font-size: 0.9rem;
        color: #666;
        margin-top: 5px;
        margin-bottom: 15px;
    }
    .next-clue-btn {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%);
        color: white;
        border: none;
        padding: 12px 25px;
        font-size: 1.1rem;
        border-radius: 50px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(255,107,107,0.4);
        transition: all 0.3s ease;
    }
    .next-clue-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255,107,107,0.6);
    }
    .back-btn {
        background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 0.9rem;
        border-radius: 50px;
        margin: 8px 5px;
        box-shadow: 0 4px 10px rgba(108,117,125,0.3);
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="final-page">', unsafe_allow_html=True)
    st.markdown('<div class="meet-text">meet at 211</div>', unsafe_allow_html=True)
    
    # Secret code input section
    st.markdown('<div class="secret-code-input">', unsafe_allow_html=True)
    secret_code = st.text_input(
        "",
        placeholder="9 small",
        key="secret_code_input",
        label_visibility="visible"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Next Clue Button - only works with correct code
    if st.button("🔍 Next Clue", key="next_clue_btn", use_container_width=True):
        if secret_code.lower() == "karokemic":
            st.session_state.current_page = "final_secret"
            st.rerun()
        else:
            st.error("പാട്ട് കേട്ടില്ലേ! എന്താ ഗിഫ്ട് ?")
    
    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to Music", key="back_to_music", use_container_width=True):
            st.session_state.current_page = "youtube_clue"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def final_secret_page():
    st.markdown("""
    <style>
    .final-secret-page {
        text-align: center;
        margin-top: 50px;
    }
    .secret-instruction {
        font-size: 1.8rem;
        color: #667eea;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .meet-text-reveal {
        font-size: 2.5rem;
        color: #FF6B6B;
        font-weight: bold;
        margin: 20px 0;
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    .what-to-do-text {
        font-size: 1.5rem;
        color: #28a745;
        font-weight: bold;
        margin: 15px 0;
    }
    .secret-input {
        margin: 25px auto;
        max-width: 400px;
    }
    .back-btn {
        background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 0.9rem;
        border-radius: 50px;
        margin: 8px 5px;
        box-shadow: 0 4px 10px rgba(108,117,125,0.3);
    }
    .what-to-do-btn {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        border: none;
        padding: 10px 25px;
        font-size: 1rem;
        border-radius: 50px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(40,167,69,0.4);
    }
    .helper-btn {
        background: linear-gradient(135deg, #FFA500 0%, #FFD700 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 0.9rem;
        border-radius: 50px;
        margin: 10px 5px;
        box-shadow: 0 4px 12px rgba(255,165,0,0.3);
        transition: all 0.3s ease;
    }
    .helper-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(255,165,0,0.5);
    }
    .helper-hint {
        background: linear-gradient(135deg, #FFF3CD 0%, #FFEAA7 100%);
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #FFA500;
        margin: 15px auto;
        max-width: 500px;
        text-align: left;
    }
    .hint-title {
        color: #856404;
        font-weight: bold;
        margin-bottom: 8px;
        font-size: 1.1rem;
    }
    .hint-text {
        color: #856404;
        font-size: 0.95rem;
        line-height: 1.4;
    }
    @keyframes glow {
        from { 
            text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #FF6B6B; 
        }
        to { 
            text-shadow: 0 0 10px #fff, 0 0 20px #FF6B6B, 0 0 25px #FF6B6B; 
        }
    }
    .meet-text {
        font-size: 3rem;
        color: #FF6B6B;
        font-weight: bold;
        animation: pulse 2s infinite;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="final-secret-page">', unsafe_allow_html=True)
    st.markdown('<div class="meet-text">കഴിഞ്ഞു ലാസ്റ്റ് </div>', unsafe_allow_html=True)
    
    
    # Check if secret word is correct and show the reveal
    if 'secret_revealed' not in st.session_state:
        st.session_state.secret_revealed = False
    
    # Check if helper hint is shown
    if 'show_helper_hint' not in st.session_state:
        st.session_state.show_helper_hint = False
    
    # Secret word input
    st.subheader("vroom")
    secret_word = st.text_input(
        "Secret Word:", 
        placeholder="11",
        key="final_secret_input",
        label_visibility="collapsed"
    )
    
    
    # Main action buttons
    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        if st.button("🔙 Back", key="back_from_final", use_container_width=True):
            st.session_state.current_page = "final_meeting"
            st.rerun()
    
    with col2:
        if st.button("🎯 What to do?", key="what_to_do_btn", use_container_width=True):
            if secret_word.lower() == "spitivalley":
                st.session_state.secret_revealed = True
                st.rerun()
            else:
                st.error("olalla")
    
    with col3:
        if st.button("💡 Ask Coder", key="ask_coder_btn", use_container_width=True):
            st.session_state.show_helper_hint = not st.session_state.show_helper_hint
            st.rerun()
    
    # Display helper hint if requested
    if st.session_state.show_helper_hint:
        st.markdown("""
        <div class="helper-hint">
            <div class="hint-title">💡 Coder's Hint:</div>
            <div class="hint-text">
                <strong>unscramble miotsidomo and whatsapp me for the clue</strong><br><br>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display the reveal if secret is correct
    if st.session_state.secret_revealed:
        # Encode image 2.png to base64 so it displays inline
        try:
            with open("2.png", "rb") as f:
                img_data = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
        except Exception:
            img_data = None
    
        if img_data:
            st.markdown(f"""
                <div class="meet-text-reveal">
                    MEET <img src="{img_data}" alt="moment" 
                    style="height: 100px; vertical-align: middle; margin-left: 10px;">
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="meet-text-reveal">MEET moment</div>', unsafe_allow_html=True)
    
        st.markdown('<div class="what-to-do-text">and collect ur 1st moment</div>', unsafe_allow_html=True)
        
        # Celebration
        st.balloons()
        st.success("It’s a canvas where we can portray our friendship.")

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
        elif st.session_state.current_page == "ask_for_clue":
            ask_for_clue_page()
        elif st.session_state.current_page == "youtube_clue":
            youtube_clue_page()
        elif st.session_state.current_page == "final_meeting":
            final_meeting_page()
        elif st.session_state.current_page == "final_secret":
            final_secret_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
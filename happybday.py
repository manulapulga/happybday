import streamlit as st
import hashlib

def check_password():
    """Returns `True` if the user had the correct password."""
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        # Hash the password to compare with stored hash
        user_hash = hashlib.sha256(st.session_state["user_id"].encode()).hexdigest()
        password_hash = hashlib.sha256(st.session_state["password"].encode()).hexdigest()
        
        # Check credentials (user: datacentre, password: spitivalley)
        if (user_hash == "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3" and 
            password_hash == "c6a66b4256a6b67d3463a7e0e6f3c2e5c63c3a5c3a3a3a3a3a3a3a3a3a3a3a3a"):
            st.session_state["password_correct"] = True
            st.session_state["user"] = st.session_state["user_id"]
            del st.session_state["password"]  # Don't store password
            del st.session_state["user_id"]
        else:
            st.session_state["password_correct"] = False

    # First run, show inputs for username and password.
    if "password_correct" not in st.session_state:
        st.title("🔐 Login Page")
        st.text_input("User ID", key="user_id", placeholder="Enter your user ID")
        st.text_input("Password", type="password", key="password", placeholder="Enter your password")
        st.button("Login", on_click=password_entered)
        return False
    
    # Password incorrect.
    elif not st.session_state["password_correct"]:
        st.title("🔐 Login Page")
        st.text_input("User ID", key="user_id", placeholder="Enter your user ID")
        st.text_input("Password", type="password", key="password", placeholder="Enter your password")
        st.button("Login", on_click=password_entered)
        st.error("😕 User ID or password incorrect")
        return False
    
    # Password correct.
    else:
        return True

def main():
    st.set_page_config(
        page_title="Secure Video Player",
        page_icon="🔐",
        layout="centered"
    )
    
    if check_password():
        # User is authenticated
        st.success(f"Welcome {st.session_state['user']}! ✅")
        st.title("🎬 Video Player")
        st.write("You have successfully logged in. Enjoy the video!")
        
        # Play the video
        try:
            # For GitHub deployment, make sure video.mp4 is in the same directory
            video_file = open('video.mp4', 'rb')
            video_bytes = video_file.read()
            
            st.video(video_bytes)
            st.write("Video is playing...")
            
        except FileNotFoundError:
            st.error("❌ Video file 'video.mp4' not found. Please make sure the video file is in the same directory as this script.")
        except Exception as e:
            st.error(f"❌ An error occurred while loading the video: {str(e)}")
        
        # Logout button
        if st.button("Logout"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()
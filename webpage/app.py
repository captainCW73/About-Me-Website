import os
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My First Website", page_icon=":rocket:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#USE LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

current_dir = os.path.dirname(__index__ if "__index__" in locals() else __file__)
css_path = os.path.join(current_dir, "style", "style.css")
img_path = os.path.join(current_dir, "images", "image-removebg-preview.png")

local_css(css_path)

## ---------HEADER SECTION ---------
with st.container():
    st.subheader("Hi, I am Chase :wave:")
    st.title("A Student learning to code and creating robotics projects :robot:")
    st.write("Welcome to my website! I am a student who is passionate about coding and robotics. Here, you can find some of my projects and learn more about me.")
    st.write("Feel free to explore and reach out if you have any questions! :smile:")
    st.write("You can also check out my GitHub profile for more projects and code samples at [GitHub](https://github.com/captainCW73?tab=repositories).")

#-------LOAD ASSETS ---------
lottie_coding = load_lottieurl("https://lottie.host/60776700-327c-45c7-85d2-2e1de862ed59/o8anp3L55H.json")  
img_traffic_light = Image.open(img_path)

 #-------WHAT I DO SECTION ---------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
            """
            I am a student who is passionate about coding and robotics. I have experience in Python and  and I am always looking to learn new programming languages and technologies. 
            I have worked on several projects, including a traffic ligh system, coded multiple apps, and am currently working on a transcription device.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#-------PROJECTS SECTION ---------
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_traffic_light)
    with text_column:
        st.subheader("Explore my traffic light project")
        st.write("""
        This is a project meant to find ways to prevent yellow light speeding crashes.
        In my current iteration, im using 2 ultrasonic sensors.
        They are set at a set distance, and i can time cars by seeing how long it takes them to cross through the 2 sensors.
""")
        
#-----CONTACT-----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")

    #Documentation !!! CHANGE EMAIL ADDRESS
    contact_form = """<form action="https://formsubmit.co/chasewong2012@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
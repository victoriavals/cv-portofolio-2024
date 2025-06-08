import streamlit as st
from PIL import Image

# Config halaman
st.set_page_config(page_title="CV Naufal Firdaus", page_icon="📄", layout="wide")

# Load foto profil
img = Image.open("assets/profile.png")

# Kolom foto dan biodata
col1, col2 = st.columns([1, 3])
with col1:
    st.image(img, width=200)
with col2:
    st.title("Naufal Firdaus")
    st.write("📍 Jakarta | 📞 +62 87838882802 | ✉️ naufalfirdaus282@gmail.com")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/naufalfirdauss/)")

st.markdown("---")

# Tentang Saya
st.subheader("🧑‍💻 About Me")
st.write("""
I am Naufal Firdaus, a Firmware Engineer with a Bachelor's in Electrical Engineering from UPN Veteran Jakarta 
and currently pursuing a Master's in Computer Science. I have experience in developing embedded systems using STM32, ESP32, and Orange Pi, and I’m passionate about AI and Machine Learning.
""")

# Pendidikan
st.subheader("🎓 Education")
st.markdown("""
- **Master of Computer Science** – Universitas Esa Unggul (2024 - now)  
- **Bachelor of Electrical Engineering** – UPN Veteran Jakarta (2020 - 2024) – GPA: 3.85  
- **Internet of Things Engineer Camp** – Indobot Academy (2022)
""")

# Pengalaman Kerja
st.subheader("💼 Work Experience")
st.markdown("""
- **Firmware Engineer** – PT. Tata Sarana Mandiri (2024 - now)  
- **Robotic Event Manager** – PT. Taman Teknologi Nusantara (2024)  
- **Various Laboratory Assistant Roles** – UPN Veteran Jakarta (2021–2023)
""")

# Organisasi
st.subheader("👥 Organizational Experience")
st.markdown("""
- **Leader** – KSM Internet of Things UPNVJ  
- **Head of Research & Technology** – KSM Mechatronics  
- **Member** – Himpunan Mahasiswa Teknik Elektro
""")

# Pelatihan
st.subheader("📚 Training")
st.markdown("""
- **IoT Engineer Camp** – Indobot Academy  
- **Multiple hands-on robotics and microcontroller-based trainings**
""")

# Prestasi
st.subheader("🏆 Achievements")
with st.expander("Show Achievements"):
    st.markdown("""
    - 1st Place in 7+ National Scientific Competitions  
    - Best Presentation in Gravity Festival 2024  
    - Runner-up in multiple robotics & essay competitions  
    - Student with the Most Achievements – UPN Veteran Jakarta 2023
    """)

# Skill
st.subheader("🛠️ Skills")
st.markdown("""
- **Programming:** Python, C++, Arduino IDE  
- **Embedded Systems:** STM32, ESP32, Orange Pi  
- **Tools:** Microsoft Office, Jupyter, Git, PLC  
- **Domains:** Robotics, IoT, AI, Data Visualization
""")

# Portofolio
st.markdown("[🔗 Link to Portfolio](https://bit.ly/PortofolioNaufalFirdausJune2024)")

st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
# 
import random
import streamlit as st 
from datetime import datetime

st.set_page_config(page_title = "Funny Fake News", layout = "centered")


celebrities = [
    "Donald Trump", "Kim Kardashian", "Shah Rukh Khan", "Lionel Messi",
    "Aamir Liaquat's Ghost", "A Technology Teacher", "A confused AI robot"
]

default_actions =  [
    "ne chai mein biscuit dooba kar dooba diya",
    "ne galti se fridge ko hi password laga diya",
    "ne university ki canteen ko VIP lounge declare kar diya",
    "ne apni bike ko aeroplane samajh kar udaane ki koshish ki",
    "ne aik din mein 15 plate biryani khaa kar world record bana diya",
    "ne mobile charging pe laga kar usay salam kiya",
    "ne apne teacher ko 'Bro' bula diya",
    "ne class ke beech mein selfie session start kar diya",
    "ne shopping mall mein 'ghar ka saman' puchna shuru kar diya",
    "ne khud ko 'future ka Elon Musk' announce kar diya"
]

default_places = [
    "Faisal Masjid ke bahar",
    "Androon Lahore ke aik chhote dhabay par",
    "Saddar ke beech traffic jam mein",
    "Gulshan ke falooda point par",
    "university ke guard room ke samne",
    "Metro bus station par",
    "apni gali ke corner par",
    "KFC ke drive-thru mein",
    "PIA ke khali office mein",
    "Liaqatabad ke anda paratha stall par"
]

default_twists = [
    "aur phir kehne laga ke ye sab aik prank tha.",
    "jis par awam ne sirf 'hmm' kar ke reaction diya.",
    "aur social media ne isay full fake declare kar diya.",
    "lekin akhir mein usay bhook lag gayi.",
    "aur pass kharay uncle ne sab record kar liya.",
    "aur phir sab log hans hans kar pagal ho gaye.",
    "lekin police ne kaha 'bhai ghar jao, araam karo'.",
    "aur uske baad WiFi bhi kaam karna band ho gaya.",
    "aur news channels ne isay breaking news bana diya.",
    "lekin ghar ja kar mummy ne dant diya."
]
# ---------- Helper function ----------
def generate_headline(subject, action_list, place_list, twist_list):
    action = random.choice(action_list)
    place = random.choice(place_list)
    twist = random.choice(twist_list)
    headline = f"{subject} {action} {place}, {twist}"
    return " ".join(headline.split())

# Add UI Title + Sidebar subject selection

# ---------- UI ----------
st.title("Funny Fake news Generator")
st.caption("Make silly headlines for fun — ye sab sirf mazaak ke liye 😂")

st.sidebar.header("Setting")

subject_option = st.sidebar.radio(
    "Select subject type",
    ("Celebrity Name", "Random Character", "Custom")
)

if subject_option == "Celebrity Name": 
    subject = st.sidebar.selectbox(
    "Choose celebrity",
    ["Donald Trump", "Haroon", "Shah Rukh Khan","Aamir Liaquat's Ghost", "Miss SAima Sipy", "Amir", "Zahoor"]
    )
elif subject_option == "Random Character": 
    subject = st.sidebar.selectbox(
        "Choose Character",
       [ "Donald Trump", "Kim Kardashian", "Shah Rukh Khan", "Lionel Messi",
    "Aamir Liaquat's Ghost", "A Technology Teacher", "A confused AI robot", "Amir", "Haroon", "Zahoor"]
    )

else: 
    subject = st.sidebar.text_input("Enter custom subject:", "Koi Shakhs")
num = st.sidebar.slider("Number of headlines:", 1, 20, 5)

# Generate button
if st.button("Generate Funny Headlines"):
    st.subheader("😂 Generated Fake News Headlines:")

    headlines = []
    for i in range(num):
        h = generate_headline(subject, default_actions, default_places, default_twists)
        headlines.append(h)
        st.write(f"🗞️ {h}")

    # Download as .txt
    txt = "\n".join(headlines)
    filename = f"funny_news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    st.download_button(
        "📥 Download Headlines (.txt)",
        data=txt,
        file_name=filename,
        mime="text/plain"
    )
# Footer / disclaimers
st.markdown("---")
st.write("⚠️ Ye sirf fun ke liye hai — kabhi bhi kisi shakhsiyat ya haqeeqi event ke khilaf ghalat khabrein phailana theek nahi. Respect karain 🙂")

# Optional: small credits
st.markdown("Made with ❤️ Waqar Ahmed.")

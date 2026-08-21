import streamlit as st
import datetime
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def asset_path(filename):
    # Handles both layouts: images next to app.py, or inside an assets/ subfolder.
    candidates = [
        os.path.join(BASE_DIR, filename),
        os.path.join(BASE_DIR, "assets", filename),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return candidates[0]  # fallback, will trigger the "not found" warning downstream

st.set_page_config(
    page_title="Ragini's Birthday HQ",
    page_icon="🎂",
    layout="wide",
)

# ---------- STYLE ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
    .main {
        background: linear-gradient(135deg, #fff5f7 0%, #fff0e6 100%);
    }
    .big-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #ff6b6b, #f9844a, #ff8fa3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #6b5b73;
        margin-top: 0;
    }
    .card {
        background: white;
        border-radius: 18px;
        padding: 1.3rem 1.6rem;
        box-shadow: 0 4px 18px rgba(0,0,0,0.06);
        margin-bottom: 1rem;
        border-left: 6px solid #ff9aa2;
    }
    .certificate {
        background: #fffaf0;
        border: 3px dashed #f4a261;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
    }
    .quote-box {
        background: #2d2d3a;
        color: #fdf6ff;
        border-radius: 16px;
        padding: 1.5rem;
        font-style: italic;
        font-size: 1.05rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<p class="big-title">🎉 Happy Birthday, Ragini Bhandekar! 🎂</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Warning: emotional honesty and light roasting incoming. Proceed with cake.</p>', unsafe_allow_html=True)
st.write("")

col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if st.button("🎈 Release the balloons"):
        st.balloons()
with col_btn2:
    if st.button("❄️ Make it extra (snow)"):
        st.snow()
with col_btn3:
    if st.button("🎲 Random Ragini Fact"):
        facts = [
            "Scientifically incapable of arriving before the event has already started.",
            "Has given more relationship advice than most licensed therapists, unlicensed but undefeated.",
            "Peak productivity hours: 1 AM–4 AM. Do not schedule anything important before noon.",
            "Belgian waffles are not a food group to her. They are a personality trait.",
            "Knows everyone's business before they've told their own mother.",
            "Used to argue like her life depended on winning. Spoiler: it usually didn't, but she won anyway.",
        ]
        st.info(random.choice(facts))

st.write("---")

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs(["💌 Messages", "📸 Photo Gallery", "🏆 Official Stats"])

# ---------- TAB 1: MESSAGES ----------
with tab1:
    st.subheader("A few things I need to say, on the record")

    st.markdown("""
    <div class="card">
    <b>1. The Sweet One 🍰</b><br>
    Happy birthday to the one person who somehow knows me better than I know myself,
    despite me being famously terrible at talking about my feelings. You didn't just become
    important to me by accident — you earned it, one late-night rant, one "you're overthinking
    this" and one "okay but here's what you should actually do" at a time. I don't say it enough,
    so I'll say it here where it's basically permanent: thank you for making me a more emotional,
    more open, better version of myself. That's rare. That's you.
    </div>

    <div class="card">
    <b>2. The Sarcastic One 😏</b><br>
    Happy birthday to the woman who has never once been on time to anything, ever, including
    possibly her own birth. Another year older, still zero minutes earlier. But hey — you make up
    for it by being the unofficial Chief Gossip Officer, Head Waffle Consultant, and Senior Director
    of Everyone's Love Lives. Truly, a well-rounded résumé.
    </div>

    <div class="card">
    <b>3. The Grateful One 🙏</b><br>
    Out of everyone in my life, you're the one person I chose to let in, on my own, without being
    asked. That says everything. Thank you for the lessons, the patience, the 2 AM conversations,
    and for never letting me get away with lying to myself. I don't say this enough, so consider
    this the official record: I'm lucky to have you in my corner, and I don't take that for
    granted.
    </div>

    <div class="card">
    <b>4. The Short & Chaotic One ⚡</b><br>
    Older, wiser, still late, still dramatic about the smallest inconveniences, still somehow the
    most reliable person in everyone's life. Make it make sense. Happy birthday, Ragini. Go eat a
    waffle, you've earned it.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="quote-box">
    "Some people bring you soup when you're sick. Ragini brings you a 45-minute pep talk on why
    you deserve better and a very confident action plan — and yes, she'll probably show up
    fashionably late to deliver it. But she shows up. Every single time."
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #a8edea 0%, #fed6e3 50%, #ffd3a5 100%);
        border-radius: 20px;
        padding: 1.8rem 2rem;
        margin-top: 0.5rem;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    ">
    <h4 style="margin-top:0;">🌟 And the part I actually mean, no jokes attached</h4>
    <p style="font-size:1.02rem; line-height:1.6; color:#3a3a3a;">
    Jokes and lateness statistics aside — you've built a genuinely good life for yourself, and
    anyone who knows you knows how much of that is because of how hard you work at it, quietly,
    without needing applause for it. So here's to more of that: more wins that make you proud,
    more peace in your relationships, people around you who actually deserve your energy, and a
    partner someday who matches the way you show up for everyone else — loyal, warm, a little
    dramatic in the best way, and completely unbothered by your 1 AM texting schedule. You've
    already given so much good to the people lucky enough to know you. May this year hand some of
    it right back to you. Happy birthday, Ragini — the world's most reliable person is allowed a
    little chaos on her own special day. 🎂💛
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------- TAB 2: PHOTO GALLERY ----------
with tab2:
    st.subheader("Exhibit A and Exhibit B")
    st.caption("Presented as evidence that she is, in fact, always effortlessly put together — unlike her punctuality.")

    c1, c2 = st.columns(2)
    with c1:
        p1 = asset_path("ragini_1.jpg")
        if os.path.exists(p1):
            st.image(p1, use_container_width=True,
                      caption="Serving looks, probably 20 minutes late to wherever this was taken.")
        else:
            st.warning("Couldn't find ragini_1.jpg — make sure the 'assets' folder is uploaded alongside app.py.")
    with c2:
        p2 = asset_path("ragini_2.jpg")
        if os.path.exists(p2):
            st.image(p2, use_container_width=True,
                      caption="Living her best palm-tree, main-character-energy life.")
        else:
            st.warning("Couldn't find ragini_2.jpg — make sure the 'assets' folder is uploaded alongside app.py.")

# ---------- TAB 3: STATS ----------
with tab3:
    st.subheader("Official, Rigorously Unverified Statistics")

    colA, colB, colC = st.columns(3)
    colA.metric("Times on time to class", "0", "-100% (all-time)")
    colB.metric("Belgian waffles consumed", "∞", "still counting")
    colC.metric("Relationship cases solved", "1,000+", "pro bono")

    colD, colE, colF = st.columns(3)
    colD.metric("Arguments once fought", "All of them", "retired undefeated")
    colE.metric("Reliability rating", "10/10", "the one stat that's real")
    colF.metric("Average bedtime", "2:25 AM", "on a good night")

    st.write("---")
    st.markdown('<div class="certificate">', unsafe_allow_html=True)
    st.markdown("### 🏅 Certificate of Chaotic Excellence")
    st.markdown(f"""
    This certifies that **Ragini Bhandekar** has, for another full year, successfully combined
    being perpetually late, occasionally dramatic, endlessly reliable, and secretly one of the
    most emotionally intelligent people around — into one very entertaining human being.

    Awarded on this day, {datetime.date.today().strftime('%B %d, %Y')}, with full honors and zero
    punctuality points.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.markdown(
    "<p style='text-align:center; color:#a08c99;'>Made with way too much love (and a little bit of sarcasm) 💗</p>",
    unsafe_allow_html=True
)

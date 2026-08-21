import streamlit as st
import datetime
import random

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
tab1, tab2, tab3, tab4 = st.tabs(["💌 Messages", "📸 Photo Gallery", "📖 Anecdotes & Legends", "🏆 Official Stats"])

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
    You're not my girlfriend, never will be, and honestly that's kind of the point — because what
    we have doesn't need a label to matter. You're the one person I chose to let in, on my own,
    without being asked. That says everything. Thank you for the lessons, the patience, the 2 AM
    conversations, and for never letting me get away with lying to myself. Here's to another year
    of you being annoyingly right about everything.
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
    "Some people bring you soup when you're sick. Ragini brings you a 45-minute monologue on why
    you deserve better, a strong opinion about your ex, and probably shows up late to do it —
    but she shows up. Every single time."
    </div>
    """, unsafe_allow_html=True)

# ---------- TAB 2: PHOTO GALLERY ----------
with tab2:
    st.subheader("Exhibit A and Exhibit B")
    st.caption("Presented as evidence that she is, in fact, always effortlessly put together — unlike her punctuality.")

    c1, c2 = st.columns(2)
    with c1:
        st.image("assets/ragini_1.jpg", use_container_width=True,
                  caption="Serving looks, probably 20 minutes late to wherever this was taken.")
    with c2:
        st.image("assets/ragini_2.jpg", use_container_width=True,
                  caption="Living her best palm-tree, main-character-energy life.")

# ---------- TAB 3: ANECDOTES ----------
with tab3:
    st.subheader("The Ragini Cinematic Universe")

    with st.expander("📞 The Encyclopedia of Feelings", expanded=True):
        st.write("""
        There is no relationship question — situationship, friendship, family drama, "does he like
        me or is he just like that" — that Ragini cannot analyze with the confidence of someone who
        minored in Human Emotions. She doesn't just give advice, she builds you a whole case file.
        Ask her one question and get a full TED talk, complete with precedent from three other
        people's love lives for context.
        """)

    with st.expander("⚔️ The Retired Undefeated Debate Champion"):
        st.write("""
        There used to be a time when Ragini would go to war over literally any disagreement —
        no argument too small, no ground ever conceded. You didn't win against her; you simply
        ran out of energy before she did. These days she's mellowed out a bit (a bit), but everyone
        who knew her back then still flinches slightly when she says "actually...".
        """)

    with st.expander("🧇 The Waffle Situation"):
        st.write("""
        Belgian waffles aren't a craving for Ragini, they're basically a love language. Suggest
        literally any place that serves them and watch her entire schedule rearrange itself
        around it — the one time she'll actually try to show up early.
        """)

    with st.expander("🌙 The Nocturnal Lifestyle"):
        st.write("""
        Text her at 2 PM: seen, no reply, she's asleep. Text her at 2 AM: instant reply, fully
        alert, ready to discuss everything from your childhood trauma to what she watched on
        Netflix at 1 AM. Her sleep schedule runs on its own time zone, and honestly, it works
        for her.
        """)

    with st.expander("💛 The Reliable One"):
        st.write("""
        For someone who is dramatic about the small stuff and can never make it anywhere on time,
        Ragini has never once failed to show up when it actually mattered. That's the real plot
        twist of the Ragini Cinematic Universe — chaos on the surface, absolutely rock-solid
        underneath.
        """)

# ---------- TAB 4: STATS ----------
with tab4:
    st.subheader("Official, Rigorously Unverified Statistics")

    colA, colB, colC = st.columns(3)
    colA.metric("Times on time to class", "0", "-100% (all-time)")
    colB.metric("Belgian waffles consumed", "∞", "still counting")
    colC.metric("Relationship cases solved", "1,000+", "pro bono")

    colD, colE, colF = st.columns(3)
    colD.metric("Arguments once fought", "All of them", "retired undefeated")
    colE.metric("Reliability rating", "10/10", "the one stat that's real")
    colF.metric("Average bedtime", "12:47 AM", "on a good night")

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

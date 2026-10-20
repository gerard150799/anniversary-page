import os
import random
import streamlit as st

# ====== EDIT THESE ======
HER_NAME = "Kyle Chrysler Belino Panaguiton"
YOUR_NAME = "Gerard Peters"
DINNER_TIME = "7:00 PM"          # Malaysia & Philippines share the same time (UTC+8)
SONG_FILE = "keshi - UNDERSTAND (Visualizer).mp3"           # put your song in the same folder as app.py
# ========================

st.set_page_config(page_title="Happy Anniversary 💌", page_icon="🌹", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Pinyon+Script&display=swap');
:root { --crimson:#5E0B1A; --deep:#7A1022; --pink:#F7A8B8; --blush:#FFD6DF; --ivory:#FFE9EE; }
header[data-testid="stHeader"], footer, #MainMenu { display:none; }
.stApp { background: radial-gradient(ellipse at top, #8E1429 0%, #5E0B1A 60%, #3F0610 100%); }
html, body, [class*="css"], p, li { font-family:'Cormorant Garamond', serif; color:var(--ivory); font-size:1.2rem; }
.block-container { max-width: 640px; padding-top: 2.5rem; }
.script { font-family:'Pinyon Script', cursive; color:var(--pink); text-align:center; font-size:3.4rem; line-height:1.1; margin:0; }
.kicker { text-align:center; font-style:italic; color:var(--blush); letter-spacing:.04em; }
.card { border:1px solid var(--pink); outline:1px solid rgba(247,168,184,.35); outline-offset:6px;
        background:rgba(255,233,238,.05); padding:2.2rem 1.8rem; margin:1.6rem 0; text-align:center; }
.card p { line-height:1.7; }
h2 { font-family:'Cormorant Garamond', serif !important; font-weight:600 !important; color:var(--pink) !important; text-align:center; font-style:italic; }
.rule { text-align:center; color:var(--pink); letter-spacing:.6em; margin:1.8rem 0; }
.sched { border-left:2px solid var(--pink); padding:.2rem 0 .2rem 1.2rem; margin:1.2rem 0; }
.sched b { color:var(--pink); font-weight:600; }
.pick { border:1px dashed var(--pink); background:rgba(247,168,184,.12); padding:1.2rem; text-align:center;
        font-style:italic; font-size:1.35rem; margin-top:1rem; }
.sign { font-family:'Pinyon Script', cursive; color:var(--pink); font-size:2.2rem; text-align:right; margin-top:1.2rem; }
div.stButton { text-align:center; }
div.stButton > button { background:var(--pink); color:#5E0B1A; border:none; border-radius:0; padding:.7rem 2rem;
        font-family:'Cormorant Garamond', serif; font-size:1.2rem; font-weight:600; letter-spacing:.05em; }
div.stButton > button:hover { background:var(--blush); color:#5E0B1A; }
div.stButton > button:focus-visible { outline:2px solid var(--blush); outline-offset:3px; }
</style>
""", unsafe_allow_html=True)

DARES = [
    "Show me your best 'I'm not crying' face. Judges are strict.",
    "Compliment me without using the word 'handsome'. Go.",
    "Describe our first date as a dramatic movie trailer.",
    "Tell me one thing I do that annoys you, then say you love it anyway.",
    "Dance for 30 seconds on camera. No cheating, I'm watching.",
    "Rank me against your other boyfriends. (There are none. Right?)",
    "Plan our dream trip. Whoever picks the more expensive place pays. Kidding. Maybe.",
    "Sing one line of our song. Off-key is mandatory.",
    "Tell me what you'd order for me at a fancy restaurant.",
    "Say three things you miss about me. The cheesy ones count double.",
]

if "opened" not in st.session_state:
    st.session_state.opened = False
if "pick" not in st.session_state:
    st.session_state.pick = None

# ---------- Gate (the tap also lets the music start) ----------
if not st.session_state.opened:
    st.markdown("<div style='height:18vh'></div>", unsafe_allow_html=True)
    st.markdown(f"<p class='script'>For {HER_NAME}</p>", unsafe_allow_html=True)
    st.markdown("<p class='kicker'>Something small, from far away, with all my love.</p>", unsafe_allow_html=True)
    st.markdown("<div class='rule'>♥</div>", unsafe_allow_html=True)
    if st.button("Open your card 💌"):
        st.session_state.opened = True
        st.rerun()
    st.stop()

# ---------- Music ----------
if os.path.exists(SONG_FILE):
    st.audio(SONG_FILE, loop=True, autoplay=True)
    st.caption("🎵 Our song is playing. You can pause it above if you like.")

# ---------- 1. Greeting card ----------
st.markdown("<p class='script'>Happy Anniversary Mahal</p>", unsafe_allow_html=True)
st.markdown("<p class='kicker'>One year of us</p>", unsafe_allow_html=True)
st.markdown(f"""
<div class='card'>
<p>My dearest {HER_NAME},</p>
<p>A whole year ago, you became my favourite person, the one who I will always choose and love forever until we cease to be. Through every eep call, through every date night, 
through moments where we do not understand each other, 
I would like to always do it with you forever and ever.</p>
<p>Today, I celebrate you. I celebrate us.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='rule'>♥ ♥ ♥</div>", unsafe_allow_html=True)

# ---------- 2. Itinerary ----------
st.markdown("## Tonight's Itinerary")
st.markdown(f"""
<div class='sched'><b>{DINNER_TIME} · Dinner on Discord</b><br>
We're gonna stuff ourselves with our favourite foods!</div>
<div class='sched'><b>After dinner · The Wheel</b><br>
We spend the evening in each other's company with small activities, chosen by the wheel.
The wheel is fair. The wheel is your favourite.</div>
<div class='sched'><b>Dress code · Elegant</b><br>
Dress like we're across the table at a fancy restaurant. I will be doing the same. Wear your best dress yea</div>
""", unsafe_allow_html=True)

# ---------- The wheel ----------#
#st.markdown("### 🎡 Spin the Wheel")
#if st.button("Spin it, if you dare"):
    #options = [d for d in DARES if d != st.session_state.pick]
    #st.session_state.pick = random.choice(options)
#if st.session_state.pick:
    #st.markdown(f"<div class='pick'>{st.session_state.pick}</div>", unsafe_allow_html=True)

#st.markdown("<div class='rule'>♥ ♥ ♥</div>", unsafe_allow_html=True)#

# ---------- 3. Anniversary wish ----------
st.markdown("## My Wish For Us")
st.markdown(f"""
<div class='card'>
<p>I wish for more mornings seeing you sleeping on my screen,
and more nights that end with goodnight as we sleep in call.</p>
<p>I wish for the day the distance becomes a story we tell,
instead of something we live.</p>
<p>Until then, I will keep loving you, choosing you and be with you every single day.</p>
<p><i>Happy first anniversary, Aking Sinta.</i></p>
<div class='sign'>Ya Nerdy Caring Overthinker Boi, {YOUR_NAME}</div>
</div>
""", unsafe_allow_html=True)

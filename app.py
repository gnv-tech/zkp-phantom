import streamlit as st
from something import collatz

st.set_page_config (
    page_title="cyclone",
    page_icon="🌀",
    layout="centered"
)

st.sidebar.title("CYcloNe")
st.sidebar.caption("it will strike you for sure!")
st.sidebar.divider()

page = st.sidebar.selectbox(
    "Navigate",
    [
        "Road",
        "1. Collatz Conjecture"
    ]
)

if page == "Road":
    st.title("Ready?")
    st.markdown("""....""")
    st.info("have fun interpreting the cyclone!")

elif page == "1. Collatz Conjecture":
    st.title("The Collatz Conjecture")
    collatz.render()

else:
    st.error("Stay tuned for a cyclone!")


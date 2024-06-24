import streamlit as st

def Home():
    st.header('Home')

def Basketball():
    st.header('Basketball')

def Tennis():
    st.header('Tennis')

pg = st.navigation(
    [
        st.Page(Home),
        st.Page(Basketball),
        st.Page(Tennis)
    ]
)
pg.run()

import streamlit as st
from icebreaker import ice_break

def start_app():
    st.set_page_config(page_title="Icebreaker", page_icon=":speech:")
    st.title("Icebreaker")
    name = st.text_input("Enter a name to search for ")
    if st.button("Search"):
        with st.spinner("Processing ..."):
            if name is not None:
                result = ice_break(name)
                if result:
                    st.json(result)
            
if __name__ == "__main__":
    start_app()
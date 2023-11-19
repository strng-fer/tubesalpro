import streamlit as st
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ("Login", "Homepage"))

    if selection == "Login":
        login_app.run()
    elif selection == "Homepage":
        homepage_app.run()

if __name__ == "__main__":
    main()

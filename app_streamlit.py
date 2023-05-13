import movie as m
import streamlit as st  

def main():
    # HTML
    st.markdown("""
    
    <center><h1 style="background-color:powderblue;">Movie Recommendation</h1></center>
    <br>
    <center><p style="background-color:coral;">Recommendation Of 30 Movies.<br>
    Recommendation Is Based On Corresponding To Your Entered Movie Name That Is Most likely You Want To Watch.</p></center>

    """, unsafe_allow_html=True)
    
    user_input = st.text_input("  ","Enter A Hollywood Movie Name")
    i=1
    if st.button("submit"):
        results=m.movie_recommend(user_input)
        for result in results:  
            st.write(i,".",result)
            i+=1
    # st.success(result)

if __name__ == "__main__":
    main()
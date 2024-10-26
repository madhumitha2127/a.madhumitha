import streamlit as st 
if "value_to_guessed" not in st.session_state:
    st.session_state['value_to_guessed']=2
if 'guessed' not in st.session_state:
    st.session_state['guessed']=1
st.write("WELCOME TO GUESSING GAME")     
st.write("YOU HAVE 6 CHANCES TO TRY")
if st.session_state['guessed']<7:
   user_guessed_number=st.text_input(label='Enter Your Guessed number between 1 to 60:',key='num_value')
   if user_guessed_number: 
    user_guessed_number=int(user_guessed_number)
    st.session_state['guessed']+=1 
    if user_guessed_number==st.session_state['value_to_guessed']:
        st.write("CONGRATULATIONS, YOU WON THE GAME.. ") 
        st.session_state['guessed']=1
    else:
        st.write("SORRY,TRY AGAIN")      
else:
    st.write("SORRY,YOU FAILED.THE NUMBER WAS: ",st.session_state['value_to_guessed'])     
    if st.button("PLAY AGAIN"):
        st.session_state['guessed']=1

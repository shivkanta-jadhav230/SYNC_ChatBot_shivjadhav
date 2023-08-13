# Importing dependencies
import asyncio
import streamlit as st
from streamlit_chat import message
from bardapi import Bard

#Check out this repository('https://github.com/dsdanielpark/Bard-API') to get your token!
token = '  '


# Funtion that generates and returns the response
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)
    return response['content']


# Main function
async def main():
    st.write('<style>h1{font-size: 60px !important;} </style>', unsafe_allow_html=True)
    st.title("🤖Personal ChatBot!")

    changes = '''
    <style>
    [data-testid="stAppViewContainer"]
    {
    background-image:url('https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1');
    background-size:cover;
    }
    .st-bx {
    background-color: rgba(255, 255, 255, 0.05);
    }

    /* .css-1hynsf2 .esravye2 */

    html {
    background: transparent;
    }
    div.esravye2 > iframe {
        background-color: transparent;
    }
    </style>
    '''

    # Pushing changes to the UI
    st.markdown(changes, unsafe_allow_html=True)
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    # Get text from the input field
    def get_text():
        input_text = st.text_input("You: ", "Hey bot!", key="input")
        return input_text

    user_input = get_text()

    if user_input:
        output = await asyncio.to_thread(generate_response, user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated']) - 1, -1, -1):
            print(st.session_state["generated"], i)
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


asyncio.run(main())
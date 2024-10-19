import warnings
import streamlit as st
import base64
from pathlib import Path
from streamlit_extras.let_it_rain import rain
# creating a encoding

warnings.filterwarnings("ignore")
This_file=Path(__file__).parent
CSS=This_file/"style.css"/"style.css"
with open(CSS)as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

class word: 
    def run_items():
        rain(emoji='📖',font_size=20,falling_speed=5,animation_length='infinite')
    st.header(':book: ENCODING AND DECODING WEBSITE',divider='green',help='This is also a secret way of writing messages to clients')
        
    def encoded(encoding='utf-8')->str:
        st.subheader(":file_folder: ENCODER")
        name=st.text_area('Enter your word',placeholder='press enter when your  done ')
        text_acepted=name.encode(encoding)
        base_display=base64.b64encode(text_acepted)
        string=base_display.decode(encoding)
        st.markdown("<div class='bok'></div> " ,unsafe_allow_html=True)
        st.cache_resource()
        output=st.write(f"{string}",unsafe_allow_html=True)
        book=st.button('generate',on_click=output)
            
        if string:
            st.code(string,language='python')
            return book
     
        elif not output:           
            book= st.markdown("<script>alert('Click the button please')</script>",unsafe_allow_html=True)
            return book
        else:
            book
        
    def decoded(encoding='utf-8')->str:
        st.subheader(":file_folder: DECODER",divider='green')
        decode_name=st.text_input('Decoder Bar',placeholder='press enter when your  done ',help='copy the encoded')
        text_decoder=decode_name.encode(encoding)
        display_decode=base64.b64decode(text_decoder + b'======')
        book=st.button('Decode button')
        
        try:
            if book:
                return st.subheader(f"{display_decode.decode(encoding)}")
               
        except(ValueError):
            st.error('This is not a copied file from encode')

# import functions from class
word.run_items()
word.encoded()

word.decoded()

import warnings
import streamlit as st
import base64
from pathlib import Path
import urllib.parse
import time
from streamlit_extras.let_it_rain import rain
# creating a encoding
st.set_page_config ( page_icon=':💬:',layout='centered',initial_sidebar_state='expanded',page_title='WhatsApp Secret writer')
image=st.image("whas.png",caption='WhatsApp Secret produced by bright',width=500)

warnings.filterwarnings("ignore")
This_file=Path(__file__).parent
CSS=This_file/"style.css"/"style.css"
with open(CSS)as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

class word(): 
    display=[]
    def run_items():
        rain(emoji='📖',font_size=20,falling_speed=5,animation_length='infinite')
    
    # code for the project
    st.header(':book: ENCODING AND DECODING WEBSITE',divider='green',help='This is also a secret way of writing messages to clients')
        
    def encoded(encoding='utf-8')->str:
        st.subheader(":file_folder: ENCODE MY WORD")
        name=st.text_area('Please Enter your prefered to be hidden ',placeholder='press enter or button when done ')
        text_acepted=name.encode(encoding)
        base_display=base64.b64encode(text_acepted)
        string=base_display.decode(encoding)
        st.markdown("<div class='bok'></div> " ,unsafe_allow_html=True)
        st.cache_resource()
        
        
        
        with st.spinner("Runing successfully"):
            time.sleep(1.92) 
            if st.button('generate'):
                if string: 
                    st.code(string,language='python',wrap_lines=True)
                    
            # whatsapp link
                        

                else:
                    return st.error("Please write something first",icon='❌')
            if st.button("Ready to chat on WhatsApp"):
                        if string:
                            encoded_message=urllib.parse.quote(string)
                            whatsapp=f"https://wa.me/?text={encoded_message}"
                            st.markdown(f"[Click here]({whatsapp})",unsafe_allow_html=True)                       
                        else:
                            st.error("You need to have an encoded word first :blue[Generate First] ")    
                    
    
        
    
            
    def decoded(encoding='utf-8')->str:
        st.subheader(":file_folder: DECODE MY WORD",divider='green')
        decode_name=st.text_input('Decoder Bar',placeholder='Past the decoded words only ',help='copy the encoded')
        text_decoder=decode_name.encode(encoding)
        display_decode=base64.b64decode(text_decoder + b'======')
        
        try:
          if st.button('Decode button'):  
                if display_decode:
                    st.subheader(f"{display_decode.decode(encoding)}")
                else:
                    st.error('Please copied file which is encoded and paste it ')
            
        except Exception:
            st.error('This is not encoded word')

            
    
        
# import functions from class
word.run_items()
word.encoded()
word.decoded()

import streamlit as st
from PIL import Image
import numpy as np
import time

st.write("# @JERRIYHAN")
st.logo("./media/logo-alpha.png")

st.write("##### This is a board of photos taken after 2023.9")

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)
percent_complete=0

a1,a2,a3 = st.columns(3)
a1.image("media/photo_little/CSC_1273.jpg")
a2.image("media/photo_little/DSC_0033.jpg")
a3.image("media/photo_little/DSC_0103 2.jpg")

percent_complete+=15
my_bar.progress(percent_complete, text=progress_text)

b1,b2,b3,b4 = st.columns(4)
b1.image("media/photo_little/DSC_0109.jpg")
b2.image("media/photo_little/DSC_0277.jpg")
b3.image("media/photo_little/DSC_0279.jpg")
b4.image("media/photo_little/DSC_0334-2.jpg")

percent_complete+=30
my_bar.progress(percent_complete, text=progress_text)

c1,c2,c3,c4,c5 = st.columns(5)
c1.image("media/photo_little/DSC_1196.jpg")
c2.image("media/photo_little/DSC_0463-2.jpg")
c3.image("media/photo_little/DSC_0585.jpg")
c4.image("media/photo_little/DSC_0683.jpg")
c5.image("media/photo_little/DSC_0942.jpg")
percent_complete+=30
my_bar.progress(percent_complete, text=progress_text)

d1,d2,d3,d4 = st.columns(4)
d1.image("media/photo_little/DSC_1107.jpg")
d2.image("media/photo_little/DSC_1292.jpg")
d3.image("media/photo_little/DSC_1209.jpg")
d4.image("media/photo_little/DSC_1218.jpg")
percent_complete+=25
my_bar.progress(percent_complete, text="Finished")
time.sleep(1)
my_bar.empty()

st.balloons()
st.write("---")






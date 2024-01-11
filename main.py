import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title("streamlit 超入門")

# Initialize session state variables
if 'progress_show' not in st.session_state:
    st.session_state.progress_show = False#ここでセッションにprogress_showという任意で作成したものを追加

st.write("プログレスバーの表示")
start_text = st.text("start!!")

# Check if the progress bar has not been shown
if not st.session_state.progress_show:
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f"Iteration {i+1}")
        bar.progress(i+1)
        time.sleep(0.05)
    latest_iteration.empty()
    bar.empty()
    start_text.empty()
    
    # Set the session state variable to True after the progress bar is shown
    st.session_state.progress_show = True

done_text = st.text("done!!")

# Hide the "done!!" message after 2 seconds
time.sleep(1)
done_text.empty()

left_column, right_column = st.columns(2)
button = left_column.button("右からむに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")

text = st.text_input("あなたの好きなタイプは？")
option = st.selectbox(
    "あなたが好きな数字を教えてください。",
    list(range(1, 11))
)
condition = st.slider("調子は？", 0, 100, 50)

f"あなたの好きなタイプは：{text}"
f"あなたの好きな数字は：{option}"
f"コンディション：{condition}"

if option >= 7 and condition >= 70:
    if st.checkbox("サービス画像を見る？"):
        img = Image.open("ero.jpg")
        st.image(img, caption="ero", use_column_width=True)



# video_file = open('test1.mp4', 'rb')
# st.video(video_file)

#st.とかかれているものは基本的にフロントエンドに出力されるもの
#pdは生成しているもの
#npはnumpyでの配列を作成しているもの
#という認識でいい


# df = pd.DataFrame(data)

# df = pd.DataFrame(np.random.rand(20,3),columns=["a","b","c"])

# df = pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],columns=['lat', 'lon'])

# st.write(df)#writeには引数が用意されていない
# st.dataframe(df.style.highlight_max(axis=0),500,500)#axis=0は行,axis=1は列,highlight_maxは最大のところに色をつける,,500,500は横幅、縦幅の指定
# st.dataframe(df.style.highlight_max(axis=0))#axis=0は行,axis=1は列,highlight_maxは最大のところに色をつける
# st.area_chart(df)
# st.map(df)

# st.table(df.style.highlight_max(axis=0))#テーブルは動かせない静的な表を作るときに使用する



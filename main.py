# beta_columns -> columns

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write("DataFrame")

df = pd.DataFrame({
    "col1" : [1,2,3,4],
    "col2" : [10,20,30,40]
})

#write는 스타일 설정(가로,세로크기 조정) 불가능
st.write(df)
#열을 기준으로 할 경우 axis=0, 행은 axis=1
st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

#マークダウン
"""
# 章
## 節
### 項

```python

import streamlist as st
import numpy as np
import pandas as pd

```
"""

#20행 3열로 이루어진 표준정규분포 난수 생성
df1 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)

st.write(df1)
st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

df2 = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)

st.write(df2)
st.map(df2)


st.write("Interactive Widgets")

# Check하면 true, 안하면 false
if st.checkbox("Show Image"):
    img = Image.open("sample.png")
    st.image(img, caption="별의 커비", use_column_width=True)

option = st.selectbox(
    'What number do you like? ',
    list(range(1,11))
)

option = st.text_input('What\'s your hobby?')
condition = st.slider('How do you feel? ', 0, 100, 50)

'your favorite number is', option, '!!!'
'Your hobby is ', option, '!!!'
'condition : ', condition

left_column, right_column = st.columns(2)
button = left_column.button('view right column')
if button:
    right_column.write('right column')

expander = st.expander('問い合わせ1')
expander.write('問い合わせの回答1')
expander = st.expander('問い合わせ2')
expander.write('問い合わせの回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせの回答')

st.write('ブレぐレスバーの表示')
'Start!!'

latest_iteration = st.empty()
# 인수가 0인 경우, 0~100, 0.0인 경우 0.0~1.0
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

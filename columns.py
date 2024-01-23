import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Versicolor")
   st.image("https://c.pxhere.com/photos/f2/77/iris_flower_purple-1401467.jpg!d")

with col2:
   st.header("Verginica")
   st.image("https://www.fs.usda.gov/wildflowers/beauty/iris/Blue_Flag/images/iris_virginica/iris_virginica_virginica_lg.jpg")

with col3:
   st.header("Setosa")
   st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg")

#import pandas as pd
df=pd.read_csv("./data/iris.csv")
st.write(df.head(10))

st.write(df.groupby('variety').mean())
chart_data=df.groupby('variety').mean()
chart_data.columns

chart_data = pd.DataFrame(
   {
       "col1": df['variety'],
       "col2": df['sepal.width'],
       "col3": df['sepal.length']
    
    }
)

st.bar_chart(chart_data, x="col1", y=["col2","col3"], color=["#FF0000", "#0000FF"])

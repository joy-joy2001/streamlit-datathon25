import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title("Datathon 2025")
st.header("Functionalities")
st.markdown("Developed for scientists. By scientists.")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')



# st.radio('Sex', ['Male', 'Female'])
# st.selectbox('Ethnicity', ['Black/African', 'Black/Caribbean', 'White/British', 'Asian/Indian', 'Asian/Chinese','Other'])
# st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune', ])
# st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
# st.slider('Pick a number', 0, 100)


# # scatter plot 1
# df = px.data.iris()
# fig = px.scatter(
#     df,
#     x="sepal_width",
#     y="sepal_length",
#     color="species",
#     size="petal_length",
#     hover_data=["petal_width"],
# )

# event = st.plotly_chart(fig, key="iris", on_select="rerun")

# event.selection

# # scatter plot 2
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3), columns=["col1", "col2", "col3"]
# )
# chart_data["col4"] = np.random.choice(["A", "B", "C"], 20)
# print(chart_data)
# st.scatter_chart(
#     chart_data,
#     x="col1",
#     y="col2",
#     color="col4",
#     size="col3",
# )

# # graph 3
# df2 = pd.DataFrame(
#     np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"]
# )

# st.scatter_chart(
#     df2,
#     x="col1",
#     y=["col2", "col3"],
#     size="col4",
#     color=["#FF0000", "#0000FF"],  # Optional
# )

st.subheader("Rainbow graph")
df3 =  pd.DataFrame({'x': np.random.uniform(size=500),
                        'y': np.random.uniform(size=500), 
                        'z':np.random.uniform(size=500)})

xyz_colors = [f'rgba({int(r*255)}, {int(g*255)}, {int(b*255)}, 1)' for r, g, b in zip(df3['x'], df3['y'], df3['z'])]

# Create a 2D scatter plot
fig = px.scatter(
    df3,
    x='x',
    y='y',
    color=xyz_colors,
    size='z',
    hover_data=['z']
)
event = st.plotly_chart(fig, on_select="rerun")
event.selection
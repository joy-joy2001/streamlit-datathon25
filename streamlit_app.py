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

# Sidebar for file upload
st.sidebar.title("Add Data")
df = pd.read_csv('train.csv')
st.dataframe(df[['gene_id', 'AE0', 'AE1']])

# uploaded_file = st.sidebar.file_uploader("Upload a file", type=["csv"])
# st.subheader("Results")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     x = df['AE0']
#     y = df['AE1']

#     # xyz_colors = [f'rgba({int(r*255)}, {int(g*255)}, {int(b*255)}, 1)' for r, g, b in zip(df3['x'], df3['y'], df3['z'])]

#     # Create a 2D scatter plot
#     fig = px.scatter(
#         df,
#         x=x,
#         y=y,
#         hover_data=['gene_id']
#     )
#     event = st.plotly_chart(fig, on_select="rerun")
#     # Read the uploaded file as a Pandas DataFrame
    

#     # Display the DataFrame on the main page
#     st.dataframe(df[['gene_id', 'AE0', 'AE1']])


    
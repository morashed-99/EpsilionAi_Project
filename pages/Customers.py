import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd


st.set_page_config(
        layout = 'wide',
        page_title = 'Customers',
        page_icon= '👫'
)

# Set colors and page configuration
color1 = ['#012340','#57B7F2','#0487D9','#F29F05','#F2E0DF']
#load data
df = pd.read_csv("cleaned_data.csv")

st.markdown('<h2 style="text-align: center; color: black;">Customers Sales and Profits</h2>', unsafe_allow_html=True)
col= st.selectbox('select feature to see its distribution', ['Sales', 'Profit'], key=10)
with st.container():
    df_top5 = df.nlargest(5, col)
    fig= px.histogram(df_top5, x= 'Customer Name',y=col, color_discrete_sequence=color1)
    st.plotly_chart(fig, use_container_width= True)

st.markdown('<h2 style="text-align: center; color: black;">Customers Location</h2>', unsafe_allow_html=True)
col= st.selectbox('select feature to see where Most customers from',['Region', 'City', 'State or Province', 'Country'])
with st.container():

   # Group the data by the selected feature and count the number of customers
   df_grouped = df[col].value_counts().reset_index()
   df_grouped.columns = [col, 'Count']

   # Filter the grouped data to include only the top 5 rows
   df_top5 = df_grouped.head(5)

   # Create the pie chart
   fig = px.pie(df_top5, names=col, values='Count',color_discrete_sequence=color1,hole=0.3).update_traces(
       textinfo='value+percent',  # Display both values and percentages on the chart
       pull=[0.1, 0, 0, 0, 0]     # Pull the first slice for emphasis
   )

# Display the pie chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown('<h2 style="text-align: center; color: black;">Customers Segment</h2>', unsafe_allow_html=True)

df_grouped = df['Customer Segment'].value_counts().reset_index()
df_grouped.columns = ['Customer Segment', 'Count']
fig = px.scatter(df_grouped,x='Customer Segment',y='Count',marginal_x='histogram',marginal_y='violin')
st.plotly_chart(fig, use_container_width=True)

st.markdown('<h2 style="text-align: center; color: black;">Customers Managers</h2>', unsafe_allow_html=True)
df_grouped = df['Manager'].value_counts().reset_index()
df_grouped.columns = ['Manager', 'Count']

# Filter the grouped data to include only the top 5 rows
df_top5 = df_grouped.head(5)

fig= px.histogram(df_top5, x= 'Manager',y='Count', color_discrete_sequence=color1)
st.plotly_chart(fig, use_container_width=True)

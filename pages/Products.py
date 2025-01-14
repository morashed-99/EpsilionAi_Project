import streamlit as st
import plotly.express as px
import pandas as pd


st.set_page_config(
        layout = 'wide',
        page_title = 'Customers',
        page_icon= '🏷️'
)

# Set colors and page configuration
color1 = ['#012340','#57B7F2','#0487D9','#F29F05','#F2E0DF']
#load data
df = pd.read_csv(cleaned_data.csv")

st.markdown('<h2 style="text-align: center; color: black;">Product Category</h2>', unsafe_allow_html=True)
col = st.radio('select feature to see its distribution', ['Unit Price','Discount','Product Base Margin'], key=3, horizontal=True)
# Group the data by Product Category and calculate the sum of the selected feature
df_grouped = df.groupby('Product Category')[col].sum().reset_index()

# Filter the grouped data to include only the top 3 rows
df_top5 = df_grouped.nlargest(3, col)

# Create the line chart
fig = px.line(
    df_top5, 
    x='Product Category',  # X-axis: Product Category
    y=col,                 # Y-axis: Selected feature (Unit Price, Discount, or Product Base Margin)
    title=f'Top 3 Product Categories by {col}',  # Chart title
    labels={col: f'Sum of {col}'}  # Label for the y-axis
).update_traces(
    line=dict(color=color1[1]),  # Use the second color in the custom color sequence
    mode='lines+markers'         # Add markers to the line
)
# Display the line chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


# Streamlit selectbox to choose a feature
col = st.selectbox('Select feature to see its distribution', ['Sales', 'Profit'])
# Group the data by Product Categories and calculate the sum of the selected feature
top_sales = df.groupby('Product Category')[col].sum().reset_index()

# Filter the grouped data to include only the top 3 rows
df_top3 = top_sales.nlargest(3, col)

# Create the pie chart
fig = px.pie(
    df_top3, 
    names='Product Category',  # Labels for the pie chart slices
    values=col,                  # Numeric values for the pie chart slices
    color_discrete_sequence=color1,  # Custom color sequence
    hole=0.3                     # Add a hole in the middle for a donut chart
).update_traces(
    textinfo='value+percent',    # Display both values and percentages on the chart
    pull=[0.1, 0, 0]             # Pull the first slice for emphasis
)

# Display the pie chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


st.markdown('<h2 style="text-align: center; color: black;">Product Name</h2>', unsafe_allow_html=True)

# Streamlit selectbox to choose a feature
col = st.selectbox('Select feature to see its distribution', ['Sales', 'Profit'],key='feature_selectbox')

# Group the data by Product Name and calculate the sum of the selected feature
top_sales = df.groupby('Product Name')[col].sum().reset_index()

# Filter the grouped data to include only the top 5 rows
df_top5 = top_sales.nlargest(5, col)

# Create the bar chart
fig = px.bar(
    df_top5, 
    x='Product Name',  # X-axis: Product Name
    y=col,             # Y-axis: Selected feature (Sales or Profit)
    color_discrete_sequence=color1,  # Custom color sequence
    labels={col: f'Total {col}'},    # Label for the y-axis
    title=f'Top 5 Products by {col}'  # Chart title
)

# Display the bar chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


col = st.selectbox('Select feature to see its distribution', ['Discount','Unit Price','Product Base Margin'])
top_price = df.groupby(['Product Name','Product Category'])[col].sum().reset_index()
# Filter the grouped data to include only the top 5 rows
df_top5 = top_price.nlargest(5, col)
fig = px.bar(df_top5, x="Product Name", y=col, 
             color='Product Category',color_discrete_sequence=color1,
             labels={col: f'Total {col}'},
             title=f'Top 5 Products by {col}'
             )

# Display the bar chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Select the columns for the pair plot
columns = ['Sales', 'Unit Price', 'Product Base Margin']

# Create a Plotly scatter matrix (similar to Seaborn pairplot)
fig = px.scatter_matrix(
    df,
    dimensions=columns,  # Columns to include in the pair plot
    title="Pair Plot of Sales, Unit Price, and Product Base Margin",  # Title of the plot
    color=columns[0],  # Color points by the first column (e.g., 'Sales')
    opacity=0.7,  # Set opacity for better visibility
    labels={col: col.replace('_', ' ') for col in columns}  # Format axis labels
)

# Update layout for better readability
fig.update_layout(
    width=1000,  # Set width of the plot
    height=800,  # Set height of the plot
    showlegend=True  # Show legend
)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig, use_container_width=True)

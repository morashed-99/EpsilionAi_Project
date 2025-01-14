import streamlit as st
import plotly.express as px
import pandas as pd


st.set_page_config(
        layout = 'wide',
        page_title = 'Time',
        page_icon= '⌛'
)

# Set colors and page configuration
color1 = ['#012340','#57B7F2','#0487D9','#F29F05','#F2E0DF']
#load data
df = pd.read_csv(r"D:\data course\epsilion\Mohamed Osama Rashed\cleaned_data.csv")

tab1, tab2 = st.tabs(['🕑 Time','🌎 Geography'])

with tab1: 
    st.markdown('<h3 style="text-align: center; color : black;">Time Period Sales</h3>', unsafe_allow_html=True)
    col= st.selectbox('select feature to see its distribution', ['Month_name','week','week_day','Day_name','Season','Quarter'], key=15)

    df_grouped = df.groupby(col)['Sales'].sum().reset_index()
    # Sort the grouped data in descending order based on the selected column
    df_grouped = df_grouped.sort_values(by=col, ascending=False)

    # Create the line chart
    fig = px.line(
        df_grouped, 
        x=col,  
        y='Sales',                 
        title=f'Sales by {col}',  # Chart title
    ).update_traces(
        line=dict(color=color1[1]),  # Use the second color in the custom color sequence
        mode='lines+markers'         # Add markers to the line
    )
    # Display the line chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    
    st.markdown('<h3 style="text-align: center; color : black;">Time Period Profit</h3>', unsafe_allow_html=True)
    col= st.selectbox('select feature to see its distribution', ['Month_name','week','week_day','Day_name','Season','Quarter'], key=16)

    df_grouped = df.groupby(col)['Profit'].sum().reset_index()
    # Sort the grouped data in descending order based on the selected column
    df_grouped = df_grouped.sort_values(by=col, ascending=False)

    # Create the bar chart
    fig = px.bar(
        df_grouped, 
        x=col,  
        y='Profit',                 
        title=f'Profit by {col}', 
        color_discrete_sequence= ['#57B7F2']
    )
    # Display the line chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)


    st.markdown('<h3 style="text-align: center; color : black;">Correlation Heatmap of Time-Based Features</h3>', unsafe_allow_html=True)
    # Select time-based columns for correlation
    time_columns = ['Month_name','week','week_day','Day_name','Season','Quarter']
    # Convert categorical time columns to numerical for correlation calculation
    df_numerical = df[time_columns].apply(lambda x: pd.factorize(x)[0])

    # Add other numerical columns (e.g., 'Sales', 'Profit') if needed
    df_numerical['Sales'] = df['Sales']
    df_numerical['Profit'] = df['Profit']

    # Compute the correlation matrix
    corr_matrix = df_numerical.corr()

    # Create the heatmap using Plotly
    fig = px.imshow(
        corr_matrix,
        text_auto=True,  # Automatically add correlation values to the heatmap
        color_continuous_scale=color1,  # Choose a color scale
    )

    # Update layout for better visualization
    fig.update_layout(
        xaxis_title='Features',
        yaxis_title='Features',
        width=800,
        height=600
    )

    # Display the heatmap in Streamlit
    st.plotly_chart(fig, use_container_width=True)


with tab2: 
    col = st.selectbox('Select feature to see its distribution', ['Region','City','State or Province'])
    st.markdown('<h3 style="text-align: center; color : black;">Sales by Geography</h3>', unsafe_allow_html=True)

    # Create the bar chart
    fig = px.bar(
        df, 
        x=col,  
        y='Sales',                 
        title=f'Sales by {col}', 
        color_discrete_sequence= color1
    )
    # Display the line chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    
    col = st.radio('Select feature to see its distribution',['Region','City','State or Province'] , key=20, horizontal=True)
    st.markdown('<h3 style="text-align: center; color : black;">Profit by Geography</h3>', unsafe_allow_html=True)

    # Create the bar chart
    fig = px.bar(
        df, 
        x=col,  
        y='Profit',                 
        title=f'Profit by {col}', 
        color_discrete_sequence= ['#57B7F2']
    )
    # Display the line chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)


    st.markdown('<h3 style="text-align: center; color : black;">Denisty Heatmap BTW Region and State</h3>', unsafe_allow_html=True)
    fig = px.density_heatmap(df,x="Region", y="State or Province",color_continuous_scale=px.colors.sequential.GnBu)

    # Display the line chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

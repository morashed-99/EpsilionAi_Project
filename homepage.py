import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

#page configration
st.set_page_config(
    layout='wide',
    page_title='HomePage',
    page_icon='🛒'
)

#Side bar
x = st.sidebar.checkbox('Show Data',False,key=1)
# Custom colored message in the sidebar
st.sidebar.markdown(
    """
    <div style="background-color: #57B7F2; padding: 10px; border-radius: 5px; text-align: center; color: white;">
        <strong>Please select a page above!</strong>
    </div>
    """,
    unsafe_allow_html=True
)

#load data
df = pd.read_csv(r"D:\data course\epsilion\Mohamed Osama Rashed\cleaned_data.csv")

# Main page title
st.markdown('<h1 style="text-align: center; color: black;">Home Page For Dashboard</h1>', unsafe_allow_html=True)
st.write("""
Welcome to the Home Page of the Dashboard! This dashboard is designed to provide insights and visualizations 
based on E-Commerce Data. You can explore the data by checking the 'Show Data' checkbox in the sidebar. 
This will display the dataset in a tabular format. Stay tuned for more features and visualizations!
""")

if x:
    st.dataframe(df.copy(), height=500, width=1000)

st.markdown('<h2 style="text-align: center; color: black;">Conclusion</h2>', unsafe_allow_html=True)
# data metric for the table
summary_data = {
    "Metric": ["Revenue", "Profit", "Cost", "Customers", "Managers", "Orders", "Categories", "Sub-Categories", "Countries", "Regions", "Cities", "States"],
    "Value": ["1.9 M$", "227.832 K$", "25.434 K$", 1130, 4, 1365, 3, 17, 1, 4, 868, 49]
}

# Convert data to a DataFrame
summary_df = pd.DataFrame(summary_data)

# Create a table using plotly.figure_factory
table = ff.create_table(summary_df)

# Display the table in Streamlit
st.plotly_chart(table, use_container_width=True)

# recommenditions
st.markdown('<h2 style="text-align: center; color: black;">Recommenditions to increase business performance, you can leverage insights from your dataset (e.g., sales, customer, and product data) to make data-driven decisions</h2>', unsafe_allow_html=True)
st.write(""" 
**1. Focus on High-Value Customers**
   
- Identify High-Value Customers:
Use (Recency, Frequency, Monetary) analysis to segment customers based on their purchasing behavior.
Focus on customers with high monetary value and frequent purchases.
- Personalized Marketing:
Offer personalized discounts, loyalty programs, or exclusive deals to retain high-value customers.
- Upselling and Cross-Selling:
Recommend complementary products or premium versions to increase average order value.
""")
st.write(""" 
**2. Optimize Product Offerings**

- Top-Performing Products:
Identify top-selling and high-margin products using sales and profit analysis.
Increase stock and marketing efforts for these products.
- Underperforming Products:
Analyze low-performing products and consider discontinuing or discounting them.
- Product Bundling:
Bundle complementary products to increase sales volume.
""")
st.write(""" 
**3. Improve Customer Experience**

- Shipping and Delivery:
Analyze shipping costs and delivery times by region and ship mode.
Optimize shipping methods to reduce costs and improve delivery speed.
- Customer Feedback:
Collect and analyze customer feedback to identify pain points and areas for improvement.
- Easy Returns:
Simplify the return process to enhance customer satisfaction.
""")
st.write(""" 
**4. Regional Performance Analysis**

- Top-Performing Regions:
Identify regions with the highest sales and profit margins.
Increase marketing and inventory in these regions.
- Underperforming Regions:
Investigate reasons for low performance (e.g., lack of awareness, high shipping costs).
Run targeted promotions or campaigns to boost sales.
""")
st.write(""" 
**5. Discount and Pricing Strategy**

- Discount Optimization
- Analyze the impact of discounts on sales and profit margis.
- Offer strategic discounts on slow-moving or high-margin products.
- Dynamic Picing:
- Implement dynamic pricing strategies based on demand, seasonality, and competitorricing.
""")
st.write(""" 
**6. Enhance Marketing Campaigns**

- Targeted Campaigns:
Use customer segmentation to create targeted marketing campaigns.
Focus on specific customer segments (e.g., high-value customers, new customers).
- Seasonal Promotions:
Run promotions during peak seasons or holidays to boost sales.
- Digital Marketing:
Invest in social media, email marketing, and search engine optimization (SEO) to reach a wider audience.
""")
st.write(""" 
**7. Sales and Unit Price Relationship**

- There appears to be a relationship between sales and unit price.
As the unit price increases, sales seem to fluctuate, but there is no clear linear trend.
This suggests that other factors might be influencing sales beyond just price.
""")
st.write(""" 
**8. Product Base Margin**

- The product base margin varies between 0.4 and 0.8. This indicates that the profitability of the products can differ significantly.
Products with higher margins are likely more profitable, assuming costs remain constant.
""") 
st.write(""" 
**9. Sales Volume**

- Sales volumes range from 0 to 45k units. The highest sales volume is 45k,
which could indicate a peak period or a particularly popular product.
""")
st.write(""" 
**10. Unit Price Range**

- The unit price ranges from 0 to 6000. 
This wide range suggests that the products vary significantly in terms of pricing,
which could be due to differences in product features, quality, or market positioning.
""") 
st.write(""" 
**11. Potential Outliers**

- There are some data points that stand out, such as the highest sales volume (45k) and the highest unit price (6000).
These could be outliers or represent special cases that warrant further investigation.
""") 
st.write(""" 
**12. Profitability Analysis**

- Combining sales volume, unit price, and product base margin could provide insights into overall profitability.
Products with higher margins and higher sales volumes are likely the most profitable.
""") 
st.write(""" 
**13. Focus on Q3 and Q4 in year because there is no sales specially in 7,8,9,10,11 Months.**
""")

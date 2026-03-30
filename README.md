# Cafe Sales Performance Analysis (End-to-End Project)

##  Project Overview
This is an end-to-end data analysis project focusing on the sales performance of a local cafe. The dataset contains 10,000 transaction records. The goal of this project is to clean the messy raw data using Python and build an interactive dashboard in Power BI to uncover business insights.

##  Tools & Technologies Used
* Python (Pandas): Data Cleaning, Data Transformation.
* Power BI: Data Visualization, Dashboarding.

##  Step 1: Data Cleaning (Python)
The raw data contained missing values, incorrect data types, and garbage text. Using Python's `pandas` library, I performed the following steps:
* Identified and replaced garbage text (`ERROR`, `UNKNOWN`) in `Payment Method` and `Location` columns with `Not Specified`.
* Dropped rows with missing `Item` names to ensure accurate product analysis.
* Handled invalid entries in the `Transaction Date` column and converted it to the correct DateTime format.
* Exported the clean dataset to `clean_cafe_sales.csv` for visualization.

##  Step 2: Data Visualization (Power BI)
![Cafe Sales Dashboard](<img width="1137" height="709" alt="Screenshot 2026-03-30 125236" src="https://github.com/user-attachments/assets/2996d22d-e009-413a-89e7-096f51d74f14" />)


I built an interactive dashboard to answer key business questions:
1. Total Revenue: Displayed via a Card visual (Total: 80.49k).
2. Top Selling Items: A Bar Chart revealing that 'Salad' and 'Sandwich' are the top revenue generators.
3. Payment Preferences: A Donut Chart showing the breakdown of payment methods (Cash, Credit Card, Digital Wallet).
4. Revenue Trend: A Line Chart tracking the total spent over the months to identify peak sales periods.

##  Key Insights
* Food items (Salad, Sandwich) generate significantly more revenue compared to beverages (Tea, Cookie).
* Customers' payment methods are fairly evenly distributed among Cash, Credit Cards, and Digital Wallets.

##  How to Run
1. Run the `project2,1.py` script to clean the raw data.
2. Open the `Cafe_Sales_Performance_Khang.pbix` file in Power BI Desktop to interact with the dashboard.

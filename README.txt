# Cafe Sales Performance Analysis (End-to-End Project)

## Project Overview
This is an end-to-end data analysis project focusing on the sales performance of a local cafe. The dataset contains 10,000 transaction records. The goal of this project is to build a complete pipeline: from handling messy, incomplete raw data using Python to designing a professional, interactive dashboard in Power BI to uncover business insights.

## Tools & Technologies Used
* **Python (Pandas & NumPy):** Data Cleaning, Missing Value Imputation, Data Transformation.
* **Power BI:** Data Modeling, Interactive Visualization, UI/UX Dashboard Design.

## Step 1: Data Cleaning (Python)
The raw data contained missing numerical values, incorrect data types, and garbage text. Using Python's `pandas` library, I performed the following steps:
* Recovered missing values in `Quantity`, `Price Per Unit`, and `Total Spent` by leveraging their mathematical relationship (`Quantity * Price Per Unit = Total Spent`).
* Filled remaining missing `Price Per Unit` values by mapping the median price of respective `Item` categories.
* Identified and replaced garbage text (`ERROR`, `UNKNOWN`) in categorical columns with `NaN` for proper handling.
* Standardized the `Transaction Date` column for time-series analysis.
* Exported the clean dataset to `clean_cafe_sales.csv` for visualization.

## Step 2: Data Visualization (Power BI)
![Cafe Sales Dashboard](<img width="1137" height="709" alt="PowerBI" src="https://github.com/user-attachments/assets/2e6bf4f4-b8b4-4e21-8985-ca06b29c9572" />)

I designed a clean, corporate-standard dashboard to answer key business questions:
1. **Executive KPIs:** 6 core metrics (Total Revenue, Total Items Sold, etc.) displayed via Card visuals for quick performance tracking.
2. **Product Performance:** A Clustered Bar Chart revealing that **Salad** and **Sandwich** are the top revenue generators.
3. **Distribution Breakdown:** Donut Charts showing customer preferences regarding **Location** (Takeaway vs. In-store) and **Payment Method** (Cash, Credit Card, Digital Wallet).
4. **Revenue Trend:** A Line Chart tracking the total spent over the months to identify seasonal peaks.
5. **Detailed Matrix:** A tabular view providing exact figures for granular operational review.

## Key Insights
* Food items (Salad, Sandwich) generate significantly more revenue compared to beverages (Tea, Cookie).
* Revenue is evenly split between In-store and Takeaway orders, indicating a balanced business model.
* Customers' payment methods are fairly evenly distributed among Cash, Credit Cards, and Digital Wallets, showing high payment flexibility.

## How to Run
1. Run the `project2,1.py` script to clean the raw data.
2. Open the `Cafe_Sales_Performance_Khang.pbix` file in Power BI Desktop to interact with the dashboard.
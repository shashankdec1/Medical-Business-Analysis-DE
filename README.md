# Medical Business Analysis - Healthcare Data Engineering Pipeline

## Project Overview

This project implements an **end-to-end Healthcare Data Engineering Pipeline** that integrates multiple healthcare datasets into a centralized **PostgreSQL Data Warehouse** and provides analytical insights through a **Python dashboard**.

The pipeline extracts healthcare data from **object storage and on-premise files**, transforms it into a unified structure, and loads it into a **PostgreSQL data warehouse** for analytics and visualization.

This project demonstrates core **Data Engineering concepts** including:

- ETL pipeline development
- Data warehouse design
- Data integration from multiple data sources
- SQL-based analytics
- Python dashboard visualization

---

---

# Data Sources

## Object Storage Dataset

Simulated object storage containing pharmaceutical sales data.


## On-Premise Dataset

Local healthcare dataset containing patient treatment records.


---
# Business Objectives & Dashboard Analytics

This dashboard analyzes healthcare data stored in the PostgreSQL data warehouse and generates insights through interactive visualizations.

The system evaluates **six key business objectives** to support healthcare analytics and decision-making.

---

# Business Objective 1: Average Sales Value per Year

Analyze the yearly trend of pharmaceutical sales to understand overall healthcare revenue growth.

**Visualization Used**

- Line chart with yearly markers

**Insights**

- Identifies growth or decline in pharma sales
- Helps hospitals evaluate yearly revenue performance
- Supports strategic healthcare planning

---

# Animated Hospital Revenue Growth

An animated bar chart visualizes how hospital revenue evolves across different years.

**Visualization Used**

- Animated bar chart with year progression

**Insights**

- Compares revenue performance across hospitals
- Shows growth patterns over time
- Helps identify top-performing hospitals

---

# Business Objective 2: Hospital Revenue Distribution

This analysis shows how total revenue is distributed among hospitals.

**Visualization Used**

- Donut chart (Pie chart with center hole)

**Insights**

- Identifies hospitals contributing the most revenue
- Helps analyze market share across healthcare providers
- Supports hospital performance benchmarking

---

# Hospital Revenue Ranking

Hospitals are ranked based on total revenue generated from medicine sales.

**Visualization Used**

- Interactive ranking table

**Insights**

- Displays top-performing hospitals
- Helps compare revenue contribution
- Useful for healthcare performance reporting

---

# Business Objective 3: Top Medicines Sold

Analyzes which medicines are sold the most across hospitals.

**Visualization Used**

- Donut chart of top 10 medicines

**Insights**

- Identifies high-demand medicines
- Supports pharmaceutical inventory planning
- Helps hospitals optimize medicine supply

---

# Business Objective 4: Treatment Cost Trend

Tracks total treatment costs across years to understand healthcare expenditure trends.

**Visualization Used**

- Yearly treatment cost line chart

**Insights**

- Shows growth in healthcare service costs
- Helps identify spending patterns
- Supports healthcare financial analysis

---

# Business Objective 5: Hospital Performance Analysis

Evaluates hospital performance using multiple metrics.

Metrics used:
- Total medicine sales revenue
- Total treatment cost
- Total medicine quantity sold

**Visualization Used**

- Bubble scatter plot

**Insights**

- Compares hospital efficiency
- Shows correlation between treatments and sales
- Identifies high-performing healthcare institutions

---

# Business Objective 6: Machine Learning – Predict Future Pharma Sales

A **Linear Regression model** is used to predict future pharmaceutical sales based on historical yearly revenue data.

**Machine Learning Model**

- Linear Regression

**Features Used**

- Year

**Target Variable**

- Sales Value

**Prediction**

The model predicts **future pharmaceutical revenue for the next year** based on historical trends.

**Visualization Used**

- Actual vs Predicted revenue line chart

**Insights**

- Forecasts healthcare revenue trends
- Helps hospitals plan inventory and budgets
- Demonstrates integration of **Machine Learning with Data Engineering**

---

# Key Technologies Used

| Technology | Purpose |
|---|---|
| Python | ETL Pipeline |
| Pandas | Data Processing |
| PostgreSQL | Data Warehouse |
| Streamlit | Dashboard |
| Plotly | Data Visualization |
| Scikit-learn | Machine Learning Model |
---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | ETL pipeline development |
| PostgreSQL | Data warehouse |
| Pandas | Data transformation |
| SQL | Business analytics queries |
| Streamlit / Python | Dashboard visualization |
| Git | Version control |

---

# Database Configuration

Example PostgreSQL configuration:

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "healthcare_dw",
    "user": "shashankbangaru",
    "password": "",
    "port": "5432"
}
```
---

# **Instructions Guide**

This guide explains how to set up and run the **Medical Business Analysis Data Engineering Project**.

---

# **1. Clone the Repository**

Clone the project from GitHub:

```bash
git clone https://github.com/shashankdec1/Medical-Business-Analysis-DE.git
```

Navigate to the project directory:

```bash
cd Medical-Business-Analysis-DE
```

---

# **2. Install Required Dependencies**

Install all required Python libraries:

```bash
pip install -r requirements.txt
```

---

# **3. Install PostgreSQL**

Install PostgreSQL on your system if it is not already installed.

Download from:

```
https://www.postgresql.org/download/
```

After installation, open **pgAdmin** or the PostgreSQL terminal.

---

# **4. Create the Project Database**

Create a new PostgreSQL database for the project:

```sql
CREATE DATABASE healthcare_dw;
```

---

# **5. Configure Database Connection**

Open the configuration file:

```
config.py
```

Update the database credentials:

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "healthcare_dw",
    "user": "postgres",
    "password": "your_password",
    "port": "5432"
}
```

Make sure the credentials match your local PostgreSQL setup.

---

# **6. Run the Data Engineering Pipeline**

Execute the main pipeline script:

```bash
python main_pipeline.py
```

This will perform the following steps:

1. Extract data from source CSV files  
2. Transform and clean the data  
3. Merge datasets  
4. Load processed data into PostgreSQL  

---

# **7. Verify Data in PostgreSQL**

Open **pgAdmin**.

Navigate to:

```
Databases → healthcare_dw → Tables
```

You should see the tables created by the pipeline.

---

# **8. Run the Analytics Dashboard**

Navigate to the dashboard directory:

```bash
cd dashboard
```

Run the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

Open the dashboard in your browser:

```
http://localhost:8501
```

---

# **9. Running the Project on Another Device**

1. Install **Python 3.9+**  
2. Install **PostgreSQL**  
3. Clone the repository  

```bash
git clone https://github.com/shashankdec1/Medical-Business-Analysis-DE.git
```

4. Navigate to the project folder  

```bash
cd Medical-Business-Analysis-DE
```

5. Install dependencies  

```bash
pip install -r requirements.txt
```

6. Create the database  

```sql
CREATE DATABASE healthcare_dw;
```

7. Update database credentials in `config.py`

8. Run the pipeline  

```bash
python main_pipeline.py
```

9. Start the dashboard  

```bash
streamlit run dashboard/dashboard.py
```

---

# **10. Stop the Dashboard**

To stop the running dashboard server:

```
CTRL + C
```

---

# **Troubleshooting**

If you encounter issues:

- Ensure PostgreSQL is running  
- Verify database credentials in `config.py`  
- Confirm Python dependencies are installed  
- Check dataset file paths


# **Conclusion**

This project demonstrates an **end-to-end Medical Business Analysis Data Engineering pipeline** that integrates healthcare datasets, processes them using an ETL workflow, and generates meaningful insights through an interactive analytics dashboard.

The pipeline extracts data from multiple sources, transforms and cleans the datasets using **Python and Pandas**, and loads the processed data into a **PostgreSQL data warehouse**. Analytical queries and visualizations are then used to evaluate key healthcare business objectives such as revenue analysis, hospital performance, medicine demand, and treatment cost trends.

Additionally, the project integrates a **Machine Learning model** to forecast future pharmaceutical sales, demonstrating how data engineering pipelines can support predictive analytics and data-driven decision making.

Overall, this project highlights the integration of **Data Engineering, Business Analytics, and Machine Learning** to build a scalable healthcare analytics solution that can support operational insights and future forecasting.

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sqlalchemy import create_engine
from config import DB_CONFIG

from sklearn.linear_model import LinearRegression
import numpy as np

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io


# PAGE SETTINGS

st.set_page_config(
    page_title="Healthcare Business Intelligence Dashboard",
    layout="wide"
)

st.title("Healthcare Data Warehouse Analytics Dashboard")

sns.set_style("whitegrid")


# DATABASE CONNECTION

engine = create_engine(
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

sales = pd.read_sql("SELECT * FROM pharma_sales", engine)
treatments = pd.read_sql("SELECT * FROM patient_treatments", engine)
merged = pd.read_sql("SELECT * FROM healthcare_merged", engine)


# SIDEBAR FILTER

st.sidebar.header("Dashboard Filters")

years = sorted(sales["year"].unique())
selected_year = st.sidebar.selectbox("Select Year", years)

sales_year = sales[sales["year"] == selected_year]
treat_year = treatments[treatments["year"] == selected_year]


# KPI METRICS

st.header("Key Business Metrics")

col1, col2, col3, col4 = st.columns(4)

# TOTAL PATIENTS TILL DATE

total_patients = treatments["patient_id"].nunique()

col1.metric(
    "Total Patients Till Date",
    f"{total_patients:,}"
)

col2.metric(
    "Total Sales Revenue",
    f"₹ {sales_year['sales_value'].sum():,.0f}"
)

col3.metric(
    "Total Medicines Sold",
    f"{sales_year['quantity'].sum():,.0f}"
)

col4.metric(
    "Total Treatment Cost",
    f"₹ {treat_year['treatment_cost'].sum():,.0f}"
)


# BUSINESS OBJECTIVE 1

st.header("Business Objective 1: Average Sales Value per Year")

avg_sales = sales.groupby("year")["sales_value"].mean().reset_index()

fig1 = px.line(
    avg_sales,
    x="year",
    y="sales_value",
    markers=True,
    title="Average Sales Trend"
)

fig1.update_layout(yaxis_title="Average Sales (₹)")

st.plotly_chart(fig1, use_container_width=True)


# Animated Revenue Trend

st.header("Animated Hospital Revenue Growth")

hospital_year_sales = sales.groupby(
    ["year", "hospital"]
)["sales_value"].sum().reset_index()

fig_anim = px.bar(
    hospital_year_sales,
    x="hospital",
    y="sales_value",
    color="hospital",
    animation_frame="year",
    title="Hospital Revenue Growth Over Years"
)

fig_anim.update_layout(yaxis_title="Revenue (₹)")

st.plotly_chart(fig_anim, use_container_width=True)


# BUSINESS OBJECTIVE 2

st.header("Business Objective 2: Hospital Revenue Distribution")

hospital_sales = sales.groupby("hospital")["sales_value"].sum().reset_index()

fig2 = px.pie(
    hospital_sales,
    names="hospital",
    values="sales_value",
    hole=0.4,
    title="Hospital Revenue Share"
)

fig2.update_traces(textinfo="percent+label")

st.plotly_chart(fig2, use_container_width=True)


# Hospital Ranking Table

st.subheader("Hospital Revenue Ranking")

hospital_ranking = hospital_sales.sort_values("sales_value", ascending=False)
hospital_ranking["Rank"] = range(1, len(hospital_ranking) + 1)
hospital_ranking["Revenue (₹)"] = hospital_ranking["sales_value"]

st.dataframe(
    hospital_ranking[["Rank", "hospital", "Revenue (₹)"]],
    use_container_width=True
)


# BUSINESS OBJECTIVE 3

st.header("Business Objective 3: Top Medicines Sold")

medicine_sales = sales.groupby("medicine")["quantity"].sum().reset_index()
medicine_sales = medicine_sales.sort_values("quantity", ascending=False).head(10)

fig3 = px.pie(
    medicine_sales,
    names="medicine",
    values="quantity",
    hole=0.4,
    title="Top Medicines Distribution"
)

fig3.update_traces(textinfo="percent+label")

st.plotly_chart(fig3, use_container_width=True)


# BUSINESS OBJECTIVE 4

st.header("Business Objective 4: Treatment Cost Trend")

treatment_cost = treatments.groupby("year")["treatment_cost"].sum().reset_index()

fig4 = px.line(
    treatment_cost,
    x="year",
    y="treatment_cost",
    markers=True,
    title="Yearly Treatment Cost Trend"
)

fig4.update_layout(yaxis_title="Treatment Cost (₹)")

st.plotly_chart(fig4, use_container_width=True)


# BUSINESS OBJECTIVE 5

st.header("Business Objective 5: Hospital Performance Analysis")

hospital_perf = merged.groupby("hospital").agg({
    "sales_value": "sum",
    "treatment_cost": "sum",
    "quantity": "sum"
}).reset_index()

fig5 = px.scatter(
    hospital_perf,
    x="sales_value",
    y="treatment_cost",
    size="sales_value",
    color="hospital",
    title="Hospital Performance Analysis"
)

fig5.update_layout(
    xaxis_title="Medicine Sales (₹)",
    yaxis_title="Treatment Cost (₹)"
)

st.plotly_chart(fig5, use_container_width=True)


# MACHINE LEARNING BUSINESS OBJECTIVE

st.header("Business Objective 6: Predict Future Pharma Sales (Machine Learning)")

ml_data = sales.groupby("year")["sales_value"].sum().reset_index()

X = ml_data["year"].values.reshape(-1, 1)
y = ml_data["sales_value"].values

model = LinearRegression()
model.fit(X, y)

next_year = np.array([[ml_data["year"].max() + 1]])
prediction = model.predict(next_year)

st.subheader("Predicted Sales for Next Year")

st.metric(
    label=f"Predicted Revenue for {int(next_year[0][0])}",
    value=f"₹ {prediction[0]:,.0f}"
)

ml_data["type"] = "Actual"

pred_df = pd.DataFrame({
    "year": [next_year[0][0]],
    "sales_value": [prediction[0]],
    "type": ["Predicted"]
})

plot_df = pd.concat([ml_data, pred_df])

fig_ml = px.line(
    plot_df,
    x="year",
    y="sales_value",
    color="type",
    markers=True,
    title="Actual vs Predicted Pharma Sales"
)

st.plotly_chart(fig_ml, use_container_width=True)


# EXPORT REPORT

st.header("Export Dashboard Report")

def generate_pdf():

    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Healthcare Analytics Report", styles['Title']))
    story.append(Spacer(1, 20))

    story.append(Paragraph("Total Revenue Analysis", styles['Heading2']))
    story.append(
        Paragraph(
            f"Total Revenue: {merged['sales_value'].sum():,.2f}",
            styles['Normal']
        )
    )

    story.append(Spacer(1, 20))

    story.append(Paragraph("Top Hospital", styles['Heading2']))

    top_hospital = hospital_sales.sort_values(
        "sales_value",
        ascending=False
    ).iloc[0]["hospital"]

    story.append(Paragraph(top_hospital, styles['Normal']))

    doc = SimpleDocTemplate(buffer)
    doc.build(story)

    buffer.seek(0)

    return buffer


st.download_button(
    label="Download Analytics Report (PDF)",
    data=generate_pdf(),
    file_name="healthcare_dashboard_report.pdf",
    mime="application/pdf"
)


# 3D ANALYTICS

st.header("3D Healthcare Analytics")

fig6 = px.scatter_3d(
    hospital_perf,
    x="sales_value",
    y="treatment_cost",
    z="quantity",
    color="hospital",
    size="sales_value",
    title="3D Hospital Performance"
)

st.plotly_chart(fig6, use_container_width=True)


# ADVANCED ANALYTICS

st.header("Advanced Data Analytics")

corr_data = merged[["sales_value", "quantity", "treatment_cost"]]

fig7, ax = plt.subplots()

sns.heatmap(
    corr_data.corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig7)


# DOWNLOAD DATA BUTTON 

st.header("Download Data")

download_df = merged.copy()

if "patient_id" in download_df.columns:
    download_df = download_df.sort_values("patient_id")

download_df = download_df.reset_index(drop=True)

csv = download_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Full Healthcare Data (CSV)",
    data=csv,
    file_name="healthcare_warehouse_data.csv",
    mime="text/csv"
)


# BUSINESS INSIGHTS

st.header("Business Insights")

top_hospital = hospital_sales.sort_values(
    "sales_value",
    ascending=False
).iloc[0]

top_medicine = medicine_sales.iloc[0]

st.success(
    f"Top Hospital: {top_hospital['hospital']} with revenue ₹{top_hospital['sales_value']:,}"
)

st.info(
    f"Most Sold Medicine: {top_medicine['medicine']} with quantity {top_medicine['quantity']}"
)

st.write(
    "This dashboard automatically updates when the ETL pipeline loads new data into the PostgreSQL data warehouse."
)
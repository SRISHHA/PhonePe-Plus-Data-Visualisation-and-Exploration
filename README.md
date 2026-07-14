# PhonePe Pulse Data Visualization and Analytics Dashboard

## Overview

This project is an interactive **PhonePe Pulse Data Visualization and Analytics Dashboard** built using **Python, Streamlit, SQLite, Plotly, and Git**. The application extracts transaction and user data from the official **PhonePe Pulse GitHub repository**, transforms the raw JSON files into structured datasets, stores them in a SQLite database, and provides interactive visualizations and analytics through a Streamlit web application.

The dashboard enables users to explore digital payment trends across India by filtering data based on **year**, **quarter**, **transaction type**, and **user statistics**.

---

# Problem Statement

India has witnessed rapid growth in digital payments, generating massive amounts of transaction and user data. However, analyzing this hierarchical JSON data manually is complex and time-consuming.

The objective of this project is to:

- Extract PhonePe Pulse data from GitHub.
- Transform nested JSON files into structured tabular datasets.
- Store the processed data in a relational database.
- Build an interactive dashboard for exploratory data analysis and visualization.
- Provide insights into transaction volume, user growth, and geographical payment trends.

---

# Dataset

**Source:** Official PhonePe Pulse GitHub Repository

The project extracts data from six major categories:

### Aggregated Transaction Data

Contains transaction statistics categorized by:

- State
- Year
- Quarter
- Transaction Type
- Transaction Count
- Transaction Amount

---

### Aggregated User Data

Contains device-wise user statistics including:

- Brand
- User Count
- User Percentage

---

### Map Transaction Data

District-level transaction information including:

- District
- Transaction Count
- Transaction Amount

---

### Map User Data

District-wise registered users.

---

### Top Transaction Data

Top performing pincodes based on transaction activity.

---

### Top User Data

Top registered users by pincode.

---

# Project Workflow

## 1. Data Extraction

- Cloned the PhonePe Pulse GitHub repository using GitPython.
- Traversed nested JSON directories.
- Parsed JSON files.
- Extracted relevant fields.

---

## 2. Data Transformation

Converted hierarchical JSON into structured Pandas DataFrames.

Created datasets for:

- Aggregated Transactions
- Aggregated Users
- Map Transactions
- Map Users
- Top Transactions
- Top Users

---

## 3. Database Loading

Designed SQLite tables for storing processed datasets.

Tables include:

- agg_tran
- agg_user
- map_tran
- map_user
- top_tran
- top_user

---

## 4. Data Visualization

Built an interactive Streamlit dashboard allowing users to:

- Filter by Year
- Filter by Quarter
- Analyze Transactions
- Analyze Users
- Visualize state-wise performance
- Compare transaction statistics

---

# System Architecture

```text
              PhonePe Pulse GitHub Repository
                          │
                          ▼
                   Git Repository Clone
                          │
                          ▼
                  JSON Data Extraction
                          │
                          ▼
                Data Transformation (Pandas)
                          │
                          ▼
                  Structured DataFrames
                          │
                          ▼
                    SQLite Database
                          │
                          ▼
                SQL Query Processing
                          │
                          ▼
                Streamlit Dashboard
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
  Interactive Maps    Analytics      Data Exploration
```

---

# ETL Pipeline

```text
GitHub Repository
        │
        ▼
Clone Repository
        │
        ▼
Read JSON Files
        │
        ▼
Extract Required Fields
        │
        ▼
Create Pandas DataFrames
        │
        ▼
Store in SQLite Database
        │
        ▼
SQL Queries
        │
        ▼
Interactive Streamlit Dashboard
```

---

# Database Schema

## Aggregated Transaction

- State
- Year
- Quarter
- Transaction Type
- Transaction Count
- Transaction Amount

---

## Aggregated User

- State
- Year
- Quarter
- Brand
- User Count
- User Percentage

---

## Map Transaction

- State
- Year
- Quarter
- District
- Transaction Count
- Transaction Amount

---

## Map User

- State
- Year
- Quarter
- District
- Registered User

---

## Top Transaction

- State
- Year
- Quarter
- Pincode
- Transaction Count
- Transaction Amount

---

## Top User

- State
- Year
- Quarter
- Pincode
- Registered User

---

# Dashboard Features

## 1. Interactive Filters

- Transaction/User Selection
- Year Selection
- Quarter Selection

---

## 2. India Choropleth Map

Visualizes:

- State-wise Transaction Amount
- State-wise Registered Users

---

## 3. Analytics Dashboard

Displays:

### Transaction Analytics

- Total Transaction Amount
- Average Transaction Amount
- Total Transaction Count
- Top 10 States by Transactions
- Top 10 Districts by Transaction Amount
- Transaction Type Distribution

---

### User Analytics

- Total Registered Users
- Top States by User Count
- Top Districts by Registered Users

---

# Visualizations

The application includes:

- Choropleth Maps
- Bar Charts
- Pie Charts
- Treemaps
- Interactive Tables

---

# SQL Queries

The project performs analytical SQL queries including:

- State-wise transaction aggregation
- User count aggregation
- District-wise transaction analysis
- Top performing states
- Top performing districts
- Transaction type comparison

---

# Technologies Used

## Programming Language

- Python

## Data Processing

- Pandas
- JSON

## Database

- SQLite

## Data Visualization

- Plotly Express
- Plotly Graph Objects
- Folium

## Web Framework

- Streamlit

## Version Control

- GitPython

---

# Project Structure

```text
PhonePe-Pulse-Data-Visualization

│
├── data_extraction.py
├── database.py
├── app.py
├── youE.db
├── requirements.txt
├── README.md
│
├── data/
│   ├── aggregated/
│   ├── map/
│   └── top/
│
└── assets/
```

---

# Key Features

- Automated GitHub repository cloning
- JSON data extraction
- ETL pipeline
- SQLite database integration
- Interactive Streamlit dashboard
- India state-wise choropleth maps
- Transaction analytics
- User analytics
- SQL-based data exploration
- Interactive visualizations

---

# Business Insights

The dashboard helps answer questions such as:

- Which states have the highest transaction volume?
- Which districts contribute the most to digital payments?
- How has transaction volume changed over time?
- Which mobile brands dominate PhonePe users?
- Which states have the highest registered users?
- What are the most popular transaction types?

---

# Future Improvements

- Integrate MySQL or PostgreSQL instead of SQLite.
- Deploy the dashboard using Streamlit Cloud or AWS.
- Add real-time data synchronization from the PhonePe Pulse repository.
- Build predictive models for transaction forecasting.
- Develop KPI dashboards using Power BI or Tableau.
- Add user authentication and role-based access.
- Enable CSV and Excel report exports.

---

# Learning Outcomes

This project demonstrates practical experience in:

- ETL Pipeline Development
- JSON Data Processing
- Git Repository Automation
- SQL Database Design
- Data Visualization
- Dashboard Development
- Exploratory Data Analysis (EDA)
- Interactive Web Applications

---

# Tech Stack

- Python
- Streamlit
- Pandas
- SQLite
- Plotly
- GitPython
- JSON
- Folium

---

# Author

**SRISHHA**

## 🚀 superstore-data-pipeline

A Medallion Architecture data pipeline for the Superstore dataset using Mage ETL and Snowflake, with analytics and dashboards in Power BI

## Pipeline Overview

This project implements a **Medallion Architecture** workflow for transforming Superstore sales data:

1. **CSV Source (Bronze layer)** – Raw sales data from Superstore.
2. **Transformations (Silver layer)** – Data cleaning, deduplication, and standardization in Mage.
3. **Gold Layer (modeled tables)** – Analytics-ready tables modeled in Mage and loaded into Snowflake. 
4. **Visualization** – Power BI dashboards connect to Snowflake to generate insights from Gold tables.

 ##  Key Technologies
| Component | Technology |
|----------|------------|
| **Orchestration / ETL** | Mage AI |
| **Storage Source** | CSV |
| **Data Warehouse** | Snowflake |
| **Data Modeling** | Medallion Architecture (Gold Layer) |
| **Visualization** | Power BI |

 ## 🏗️ Pipeline Architecture

<img width="859" height="273" alt="2+docker" src="https://github.com/user-attachments/assets/b581a259-0755-4163-bdb0-589fe43fe63c" />


## 🧱 Mage AI Pipeline Implementation 
<img width="934" height="535" alt="ETL_MAGE" src="https://github.com/user-attachments/assets/05498c1f-3784-4a37-92f7-8453bdc9c7b6" />

## 📊 Gold Layer Data Model 
The Gold Layer is designed using a Star Schema to ensure optimal query performance for Power BI.
The Gold layer contains dimensional and fact tables created in Mage AI.

- dim_customers
- dim_products
- dim_dates
- fact_sales

These tables are modeled in Mage (Transform blocks) and loaded to Snowflake.
<img width="1087" height="715" alt="Modeling" src="https://github.com/user-attachments/assets/7c539826-ddc8-474b-94de-30f5353d5ac4" />

## 📈 Visualization and Business Insights (Power BI)
The Power BI report is configured to connect directly to the cleaned and modeled tables in Snowflake.

Platform: Microsoft Power BI Desktop / Service

Data Source: Snowflake Data Warehouse

Connection Mode: Import Mode

note: data is refreshed daily/hourly, providing fast dashboard performance.

## Core Insights and Metrics
The dashboard is designed to answer the following core business questions:

1. Profitability Analysis: Tracks Profit Margin and Return on Investment (ROI) by region and product category.

2. Sales Trends: Monitors month-over-month and year-over-year Sales Growth and volume.

3. Customer Performance: Identifies top customers and measures sales by customer segment.

4. Operational Efficiency: Tracks the average time from Order Date to Ship Date.

<img width="1324" height="740" alt="Dashboard page" src="https://github.com/user-attachments/assets/92d6b366-491a-438e-853b-db93840fe32c" />


## 🛠️ 1. Setup and Installation

Prerequisites: 

Python 3.10+

Docker and Docker Compose 

Snowflake Account Access (Role and Warehouse permissions)

### Installation Steps

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/IbtsamGhreeb/superstore-data-pipeline.git
    cd superstore-data-pipeline
    ```

2.  **Install Python Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Start Mage AI (using Docker):**

    ```bash
    docker compose up -d
    ```

    *This command will start the Mage server and all required services.*

4.  **Access Mage UI:** Open your browser to `http://localhost:6789`.



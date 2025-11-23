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


## 📊 Gold Layer Data Model
The Gold Layer is designed using a Star Schema to ensure optimal query performance for Power BI.

## 🧱 Mage AI Pipeline Implementation 
<img width="934" height="535" alt="ETL_MAGE" src="https://github.com/user-attachments/assets/05498c1f-3784-4a37-92f7-8453bdc9c7b6" />

## 📊 Gold Layer Data Model (ERD)
<img width="1087" height="715" alt="Modeling" src="https://github.com/user-attachments/assets/7c539826-ddc8-474b-94de-30f5353d5ac4" />



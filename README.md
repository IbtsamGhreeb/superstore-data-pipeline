##🚀 superstore-data-pipeline
A Medallion Architecture data pipeline for the Superstore dataset using Mage ETL and Snowflake, with analytics and dashboards in Power BI

## Pipeline Overview

This project implements a **Medallion Architecture** workflow for transforming Superstore sales data:

1. **CSV Source (Bronze layer)** – Raw sales data from Superstore.
2. **Transformations (Silver layer)** – Data cleaning, deduplication, and standardization in Mage.
3. **Gold Layer (modeled tables)** – Analytics-ready tables modeled in Mage and loaded into Snowflake. 
4. **Visualization** – Power BI dashboards connect to Snowflake to generate insights from Gold tables.

 ##  Key Technologies
 <img width="441" height="92" alt="Tools" src="https://github.com/user-attachments/assets/41eee7a3-52a3-4ee9-acd6-97c9aa125342" />


 ## 🏗️ Pipeline Architecture

<img width="859" height="273" alt="2+docker" src="https://github.com/user-attachments/assets/b581a259-0755-4163-bdb0-589fe43fe63c" />

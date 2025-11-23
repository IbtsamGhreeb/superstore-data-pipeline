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
<img width="1087" height="715" alt="Modeling" src="https://github.com/user-attachments/assets/7c539826-ddc8-474b-94de-30f5353d5ac4" />

This is an excellent, visually rich, and well-structured README! The immediate display of the three key diagrams (Architecture, DAG, and ERD) makes it highly effective.

To make it a complete and professional data engineering document, you need to add the operational and developer-focused sections—the "How-to" instructions that a new team member would need.

Here are the essential sections to add:

## 🛠️ 1. Setup and Installation

Prerequisites
Python 3.10+

Docker and Docker Compose 

Snowflake Account Access (Role and Warehouse permissions)
Installation Steps
Clone the Repository:

```markdown
### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/superstore-data-pipeline.git](https://github.com/your-username/superstore-data-pipeline.git)
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

4.  **Access Mage UI:** Open your browser to `http://localhost:6789`..



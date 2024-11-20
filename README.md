# Reddit Data Engineering Pipeline

This project offers a robust ETL (Extract, Transform, Load) solution for ingesting Reddit data into an Amazon Redshift data warehouse. The pipeline utilizes a variety of tools and services, including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)

## Overview
The data pipeline is designed to:
- Extract Reddit data via its API.
- Store raw data in an Amazon S3 bucket using Apache Airflow.
- Transform the data with AWS Glue and Amazon Athena.
- Load the transformed data into Amazon Redshift for analysis and querying.

## Architecture
(https://github.com/user-attachments/assets/5985e50d-2ac9-40d4-9267-0926e75f7448)

### Components
- **Reddit API**: Data source.
- **Apache Airflow & Celery**: Coordinate the ETL workflow and handle task execution.
- **PostgreSQL**: Temporary data storage and metadata management.
- **Amazon S3**: Storage for raw data.
- **AWS Glue**: Data cataloging and ETL processing.
- **Amazon Athena**: Perform SQL-based transformations.
- **Amazon Redshift**: Final data storage and analytics platform.

## Prerequisites
To set up and run the pipeline, ensure the following:
- An AWS account with permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials.
- Docker installed on your system.
- Python version 3.9 or higher.

﻿# UserDataPipeline

## Project Overview

This project sets up a data pipeline that extract user data from a public API, stores it in an S3 bucket, processes and transform the data using AWS Lambda, and then saves it into an RDS database. This project demonstrates how to automate data collection and storage using AWS services, making data management easier and more efficient. The pipeline ensures that user data is systematically collected, transformed, and stored for further use.


## Architecture

![Architecture Diagram](./architecture.png)

- **API**: Fetches user data.
- **Amazon S3**: Stores the fetched data.
- **AWS Lambda**: Processes the stored data.
- **Amazon RDS**: Saves the processed & formated data in a db.

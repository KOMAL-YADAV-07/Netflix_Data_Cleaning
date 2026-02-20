# netflix_data_cleaning
The final cleaned dataset is consistent, well-structured, and ready for exploratory data analysis and visualization. This project demonstrates practical skills in data wrangling, feature engineering, and preprocessing using Python and Pandas.

# 📊 Netflix Data Cleaning & Preprocessing Project

## 🔍 Project Overview

This project focuses on cleaning and preprocessing the Netflix Movies & TV Shows dataset to make it analysis-ready.

Raw datasets often contain missing values, inconsistent formats, mixed data types, and noisy text. The objective of this project is to apply systematic data cleaning techniques using Python and Pandas to improve data quality and ensure accurate analysis.

---

## 📁 Dataset Details

* Dataset: Netflix Movies & TV Shows
* Total Records: 7,787
* Total Features: 12
* File: `movies_netflix.csv`
* Tools Used: Python, Pandas, VS Code

---

## 🧹 Data Cleaning & Preprocessing Steps

### 1️⃣ Missing Value Treatment

* **Director & Cast**
  Replaced missing values with `"Not Available"` to retain records.

* **Country**
  Filled missing values with `"Unknown"` to preserve dataset completeness.

* **Rating**
  Imputed missing values using the mode (most frequent category).

* **Date Added**
  Removed rows with missing values as they were minimal and critical for time-based analysis.

---

### 2️⃣ Date Formatting & Standardization

* Removed leading/trailing spaces using `.str.strip()`
* Converted `date_added` column to datetime format using `pd.to_datetime()`

This enables:

* Year-wise analysis
* Month-wise trend analysis
* Time-based visualizations

---

### 3️⃣ Duration Column Transformation

The `duration` column contained mixed units such as:

* "93 min" (Movies)
* "4 Seasons" (TV Shows)

To prevent incorrect statistical calculations:

* Extracted numeric values → `duration_number`
* Extracted unit values → `duration_type`
* Ensured movies and TV shows can be analyzed separately

---

### 4️⃣ Duplicate Removal

* Identified and removed duplicate records to maintain data integrity.

---

### 5️⃣ Column Standardization

* Converted all column names to lowercase
* Removed unnecessary spaces
* Improved naming consistency for professional coding standards

---

## 📈 Outcome

After preprocessing, the dataset became:

* Structured
* Consistent
* Free from major missing value issues
* Ready for Exploratory Data Analysis (EDA)
* Suitable for visualization and machine learning tasks

---

## 🚀 Skills Demonstrated

* Data Cleaning
* Missing Value Handling
* Regular Expressions (Regex)
* Data Type Conversion
* Feature Engineering
* Data Standardization
* Pandas Data Manipulation

---

## 👩‍💻 Author

Komal<br>
Aspiring Data Analyst | Python & Data Analytics Enthusiast

---

⭐ This project demonstrates practical data preprocessing skills applied to a real-world dataset.


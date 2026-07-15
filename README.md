# Generative AI Usage Dashboard

The dashboard provides interactive visualizations and summary insights into AI model usage, prompt characteristics, latency, token consumption, and inference costs.

---

## Project Overview

This project analyzes a dataset containing information about interactions with various Large Language Models (LLMs). It aims to provide an overview of usage patterns through descriptive statistics and interactive visualizations.

The dashboard is built using **Streamlit**, **Pandas**, **Plotly**, **Matplotlib**, and **Seaborn**, making it easy to explore the dataset without writing additional code.

---

## Features

### Dataset Overview

- Displays the total number of rows and columns
- Reports the number of missing values
- Identifies duplicate records

### Numerical Variable Analysis

For every numerical variable, the dashboard displays:

- Histogram showing the data distribution
- Box plot for identifying spread and potential outliers
- Mean
- Median
- Standard Deviation
- Skewness

### Categorical Variable Analysis

For every categorical variable, the dashboard displays:

- Frequency bar chart
- Most frequent category
- Number of occurrences of the most common category

### Overall Dataset Insights

Provides a concise summary including:

- Total sessions analyzed
- Most popular AI model
- Most common application domain
- Most common task type
- Average prompt length
- Average total tokens
- Average response latency
- Average estimated inference cost

---

## Technologies Used

- Python 3.x
- Streamlit
- Pandas
- NumPy
- Plotly Express
- Matplotlib
- Seaborn
- SciPy

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/generative-ai-usage-dashboard.git

cd generative-ai-usage-dashboard
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Application

Start the Streamlit server

```bash
streamlit run app.py
```

The dashboard will automatically open in your web browser.

---

## Dataset

The project uses a dataset containing usage information for multiple Generative AI models.

Example variables include:

| Variable | Description |
|----------|-------------|
| model_name | AI model used |
| application_domain | Application category |
| task_type | Type of prompt/task |
| prompt_length | Prompt length |
| total_tokens | Number of tokens processed |
| latency_sec | Response latency |
| estimated_cost_usd | Estimated API cost |

Several columns that are not required for the current descriptive analysis are excluded during preprocessing:

- session_id
- temperature
- top_p
- rag_enabled
- hallucination_flag
- user_satisfaction

---

## 📈 Dashboard Output

The dashboard currently includes:

- Dataset overview metrics
- Histograms for numerical variables
- Box plots for numerical variables
- Frequency charts for categorical variables
- Automatic statistical summaries
- Overall dataset insights

---


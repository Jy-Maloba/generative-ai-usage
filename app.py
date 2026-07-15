import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

st.set_page_config(
    page_title="GenAI Usage Dashboard",
    layout="wide"
)

st.title("Generative AI Usage Dataset")

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------

df = pd.read_csv("data/genai_llm_usage_dataset_1000.csv")

# -----------------------------------------------------
# Dataset Overview
# -----------------------------------------------------

st.header("Dataset Overview")

col1,col2,col3,col4=st.columns(4)

col1.metric("Rows",len(df))
col2.metric("Columns",len(df.columns))
col3.metric("Missing Values",df.isnull().sum().sum())
col4.metric("Duplicates",df.duplicated().sum())

# -----------------------------------------------------
# Numerical Analysis
# -----------------------------------------------------
df = df.drop(["session_id", "temperature", "top_p", "rag_enabled", "hallucination_flag", "user_satisfaction"],axis=1)

st.header("Numerical Variable Analysis")

numeric=df.select_dtypes(include=np.number).columns

for col in numeric:

    st.subheader(col)

    c1,c2=st.columns(2)

    with c1:

        fig=px.histogram(
            df,
            x=col,
            nbins=30,
            title=f"{col} Distribution"
        )

        st.plotly_chart(fig,use_container_width=True)

    with c2:

        fig=px.box(
            df,
            y=col,
            title=f"{col} Boxplot"
        )

        st.plotly_chart(fig,use_container_width=True)

    st.info(
        f"""
        Mean = {df[col].mean():.2f}

        Median = {df[col].median():.2f}

        Standard deviation = {df[col].std():.2f}

        Skewness = {skew(df[col]):.2f}
        """
    )

# -----------------------------------------------------
# Categorical Analysis
# -----------------------------------------------------

st.header("Categorical Variables")

categorical=df.select_dtypes(include='object').columns

for col in categorical:

    st.subheader(col)

    counts=df[col].value_counts()

    fig=px.bar(
        counts,
        x=counts.index,
        y=counts.values,
        labels={"x":col,"y":"Count"},
        title=f"{col} Frequency"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.success(
        f"Insight: {counts.idxmax()} is the most frequent category with {counts.max()} records."
    )

# -----------------------------------------------------
# Final Insights
# -----------------------------------------------------

st.header("Overall Insights")

st.markdown(f"""
- Total sessions analysed: **{len(df)}**

- Most popular model: **{df['model_name'].mode()[0]}**

- Most common application: **{df['application_domain'].mode()[0]}**

- Most common task: **{df['task_type'].mode()[0]}**

- Average prompt length: **{df['prompt_length'].mean():.0f}**

- Average total tokens: **{df['total_tokens'].mean():.0f}**

- Average latency: **{df['latency_sec'].mean():.2f} sec**

- Average cost: **${df['estimated_cost_usd'].mean():.4f}**

""")
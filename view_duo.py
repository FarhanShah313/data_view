import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data
iris = sns.load_dataset("iris")

# Set page title
st.title("Data Visualization with Streamlit")

# Display sample data
st.subheader("Sample Iris Dataset")
st.dataframe(iris)

# Select columns for visualization
columns = st.multiselect("Select columns to visualize", iris.columns)

# Plot data based on selected columns
if columns:
    selected_data = iris[columns]
    st.subheader("Data Visualization")
    st.line_chart(selected_data)

    if len(columns) == 2:
        st.subheader("Scatter Plot")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=iris, x=columns[0], y=columns[1], hue='species')
        st.pyplot(plt)
else:
    st.info("Please select at least one column.")

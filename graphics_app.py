import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def generate_line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Line Plot')

    return fig


def generate_bar_chart():
    categories = ['A', 'B', 'C', 'D']
    values = [3, 7, 4, 9]

    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart')

    return fig


def generate_scatter_plot():
    x = np.random.randn(100)
    y = np.random.randn(100)

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Scatter Plot')

    return fig


# Set page title
st.title("Sample Graphics with Streamlit")

# Generate and display line plot
st.subheader("Line Plot")
line_plot = generate_line_plot()
st.pyplot(line_plot)

# Generate and display bar chart
st.subheader("Bar Chart")
bar_chart = generate_bar_chart()
st.pyplot(bar_chart)

# Generate and display scatter plot
st.subheader("Scatter Plot")
scatter_plot = generate_scatter_plot()
st.pyplot(scatter_plot)

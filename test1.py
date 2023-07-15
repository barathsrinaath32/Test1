import pandas as pd
import seaborn as sns
import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Define a function to load the CSV file
def load_csv(file):
    return pd.read_csv(file)

# Add a file uploader widget
file = st.file_uploader("Upload CSV file", type=["csv"])

# Check if a file is uploaded
if file is not None:
    # Load the CSV file
    df = load_csv(file)

    # Data Cleaning
    df['Page'] = df['Page'].astype(str)
    df['Total Followers'] = pd.to_numeric(df['Total Followers'])
    df['New Followers'] = pd.to_numeric(df['New Followers'])
    df['Total post engagements'] = pd.to_numeric(df['Total post engagements'])
    df['Total post reactions'] = pd.to_numeric(df['Total post reactions'])
    df['Total post comments'] = pd.to_numeric(df['Total post comments'])
    df['Total reposts'] = pd.to_numeric(df['Total reposts'])
    df['Total posts'] = pd.to_numeric(df['Total posts'])

    # Display the data type of 'Page' column
    column_data_type = df['Page'].dtype
    st.write("Data type of 'Page' column:", column_data_type)

    # Create bar plot for 'Total Followers'
    st.subheader("Bar Plot - Total Followers")
    fig1, ax1 = plt.subplots()
    ax1 = sns.barplot(data=df, x='Page', y='Total Followers', palette='viridis')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)
    for p1 in ax1.patches:
        ax1.annotate(format(p1.get_height(), '.2f'), (p1.get_x() + p1.get_width() / 2., p1.get_height()),
                     ha='center', va='center', xytext=(0, 5), textcoords='offset points')
    st.pyplot(fig1)

    # Create bar plot for 'New Followers'
    st.subheader("Bar Plot - New Followers")
    fig2, ax2 = plt.subplots()
    ax2 = sns.barplot(data=df, x='Page', y='New Followers', palette='magma')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
    for p2 in ax2.patches:
        ax2.annotate(format(p2.get_height(), '.2f'), (p2.get_x() + p2.get_width() / 2., p2.get_height()),
                     ha='center', va='center', xytext=(0, 5), textcoords='offset points')
    st.pyplot(fig2)

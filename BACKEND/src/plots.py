import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import pandas as pd
import seaborn as sns
import findspark
from pymongo import MongoClient
from pyspark.sql.functions import isnan, when, count, col
import pyspark.sql.functions as F
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType
from flask import  jsonify
import pyspark.sql.functions as F
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

spark=SparkSession.builder.appName('NITIAYOG Health data analysis').getOrCreate()

df=None

# def load_db():
#     global df1
#     csv_file_path = "./DATABASE/NDAP.csv"
#     df1= spark.read.csv(csv_file_path, header=True, inferSchema=True)

def connectToDB():
    global df
    client = MongoClient('mongodb://localhost:27017/')
    db = client['NITIAYOG']
    collection = db['Health']
    cursor = collection.find()
    data_list = list(cursor)
    df = pd.DataFrame(data_list)

# Call the function to connect to MongoDB and create the Spark DataFrame

def plot_histogram(column_name):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column_name], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def plot_boxplot(column_name):
    plt.figure(figsize=(10, 6))
    plt.boxplot(df[column_name], vert=False)
    plt.title(f'Box Plot of {column_name}')
    plt.xlabel(column_name)
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def plot_scatter(col1, col2):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[col1], df[col2], alpha=0.5)
    plt.title(f'Scatter Plot of {col1} vs {col2}')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.grid(True)
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

# Define a function to plot pie chart for a column
def plot_pie_chart(col_name, group_by_col):
    # Group the DataFrame by group_by_col and calculate the mean of col_name
    grouped_df = df.groupby(group_by_col)[col_name].mean().reset_index().sort_values(by=group_by_col)
    
    # Plot pie chart
    plt.figure(figsize=(10, 6))
    plt.pie(grouped_df[col_name], labels=grouped_df[group_by_col], autopct='%1.1f%%', startangle=140)
    plt.title(f'Pie Chart for {col_name} grouped by {group_by_col}')
    plt.axis('equal')
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64
    
def plot_line(col1 , col2):
    plt.figure(figsize=(10, 6))
    df.plot(x=col1, y=col2, kind='line')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title(f'Lineplot Plot of {col1} vs {col2}')
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def lr1():
    selected_columns = [
    "Stunted children under the age of 5 years (%)",
    "Severely stunted children under the age of 5 years (%)",
    "Wasted children under the age of 5 years (%)",
    "Underweight children under the age of 5 years (%)"
    ]

    # Filter the DataFrame to keep only the selected columns
    df_filtered = df[selected_columns]

    # Drop rows with missing values
    df_filtered = df_filtered.dropna()

    # Separate features and target
    X = df_filtered[selected_columns[:-1]]  # Features
    y = df_filtered[selected_columns[-1]]   # Target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the linear regression model
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # Make predictions
    y_pred = lr.predict(X_test)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    title_text = "Stunted children under the age of 5 years (%)\nSeverely stunted children under the age of 5 years (%)\nWasted children under the age of 5 years (%)\nUnderweight children under the age of 5 years (%)"
    plt.title(title_text, loc='left') 
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def lr2():
    selected_columns = [
    "Stunted children under the age of 5 years (%)",
    "Severely stunted children under the age of 5 years (%)"
    ]
    df1 = df.dropna(subset=selected_columns)

    # Prepare features and target
    X = df1[selected_columns[0]].values.reshape(-1, 1)  # Features
    y = df1[selected_columns[1]]  # Target

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Fit the model
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # Make predictions
    predictions = lr.predict(X_test)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, predictions,c='red',label='Predicted values')
    plt.scatter(X_test , y_test , c='green',label='Actual values')
    plt.legend()
    plt.xlabel("Stunted children under the age of 5 years (%)")
    plt.ylabel("predicted Severely stunted children under the age of 5 years (%)")
    plt.title("Stunted children under the age of 5 years (%) , Severely stunted children under the age of 5 years (%)")
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def lr3():
    selected_columns = [
    "Wasted children under the age of 5 years (%)",
    "Severely wasted children under the age of 5 years (%)"
    ]

    # Drop rows with null values in selected columns
    df1 = df.dropna(subset=selected_columns)

    # Assemble features
    X = df1[selected_columns]

    # Select target column
    y = df1["Severely wasted children under the age of 5 years (%)"]

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create Linear Regression model
    lr = LinearRegression()

    # Fit the model
    lr.fit(X_train, y_train)

    # Make predictions
    predictions = lr.predict(X_test)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions)
    plt.xlabel("Wasted children under the age of 5 years (%)")
    plt.ylabel("Severely wasted children under the age of 5 years (%)")
    plt.title("Wasted children under the age of 5 years (%) \n Severely wasted children under the age of 5 years (%)" )
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def kmeans1():
        
    # Select appropriate columns for clustering
    columns_for_clustering = ['Stunted children under the age of 5 years (%)',
                            'Severely stunted children under the age of 5 years (%)']

    # Assemble the features vector
    data = df[columns_for_clustering]

    # Scale the features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Define the number of clusters
    num_clusters = 3

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(scaled_data)
    predictions = kmeans.predict(scaled_data)

    # Get cluster centers
    cluster_centers = kmeans.cluster_centers_

    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    for i in range(num_clusters):
        cluster_data = data[predictions == i]
        plt.scatter(cluster_data.iloc[:, 0], cluster_data.iloc[:, 1], label=f'Cluster {i+1}')

    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', color='black', label='Centroids')
    plt.xlabel(columns_for_clustering[0])
    plt.ylabel(columns_for_clustering[1])
    plt.title('K-means Clustering')
    plt.legend()
    plt.grid(True)
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64
    

def kmeans2():
    # Select appropriate columns for clustering
    columns_for_clustering = ['Wasted children under the age of 5 years (%)',
                            'Severely wasted children under the age of 5 years (%)']

    # Drop rows with missing values in selected columns
    df1= df.dropna(subset=columns_for_clustering)

    # Scale the features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df1[columns_for_clustering])

    # Define the number of clusters
    num_clusters = 3

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(scaled_data)
    clusters = kmeans.predict(scaled_data)
    centroids = kmeans.cluster_centers_

    # Convert cluster centers to DataFrame
    cluster_centers_pd = pd.DataFrame(centroids, columns=columns_for_clustering)

    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    for i in range(num_clusters):
        cluster_data = scaled_data[clusters == i]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {i+1}')

    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='black', label='Centroids')
    plt.xlabel(columns_for_clustering[0])
    plt.ylabel(columns_for_clustering[1])
    plt.title('K-means Clustering')
    plt.legend()
    plt.grid(True)
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def gmm1():
    # Select appropriate columns for clustering
    columns_for_clustering = ['Stunned children age group of 5 to 9 years (%)', 'Severely stunted children age group of 5 to 9 years (%)']

    # Scale the features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[columns_for_clustering])

    # Define the number of clusters
    num_clusters = 3

    # Apply Gaussian Mixture Model clustering
    gmm = GaussianMixture(n_components=num_clusters)
    model = gmm.fit(scaled_data)
    predictions = model.predict(scaled_data)

    # Get cluster centers
    cluster_centers = model.means_

    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    for i in range(num_clusters):
        cluster_data = scaled_data[predictions == i]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {i+1}')

    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', color='black', label='Centroids')
    plt.xlabel(columns_for_clustering[0])
    plt.ylabel(columns_for_clustering[1])
    plt.title('Gaussian Mixture Model Clustering')
    plt.legend()
    plt.grid(True)
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64
    

def gmm2():
    # Select appropriate columns for clustering
    columns_for_clustering = ['Severely thin adolescents age group of 10 to 14 years less than -3 SD (%)', 
                            'Severely thin adolescents age group of 15 to 19 years less than -3 SD (%)']

    # Assemble the features vector
    data = df[columns_for_clustering]

    # Scale the features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Define the number of clusters
    num_clusters = 3

    # Apply Gaussian Mixture Model clustering
    gmm = GaussianMixture(n_components=num_clusters)
    model = gmm.fit(scaled_data)
    predictions = model.predict(scaled_data)

    # Get cluster centers
    cluster_centers = model.means_

    # Convert cluster centers to Pandas DataFrame for visualization
    cluster_centers_pd = pd.DataFrame(cluster_centers, columns=columns_for_clustering)

    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    for i in range(num_clusters):
        cluster_data = data[predictions == i]
        plt.scatter(cluster_data.iloc[:, 0], cluster_data.iloc[:, 1], label=f'Cluster {i+1}')

    plt.scatter(cluster_centers_pd.iloc[:, 0], cluster_centers_pd.iloc[:, 1], marker='x', color='black', label='Centroids')
    plt.xlabel(columns_for_clustering[0])
    plt.ylabel(columns_for_clustering[1])
    plt.title('Gaussian Mixture Model Clustering')
    plt.legend()
    plt.grid(True)
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

def cor1():
    numeric_columns = [col_name for col_name, data_type in df.dtypes if data_type == "double"]
    df = df.select(numeric_columns)

    # Convert Spark DataFrame to Pandas DataFrame
    df_pd = df.toPandas()

    # Calculate correlation matrix
    correlation_matrix = df_pd.corr()

    # Plot correlation matrix heatmap
    plt.figure(figsize=(25, 25))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix')
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    return img_base64

    
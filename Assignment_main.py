# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:21:43 2023

@author: hm23abi
"""

import pandas as pd
import matplotlib.pyplot as plt


def line_plot(data, title, xlabel, ylabel):
    """
    Show a graph that helps us see how the average delivery time changes with 
    delivery persons' age for different vehicle types.

    Parameters:
        data: Information about deliveries, including the type of vehicle, 
              delivery person's age, and time taken for delivery.
        title: A title for the graph.
        xlabel: Description for the horizontal axis.
        ylabel: Description for the vertical axis.
    """

    # Group data by vehicle type and Age of Delivery person
    # calculate avg delivery time with grouped data
    grouped = data.groupby(['Type_of_vehicle', 'Delivery_person_Age'])[
        'Time_taken(min)'].mean().reset_index()

    # Set the figure size
    plt.figure(figsize=(12, 6))

    # Plot a line for each unique type of vehicle
    for vehicle in grouped['Type_of_vehicle'].unique():
        vehicle_data = grouped[grouped['Type_of_vehicle'] == vehicle]
        plt.plot(vehicle_data['Delivery_person_Age'],
                 vehicle_data['Time_taken(min)'], label=vehicle)

    # Set title and labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Display legend, grid, and show the plot
    plt.legend()
    plt.grid(True)
    plt.show()


def bar_graph(data, title, xlabel, ylabel):
    """
    Display a graph showing how many orders were made for each type of vehicle.

    Parameters:
        data: Information about deliveries, including the type of vehicle.
        title: A title for the graph.
        xlabel: Description for the horizontal axis.
        ylabel: Description for the vertical axis.
    """

    # Set the figure size
    plt.figure(figsize=(8, 6))

    # Count the number of occurrences of each type of vehicle
    vehicle_counts = data['Type_of_vehicle'].value_counts()

    # Plot a bar for each type of vehicle
    plt.bar(vehicle_counts.index, vehicle_counts)

    # Set labels and title
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel(ylabel, fontsize=15)
    plt.title(title, fontsize=20, fontstyle='italic')

    # Show the plot
    plt.show()


def pie_chart(data, title):
    """
    Display a pie chart showing the distribution of different types of food 
    orders.

    Parameters:
        data: Information about orders, including the type of food ordered.
        title: A title for the pie chart.
    """

    # Set the figure size
    plt.figure(figsize=(12, 8))

    # Count the number of occurrences of each type of food order
    order_counts = data['Type_of_order'].value_counts()

    # Create labels with counts for each type of food order
    labels = [f'{label} ({count})' for label, count in zip(
        order_counts.index, order_counts)]

    # Plot a pie chart
    plt.pie(order_counts, labels=labels,
            autopct='%1.1f%%', textprops={'fontsize': 20})

    # Set title and show the pie chart.
    plt.title(title, fontsize=25, fontstyle='italic')
    plt.show()


# Read the data from the CSV file
df = pd.read_csv("deliverytime.csv")

# Call functions to generate and display plots
line_plot(df, 'Delivery time Analysis', 'Age of delivery person',
          'Delivery time taken(in mins)')
bar_graph(df, 'No of orders delivered by the type of vehicle',
          'Type of Vehicle', 'No of orders delivered')
pie_chart(df, 'Distribution of type of food ordered')

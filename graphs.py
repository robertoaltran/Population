import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_graph(data):
    # for col in ['0', '1', '2', '3', '4', '5+']:
    #     data[col] = data[col].str.replace(',', '').str.replace('$', '').astype(float)

    data.set_index('Focus_Area', inplace=True)
    data_transposed = data.transpose()

    fig, ax = plt.subplots(figsize=(20, 15))

    for focus_area in data_transposed.columns:
        ax.plot(data_transposed.index, data_transposed[focus_area], label=focus_area)

    ax.set_title('Average Sale Prices by Focus Area')
    ax.set_xlabel('Number of Bedroom')
    ax.set_ylabel('Average Sale Price')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_xticklabels(data_transposed.index, rotation=45)  # Set and rotate the x-axis labels

    plt.tight_layout()


    return fig

def plot_bar(data):
    # for col in ['0', '1', '2', '3', '4', '5+']:
    #     data[col] = data[col].str.replace(',', '').str.replace('$', '').astype(float)

    data.set_index('Focus_Area', inplace=True)
    data_transposed = data.transpose()

    fig, ax = plt.subplots(figsize=(20, 15))

    for focus_area in data_transposed.columns:
        plt.bar(data_transposed.index, data_transposed[focus_area], label=focus_area, alpha=0.7)

    ax.set_title('Average Sale Prices by Focus Area')
    ax.set_xlabel('Number of Bedroom')
    ax.set_ylabel('Average Sale Price')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_xticklabels(data_transposed.index, rotation=45)  # Set and rotate the x-axis labels

    plt.tight_layout()

    return fig

def plot_graph_rent(data):
    data.set_index('Focus_Area', inplace=True)
    data = data.replace('[\$,]', '', regex=True).astype(float)
    data_transposed = data.transpose()

    fig, ax = plt.subplots(figsize=(20, 15))

    for focus_area in data_transposed.columns:
        ax.plot(data_transposed.index, data_transposed[focus_area], label=focus_area)

    ax.set_title('Average Weekly Rent by Focus Area')
    ax.set_xlabel('Number of Bedroom')
    ax.set_ylabel('Average Weekly Rent')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_xticklabels(data_transposed.index, rotation=45)  # Set and rotate the x-axis labels

    plt.tight_layout()

    return fig

def plot_bar_rent(data):
    data.set_index('Focus_Area', inplace=True)
    data = data.replace('[\$,]', '', regex=True).astype(float)
    data_transposed = data.transpose()

    fig, ax = plt.subplots(figsize=(20, 15))

    for focus_area in data_transposed.columns:
        ax.bar(data_transposed.index, data_transposed[focus_area], label=focus_area)

    ax.set_title('Average Weekly Rent by Focus Area')
    ax.set_xlabel('Number of Bedroom')
    ax.set_ylabel('Average Weekly Rent')
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_xticklabels(data_transposed.index, rotation=45)  # Set and rotate the x-axis labels

    plt.tight_layout()

    return fig

def display_graphs_page(plot_data, graph_type):
    # st.title('Graphs Page')

    A_Sale = pd.read_csv("data/Average Sale Price.csv")
    A_Rent = pd.read_csv("data/Average weekly rent.csv")
    P_Num = pd.read_csv("data/Number of rental properties.csv")
    S_Vol = pd.read_csv("data/Sales volume.csv")

    A_Sale = A_Sale.replace('-', 0)
    A_Sale['Focus Area'] = A_Sale['Focus Area'] + '_average_sale_price'
    A_Sale = A_Sale.rename(columns={'Focus Area': 'Focus_Area'})

    for col in ['0', '1', '2', '3', '4', '5+']:
        A_Sale[col] = A_Sale[col].str.replace(',', '').str.replace('$', '').astype(float)

    A_Rent = A_Rent.rename(columns={'Number of Bedrooms': 'Focus Area'})
    A_Rent = A_Rent[~A_Rent['Focus Area'].str.contains('Total', case=False)]
    A_Rent['Focus Area'] = A_Rent['Focus Area'] + '_average_weekly_rent'
    A_Rent = A_Rent.rename(columns={'Focus Area': 'Focus_Area'})

    # A_Rent = A_Rent.replace('[\$,]', '', regex=True).astype(float)


    if plot_data and graph_type:
        if plot_data == 'Average sale price':
            data = A_Sale
            if graph_type == 'line':
                plot = plot_graph(data)
                st.pyplot(plot)
            elif graph_type == 'bar':
                plot = plot_bar(data)
                st.pyplot(plot)

        elif plot_data == 'Average weekly rent':
            data = A_Rent
            if graph_type == 'line':
                plot = plot_graph_rent(data)
                st.pyplot(plot) 
            elif graph_type == 'bar':
                plot = plot_bar_rent(data)
                st.pyplot(plot)
    else:
        st.write("Please select a metric to display")

   

# -*- coding: utf-8 -*-
"""
Created on Sun Sept 5, 2021 16:07
@author: Ricardo Lezama
Count the number of tames ANY
"""

import matplotlib.pyplot as plt

import numpy as np


def plot_terms(topic, data, frequency_cutoff):
    """
    The function 'plot_terms' is designed to receive as input a dictionary formatted piece
    of data and plot out a chart visualization. 
      
    
    Args: Topic is the name of the plot/category. Data is a dictionary with frequency counts.
    
    Returns: No object returned. However, plot is automatically generated.
    """
    filter_ones = {term:frequency for term, frequency in data.items() if frequency > frequency_cutoff}  
    filtered = {term:frequency for term, frequency in filter_ones.items() if frequency > round(sum(filter_ones.values())/len(filter_ones))}  
    print(round(sum(filtered.values())/len(filtered)), "Average count as result of total terms minus once identified terms divided by all terms.")
    terms = filtered.keys()
    frequency = filtered.values()   
    y_pos = np.arange(len(terms),step=1)
    x_pos = np.arange(min(filtered.values()), max(filtered.values()), step=round(sum(filtered.values())/len(filtered)))
    plt.barh(y_pos, frequency, align='center', alpha=1)
    plt.yticks(y_pos, terms, fontsize=10)
    plt.xticks(x_pos)
    plt.xlabel('Frecuencia en encabezados')
    plt.title(str(topic), fontsize=13)
    plt.tight_layout()
    plt.show()
    return filtered

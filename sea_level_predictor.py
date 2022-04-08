import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    sea = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(sea['Year'], sea['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(sea['Year'], sea['CSIRO Adjusted Sea Level'])
    best_fit_data = np.array([year for year in range(min(sea['Year']), 2051)])
    ax = plt.plot(best_fit_data, res.intercept + (res.slope*best_fit_data))

    # Create second line of best fit
    lis = linregress(sea[sea['Year'] >= 2000]['Year'], sea[sea['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    second_best_fit_data = np.array([year for year in range(2000, 2051)])
    ax = plt.plot(second_best_fit_data, lis.intercept + (lis.slope*second_best_fit_data))
  
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
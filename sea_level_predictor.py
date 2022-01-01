import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')
    
    # Create scatter plot
    # Use directly plot as it is converted into a fig at the end
    plt.scatter('Year','CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    sci_obj = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    # The result is an object with slope and intercept as attributes
    # We're using the available data from 1980 to 2013 to get a slope and we are plotting it but for 1980 to 2051
    yrs_range = pd.Series([i for i in range(1880,2051)])
    sea_level = sci_obj.slope*yrs_range + sci_obj.intercept # y = mx + b
    plt.plot(yrs_range, sea_level, 'g')

    # Create second line of best fit
    df_pred = df.loc[df["Year"]>=2000]
    # Now we're using the available data from 2000 to 2013 to make  more accurate predictions
    sci_pred = linregress(df_pred["Year"],df_pred["CSIRO Adjusted Sea Level"])
    yrs_pred = pd.Series([i for i in range(2000,2051)])
    sea_level_pred = sci_pred.slope*yrs_pred + sci_pred.intercept
    plt.plot(yrs_pred, sea_level_pred, 'b')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
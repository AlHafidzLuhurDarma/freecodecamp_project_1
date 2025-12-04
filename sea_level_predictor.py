import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress


df = pd.read_csv("/content/epa-sea-level.csv")

def draw_plot():
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
  plt.xlabel('Year')
  plt.ylabel('CSIRO Adjusted Sea Level')
  plt.title('Scatter Plot of Year vs CSIRO Adjusted Sea Level')
  plt.show()

  line_fit = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
  mask = df["Year"] >= 2000
  line_fit_recent = linregress(df[mask]["Year"], df[mask]["CSIRO Adjusted Sea Level"])

  # Add labels and title
  plt.plot(range(1880, 2051, 1), line_fit.slope*range(1880, 2051, 1)+line_fit.intercept, color="red")
  plt.plot(range(2000, 2051, 1), line_fit_recent.slope*range(2000, 2051, 1)+line_fit_recent.intercept, color='green')
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
  plt.show()
  plt.savefig('sea_level_plot.png')

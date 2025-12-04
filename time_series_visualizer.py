# Pandas, Matplotlib, and Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("/content/fcc-forum-pageviews.csv")


#Set the index to the date column.
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')


#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
less_25 = df['value'] >= df['value'].quantile(0.025)
more_25 = df['value'] <= df['value'].quantile(0.975)

df_clean = df.loc[(less_25 & more_25)]

# Create a draw_line_plot function
def draw_line_plot():
  fig, axes = plt.subplots(figsize=(10,5), dpi=100)
  axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  axes.set_xlabel('Date')
  axes.set_ylabel('Page Views')
  sns.lineplot(data=df_clean, legend=False)
  plt.show()

  fig.savefig('line_plot.png')
  return fig

#Create a draw_bar_plot function
def draw_bar_plot():
  df_bar = df_clean.copy()
  df_bar["Years"] = df_bar.index.year
  df_bar["Months"] = df_bar.index.month_name()

  df_bar = df_bar.groupby(['Years', 'Months'], sort=False)['value'].mean().round().astype(int)
  df_bar = pd.DataFrame(df_bar)
  df_bar = df_bar.rename(columns={'value': 'Average Page Views'})
  df_bar = df_bar.reset_index()

  missing_data = {
      "Years": [2016, 2016, 2016, 2016],
      "Months": ['January', 'February', 'March', 'April'],
      "Average Page Views": [0, 0, 0, 0]
  }
  df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw bar plot
  fig, axes = plt.subplots(figsize=(19.2, 10.8), dpi=100)
  axes.set_title("Daily freeCodeCamp Forum Average Page Views per Month")

  chart = sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", palette="tab10")
  chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='center')


  fig.savefig('bar_plot.png')
  return fig

#Create a draw_box_plot function
def draw_box_plot():
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(32, 10), dpi=100)
    
    # Yearly boxplot
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    # Monthly boxplot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig('box_plot.png')
    return fig

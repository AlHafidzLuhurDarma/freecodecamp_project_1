import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("/content/medical_examination.csv")

'''
Add an overweight column to the data.
To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
'''

bmi = df['weight'] / ((df['height']/100) ** 2)
overweight = []
for i in bmi:
  if i > 25:
    overweight.append(1)
  if i <= 25:
    overweight.append(0)

df['overweight'] = overweight

#Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, 
#set the value to 0. If the value is more than 1, set the value to 1.

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


#Draw the Categorical Plot in the draw_cat_plot function.

def draw_cat_plot():
  df_cat = df.melt(id_vars='cardio',
                   value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                   value_name='value')
  '''
  df_cat = pd.DataFrame({'total':df_cat.groupby(['cardio', 'variable'])['value'].value_counts()})\
                                  .rename(columns={'total':'value'})\
                                  .reset_index()
  '''
  df_cat = pd.DataFrame({'total':df_cat.groupby(['cardio', 'variable'])['value'].value_counts()})\
                                     .rename(columns={'cardio':'Cardio','variable':'Variable', 'value':'Value'})\
                                     .reset_index()
  catplot = sns.catplot(x='variable',
                        y='total',
                        hue='value',
                        col='cardio',
                        data=df_cat,
                        kind='bar')

  fig = catplot.fig

  fig.savefig('catplot.png')
  return fig


'''
* Draw the Heat Map in the draw_heat_map function.

* Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
height is more than the 97.5th percentile
weight is less than the 2.5th percentile
weight is more than the 97.5th percentile

* Calculate the correlation matrix and store it in the corr variable.

* Generate a mask for the upper triangle and store it in the mask variable.

* Set up the matplotlib figure.

* Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
'''

def draw_heat_map():
    # Clean the data
    df_heat = \
        df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(df_heat.corr(), dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr,
                annot=True,
                fmt=".1f",
                linewidth=.5,
                mask=mask,
                annot_kws={'fontsize':7},
                cbar_kws={"shrink": .7},
                square=False,
                center=0,
                vmax=0.30);


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

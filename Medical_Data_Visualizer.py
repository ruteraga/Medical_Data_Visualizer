import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

df['cholesterol']=(df['cholesterol']>1).astype(int)
df['gluc']=(df['gluc']>1).astype(int)

def catplot():
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc','smoke', 'alco', 'active','overweight'])
  df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
  df_cat = df_cat.rename(columns={0: 'total'})
  graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")
  fig = graph.fig
  fig.savefig('catplot.png')
  return fig

def draw_heat_map():
  df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
  (df['height'] >= df['height'].quantile(0.025)) &
  (df['height'] <= df['height'].quantile(0.975)) &
  (df['weight'] >= df['weight'].quantile(0.025)) &
  (df['weight'] <= df['weight'].quantile(0.975))]
  corr = df_heat.corr()
  mask = np.triu(np.ones_like(corr, dtype=bool))
  fig, ax = plt.subplots(figsize=(16, 9))
  sns.heatmap(corr, mask=mask, square=True,
              linewidths=0.5, annot=True, fmt="0.1f")
  fig.savefig('heatmap.png')
  return fig


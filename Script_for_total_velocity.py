# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:39:40 2024

@author: db1671
Scripts to extract and pivot the tables for MoSeq project

"""

#%% Open the file

import pandas as pd
folder = 'C:/Users/db1671/Desktop/MoSeq article draft/Pictures_8-7/raw_data/6OHDA_'
stats_df = pd.read_csv(folder + 'stats_df.csv', usecols=['group','name','syllable','duration','velocity_px_s_mean','frequency'])
moseq_df = pd.read_csv(folder + 'moseq_df.csv', usecols=['group','name','centroid_x','centroid_y','syllable','frame_index'])


#%% Modify the velocity from pixels to mm/s

length_mm = 500
length_px = 300  ## 300 for Mitopark and 6OHDA, 480 for LDOPA
translation_const = length_mm/length_px


#%% Make a table for plotting image
import numpy as np
fps = 30 ## 30 for Mitopark and 6OHDA, 25 for LDOPA


image = moseq_df.pivot(index=['frame_index'], columns=['group','name'], values='syllable')
dx = moseq_df.pivot(index=['frame_index'], columns=['group','name'], values='centroid_x')
dy = moseq_df.pivot(index=['frame_index'], columns=['group','name'], values='centroid_y')
dx = dx.diff()**2
dy = dy.diff()**2
dE = np.sqrt(dx + dy)
distance = dE.sum()

distance_in_mm = distance*transition_const
length=dE.count()
speed = distance_in_mm/(length/fps)

#%% Use the same transition_const to modify all moseq dataframe values from px to mm

stats_df['velocity_mm_s_mean'] = stats_df['velocity_px_s_mean'] * translation_const
moseq_df['centroid_x'] = moseq_df['centroid_x'] * translation_const
moseq_df['centroid_y'] = moseq_df['centroid_y'] * translation_const


#%% Plot everything

sns.boxplot(distance_6OHDA.reset_index().sort_values(by='group'), x='group', y=0)
sns.boxplot(speed_6OHDA.reset_index().sort_values(by='group'), x='group', y=0)
sns.boxplot(distance_Mitopark.reset_index().sort_values(by='group'), x='group', y=0)
sns.boxplot(speed_Mitopark.reset_index().sort_values(by='group'), x='group', y=0)
sns.boxplot(distance_LDOPA.reset_index().sort_values(by='group'), x='group', y=0)
sns.boxplot(speed_LDOPA.reset_index().sort_values(by='group'), x='group', y=0)
sns.boxplot(speed_Mitopark.reset_index().sort_values(by='group'), x='group', y=0)


#%%

# figure styles
sns.set_style('white')
sns.set_context('paper', font_scale=2)
plt.figure(figsize=(12,7))
sns.set_style('ticks', {'axes.edgecolor': '0',  
                        'xtick.color': '0',
                        'ytick.color': '0'})


PROPS = {
    'boxprops':{'facecolor':'none', 'edgecolor':'red'},
    'medianprops':{'color':'green'},
    'whiskerprops':{'color':'blue'},
    'capprops':{'color':'magenta'}
}

ax = sns.lineplot(x="syllable", y="frequency", data=syll_frequency_melted, color='black', hue='Group', err_style='bars')
sns.despine(offset=0, trim=False)
ax.set_xlim(0,50)
ax.set_xticks(range(0,50,10))
plt.axhline(0.005, color='black', linestyle=':')
#sns.plt.show()
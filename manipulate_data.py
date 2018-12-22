import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import os
import re


current_dir = os.path.dirname(os.path.abspath(__file__))

# def f(df):
#     df = df.copy()
#     df['Year'] = DatetimeIndex(df['Date']).year
#     df['Month'] = DatetimeIndex(df['Date']).month
#     df['Day'] = DatetimeIndex(df['Date']).day
#     return df

movies_metadata_csv = os.path.join(current_dir,  'movies_metadata.csv')
# Use tab as delimiter
movies_metadata_pd = pd.read_csv(movies_metadata_csv, sep=',')

# Drop old movies and split date
movies_metadata_pd = movies_metadata_pd[movies_metadata_pd.release_date.str.contains('2[0-9][0-9][0-9]') == True]
movies_metadata_pd['release_month']=[d.split('/')[0] for d in movies_metadata_pd.release_date]
movies_metadata_pd['release_day']=[d.split('/')[1] for d in movies_metadata_pd.release_date]
movies_metadata_pd['release_year']=[d.split('/')[2] for d in movies_metadata_pd.release_date]
#del boxoffice_pd.release_date
movies_metadata_pd['release_month'] = pd.to_numeric(movies_metadata_pd.release_month)
movies_metadata_pd['release_day'] = pd.to_numeric(movies_metadata_pd.release_day)
movies_metadata_pd['release_year'] = pd.to_numeric(movies_metadata_pd.release_year)
movies_metadata_pd['budget'] = pd.to_numeric(movies_metadata_pd.budget)

budget_categories_list = movies_metadata_pd.budget
unique_budget_categories_list = np.unique(budget_categories_list)

boxoffice_csv = os.path.join(current_dir,  'boxoffice.csv')
boxoffice_pd = pd.read_csv(boxoffice_csv, sep=',')

boxoffice_pd = boxoffice_pd[boxoffice_pd.year >= 2000]
boxoffice_pd['studio_u'] = boxoffice_pd.studio.astype("category").cat.codes
# boxoffice_pd['studio_u2'] = pd.Categorical(boxoffice_pd['studio']).codes

studio_categories_list = boxoffice_pd.studio_u
unique_studio_categories_list = np.unique(studio_categories_list)
# display(boxoffice_pd.head(20))

fig, axes = plt.subplots(ncols=1, nrows=2, sharey=True)
plt.subplot(2, 1, 1)
plt.hist(np.array(boxoffice_pd['studio_u']), bins=unique_studio_categories_list, facecolor='green', alpha=4)
plt.xlabel('Studios')
plt.ylabel('Number of movies produced')
plt.subplot(2, 1, 2)
#plt.hist(np.array(boxoffice_pd['studio_u']), bins=unique_studio_categories_list/10, facecolor='green', alpha=4)
plt.hist(np.array(movies_metadata_pd['release_month']), bins=12, facecolor='blue', alpha=0.75)
plt.xlabel('month of release')
plt.ylabel('movies released')
plt.show()


# boxoffice_pd.to_csv('tmp.csv')


# genres to columns
# tmp = boxoffice_pd['genres']
# i = boxoffice_pd.Index("{'id': 10749, 'name': 'Romance'}, {'id': 35, 'name': 'Comedy'}")
# i.str.split(expand=True)
# apply(pd.Series).tolist()

#tmp.to_csv('tmp.csv')

# display(tmp.head(20))

#

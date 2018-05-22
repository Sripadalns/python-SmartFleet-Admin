# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:20:39 2018

@author: sripals
"""

import pandas as pd, numpy as np, matplotlib.pyplot as plt, time
from sklearn.cluster import DBSCAN
from sklearn import metrics
from geopy.distance import great_circle
from shapely.geometry import MultiPoint


# define the number of kilometers in one radian
kms_per_radian = 6371.0088
df = pd.read_csv('location.csv')

# represent points consistently as (lat, lon)
coords = df.as_matrix(columns=['Latitude_1', 'Longitude_1'])

# define epsilon as 0.75 kilometers, converted to radians for use by haversine
epsilon = 0.75/ kms_per_radian

db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))

cluster_labels = db.labels_

# Please refer this link for pandas to csv "https://www.quora.com/How-do-I-add-a-new-column-to-my-already-existing-CSV-file-using-Pandas"

df['CID']=db.labels_
df.to_csv('location.csv')


# get the number of clusters
num_clusters = len(set(cluster_labels))

##print (num_clusters)
##print (cluster_labels)
##print ( len ( coords))



# turn the clusters in to a pandas series, where each element is a cluster of points
clusters = pd.Series([coords[cluster_labels==n] for n in range(num_clusters)])


def get_centermost_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)

centermost_points = clusters.map(get_centermost_point)
print centermost_points

# unzip the list of centermost points (lat, lon) tuples into separate lat and lon lists
lats, lons = zip(*centermost_points)

# from these lats/lons create a new df of one representative point for each cluster
rep_points = pd.DataFrame({'lon':lons, 'lat':lats})


rep_points.to_csv('Center_Point.csv',mode ='a')



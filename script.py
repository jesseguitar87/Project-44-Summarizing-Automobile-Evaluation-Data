import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

manufacturer_country = car_eval.manufacturer_country.value_counts(normalize = True)
print(manufacturer_country)
manufacturer_no_value = car_eval['manufacturer_country'].value_counts()/len(car_eval['manufacturer_country'])
print(manufacturer_no_value)

buying_cost = car_eval['buying_cost'].unique()
print(buying_cost)

buying_cost_categories = ['low', 'med', 'high', 'vhigh']

car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered=True)

median = np.median(car_eval['buying_cost'].cat.codes)
print(median)
median_category = buying_cost_categories[int(median)]
print(median_category)

luggage = car_eval.luggage.value_counts(normalize = True)
print(luggage)
luggage_nodrop = car_eval.luggage.value_counts(dropna = False, normalize = True)
print(luggage_nodrop)

luggage_no_value = car_eval['luggage'].value_counts()/len(car_eval['luggage'])
print(luggage_no_value)

doors = (car_eval['doors'] == '5more').sum()
print(doors)

doors_mean = (car_eval['doors'] == '5more').mean()
print(doors_mean)


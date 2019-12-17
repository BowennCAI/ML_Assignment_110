import csv
import pandas as pd

pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

products_reviews = pd.read_csv('/Users/Lfear/PycharmProjects/ML_Assignment_110/amazon_reviews_us_Gift_Card_v1_00.tsv', sep='\t')
print(products_reviews['star_rating'])

a = [2, 0, 0, 0, 0]

for i in products_reviews['star_rating']:
    a[i-1] = a[i-1] + 1

print(a)
plt.figure(figsize=(16,6))
sns.distplot(a=products_reviews['star_rating'], kde=False)
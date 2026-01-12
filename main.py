def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


df = pd.read_csv("Mall_Customers.csv")
a = df.head()
print(a)
#erkek ve kadın oranini belirleyebiliriz
num_male = df[df['Gender'] == 'Male'].shape[0]
num_female = df[df['Gender'] == 'Female'].shape[0]
plt.pie(
    [num_male, num_female],
    labels=['Male', 'Female'],
    startangle=90,
    autopct='%1.f%%',
    colors=['lavender', 'thistle'])
plt.title('Gender of survey respondants')
plt.show()
#sonucu : %56 female,%44 male
#yillik gelir dagilimlari icin;
plt.hist(df['Annual Income (k$)'], bins=10)
plt.show()
#yillik gelir ve harcama skorlari arasindaki fark;
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'])
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()
#scotter plot incelendiginde 5 farklı kume bulunmustur.

kmeans = KMeans(n_clusters=5,random_state=42)
kmeans.fit(X)

for label in np.unique(kmeans.labels_):
    X_ = X[label == kmeans.labels_]
    plt.scatter(
        X_['Annual Income (k$)'],
        X_['Spending Score (1-100)'],
        label=f'Cluster {label}'
    )

plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segmentation using K-Means')
plt.legend()
plt.show()
#k_means sonucu her musteri gurubu farkli renklerle gosterilmis
#ve benzer davranıslara gore ayrilmistir.

#cluster_1 → Orta gelirli ama çok harcayanlar
#cluster_3 → Zengin ama az harcayanlar

df['Cluster'] = kmeans.labels_
cluster_1 = df[df['Cluster'] == 1]
cluster_3 = df[df['Cluster'] == 3]

df.loc[df['Cluster'] == 1, 'Campaign'] = 'indirim  & sadakat kampanyası'
df.loc[df['Cluster'] == 3, 'Campaign'] = 'VIP Premium kampanya'
#ilk 10 ornek icin cıktı
df[['Annual Income (k$)', 'Spending Score (1-100)', 'Cluster', 'Campaign']].head(10)
x = df['Campaign'].value_counts() #kampanyaya girecek musteri sayisi
print(x)
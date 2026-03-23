import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('TkAgg')
df = pd.read_csv("/Users/fannymarchand/Desktop/Excel portfolio/ecommerce_dataset.csv")
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Nettoyage
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M')
df['Year'] = df['Order_Date'].dt.year
df['Profit_Margin'] = df['Profit'] / df['Sales']

print("Nettoyage OK — shape:", df.shape)

# Analyses
print(df.groupby('Product_Category')['Sales'].sum().round(2))
print(df.groupby('Gender')['Sales'].mean().round(2))
print("Commandes à perte :", (df['Profit'] < 0).sum())

sns.set_theme(style="darkgrid")

# Graphique 1 - Distribution des ventes par catégorie
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='Product_Category', y='Sales', estimator=sum)
plt.title("CA total par catégorie")
plt.savefig("graphique_categories.png")
plt.show()

# Graphique 2 - Répartition par genre
plt.figure(figsize=(6,5))
sns.countplot(data=df, x='Gender', hue='Device_Type')
plt.title("Répartition Homme/Femme par device")
plt.savefig("graphique_genre.png")
plt.show()

# Graphique 3 - Impact du discount sur le profit
plt.figure(figsize=(6,5))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Product_Category', alpha=0.3)
plt.title("Impact du discount sur le profit")
plt.savefig("graphique_discount.png")
plt.show()

# Doublons
print("Doublons :", df.duplicated().sum())

# Valeurs manquantes
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(1)
print(missing_pct[missing_pct > 0])

# Résumé statistique par catégorie
print(df.groupby('Product_Category')[['Sales', 'Profit', 'Discount']].mean().round(2))
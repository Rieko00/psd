---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Data Understanding

## Pengumpulan Data

Dalam proyek ini, data historis saham dari Bank Central Asia (BBCA) dikumpulkan untuk dianalisis. Data diambil dari situs [Investing](https://www.investing.com/equities/bnk-central-as-historical-data), yang menyediakan informasi lengkap terkait pergerakan harga saham selama periode yang ditentukan. Proses pengumpulan data dilakukan dengan mengekspor data dalam bentuk file CSV. Data yang terkumpul mencakup rentang waktu mulai dari tahun 2015 hingga 2024, dengan total 2361 baris data yang mewakili tiap hari perdagangan selama periode tersebut.

## Deskripsi Data

Data saham yang diambil memilik 7 fitur atau kolom, yaitu :

- Tanggal : Tanggal perdagangan saham dengan format YYYY-MM-DD.
- Terakhir : Harga penutupan (Close) saham pada akhir hari perdagangan.
- Pembukaan : Harga saham saat pembukaan (Open) pasar pada awal hari perdagangan.
- Tertinggi : Harga tertinggi yang dicapai oleh saham selama hari perdagangan.
- Terendah : Harga terendah yang dicapai oleh saham selama hari perdagangan.
- Vol.: Volume saham yang diperdagangkan selama hari tersebut.
- Perubahan% : Persentase perubahan harga saham dibandingkan dengan hari perdagangan sebelumnya.

## Exploratory Data Analysis (EDA)

```{code-cell}
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Use raw.githubusercontent.com to access raw data
df = pd.read_csv('https://raw.githubusercontent.com/Rieko00/psd/main/bbca_csv.csv')
df.head()
```

```{code-cell}
df.info()
```

```{code-cell}
df.describe()
```

```{code-cell}
df_numeric = df.select_dtypes(include=['float64', 'int64'])
corelation_matrix = df_numeric.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corelation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```

```{code-cell}
num_column = len(df_numeric.columns)
num_rows = num_column

plt.figure(figsize=(12, 4 * num_column))
for i, column in enumerate(df_numeric.columns, 1):
    plt.subplot(num_column, 1, i)
    plt.hist(df_numeric[column], bins = 20, alpha = 0.5)
    plt.title(column)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
```

```{code-cell}
features = ['Terakhir', 'Pembukaan', 'Tertinggi', 'Terendah', 'Vol.', 'Perubahan%']
plt.subplots(figsize=(20,10))
for i, col in enumerate(features):
  plt.subplot(2,3,i+1)
  sns.boxplot(df[col])
plt.show()
```

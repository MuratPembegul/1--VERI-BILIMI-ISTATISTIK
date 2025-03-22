import pandas as pd

# Örnek veri seti
data = {'Gelir': [5000, 7000, 8000, 7500, 7200, 6800, 7900]}
df = pd.DataFrame(data)

# Tanımlayıcı istatistikler
summary = df.describe()
print(summary)

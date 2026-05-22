#Q6

import pandas as pd
import numpy as np

data = {'A':[1, 2, np.nan, 4],
        'B':[5, np.nan, np.nan, 8]}

df = pd.DataFrame(data)

print("Original Data:\n", df)

df_filled = df.fillna(0)

print("\nAfter replacing missing values:\n", df_filled)

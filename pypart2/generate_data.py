import pandas as pd
import numpy as np
import random

# Set a random seed for reproducibility
np.random.seed(42)
num_samples = 545 # The exact number of rows from your colleague's notebook

# Generate synthetic data
data = {
    'price': np.random.randint(2_000_000, 25_000_000, num_samples), # Prices from 2M to 25M
    'area': np.random.randint(2000, 15000, num_samples),           # Square footage
    'bedrooms': np.random.randint(1, 6, num_samples),              # 1 to 5 bedrooms
    'bathrooms': np.random.randint(1, 4, num_samples),             # 1 to 3 bathrooms
    'stories': np.random.randint(1, 4, num_samples),               # 1 to 3 stories
    'mainroad': np.random.choice(['yes', 'no'], num_samples),
    'guestroom': np.random.choice(['yes', 'no'], num_samples, p=[0.2, 0.8]),
    'basement': np.random.choice(['yes', 'no'], num_samples, p=[0.3, 0.7]),
    'hotwaterheating': np.random.choice(['yes', 'no'], num_samples, p=[0.1, 0.9]),
    'airconditioning': np.random.choice(['yes', 'no'], num_samples, p=[0.4, 0.6]),
    'parking': np.random.randint(0, 4, num_samples),               # 0 to 3 parking spots
    'prefarea': np.random.choice(['yes', 'no'], num_samples, p=[0.3, 0.7]),
    'furnishingstatus': np.random.choice(['furnished', 'semi-furnished', 'unfurnished'], num_samples)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add some logical correlation so the model can actually learn something
# (e.g., more bedrooms/bathrooms/area = higher price)
df['price'] += (df['bedrooms'] * 1_500_000)
df['price'] += (df['bathrooms'] * 2_000_000)
df['price'] += np.where(df['airconditioning'] == 'yes', 1_200_000, 0)
df['price'] += np.where(df['prefarea'] == 'yes', 2_500_000, 0)

# Save to CSV
file_name = 'Housing.csv'
df.to_csv(file_name, index=False)

print(f"✅ Successfully generated '{file_name}' with {num_samples} rows!")
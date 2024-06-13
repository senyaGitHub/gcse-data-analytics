import pandas as pd
import matplotlib.pyplot as plt

# Data for girls
data_girls = {
    'Gender': 'Girls',
    '5+ A*-C inc. English & mathematics': 61.6,
    'Remaining': 100 - 61.6,  # Calculate remaining percentage for pie chart
}

# Data for boys
data_boys = {
    'Gender': 'Boys',
    '5+ A*-C inc. English & mathematics': 52.8,
    'Remaining': 100 - 52.8,  # Calculate remaining percentage for pie chart
}

# Create DataFrames for girls and boys
df_girls = pd.DataFrame(data_girls, index=[0])
df_boys = pd.DataFrame(data_boys, index=[0])

# Plotting pie charts
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Pie chart for girls
ax[0].pie(df_girls[['5+ A*-C inc. English & mathematics', 'Remaining']].transpose()[0], 
          labels=['5+ A*-C inc. English & mathematics', 'Remaining'], 
          autopct='%1.1f%%', startangle=140)
ax[0].set_title('Girls')

# Pie chart for boys
ax[1].pie(df_boys[['5+ A*-C inc. English & mathematics', 'Remaining']].transpose()[0], 
          labels=['5+ A*-C inc. English & mathematics', 'Remaining'], 
          autopct='%1.1f%%', startangle=140)
ax[1].set_title('Boys')

plt.tight_layout()
plt.show()

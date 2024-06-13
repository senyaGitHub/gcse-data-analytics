import pandas as pd
import matplotlib.pyplot as plt

# Mocked data based on the information provided in the images
data_gender = {
    'Gender': ['Girls', 'Boys'],
    '5+ A*-C grades': [72.0, 70.5],
    '5+ A*-C grades including English & Mathematics': [61.6, 60.3]
}

# Create a DataFrame
df_gender = pd.DataFrame(data_gender)

# Plotting the bar chart
plt.figure(figsize=(12, 6))

# Bar Chart for 5+ A*-C grades
plt.subplot(1, 2, 1)
plt.bar(df_gender['Gender'], df_gender['5+ A*-C grades'], color=['blue', 'orange'])
plt.xlabel('Gender')
plt.ylabel('Percentage of Pupils Achieving 5+ A*-C Grades')
plt.title('Percentage of Pupils Achieving 5+ A*-C Grades by Gender')

# Bar Chart for 5+ A*-C grades including English & Mathematics
plt.subplot(1, 2, 2)
plt.bar(df_gender['Gender'], df_gender['5+ A*-C grades including English & Mathematics'], color=['blue', 'orange'])
plt.xlabel('Gender')
plt.ylabel('Percentage of Pupils Achieving 5+ A*-C Grades Including English & Mathematics')
plt.title('Percentage of Pupils Achieving 5+ A*-C Grades (Inc. English & Math) by Gender')

plt.tight_layout()
plt.show()

# Plotting the pie chart
plt.figure(figsize=(12, 6))

# Pie Chart for 5+ A*-C grades
plt.subplot(1, 2, 1)
plt.pie(df_gender['5+ A*-C grades'], labels=df_gender['Gender'], autopct='%1.1f%%', colors=['blue', 'orange'])
plt.title('Percentage of Pupils Achieving 5+ A*-C Grades by Gender')

# Pie Chart for 5+ A*-C grades including English & Mathematics
plt.subplot(1, 2, 2)
plt.pie(df_gender['5+ A*-C grades including English & Mathematics'], labels=df_gender['Gender'], autopct='%1.1f%%', colors=['blue', 'orange'])
plt.title('Percentage of Pupils Achieving 5+ A*-C Grades (Inc. English & Math) by Gender')

plt.tight_layout()
plt.show()

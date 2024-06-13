import pandas as pd
import matplotlib.pyplot as plt

# Data for girls
data_girls = {
    'School Type': [
        'All state-funded mainstream schools', 'Local authority maintained mainstream schools',
        'Academies and free schools', 'Sponsored academies', 'Converter academies',
        'Free schools', 'University technical colleges (UTCs)', 'Studio schools',
        'Further education colleges with provision for 14- to 16-year-olds', 'All state-funded special schools',
        'All state-funded schools', 'Hospital schools and alternative provision including academy and free school alternative provision and pupil referral units',
        'All state-funded schools, hospital schools and alternative provision including academy and free school alternative provision and pupil referral units',
        'Non-maintained special schools', 'Independent schools', 'Independent special schools', 'All independent schools', 'All special schools', 'All schools'
    ],
    'Number of schools': [3071, 1227, 1837, 503, 1272, 20, 19, 23, 4, 737, 3808, 421, 4229, 62, 843, 236, 1141, 1035, 5380],
    'Number of pupils at the end of key stage 4': [268456, 106812, 161199, 38534, 121499, 467, 288, 411, 140, 2764, 271220, 3128, 274348, 118, 23571, 427, 24116, 3309, 298464],
    '5+ A*-C grades': [72.0, 70.7, 72.9, 59.3, 77.5, 65.3, 54.5, 26.5, 7.1, 0.3, 71.3, 3.0, 70.5, 5.1, 67.9, 3.7, 66.5, 0.9, 70.2],
    '5+ A*-C inc. English & mathematics': [61.6, 59.7, 62.9, 49.3, 67.4, 51.6, 48.3, 17.8, 4.3, 0.2, 61.0, 1.8, 60.3, 4.2, 31.7, 2.1, 31.1, 0.6, 58.0],
    '1+ A*-C grades': [93.8, 93.4, 94.1, 90.7, 95.3, 92.1, 87.5, 72.0, 48.6, 5.5, 92.9, 26.2, 92.2, 18.6, 96.7, 23.7, 95.0, 8.3, 92.7],
    'Any passes': [99.3, 99.3, 99.3, 98.7, 99.5, 98.5, 99.0, 96.1, 73.6, 26.7, 98.6, 62.7, 98.2, 41.5, 98.2, 67.0, 97.4, 32.4, 98.6]
}

# Data for boys
data_boys = {
    'School Type': [
        'All state-funded mainstream schools', 'Local authority maintained mainstream schools',
        'Academies and free schools', 'Sponsored academies', 'Converter academies',
        'Free schools', 'University technical colleges (UTCs)', 'Studio schools',
        'Further education colleges with provision for 14- to 16-year-olds', 'All state-funded special schools',
        'All state-funded schools', 'Hospital schools and alternative provision including academy and free school alternative provision and pupil referral units',
        'All state-funded schools, hospital schools and alternative provision including academy and free school alternative provision and pupil referral units',
        'Non-maintained special schools', 'Independent schools', 'Independent special schools', 'All independent schools', 'All special schools', 'All schools'
    ],
    'Number of schools': [3071, 1227, 1837, 503, 1272, 20, 19, 23, 4, 737, 3808, 421, 4229, 62, 843, 236, 1141, 1035, 5380],
    'Number of pupils at the end of key stage 4': [275227, 109370, 165492, 40973, 122362, 655, 1044, 458, 124, 7393, 282620, 5892, 288512, 354, 23651, 1367, 25372, 9114, 313884],
    '5+ A*-C grades': [61.8, 60.0, 63.0, 48.3, 68.2, 60.3, 41.4, 22.9, 5.6, 0.5, 60.2, 1.0, 59.0, 4.5, 57.0, 5.2, 53.5, 1.4, 58.5],
    '5+ A*-C inc. English & mathematics': [52.8, 50.6, 54.2, 40.4, 59.2, 49.8, 33.0, 17.5, 4.8, 0.4, 51.4, 0.7, 50.3, 2.8, 21.6, 2.0, 20.3, 0.7, 47.9],
    '1+ A*-C grades': [89.9, 89.1, 90.5, 86.1, 92.2, 90.1, 83.6, 63.1, 37.9, 9.2, 87.8, 16.9, 86.4, 29.4, 95.5, 27.7, 91.0, 12.7, 87.0],
    'Any passes': [99.1, 99.1, 99.1, 98.4, 99.4, 99.1, 98.7, 94.3, 75.8, 40.5, 97.6, 55.5, 96.7, 51.7, 97.8, 63.9, 95.3, 44.4, 97.1]
}

# Create DataFrames for girls and boys
df_girls = pd.DataFrame(data_girls)
df_boys = pd.DataFrame(data_boys)

# Set 'School Type' as the index for both DataFrames
df_girls.set_index('School Type', inplace=True)
df_boys.set_index('School Type', inplace=True)


fig, ax = plt.subplots(figsize=(10, 6))
index = df_girls.index
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, df_girls['5+ A*-C inc. English & mathematics'], bar_width, alpha=opacity, color='b', label='Girls')
rects2 = plt.bar(index, df_boys['5+ A*-C inc. English & mathematics'], bar_width, alpha=opacity, color='g', label='Boys', bottom=df_girls['5+ A*-C inc. English & mathematics'])

plt.xlabel('School Type')
plt.ylabel('Percentage')
plt.title('5+ A*-C grades including English & Mathematics by School Type and Gender')
plt.xticks(rotation=90)
plt.legend()

plt.tight_layout()
plt.show()

# Pie Chart for 5+ A*-C grades including English & Mathematics
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].pie(df_girls['5+ A*-C inc. English & mathematics'], labels=df_girls.index, autopct='%1.1f%%', startangle=140)
ax[0].set_title('Girls')

ax[1].pie(df_boys['5+ A*-C inc. English & mathematics'], labels=df_boys.index, autopct='%1.1f%%', startangle=140)
ax[1].set_title('Boys')

plt.tight_layout()
plt.show()

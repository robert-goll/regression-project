import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Country': ['Antigua and Barbuda', 'Argentina', 'Australia', 'Bahrain', 'Belgium', 'Russia', 'Bosnia and Harzegovina', 'Brazil', 'Brunei', 'Maldives', 'New Zealand', 'Comoros', 'Cuba', 'Ivory Coast', 'Dijbouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'South Korea', 'Eritrea', 'Estonia', 'Fiji', 'Georgia', 'Germany', 'Greece', 'Grenada', 'Guatemala', 'Sri Lanka', 'Hungary', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Jordan', 'Kazakhstan', 'United Kingdom', 'Kuwait', 'Laos', 'Lebanon', 'China', 'Luxembourg', 'Sweden', 'Malta', 'Canda', 'Moldova', 'Monaco', 'Montenegro', 'Turkey', 'El Salvador', 'Armenia', 'Nigeria', 'North Macedonia', 'Norway', 'Denmark', 'Bermuda', 'Peru', 'Bulgaria', 'Portugal', 'Qatar', 'Saint Lucia', 'Peru', 'Ukraine', 'Saudi Arabia', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'Algeria', 'Suriname', 'Sweden', 'Taiwan', 'Japan', 'Thailand', 'Seychelles', 'Syria', 'Jamaica', 'Colombia', 'United Arab Emirates', 'United States', 'Uruguay', 'Vietnam', 'Cyprus', 'Poland', 'Zimbabwe', 'Netherlands'],  # Replace with your actual names/identifiers
    'Mean Monthly Salary': [1700, 870, 3540, 2300, 3800, 783, 1060, 580, 2500, 1237, 3760, 670, 50, 560, 1550, 580, 350, 530, 300, 3420, 460, 2920, 2140, 2490, 4220, 2520, 2310, 1360, 273, 1560, 110, 780, 3920, 3230, 2660, 2230, 660, 7365, 4600, 220, 150, 1220, 3350, 2862, 5130, 3497, 1490, 4660, 3050, 276, 1751, 669, 400, 820, 4770, 6203, 1523, 510, 1050, 1090, 4330, 1060, 505, 477, 4440, 775, 6440, 2300, 2040, 1335, 140, 2860, 1680, 2993, 420, 1481, 12, 624, 1166, 5300, 4640, 880, 290, 2388, 1672, 670, 5333],  # Replace with your actual data
    'Divorce Rate': [3.4, 5.7, 1.9, 1.3, 3.7, 3.9, 0.8, 1.4, 1.4, 5.52, 1.7, 1.1, 2.9, 3.4, 1.7, 1, 1.2, 1.1, 2.3, 2.1, 1.3, 1.9, 0.66, 2.1, 1.7, 1.8, 1.1, 0.2, 0.15, 1.5, 0.01, 1.6, 0.7, 1.8, 1.4, 1.6, 4.6, 1.7, 1.3, 3.4, 1.6, 3.2, 2.3, 2.5, 0.7, 2.1, 3.3, 1.7, 1.3, 1.6, 0.8, 1.1, 2.9, 0.8, 1.9, 2.7, 1.9, 0.5, 1.3, 2.0, 0.7, 0.7, 0.5, 2.88, 2.1, 1.3, 1.7, 1.7, 0.8, 1.6, 1.4, 2.5, 2.3, 1.7, 1.4, 1.7, 1.3, 1.2, 0.7, 0.7, 2.7, 0.9, 0.2, 2.6, 1.7, 0.07, 1.7]
}

print(len(data['Country']))
print(len(data['Mean Monthly Salary']))
print(len(data['Divorce Rate']))

df = pd.DataFrame(data)

slope, intercept = np.polyfit(df['Mean Monthly Salary'], df['Divorce Rate'], 1)

df['Predicted Divorce Rate'] = slope * df['Mean Monthly Salary'] + intercept

df['Residuals'] = df['Divorce Rate'] - df['Predicted Divorce Rate']

plt.scatter(df['Mean Monthly Salary'], df['Residuals'])

plt.axhline(y=0, color='r', linestyle='-')

plt.title('Residual Plot')
plt.xlabel('Mean Monthly Salary (In USD)')
plt.ylabel('Residuals')

plt.show()
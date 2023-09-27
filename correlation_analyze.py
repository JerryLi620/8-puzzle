
import pandas as pd
from scipy.stats import pearsonr

user_data_path = 'result_table.csv'
user_data = pd.read_csv(user_data_path)

russel_norvig_data_path = 'Russell and Norvig\'s Result.csv'
russel_norvig_data = pd.read_csv(russel_norvig_data_path)

user_data.head(), russel_norvig_data.head()

def compute_pearson_correlation(column1, column2):
    
    valid_indices = column1.notna() & column2.notna()
    column1_valid = column1[valid_indices]
    column2_valid = column2[valid_indices]
    
    
    correlation, _ = pearsonr(column1_valid, column2_valid)
    return correlation


columns_to_compare = [
    'A*(h1).b*', 'A*(h2).b*', 'IDS.b*', 
    'A*(h1).total nodes', 'A*(h2).total nodes', 'IDS.total nodes'
]


correlations = {}
for column in columns_to_compare:
    correlations[column] = compute_pearson_correlation(user_data[column], russel_norvig_data[column])

print(correlations)

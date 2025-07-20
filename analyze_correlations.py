#!/usr/bin/env python3
"""
Retail Sales Correlation Analysis
Computes Pearson correlation coefficients for RetailPro data
"""

import pandas as pd
import re
import json
from scipy.stats import pearsonr

def extract_data_from_sql(sql_file_path):
    """Extract INSERT statements from SQL file and convert to DataFrame"""
    data = []
    
    with open(sql_file_path, 'r') as f:
        content = f.read()
    
    # Find all INSERT statements
    insert_pattern = r"INSERT INTO retail_data VALUES \('([^']+)', (\d+), (\d+), (\d+), (\d+), (\d+)\);"
    matches = re.findall(insert_pattern, content)
    
    for match in matches:
        store_id, footfall, promo_spend, avg_basket, returns, net_sales = match
        data.append({
            'Store_ID': store_id,
            'Footfall': int(footfall),
            'Promo_Spend': int(promo_spend),
            'Avg_Basket': int(avg_basket),
            'Returns': int(returns),
            'Net_Sales': int(net_sales)
        })
    
    return pd.DataFrame(data)

def calculate_correlations(df):
    """Calculate Pearson correlations for the specified pairs"""
    correlations = {}
    
    # Avg_Basket – Net_Sales
    corr_basket_sales, p_val1 = pearsonr(df['Avg_Basket'], df['Net_Sales'])
    correlations['Avg_Basket-Net_Sales'] = corr_basket_sales
    
    # Avg_Basket – Returns
    corr_basket_returns, p_val2 = pearsonr(df['Avg_Basket'], df['Returns'])
    correlations['Avg_Basket-Returns'] = corr_basket_returns
    
    # Net_Sales – Returns
    corr_sales_returns, p_val3 = pearsonr(df['Net_Sales'], df['Returns'])
    correlations['Net_Sales-Returns'] = corr_sales_returns
    
    return correlations

def find_strongest_correlation(correlations):
    """Find the correlation with the highest absolute value"""
    strongest_pair = max(correlations.items(), key=lambda x: abs(x[1]))
    return strongest_pair[0], strongest_pair[1]

def main():
    # Load and analyze data
    print("Loading retail data...")
    df = extract_data_from_sql('q-sql-correlation-github-pages.sql')
    print(f"Loaded {len(df)} records")
    
    # Calculate correlations
    print("\nCalculating Pearson correlations...")
    correlations = calculate_correlations(df)
    
    # Display all correlations
    print("\nCorrelation Results:")
    for pair, corr in correlations.items():
        print(f"{pair}: {corr:.6f}")
    
    # Find strongest correlation
    strongest_pair, strongest_corr = find_strongest_correlation(correlations)
    print(f"\nStrongest correlation (by absolute value):")
    print(f"Pair: {strongest_pair}")
    print(f"Correlation: {strongest_corr:.6f}")
    
    # Create result JSON
    result = {
        "pair": strongest_pair,
        "correlation": round(strongest_corr, 6)
    }
    
    # Save to JSON file
    with open('correlation_result.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\nResult saved to correlation_result.json")
    return result

if __name__ == "__main__":
    main() 
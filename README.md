# RetailPro Correlation Analysis

This repository contains a correlation analysis of retail store performance metrics for RetailPro, a retail chain analyzing store performance drivers.

## Analysis Overview

The analysis computes Pearson correlation coefficients for three key retail metric pairs:

1. **Avg_Basket – Net_Sales**: Relationship between average basket size and net sales
2. **Avg_Basket – Returns**: Relationship between average basket size and returns  
3. **Net_Sales – Returns**: Relationship between net sales and returns

## Results

The strongest correlation (by absolute value) was found to be:
- **Pair**: Avg_Basket-Net_Sales
- **Correlation**: 0.665691

This indicates a moderately strong positive correlation between average basket size and net sales, suggesting that higher basket values correlate with higher net sales.

## Files

- `q-sql-correlation-github-pages.sql` - Original retail sales data
- `analyze_correlations.py` - Python script for correlation analysis
- `correlation_result.json` - Final JSON result in required format
- `index.html` - GitHub Pages display of results

## Data Source

The analysis uses retail data with 127 records containing:
- Store_ID: Store identifier
- Footfall: Customer traffic
- Promo_Spend: Promotional spending
- Avg_Basket: Average basket value
- Returns: Number of returns
- Net_Sales: Net sales amount

## Usage

View the published results at: [GitHub Pages URL will be available after deployment]

Or download the raw JSON data: [correlation_result.json](correlation_result.json)

## Technical Details

- Analysis performed using Python with pandas and scipy
- Pearson correlation coefficient calculation
- Results published as open data on GitHub Pages 
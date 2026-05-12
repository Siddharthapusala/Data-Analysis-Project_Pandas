# Sales Data Analysis Project

This project provides a comprehensive analysis of sales data using Python, Pandas, and Matplotlib. It includes data cleaning, statistical analysis, and visualization to identify key business insights.

## Project Structure

- **sales_data.csv**: The raw input dataset containing transaction records (Date, Region, Product, Units Sold, Unit Price).
- **sales_data_analysis.ipynb**: A Jupyter Notebook containing the 3-cell analysis pipeline:
    - **Cell 1**: Data Loading & Preview.
    - **Cell 2**: Data Cleaning (removing nulls/duplicates) and Revenue Analysis.
    - **Cell 3**: Data Visualization and Exporting results.
- **cleaned_sales_data.csv**: The processed and cleaned dataset exported after analysis.
- **revenue_by_region_chart.png**: A bar chart visualization showing total revenue distribution across different regions.

## Key Insights

Based on the analysis of the provided dataset:
1. **Top Performing Region**: North (₹416,000.00)
2. **Highest Revenue Product**: Laptop (₹400,000.00)
3. **Total Revenue Generated**: ₹615,500.00
4. **Average Revenue per Sale**: ₹61,550.00

## Requirements

To run this project, the following dependencies are required:
- **Python 3.x**
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Jupyter Notebook/VS Code**: To execute the `.ipynb` file.

## Screenshots Captured

The following screenshots have been generated and provided as part of the project documentation:
1. **Notebook Code**: Full view of the 3-cell Jupyter Notebook.
2. **Dataset Preview**: Display of the first 5 rows of the sales data.
3. **Summary Statistics**: Statistical summary of Units Sold, Unit Price, and Revenue.
4. **Grouped Analysis**: Revenue totals categorized by Region and Product.
5. **Meaningful Insights**: Key findings extracted from the data analysis.
6. **Bar Chart**: Visual representation of Revenue by Region.

## How to Run

1. Ensure you have Python installed along with `pandas` and `matplotlib`.
2. Open the `sales_data_analysis.ipynb` file in a Jupyter environment (VS Code, JupyterLab, or Jupyter Notebook).
3. Run the cells in order to perform the analysis and generate the output files.


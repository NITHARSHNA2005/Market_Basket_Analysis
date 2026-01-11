# Market Basket Analysis Flask Application

This Flask web application provides an interactive interface for market basket analysis using the BigBasket dataset. It implements both Apriori and FP-Growth algorithms to discover association rules and product recommendations.

## Features

- **Interactive Web Interface**: Clean, responsive web interface built with Bootstrap
- **Dual Algorithm Support**: Compare results from both Apriori and FP-Growth algorithms
- **Real-time Visualizations**: Dynamic plots showing support vs confidence and top frequent itemsets
- **Product Recommendations**: Get product recommendations based on association rules
- **Algorithm Statistics**: Compare performance metrics between algorithms

## Installation

1. Install the required dependencies:

pip install -r requirements.txt


2. Make sure your BigBasket Data.csv file is in the correct path:
   - Update the file path in `app.py` line 18 if needed
   
## Running the Application

1. Run the Flask application:

python app.py


2. Open your web browser and navigate to:

## How to Use

1. **Load Data**: Click the "Load Data" button to process the BigBasket dataset
2. **View Statistics**: See algorithm comparison statistics
3. **Explore Visualizations**: Switch between different plot types and algorithms
4. **Browse Association Rules**: View the top association rules for each algorithm
5. **Get Recommendations**: Enter a product name to get related product recommendations

## File Structure

ML COMPLETE PROJECT/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface template
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── BigBasket Data.csv   # Dataset (update path as needed)




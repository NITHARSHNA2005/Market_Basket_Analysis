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


## API Endpoints

- `GET /` - Main web interface
- `GET /load_data` - Load and process the dataset
- `GET /get_rules/<algorithm>` - Get association rules for specified algorithm
- `GET /get_plot/<plot_type>/<algorithm>` - Generate visualization plots
- `GET /get_recommendations` - Get product recommendations
- `GET /get_stats` - Get algorithm statistics

## Dataset Requirements

The application expects a CSV file with the following columns:
- `Invoice No.` - Transaction identifier
- `Category` - Product category

## Troubleshooting

1. **File Path Error**: Update the CSV file path in `app.py` line 18
2. **Port Already in Use**: Change the port in `app.py` line 174
3. **Missing Dependencies**: Run `pip install -r requirements.txt`

## Notes

- The application uses a minimum support threshold of 0.01 for both algorithms
- Only rules with lift > 1 are considered significant
- The web interface is optimized for desktop browsers
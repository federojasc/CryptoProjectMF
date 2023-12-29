# Crypto Project

## Overview

This tool is designed to analyze cryptocurrency data, focusing especially on currency pairs and their technical indicators. It uses the Kraken API to fetch real-time data and offers interactive charts to visualize data and calculate technical indicators such as the Stochastic Oscillator and Moving Averages.

## Installation

### Requirements

- Python 3.x
- Required Python libraries as listed in `requirements.txt`

### Setup

1. **Clone the Repository (Assuming Git is installed)**

    ```bash
    git clone 'https://github.com/federojasc/CryptoProjectMF.git'
    cd 'user_path'
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Dash Application**

    ```bash
    python application.py
    ```

2. **Access the Web Interface**

    Open a web browser and navigate to `http://127.0.0.1:8050/` (or the address indicated in the terminal).

## Features

- **Data Retrieval**: Fetch real-time cryptocurrency data from Kraken.
- **Interactive Charts**: Visualize currency pairs and their movements over time.
- **Technical Indicators**: Calculate and display indicators such as the Stochastic Oscillator and Moving Averages.
- **User Input**: Customize data display through various input options.

## File Structure

- `main.py`: Main configuration of the Dash application and server.
- `Kraken_data.py`: Handles fetching data from the Kraken API.
- `Graph.py`: Functions to generate interactive charts.
- `TechnicalIndicators.py`: Calculation of technical indicators.
- `requirements.txt`: List of Python dependencies.

## Usage Notes

- Ensure you have a stable internet connection for data retrieval.
- The tool is designed for educational purposes and not for live trading operations.

## Contributing

Feel free to fork the project and submit pull requests for any improvements.

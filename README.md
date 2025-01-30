# Sports Dashboard: NFL Passing Stats


An interactive Streamlit dashboard to visualize and analyze NFL quarterback passing stats, powered by data scraped from ESPN. This project allows users to filter player and team stats, visualize key performance metrics, and gain insights into NFL quarterbacks' performance across the 2024 season.

The data used in this project is scraped from ESPN's website using Selenium and Python. The scraping script collects the latest passing statistics, which are then processed and visualized in the dashboard.


<img width="1056" alt="Screenshot 2025-01-30 at 1 37 54 PM" src="https://github.com/user-attachments/assets/da7ee0cf-e9a9-4367-ba08-041a71a3217f" />


## Features

- **NFL Passing Stats Visualization**: Displays detailed passing statistics of NFL quarterbacks, including Yards, Touchdowns, Interceptions, Completion Percentage, and more.
- **Interactive Filters**: Allows filtering by player name and team to focus on specific data.
- **Visualizations**: Various charts (bar charts, scatter plots, etc.) for a deeper analysis of quarterback performance:
  - Total Passing Yards by Player
  - Completion Percentage vs. Yards
  - Touchdowns vs. Interceptions
  - And more...

<img width="742" alt="Screenshot 2025-01-30 at 1 40 40 PM" src="https://github.com/user-attachments/assets/20171b59-a9e8-4eb9-9188-7b1d87e8bd8c" />

<img width="731" alt="Screenshot 2025-01-30 at 1 41 58 PM" src="https://github.com/user-attachments/assets/d17d2b77-3043-440b-970c-a6db4fe45597" />


## Project Structure

Sports_Dashboard/ <br>
  - nfl_qb_webscrape.py 
    -  Python script for scraping ESPN stats <br>
  - nfl_passing_stats.csv 
    -  CSV file containing the scraped passing stats <br>
  - qb_dashboard.py 
    -  Streamlit dashboard for visualizing stats <br>
  - requirements.txt 
    - Python dependencies for the project <br>
  
 README.md


## Web Scraping

The project includes a web scraping script (`nfl_qb_webscrape.py`) that collects the passing statistics of NFL quarterbacks from ESPN. This script uses the **Selenium** package to interact with the ESPN website, extracting relevant data such as player name, team, yards, touchdowns, interceptions, and more. The scraped data is then stored in a CSV file (`nfl_passing_stats.csv`), which is used to populate the dashboard.

To run the scraping script:

1. Ensure you have **Selenium** and the required dependencies installed (listed in `requirements.txt`).
2. Run the following command to scrape the data:

  ```bash
  python nfl_qb_webscrape.py
  ```
   

## Running the Dashboard

After you have successfully scraped the data, you can run the Streamlit dashboard to visualize the stats.

To run the dashboard:

1. Ensure the required dependencies are installed.
2. Run the Streamlit dashboard: To start the Streamlit app, use the following command:

  ```bash
  streamlit run qb_dashboard.py
  ```

This will launch the dashboard, and you can view it in your web browser. You’ll be able to filter the data by player or team and explore various visualizations such as passing yards, touchdowns, completion percentage, and more.


**Note**: To get the latest data, simply re-run the scraping script using the URL `https://www.espn.com/nfl/stats/player` (or any other valid URL) to scrape updated NFL passing statistics. Just modify the `url` variable in the `nfl_qb_webscrape.py` script to the desired ESPN page URL.


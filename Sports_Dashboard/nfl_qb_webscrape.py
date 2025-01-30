import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_espn_stats(url):
    # Set up the WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no UI)

    # Use webdriver-manager to handle chromedriver installation
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get(url)

    # Wait for the page to load (dynamic content might take time)
    time.sleep(5)  # You can also use WebDriverWait for better dynamic loading handling
    
    try:
        # Extract basic player information (Rank, Name, Team)
        player_table = driver.find_element(By.CLASS_NAME, "Table")

        # Extract headers (Rank, Player, Team)
        player_headers = [th.text.strip() for th in player_table.find_elements(By.TAG_NAME, "th")]
        print("Player Table Headers:", player_headers)  # Debugging line

        # Extract rows with player data
        player_rows = []
        for row in player_table.find_elements(By.TAG_NAME, "tr")[1:]:  # Skip header row
            cells = row.find_elements(By.TAG_NAME, "td")
            player_data = [cell.text.strip() for cell in cells]
            
            if player_data:  # Only add rows that are not empty
                player_rows.append(player_data)

        # Create the player DataFrame
        player_df = pd.DataFrame(player_rows, columns=player_headers)
        print("Sample Player DataFrame before splitting 'NAME':")
        print(player_df.head())

        # Split the NAME column into 'NAME' and 'Team'
        player_df[['NAME', 'Team']] = player_df['NAME'].str.split('\n', expand=True)
        print("Player DataFrame after splitting 'NAME':")
        print(player_df[['NAME', 'Team']].head())

        # Extract the detailed stats table (second table)
        stat_table = driver.find_elements(By.CLASS_NAME, "Table")[1]  # Second table for stats

        # Extract stats headers (e.g., Passing Yards, TDs, etc.)
        stat_headers = [th.text.strip() for th in stat_table.find_elements(By.TAG_NAME, "th")]
        print("Stat Table Headers:", stat_headers)  # Debugging line

        # Extract rows with stats data
        stat_rows = []
        for row in stat_table.find_elements(By.TAG_NAME, "tr")[1:]:  # Skip header row
            cells = row.find_elements(By.TAG_NAME, "td")
            stat_data = [cell.text.strip() for cell in cells]
            
            if stat_data:  # Only add rows that are not empty
                stat_rows.append(stat_data)

        # Create the stats DataFrame
        stats_df = pd.DataFrame(stat_rows, columns=stat_headers)
        print("Sample Stat DataFrame:")
        print(stats_df.head())

        # Merge the player DataFrame with the stats DataFrame
        # Include the "NAME" and "Team" columns from player_df
        merged_df = pd.concat([player_df[['RK', 'NAME', 'Team']], stats_df], axis=1)
        print("Merged DataFrame:")
        print(merged_df.head())
        
        driver.quit()
        return merged_df

    except Exception as e:
        driver.quit()
        print(f"An error occurred: {e}")
        return None


# URL for passing stats
passing_url = "https://www.espn.com/nfl/stats/player/_/season/2024/seasontype/2"

# Scrape passing stats and save to CSV
print("Scraping Passing stats...")
passing_df = scrape_espn_stats(passing_url)
if passing_df is not None:
    passing_df.to_csv("nfl_passing_stats.csv", index=False)
    print("Passing stats saved to nfl_passing_stats.csv")
else:
    print("Failed to scrape Passing stats.")


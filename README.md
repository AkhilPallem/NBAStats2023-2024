# NBAStats2023-2024

* This script utilizes Python's requests and pandas libraries for scraping NBA statistics from the NBA website.
* It begins by importing necessary modules and setting display options for pandas.
* Then, it defines a URL (testURL) to access NBA statistics data and makes a GET request to retrieve JSON-formatted data.
* After extracting headers and row data from the response, it constructs a DataFrame to organize the retrieved information.
* The script also specifies HTTP headers required for accessing the NBA API.
* It then enters a loop to fetch data for specified years and season types, concatenating the retrieved data into the DataFrame.
* To prevent overloading the server, it introduces a random delay between requests.
* Finally, the script prints the resulting DataFrame, which contains the compiled NBA statistics.
* This script provides a structured approach for extracting and analyzing NBA statistics, particularly focusing on points per game (PTS) during playoff seasons for specified years.



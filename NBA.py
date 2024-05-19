import pandas as pd
import requests 
pd.set_option("display.max_columns", None)
import time 
import numpy as np
testURL = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Playoffs&StatCategory=PTS"
r = requests.get(url = testURL ).json()
tableHeader = r["resultSet"]["headers"]
pd.DataFrame(r["resultSet"]["rowSet"], columns = tableHeader)

dfCOLS = ["Year", "Season Type"] + tableHeader
pd.DataFrame(columns = dfCOLS)
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "stats.nba.com",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
df = pd.DataFrame(columns = dfCOLS)
seasonType = ["Playoffs"]
years = ["2023-24"]
begin = time.time()

for y in years:
    for s in seasonType:
        apiURL = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Playoffs&StatCategory=PTS"
        r = requests.get(url= apiURL, headers = headers).json()
        tempDF1 = pd.DataFrame(r["resultSet"]["rowSet"], columns = tableHeader)
        tempDF2 = pd.DataFrame({"Year" : ["2023-24" for i in range(len(tempDF1))], "Season Type" : ["Playoffs" for i in range(len(tempDF1))]})
        tempDF3 = pd.concat([tempDF2, tempDF1], axis = 1)
        df = pd.concat([df, tempDF3], axis = 0)
        print(f"Finished scaping data!")
        lag = np.random.uniform(low = 5, high = 40)

print(df)

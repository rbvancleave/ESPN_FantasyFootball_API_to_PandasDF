# ESPN_FantasyFootball_API_to_PandasDF
Create Pandas DataFrames for ESPN's FantasyFootball.


Tables Include:
- head to head weekly matchups DateFrame
- team seasonal totals DataFrame
- seasonal transactions DataFrame
- total points from each football stat DataFrame

## Start with "Starter Notebook with Examples" Python Notebook
![Find League ID](https://github.com/rbvancleave/ESPN_FantasyFootball_API_to_PandasDF/blob/master/images/Starter_notebook.PNG?raw=true)

How to grab League ID:

![Find League ID](https://github.com/rbvancleave/ESPN_FantasyFootball_API_to_PandasDF/blob/master/images/leagueid_from_url.png?raw=true)

How to grab swid and espn_s2:
### 1:
![Find League ID](https://github.com/rbvancleave/ESPN_FantasyFootball_API_to_PandasDF/blob/master/images/swid%2Bespn_s2_1.png?raw=true)
### 2:
![Find League ID](https://github.com/rbvancleave/ESPN_FantasyFootball_API_to_PandasDF/blob/master/images/swid%2Bespn_s2_2.png?raw=true)
### 3:
![Find League ID](https://github.com/rbvancleave/ESPN_FantasyFootball_API_to_PandasDF/blob/master/images/swid%2Bespn_s2_3.png?raw=true)

## Built With

[matplotlib](https://github.com/matplotlib/matplotlib) - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

[numpy](https://github.com/numpy/numpy) - NumPy is the fundamental package needed for scientific computing with Python.

[pandas](https://github.com/pandas-dev/pandas) - Powerful Python data analysis toolkit.

[requests](https://github.com/psf/requests) - Requests is a simple, yet elegant, HTTP library.

[seaborn](https://github.com/seaborn/seaborn) - Seaborn is a Python visualization library based on matplotlib.

| Script           | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| ESPN_FFL_API.py            | Runs request to ESPN API and builds DataFrame's.                                           |
| Starter Notebook with Examples.ipynb       |  4 DataFrames are saved as well as original response_json.                                              |
| config.py            | Asks for LeagueID, SWID, and espn_s2. Can be uncomented to hardcode variables                                    |


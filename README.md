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
| Starter Notebook with Examples.ipynb       | Asks for LeagueID, SWID, and espn_s2. Enter specific league year or all years. 4 DataFrames are saved as well as original repsponse_json                                              |
| clean            | Runs all clean scripts.                                      |
| clean:dist       | Removes the dist folder.                                     |
| clean:docs       | Removes the docs folder.                                     |
| ci               | Runs continuous integration tasks. Currently runs lint, unit and integration tests, and build. |
| lint             | Ensures code style is correct.                               |
| serve:docs       | Builds and serves docs. Defaults to port 8080.               |
| test             | Starts a jest test runner with access to all tests. Pass `--watch` to keep jest alive and watching for changes. Pass a string as a file inclusion pattern. |
| test:all         | Runs the unit tests then the integration tests.              |
| test:integration | Runs the integration tests.                                  |
| test:unit        | Runs the unit tests.                                         |

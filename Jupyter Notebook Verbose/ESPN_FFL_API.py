#!/usr/bin/env python
# coding: utf-8

import re
import requests
import json
import pandas as pd
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')

from config import leagueID, swid, espn_s2

# Set Up Parameters
def Get_ESPN_data(year=2021,leagueID=leagueID,swid=swid,espn_s2=espn_s2):
    base = "http://fantasy.espn.com/apis/v3/games/ffl/seasons/"
    year = str(year)
    mid = "/segments/0/leagues/"
    leagueID = leagueID
    tail = "?view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mTeam&view=modular&view=mNav&view=mMatchupScore"
    url = (base+year+mid+leagueID+tail)

    r = requests.get(url,
                 cookies={"SWID": swid,
                          "espn_s2": espn_s2})
    return r.json()

def Get_OwnerID(num):
    return response_json['teams'][num-1]['owners'][0]

def Get_OwnerName(num):
    owner_id = Get_OwnerID(num)
    for member in response_json['members']:
        if member['id'] == owner_id:
            return member['firstName']+" "+member['lastName']

def Get_TeamName(num):
    return response_json['teams'][num-1]['location'] + " " + response_json['teams'][num-1]['nickname']
        

def Build_scoreboard(response_json):
    score_board = {}

    for i in response_json['schedule']:

        try:
            week_num = i['matchupPeriodId']
            game_id = i['id']

            if i['away']['pointsByScoringPeriod'][str(week_num)] > i['home']['pointsByScoringPeriod'][str(week_num)]:
                winning_location = 'away'
                losing_location = 'home'
            else:
                winning_location = 'home'
                losing_location = 'away'

            winning_team = Get_TeamName(i[winning_location]['teamId'])
            winning_team_points = i[winning_location]['pointsByScoringPeriod'][str(week_num)]
            losing_team = Get_TeamName(i[losing_location]['teamId'])
            losing_team_points = i[losing_location]['pointsByScoringPeriod'][str(week_num)]

            score_board[game_id] = {'week_num':week_num,'winning_team':winning_team,'winning_team_points':winning_team_points,
                                   'losing_team':losing_team,'losing_team_points':losing_team_points}
        except:
            break
    return pd.DataFrame(score_board).T


def Build_teams_table(response_json,sortby='ranking',asc=True):
    team_totals = {}

    for team in response_json['teams']:
        team_name = team['location'] + " " + team['nickname']
        team_manager = Get_OwnerName(team['id'])
        draft_day_proj_rank = team['draftDayProjectedRank']
        current_proj_rank = team['currentProjectedRank']
        change_in_proj_rank = draft_day_proj_rank - current_proj_rank
        ranking = team['playoffSeed']
        points_for = team['record']['overall']['pointsFor']
        points_against = team['record']['overall']['pointsAgainst']
        games_back = team['record']['overall']['gamesBack']
        losses = team['record']['overall']['losses']
        wins = team['record']['overall']['wins']
        streak_length = team['record']['overall']['streakLength']
        streak_type = team['record']['overall']['streakType']
        waiver_rank = team['waiverRank']

        team_totals[team['id']] = {'team_name':team_name,'team_manager':team_manager,
                                   'draft_day_proj_rank':draft_day_proj_rank,
                                  'current_proj_rank':current_proj_rank,'change_in_proj_rank':change_in_proj_rank,
                                 'ranking':ranking,'points_for':points_for,'points_against':points_against,
                                 'games_back':games_back,'losses':losses,'wins':wins,'streak_length':streak_length,
                                 'streak_type':streak_type,'waiver_rank':waiver_rank}
    df = pd.DataFrame(team_totals).T
    
    return df.sort_values(sortby,ascending=asc)


def Build_transactions_table(response_json):
    transaction_table = {}
    team_names = []
    team_managers = []
    budget_remaining = []
    for team in response_json['teams']:
        transaction_table[team['id']] = team['transactionCounter']
        team_names.append(team['location'] + " " + team['nickname'])
        team_managers.append(Get_OwnerName(team['id']))
        budget_remaining.append(100 - team['transactionCounter']['acquisitionBudgetSpent'])
    df = pd.DataFrame(transaction_table).T
    df['team_name'] = team_names
    df['team_manager'] = team_managers
    df['budget_remaining'] = budget_remaining
    return df[['team_name', 'team_manager','acquisitionBudgetSpent', 'budget_remaining','acquisitions', 'drops','misc', 'moveToActive', 'trades']]


def Build_points_by_stats(response_json):
    pts_by_stat = {}
    team_names = []
    team_managers = []
    
    for team in response_json['teams']:
        pts_by_stat[team['id']] = team['valuesByStat']
        team_names.append(team['location'] + " " + team['nickname'])
        team_managers.append(Get_OwnerName(team['id']))
        
    df = pd.DataFrame(pts_by_stat).T
    df['team_name'] = team_names
    df['team_manager'] = team_managers
    
    
    
    df = df[['team_name','team_manager', '3', '4', '18',
       '19', '20', '24', '25', '26', '35', '37', '38', '42', '43', '44', '46',
       '53', '56', '57', '63',  '72',  '77', '80', '85', '86',
       '88', '89', '90', '91', '92', '93', '95', '96', '97', '98', '99', '101',
       '102', '103', '104', '106', '123', '124', '125','128', '129', '130','132', '133', '134', '135', '136','198','201']]
    
    df.rename(columns={'3':'Passing-Yds','4':'Passing-TD','18':'Passing-400+ Yds','19':'Passing-2pt conversion**',
                       '20':'Passing-INT','24':'Rushing-Yds','25':'Rushing-TD',
                      '26':'Rushing-2ptConversion','37':'Rushing-100_190 Yds',
                       '35':'Rushing-40+yardTD','38':'Rushing-200+ Yds','57':'Receiving-200+Yds','42':'Receiving-Yds',
                       '43':'Receiving-TD', '44':'Receiving-2pt conversion','46':'Receiving-50+yard TD', 
                       '53':'Receiving-REC',
                      '56':'Receiving-100_190 Yds','86':'K-PAT','95':'DF/ST-INT','88':'K-PAT Missed',
                       '89':'D/ST-0 Pts Allowed','90':'D/ST-1_6 Pts Allowed','91':'D/ST-7_13 Pts Allowed',
                       '92':'D/ST-14_17 Pts Allowed','93':'D/ST-Blocked Punt,PAT,FG Return for TD',
                       '96':'D/ST-Fumble Recovery','97':'D/ST-Blocked Punt,PAT,FG','99':'DF/ST-Sack',
                       '103':'D/ST-INT Return TD','106':'D/ST-Fumble Forced',
                      '129':'D/ST-100_199 Yds Allowed','130':'D/ST-200_299 Yds Allowed','132':'D/ST-350_399 Yds Allowed',
                      '133':'D/ST-400_449 Yds Allowed','134':'D/ST-450_499 Yds Allowed','135':'D/ST-500_549 Yds Allowed',
                      '18':'Passing-400+ Yds'},inplace=True)
    return df

all_data = input('Would you like 2018 - 2021 data? (y/n): ').lower()
if all_data == 'n':
    year = int(input('What year would you like? :'))
    response_json = Get_ESPN_data(year=year)

    scoreboard_df = Build_scoreboard(response_json)
    teams_df = Build_teams_table(response_json)
    transactions_df = Build_transactions_table(response_json)

    if year > 2019:
        points_by_stats_df = Build_points_by_stats(response_json)
        print('Done!')
        print('-----------------------')
        print('Dataframes include: scoreboard_df, teams_df, transactions_df, points_by_stats_df')
        print("You will need to manually import points_by_stats DataFrame by running: 'from ESPN_FFL_API import points_by_stats_df'")
    else:
        print('Done!')
        print('-----------------------')
        print('Dataframes include: scoreboard_df, teams_df, transactions_df')
else:
    print('points_by_stats_df is not available for this option... fyi')
    print('Done!')
    print('-----------------------')
    print('Dataframes include: scoreboard_df, teams_df, transactions_df')
    response_json = Get_ESPN_data(2018)

    scoreboard_df = Build_scoreboard(response_json)
    scoreboard_df['Year'] = 2018

    teams_df = Build_teams_table(response_json)
    teams_df['Year'] = 2018

    transactions_df = Build_transactions_table(response_json)
    transactions_df['Year'] = 2018


    for year in range(2019,2022):
        response_json = Get_ESPN_data(year)

        temp_df = Build_scoreboard(response_json)
        temp_df['Year'] = year
        scoreboard_df = scoreboard_df.append(temp_df)

        temp_df = Build_teams_table(response_json)
        temp_df['Year'] = year
        teams_df = teams_df.append(temp_df)

        temp_df = Build_transactions_table(response_json)
        temp_df['Year'] = year
        transactions_df = transactions_df.append(temp_df)


    scoreboard_df.reset_index(inplace = True)  
    teams_df.reset_index(inplace = True)  
    transactions_df.reset_index(inplace = True)

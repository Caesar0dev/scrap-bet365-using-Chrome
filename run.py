import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from datetime import datetime
from datetime import date
import time
import undetected_chromedriver as uc

def execute_code():
    threading.Timer(100.0, execute_code).start()

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # driver = webdriver.Chrome(
    #     options=options, executable_path=r'./chromedriver.exe')
    driver = uc.Chrome()
    driver.get("https://www.va.bet365.com/?_h=s6x46Uz5T6ldi6yBgpD-IA%3D%3D#/AC/B1/C1/D1002/E76169582/G938/")
    time.sleep(60)
    match_dates = []
    match_time = []
    home_team_name = []
    away_team_name = []
    home_team_odds = []
    away_team_odds = []
    scores = []
    home_team_Asian_Handicap_odds = []
    away_team_Asian_Handicap_odds = []
    home_team_Line = []
    away_team_Line = []
    num = [0, 0, 0, 0, 0, 0]
    n = 0
    date_num = 0
    write_data = []

    league_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/div/span').text
    match_round = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/div/span').text

    header = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]')

    all_childrens = header.find_elements(By.XPATH, './div')

    for c in range(0, len(all_childrens)):
        div_class_name = all_childrens[c].get_attribute("class")
        div_childrens = all_childrens[c].find_elements(By.XPATH, './*')
        if (div_class_name.__contains__("rcl-MarketHeaderLabel-isdate")):
            match_dates.append(all_childrens[c].text)
            n = n + 1
        elif (len(div_childrens) != 0) :
            num[n-1] = num[n-1] + 1

    match_times = driver.find_elements(By.CLASS_NAME, 'src-ParticipantFixtureDetailsExtraLineHigher_BookCloses')

    for i in range(0, len(match_times)):
        match_time.append(match_times[i].text)

    team_names = driver.find_elements(By.CLASS_NAME, 'src-ParticipantFixtureDetailsExtraLineHigher_TeamWrapper')

    for i in range(len(team_names)):
        
        if (i % 3 == 0):
            home_team_name.append(team_names[i].text)

        elif (i % 3 ==1):
            away_team_name.append(team_names[i].text)

    scores = driver.find_elements(By.CLASS_NAME, 'src-ParticipantCenteredStacked48ET')

    for j in range(0, len(home_team_name) * 3):
        if (j % 3 == 0):
            home_team_odds.append(scores[j].text)
        elif (j % 3 ==1):
            away_team_odds.append(scores[j].text)

    for k in range(len(home_team_name) * 3, len(home_team_name) * 3 * 2):
        if (k % 3 == 0):
            home_team_Asian_Handicap_odds.append(scores[k].text)
        elif (k % 3 ==1) :
            away_team_Asian_Handicap_odds.append(scores[k].text)

    for l in range(len(home_team_name) * 3 * 2, len(home_team_name) * 3 * 3):
        if (l % 3 == 0):
            home_team_Line.append(scores[l].text)
        elif (l % 3 ==1) :
            away_team_Line.append(scores[l].text)

    today = date.today()
    today_time = datetime.now()
    with open('Bet365_result.csv', 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        for j in range(0, len(num)):
                
            for i in range(0, num[j]):

                write_data.append(str(today))
                write_data.append(str(today_time))
                write_data.append(league_name)
                write_data.append(match_round)
                write_data.append(match_dates[j])
                write_data.append(match_time[date_num + i])
                write_data.append(home_team_name[date_num + i])
                write_data.append(away_team_name[date_num + i])
                write_data.append(home_team_odds[date_num + i])
                write_data.append(away_team_odds[date_num + i])
                write_data.append(home_team_Asian_Handicap_odds[date_num + i])
                write_data.append(away_team_Asian_Handicap_odds[date_num + i])
                write_data.append(home_team_Line[date_num + i])
                write_data.append(away_team_Line[date_num + i])
                
                writer.writerow(write_data)
                write_data = []

    driver.close()
    
execute_code()
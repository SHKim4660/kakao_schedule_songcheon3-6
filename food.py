from pytz import timezone
from datetime import datetime
import time, win32con, win32api, win32gui
import requests
import bs4
import schedule
from datetime import timedelta
now = datetime.now(timezone('Asia/Seoul'))

day_of_week = now.weekday() #Date Of Week 현재 요일
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.minute

weekday = True
date = ""

def get_food(date):
    try:

        if date == '월요일':
            nextday = now + timedelta(days=3)

            nextd = nextday.strftime("%d")
        else:
            nextday = now + timedelta(days=1)

            nextd = nextday.strftime("%d")

        nexty = nextday.strftime("%Y")
        nextm = nextday.strftime("%m")

        nextmz = str(nextm).zfill(2)
        nextdl = list(nextd)
        if nextdl[0] == "0":
            nextdnonz = nextd.replace("0","")
            nextd = nextdnonz
        Url = f'https://school.koreacharts.com/school/meals/B000012253/{nexty}{nextmz}.html'
        response = requests.get(Url)
        response.raise_for_status()


        soup = bs4.BeautifulSoup(response.text,"html.parser")

        text = soup.findAll('tr')
        datesplit = str(text).split("</tr>")
        foodrelocationslpitstr = "급식"

        for i in range(len(datesplit)):
            if f">{nextd}" in datesplit[i] and f"{date}" in datesplit[i]:
                foodsplit = datesplit[i].split("<p>")
                for j in range(len(foodsplit)):
                    if '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' in foodsplit[j]:
                        foodrelocation = foodsplit[j].replace("\n","").replace("\t","").replace("<b>[중식]</b>","").replace("<br/>","").replace("&amp;","\n-").replace("<br>","\n").replace("</br></p></td>","")
                        foodrelocationslpit = foodrelocation.split("-")
                        for k in range(1,len(foodrelocationslpit)):
                            foodrelocationslpit[k] = foodrelocationslpit[k].replace("\n","")
                            foodrelocationslpitstr = f"{foodrelocationslpitstr}\n-{foodrelocationslpit[k]}"

        return foodrelocationslpitstr
    except:
        foodrelocationslpitstr = "급식 오류"
        return foodrelocationslpitstr

print()


def main():
    now = datetime.now(timezone('Asia/Seoul'))

    day_of_week = now.weekday() #Date Of Week 현재 요일
    year = now.year
    month = now.month
    day = now.day   

    if day_of_week == 0:
        date = "화요일"
    elif day_of_week == 1:
        date = "수요일"
    elif day_of_week == 2:
        date = "목요일"
    elif day_of_week == 3:
        date = "금요일"
    elif day_of_week == 4:
        date = "월요일"
    else : weekday = False

    food = get_food(date)
    print(food)
# schedule.every().day.at("16:40").do(main)

# while weekday:
#     schedule.run_pending()
#     time.sleep(60)
    
main()


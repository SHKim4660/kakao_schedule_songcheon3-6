from pytz import timezone
from datetime import datetime
import time, win32con, win32api, win32gui
import requests
import bs4
import schedule



def get_food():
    # month = str(month).zfill(2)
    URL = f'https://school.koreacharts.com/school/meals/B000012253/202403.html'
    response = requests.get(URL)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text,"html.parser")

    text = soup.findAll('tr')
    datesplit = str(text).split("</tr>")
    foodrelocationslpitstr = "급식"

    for i in range(len(datesplit)):
        if ">29</td>" in datesplit[i] and ">금요일</td>" in datesplit[i]:
            foodsplit = datesplit[i].split("<p>")
            for j in range(len(foodsplit)):
                if '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' in foodsplit[j]:
                    foodrelocation = foodsplit[j].replace("\n","").replace("\t","").replace("<b>[중식]</b>","").replace("<br/>","").replace("&amp;","\n-").replace("<br>","\n").replace("</br></p></td>","")
                    foodrelocationslpit = foodrelocation.split("-")
                    for k in range(1,len(foodrelocationslpit)):
                        foodrelocationslpit[k] = foodrelocationslpit[k].replace("\n","")
                        foodrelocationslpitstr = f"{foodrelocationslpitstr}\n-{foodrelocationslpit[k]}"

    return foodrelocationslpitstr



get_food()


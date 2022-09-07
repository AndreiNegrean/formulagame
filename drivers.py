import requests
import pathlib
import os
import bs4
import re


def get_drivers_icons():
    try:
        directory = 'drivers'
        parent_dir = pathlib.Path(__file__).parent.resolve()
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
    except:
        pass

    res = requests.get('https://www.motorsport.com/f1/drivers/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    names_list = []
    for name_code in soup.select('p.ms-item_title'):
        x_name = name_code.text
        name = x_name.strip()
        names_list.append(name)
        if len(names_list) == 20:
            break

    nationalities_list = []
    for nationality_code in soup.select('div.ms-item-driver_info'):
        x_nationality = nationality_code.text
        y_nationality = x_nationality.strip()
        nationality = re.findall(r'(?<=Nationality:\n                ).*', y_nationality)[0]
        nationalities_list.append(nationality)
        if len(nationalities_list) == 20:
            break

    numbers_list = []
    for number_code in soup.select('span.ms-item-driver_number'):
        x_number = number_code.text
        number = x_number.strip()
        numbers_list.append(number)
        if len(numbers_list) == 20:
            break

    teams_list = []
    for team_code in soup.select('div.ms-item-driver_info'):
        x_team = team_code.text
        y_team = x_team.strip()
        team = re.findall('Team:\n\n                    (.*)                ', y_team)[0]
        teams_list.append(team)
        if len(teams_list) == 20:
            break

    icons_list = []
    for icon_code in soup.select('.ms-item_img.ms-item_img--3_2'):
        icon = icon_code['src']
        icons_list.append(icon)
        if len(icons_list) == 20:
            break

    drivers_list = [(names_list[i],
                     nationalities_list[i],
                     numbers_list[i],
                     teams_list[i],
                     icons_list[i]) for i in range(0, 20)]

    path = pathlib.Path(__file__).parent.resolve()

    for name, nationality, number, team, icon in drivers_list:
        if not os.path.exists(f'{path}/drivers/{name}_image.jpg'):
            f = open(f'{path}/drivers/{name}_image.jpg', 'wb')
            icon_link = requests.get(icon)
            f.write(icon_link.content)
            f.close()

    return drivers_list


class Driver:
    def __init__(self, name, nationality, number, team, icon):
        self.name = name
        self.nationality = nationality
        self.number = number
        self.team = team
        self.icon = icon


drivers_list = get_drivers_icons()


def init_drivers():
    drivers = []
    for i in range(0, 20):
        driver = Driver(name=drivers_list[i][0],
                        nationality=drivers_list[i][1],
                        number=drivers_list[i][2],
                        team=drivers_list[i][3],
                        icon=drivers_list[i][4])
        drivers.append(driver)

    return drivers

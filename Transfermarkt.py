import requests
from bs4 import BeautifulSoup
import pyodbc

#-----------Datenbankverbindung aufbauen-------------
from pip._internal.utils import datetime

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-E7UB9K9;'
                      'Database=Managerspiel;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

#------------------------------------------------------


headers = {"User-Agent":"Mozilla/5.0"}
# Bayern TeamPage = requests.get("https://www.transfermarkt.de/fc-bayern-munchen/kader/verein/27/saison_id/2020/plus/1", headers=headers)
TeamPage = requests.get("https://www.transfermarkt.de/borussia-dortmund/kader/verein/16/saison_id/2019/plus/1", headers=headers)
#Eintracht TeamPage = requests.get("https://www.transfermarkt.de/eintracht-frankfurt/kader/verein/24/saison_id/2020/plus/1", headers=headers)

soup = BeautifulSoup(TeamPage.content, 'html.parser')
soup1 = soup.find_all('tr', 'even')
soup2 = soup.find_all('tr', 'odd')

"""
Positionen = soup2[3].find_all('tr')
Position = Positionen[1].text
Eigenschaften = soup2[3].find_all('td', class_='zentriert')
Marktwert = soup2[3].find_all('td', class_='rechts hauptlink')
Rueckennummer = soup2[3].div.text
Name = soup2[3].find('a', class_='spielprofil_tooltip').text
Vorname = Name.split()
Vorname = Vorname[0]
Nachname = Name.split()
Nachname = Nachname[Nachname.__len__()-1]
Geburtstag = Eigenschaften[1].text
Geburtstag = Geburtstag.split()
Groesse = Eigenschaften[3].text
StarkerFuss = Eigenschaften[4].text
ImTeamSeit = 'Im Team seit: ' + Eigenschaften[5].text
VertragBis = 'Vertrag bis: ' + Eigenschaften[7].text
Marktwert = Marktwert[0].text

print (Rueckennummer + ' ' + Vorname + ' ' +  Nachname +'  ' + Marktwert)
"""
id = 57
for x in range(soup1.__len__()):
    Positionen = soup1[x].find_all('tr')
    Positionen2 = soup2[x].find_all('tr')
    Position = Positionen[1].text
    Position2 = Positionen2[1].text
    Eigenschaften = soup1[x].find_all('td', class_='zentriert')
    Eigenschaften2 = soup2[x].find_all('td', class_='zentriert')
    Marktwert = soup1[x].find_all('td', class_='rechts hauptlink')
    Marktwert2 = soup2[x].find_all('td', class_='rechts hauptlink')
    Rueckennummer = soup1[x].div.text
    Rueckennummer2 = soup2[x].div.text
    Name = soup1[x].find('a', class_='spielprofil_tooltip').text
    Name2 = soup2[x].find('a', class_='spielprofil_tooltip').text
    Vorname = Name.split()
    Vorname2 = Name2.split()
    Vorname = Vorname[Vorname.__len__()-2]
    Vorname2 = Vorname2[Vorname2.__len__()-2]
    Nachname = Name.split()
    Nachname2 = Name2.split()
    Nachname = Nachname[Nachname.__len__()-1]
    Nachname2 = Nachname2[Nachname2.__len__()-1]
    Geburtstag = Eigenschaften[1].text
    Geburtstag2 = Eigenschaften2[1].text
    Geburtstag = Geburtstag.split()
    Geburtstag2 = Geburtstag2.split()
    Groesse = Eigenschaften[3].text
    Groesse = Groesse.split()
    Groesse2 = Eigenschaften2[3].text
    Groesse2 = Groesse2.split()
    StarkerFuss = Eigenschaften[4].text
    StarkerFuss2 = Eigenschaften2[4].text
    ImTeamSeit = Eigenschaften[6].text
    if ImTeamSeit == '-':
        ImTeamSeit = '01.01.1900'
    print(ImTeamSeit)
    ImTeamSeit2 = Eigenschaften2[5].text
    if ImTeamSeit2 == '-':
        ImTeamSeit2 = '01.01.1900'
    #ImTeamSeit = datetime.strptime(ImTeamSeit, '%m-%d-%Y')
    VertragBis = Eigenschaften[7].text
    if VertragBis == '-':
        VertragBis = '01.01.1900'
    VertragBis2 = Eigenschaften2[7].text
    if VertragBis2 == '-':
        VertragBis2 = '01.01.1900'
    #VertragBis = datetime.strptime(VertragBis, '%m-%d-%Y')
    Marktwert = Marktwert[0].text
    Marktwert2 = Marktwert2[0].text
    Marktwert = Marktwert.split()
    Marktwert2 = Marktwert2.split()
    Marktwert = Marktwert[0].replace(",", ".")
    Marktwert2 = Marktwert2[0].replace(",", ".")
    Marktwert = float(Marktwert)*1000000
    Marktwert2 = float(Marktwert2)*1000000
    #print(Marktwert)
    Verein = 'Borussia Dortmund'
    #print(Verein)
    #print (Rueckennummer + ' ' + Position + ' ' + Vorname + ' ' + Nachname + ' ' + Marktwert + ' ' + Geburtstag[0] + ' ' + Groesse[0] + ' ' + StarkerFuss + ' ' + ImTeamSeit + ' ' + VertragBis)
    print (Rueckennummer + ' ' + Position + ' ' + Vorname + ' ' + Nachname + ' ' + ' ' + Geburtstag[0] + ' ' + ' ' + StarkerFuss + ' ' + ImTeamSeit + ' ' + VertragBis)
    #print (Rueckennummer2 + ' ' + Position2 + ' ' + Vorname2 + ' ' + Nachname2 + ' ' + Marktwert2 + ' ' + Geburtstag2[0] + ' ' + Groesse2[0] + ' ' + StarkerFuss2 + ' ' + ImTeamSeit2 + ' ' + VertragBis2)
    #cursor.execute('INSERT INTO dbo.Spieler (Rueckennummer, Position, Vorname, Nachname, Marktwert, Verein, StarkerFuss, ImTeamSeit, VertragBis) VALUES(' + Rueckennummer + ',' + Position + ',' + Vorname + ',' + Nachname + ',' + Marktwert + ',' + Verein + ',' + StarkerFuss + ',' + ImTeamSeit + ',' + VertragBis)

    cursor.execute(
        """
        INSERT INTO dbo.Spieler
        (id, Rueckennummer, Position, Vorname, Nachname, Marktwert, Verein, StarkerFuss, ImTeamSeit, VertragBis)
        VALUES (?,?, ?, ?, ?,?,?,?,?,?)
        """,
        (id,Rueckennummer, Position, Vorname, Nachname, Marktwert, Verein, StarkerFuss, ImTeamSeit, VertragBis)
    )
    id = id + 1
    cursor.commit()

#print(soup1.__len__())




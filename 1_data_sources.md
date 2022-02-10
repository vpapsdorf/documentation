# Herkunft und Beschreibung der Daten
Für die Auswertung habe ich - wenn möglich - den Zeitraum von **2010 bis 2020** gewählt. Zur Exploration wurde 
## 1. Bibliotheksstatistik
Daten über aktive Nutzer*innen und Ausleihen (Deutscher Bibliotheksverbund, 2010–2020).

Folgende Variablen habe ich ausgewählt:
- Ausgaben Erwerbungen
- Bestand (print)
- Bestand (virtuell)
- Bestand (insgesamt)
- Entleihen (print)
- Entleihen (virtueller Bestand)
- Entleihen (gesamt)
- Entleihende (insgesamt)

Das Ergebnis habe ich als **csv-Datei** heruntergeladen.


## 2. Bevölkerungsstatistik

Daten zur Bevölkerung in Deutschland (Statistisches Bundesamt, 2010–2020).

Das Ergebnis habe ich als **csv-Datei** heruntergeladen.

### 3. Weitere Daten
Daten zum Leseverhalten der Deutschen und Verkaufszahlen der Buchbranche.

Folgende Variablen habe ich ausgewählt:
| Variable | Schnellzugriff | Quelle |
| --- | --- | --- |
| Anzahl der Menschen, die E-Books lesen | [Statista](https://de.statista.com/statistik/daten/studie/265230/umfrage/e-reader-tablet-smartphone-lesen-von-buechern-auf-elektronischen-geraeten/) | IfD Allensbach (2021a) |
| Anzahl der Menschen, die mehrmals die Woche/mehrmals im Monat/einmal im Monat lesen | [Statista](https://de.statista.com/statistik/daten/studie/232191/umfrage/absatz-von-e-books-in-deutschland/) | IfD Allensbach (2021b) |
| Anzahl der verkauften E-Book | [Statista](https://de.statista.com/statistik/daten/studie/232191/umfrage/absatz-von-e-books-in-deutschland/) | Börsenverein des Deutschen Buchhandels (o. D.) |
| Anzahl der verkauften gedruckten Bücher | [Statista](https://de.statista.com/statistik/daten/studie/416380/umfrage/absatz-von-buechern-in-deutschland/) | Börsenblatt, & Börsenverein des Deutschen Buchhandels (2018) |

Die Daten habe ich direkt in das Dataframe übertragen, weil es keine gute Datenquellen außer der graphischen Darstellungen gab.

---
## Quellen
- Börsenblatt & Börsenverein des Deutschen Buchhandels. (2018, 7. Juni). *Absatz von Büchern in Deutschland in den Jahren 2004 bis 2017 (in Millionen Titel)* [Graph]. In Statista. Zugriff am 09. Februar 2022, von https://de.statista.com/statistik/daten/studie/416380/umfrage/absatz-von-buechern-in-deutschland/
- Börsenverein des Deutschen Buchhandels. (o. D.). *Faktencheck E-Book-Leihe*. https://www.boersenverein.de/fileadmin/bundesverband/dokumente/politik_positionen/Faktencheck_E-Book-Leihe.pdf
-Deutscher Bibliotheksverband. (2021, Oktober). *E-Lending in Öffentlichen Bibliotheken: Antworten auf häufige Fragen*. https://dbv-cs.e-fork.net/sites/default/files/2021-10/FAQs%20zu%20E-lending%20Bibliotheken_20211018_0.pdf
- IfD Allensbach. (2021a, 28. Juni). *Anzahl der Personen in Deutschland, die Bücher auf elektronischen Geräten (E-Reader, Tablet-PC, Smartphone) lesen, von 2017 bis 2021 (in Millionen)* [Graph]. In Statista. Abgerufen am 09. Januar 2022, von https://de.statista.com/statistik/daten/studie/265230/umfrage/e-reader-tablet-smartphone-lesen-von-buechern-auf-elektronischen-geraeten/
- IfD Allensbach. (2021b, 28. Juni). *Anzahl der Personen in Deutschland, die Bücher lesen, nach Häufigkeit von 2017 bis 2021 (in Millionen)* [Graph]. In Statista. Abgerufen am 09. Januar 2022, von https://de.statista.com/statistik/daten/studie/171231/umfrage/haeufigkeit-des-lesens-von-einem-buch/
-Statistisches Bundesamt. (2010–2020). 'Fortschreibung des Bevölkerungsstandes* (eigens erstellt) [Datensatz]. Statistisches Bundesamt. https://www-genesis.destatis.de/genesis/online?operation=statistic&levelindex=0&levelid=1637662639240&code=12411#abreadcrumb

# NBP_Currency
# Stworzenie kalkulatora domowego budrzetu. 
# Dodawniae za pomocą aplikacji, która korzysta z funkcji. Umieszcza dane w lokalnej bazie danych. 
# Osobna aplikacja publikuje Server Django który na bierząco wyświetla dane. 


Instalacja odbywa się za pomocą sciągnięcia aplikacji 
# git clone
następnie uruchomienia instalatora w python3 install.sh

#
mona dodać remove sh.

Flask podgląda status i na bierząco pokazuje raport w zł

# na koniec mówi jaki jest nasz majątek z USD bierze pod uwagę ostatnią aktualną walutę. 

## Baza danych
Kolumny kolejno składają się z 
* ID - INtiger unikatowe ID dla kazdego wpisu
* STAT - Informacja czy wpis jest aktywny. Program urzywa tylko danych ustawione jako true
* CURRE - Waluta jaka wpłyneła do burzetu
* VALUE - Wartosc jaka wplynela 
* USER - KTO wprowadzil dane
* TAG  - Jeden z 9 tagów 
* RICHES - Ogólny stan majątku
* datetime - nic innego jak datastamp


# at

> A parancsok egyszeri végrehajtása egy későbbi időpontban. Az atd (vagy atrun) szolgáltatásnak futnia kell a tényleges végrehajtásokhoz. További információ: <https://manned.org/at>.

- Futtasson parancsokat a standard bemenetről 5 perc alatt (nyomja meg a `Ctrl + D` gombot, ha végzett):

`at now + 5 minutes`

- Egy parancs végrehajtása a standard bemenetről ma délelőtt 10:00-kor:

`echo "{{./make_db_backup.sh}}" | at 1000`

- Parancsok végrehajtása egy adott fájlból jövő kedden:

`at -f {{path/to/file}} 9:30 PM Tue`

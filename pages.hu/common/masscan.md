# masscan

> Hálózati szkenner a lehető leggyorsabb szkenneléshez. Legjobb emelt jogosultságokkal futtatni. Nmap kompatibilitás futtatása: `masscan --nmap`. További információ: <https://github.com/robertdavidgraham/masscan>.

- IP vagy hálózati alhálózat vizsgálata a 80-as portra:

`masscan {{ip_address|network_prefix}} --ports {{80}}`

- B osztályú alhálózat szkennelése a 100 legfontosabb portra 100 000 csomag/másodperc sebességgel:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --rate {{100000}}`

- Egy B osztályú alhálózat átvizsgálása, elkerülve egy adott kizáró fájl tartományait:

`masscan {{10.0.0.0/16}} --top-ports {{100}} --excludefile {{path/to/file}}`

- Az internet 443-as portjának vizsgálata:

`masscan {{0.0.0.0/0}} --ports {{443}} --rate {{10000000}}`

- Az internet átvizsgálása egy adott porttartományra és exportálása egy fájlba:

`masscan {{0.0.0.0/0}} --ports {{0-65535}} -output-format {{binary|grepable|json|list|xml}} --output-filename {{path/to/file}}`

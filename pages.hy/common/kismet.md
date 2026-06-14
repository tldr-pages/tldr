#կիսմետ

> Անլար ցանցի և սարքի դետեկտոր, սնիֆեր, պաշտպանիչ գործիք և WIDS (անլար ներխուժման հայտնաբերում) շրջանակ:.
> Լրացուցիչ տեղեկություններ. <https://www.kismetwireless.net/docs/readme/starting/commandline/>:.

- Փաթեթներ վերցրեք հատուկ անլար ինտերֆեյսից.:

`sudo kismet -c {{wlan0}}`

- Դիտեք բազմաթիվ ալիքներ անլար ինտերֆեյսի վրա.:

`sudo kismet -c {{wlan0,wlan1}} -m`

- Գրեք փաթեթներ և պահեք դրանք որոշակի գրացուցակում.:

`sudo kismet -c {{wlan0}} -d {{path/to/output}}`

- Սկսեք Kismet-ը հատուկ կազմաձևման ֆայլով.:

`sudo kismet -c {{wlan0}} {{[-f|--config-file]}} {{path/to/config.conf}}`

- Դիտեք և գրանցեք տվյալները SQLite տվյալների բազայում.:

`sudo kismet -c {{wlan0}} --log-to-db`

- Մոնիտորինգ օգտագործելով տվյալների հատուկ աղբյուր.:

`sudo kismet -c {{wlan0}} --data-source={{rtl433}}`

- Միացնել ծանուցումները հատուկ իրադարձությունների համար.:

`sudo kismet -c {{wlan0}} --enable-alert={{new_ap}}`

- Ցուցադրել մանրամասն տեղեկատվություն կոնկրետ AP-ի փաթեթների մասին.:

`sudo kismet -c {{wlan0}} --info {{bssid}}`

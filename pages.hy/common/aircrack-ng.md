# aircrack-ng

> Ճեղքեք WEP և WPA/WPA2 ստեղները ձեռքսեղմումից ստացված փաթեթներում:.
> Aircrack-ng ցանցային ծրագրային փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>:.

- Կտրեք բանալին ձայնագրման ֆայլից՝ օգտագործելով [w]ordlist.:

`aircrack-ng -w {{path/to/wordlist.txt}} {{path/to/capture.cap}}`

- Ճեղքեք ստեղնը, օգտագործելով մի քանի պրոցեսորի թելեր ձայնագրման ֆայլից՝ օգտագործելով [w]ordlist:

`aircrack-ng -p {{number}} -w {{path/to/wordlist.txt}} {{path/to/capture.cap}}`

- Կտրեք ստեղնը ձայնագրման ֆայլից՝ օգտագործելով [w]ordlist և մուտքի կետի [e]ssid:

`aircrack-ng -w {{path/to/wordlist.txt}} -e {{essid}} {{path/to/capture.cap}}`

- Կտրեք բանալին ձայնագրման ֆայլից՝ օգտագործելով [w]ordlist-ը և մուտքի կետի MAC հասցեն.:

`aircrack-ng -w {{path/to/wordlist.txt}} --bssid {{mac}} {{path/to/capture.cap}}`

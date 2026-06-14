# airdecap-ng

> Վերծանել WEP, WPA կամ WPA2 կոդավորված նկարահանման ֆայլը:.
> Aircrack-ng ցանցային ծրագրային փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>:.

- Հեռացրեք անլար վերնագրերը բաց ցանցային ֆայլից և օգտագործեք մուտքի կետի MAC հասցեն՝ զտելու համար.:

`airdecap-ng -b {{ap_mac}} {{path/to/capture.cap}}`

- Ապակոդավորեք [w]EP կոդավորված նկարահանման ֆայլը՝ օգտագործելով վեցանկյուն ձևաչափով բանալի.:

`airdecap-ng -w {{hex_key}} {{path/to/capture.cap}}`

- WPA/WPA2 կոդավորված նկարահանման ֆայլի վերծանումը՝ օգտագործելով մուտքի կետի [e]ssid և [p]գաղտնաբառը՝:

`airdecap-ng -e {{essid}} -p {{password}} {{path/to/capture.cap}}`

- WPA/WPA2 կոդավորված նկարահանման ֆայլի վերծանումը՝ պահպանելով վերնագրերը՝ օգտագործելով մուտքի կետի [e]ssid և [p]գաղտնաբառը՝:

`airdecap-ng -l -e {{essid}} -p {{password}} {{path/to/capture.cap}}`

- Ապակոդավորեք WPA/WPA2 կոդավորված նկարահանման ֆայլը՝ օգտագործելով մուտքի կետի [e]ssid և [p]գաղտնաբառերը և օգտագործեք դրա MAC հասցեն՝ զտելու համար.:

`airdecap-ng -b {{ap_mac}} -e {{essid}} -p {{password}} {{path/to/capture.cap}}`

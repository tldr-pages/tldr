# ethtool

> Afișați și modificați parametrii controlerului de interfață de rețea (NIC).
> Mai multe informaţii: <http://man7.org/linux/man-pages/man8/ethtool.8.html>

- Afișează setările curente pentru o interfață:

`ethtool {{eth0}}`

- Afișează informațiile driverului pentru o interfață:

`ethtool --driver {{eth0}}`

- Afișează statisticile de utilizare a rețelei pentru o interfață:

`ethtool --statistics {{eth0}}`

- Clipiți unul sau mai multe LED-uri pe o interfață timp de 10 secunde:

`ethtool --identify {{eth0}} {{10}}`

- Setați viteza legăturii, modul duplex, și parametrul auto-negociere pentru o anumită interfață:

`ethtool -s {{eth0}} speed {{10|100|1000}} duplex {{half|full}} autoneg {{on|off}}`

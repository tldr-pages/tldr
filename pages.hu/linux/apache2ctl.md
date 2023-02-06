# apache2ctl

> A CLI eszköz a HTTP webszerver Apache adminisztrációjához. Ez a parancs Debian alapú operációs rendszerekhez jár, RHEL alapúakhoz lásd: `httpd`. További információ: <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

- Indítsa el az Apache démont. Üzenetet dob, ha már fut:

`sudo apache2ctl start`

- Állítsa le az Apache démont:

`sudo apache2ctl stop`

- Az Apache démon újraindítása:

`sudo apache2ctl restart`

- A konfigurációs fájl szintaxisának tesztelése:

`sudo apache2ctl -t`

- Betöltött modulok listája:

`sudo apache2ctl -M`

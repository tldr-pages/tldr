# svccfg

> Szolgáltatási konfigurációk importálása, exportálása és módosítása. További információ: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Konfigurációs fájl hitelesítése:

`svccfg validate {{smf.xml}}`

- Szolgáltatási konfigurációk exportálása fájlba:

`svccfg export {{servicename}} > {{smf.xml}}`

- Szolgáltatási konfigurációk importálása/frissítése fájlból:

`svccfg import {{smf.xml}}`

# svcs

> A futó szolgáltatásokra vonatkozó információk listázása. További információ: <https://www.unix.com/man-page/linux/1/svcs>.

- Az összes futó szolgáltatás listázása:

`svcs`

- A nem futó szolgáltatások listázása:

`svcs -vx`

- Információk listázása egy szolgáltatásról:

`svcs apache`

- A szolgáltatás naplófájljának helyének megjelenítése:

`svcs -L apache`

- Szolgáltatási naplófájl végének megjelenítése:

`tail $(svcs -L apache)`

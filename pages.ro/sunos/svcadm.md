# svcadm

> Gestionează instanțele serviciilor.
> Mai multe informații: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Activează un serviciu în baza de date a serviciilor:

`svcadm enable {{nume_serviciu}}`

- Dezactivează un serviciu:

`svcadm disable {{nume_serviciu}}`

- Repornește un serviciu care rulează:

`svcadm restart {{nume_serviciu}}`

- Solicită serviciului să recitească fișierele de configurare:

`svcadm refresh {{nume_serviciu}}`

- Scoate un serviciu din starea de întreținere și îi comandă să pornească:

`svcadm clear {{nume_serviciu}}`
# last

> A legutóbb bejelentkezett felhasználók megtekintése. További információ: <https://manned.org/last>.

- Az utolsó bejelentkezések, azok időtartama és egyéb információk megtekintése a `/var/log/wtmp` oldalon:

`last`

- Adja meg, hogy hány utolsó bejelentkezést mutasson meg:

`last -n {{login_count}}`

- Nyomtassa ki a teljes dátumot és időt a bejegyzésekhez, majd a csonkítás elkerülése érdekében a hostnév oszlopot jelenítse meg utoljára:

`last -F -a`

- Egy adott felhasználó összes bejelentkezésének megtekintése, és a hostnév helyett az IP-cím megjelenítése:

`last {{username}} -i`

- Az összes rögzített újraindítás megtekintése (azaz az "újraindítás" álfelhasználó utolsó bejelentkezései):

`last reboot`

- Az összes rögzített leállítás megtekintése (azaz a "shutdown" álfelhasználó utolsó bejelentkezései):

`last shutdown`

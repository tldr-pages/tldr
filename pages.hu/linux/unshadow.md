# unshadow

> A John the Ripper projekt által biztosított segédprogram a hagyományos Unix jelszófájl megszerzésére, ha a rendszer árnyékjelszavakat használ. További információ: <https://www.openwall.com/john/>.

- Az aktuális rendszer `/etc/shadow` és `/etc/passwd` kombinálása:

`sudo unshadow /etc/passwd /etc/shadow`

- Két tetszőleges árnyék- és jelszófájl kombinálása:

`sudo unshadow {{path/to/passwd}} {{path/to/shadow}}`

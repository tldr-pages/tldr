# brightnessctl

> Segédprogram a GNU/Linux operációs rendszerek eszközfényességének olvasására és vezérlésére. További információ: <https://github.com/Hummer12007/brightnessctl>.

- Változtatható fényerővel rendelkező eszközök listázása:

`brightnessctl --list`

- Kiírja a kijelző háttérvilágításának aktuális fényerejét:

`brightnessctl get`

- A kijelző háttérvilágítás fényerejének beállítása egy megadott tartományon belüli százalékos értékre:

`brightnessctl set {{50%}}`

- A fényerő növelése egy megadott lépcsőfokkal:

`brightnessctl set {{+10%}}`

- A fényerő csökkentése egy megadott dekrementummal:

`brightnessctl set {{10%-}}`

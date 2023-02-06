# setserial

> Soros port információk olvasása és módosítása. További információ: <https://manned.org/setserial>.

- Egy adott soros eszközre vonatkozó összes információ kinyomtatása:

`setserial -a {{/dev/cuaN}}`

- Egy adott soros eszköz konfigurációs összefoglalójának kinyomtatása (hasznos az indítási folyamat során történő nyomtatáshoz):

`setserial -b {{device}}`

- Egy adott konfigurációs paraméter beállítása egy eszközhöz:

`sudo setserial {{device}} {{parameter}}`

- Egy eszközlista konfigurációjának kinyomtatása:

`setserial -g {{device1 device2 ...}}`

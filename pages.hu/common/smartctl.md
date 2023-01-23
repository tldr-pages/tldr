# smartctl

> A lemez állapotának felügyelete, beleértve a SMART-adatokat. További információ: <https://www.smartmontools.org>.

- SMART állapotösszefoglaló megjelenítése:

`sudo smartctl --health {{/dev/sdX}}`

- Eszközinformációk megjelenítése:

`sudo smartctl --info {{/dev/sdX}}`

- Rövid önellenőrzés indítása a háttérben:

`sudo smartctl --test short {{/dev/sdX}}`

- Jelenlegi/utolsó önellenőrzés állapotának és egyéb SMART-képességek megjelenítése:

`sudo smartctl --capabilities {{/dev/sdX}}`

- Kimerítő SMART-adatok megjelenítése:

`sudo smartctl --all {{/dev/sdX}}`

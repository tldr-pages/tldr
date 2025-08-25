# top

> Zobrazuje dynamické informace o běžících procesech v reálném čase.
> Více informací: <https://manned.org/top>.

- Zapnout `top`:

`top`

- Nezobrazovat nečinné nebo zombie procesy:

`top {{[-i|--idle-toggle]}}`

- Zobrazovat pouze procesy vlastněné daným uživatelem:

`top {{[-u|--filter-only-euser]}} {{jmeno_uzivatele}}`

- Řadit procesy podle pole:

`top {{[-o|--sort-override]}} {{nazev_pole}}`

- Zobrazovat individuální vlákna daného procesu:

`top {{[-Hp|--threads-show --pid]}} {{id_procesu}}`

- Zobrazovat pouze procesy s daným(i) PID, předaný jako list rozdělený čárkou. (Normálně byste nevěděli PID z hlavy. Tento příklad vybíra PIDs podle názvu procesu):

`top {{[-p|--pid]}} $(pgrep {{[-d|--delimiter]}} ',' {{nazev_procesu}})`

- Zobrazit nápovědu o interaktivních příkazech:

`<?>`

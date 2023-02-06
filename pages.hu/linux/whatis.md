# whatis

> Egysoros leírások megjelenítése kézikönyvoldalakról. További információ: <https://manned.org/whatis>.

- Leírás megjelenítése egy man oldalról:

`whatis {{command}}`

- Ne vágja le a leírást a sor végén:

`whatis --long {{command}}`

- A globusnak megfelelő összes parancs leírásának megjelenítése:

`whatis --wildcard {{net*}}`

- A man oldal leírásainak keresése reguláris kifejezéssel:

`whatis --regex '{{wish[0-9]\.[0-9]}}'`

- Egy adott nyelv leírásainak megjelenítése ( `manpage-{{locale}}` csomagot igényel):

`whatis --locale={{en}} {{command}}`

# surfraw

> CLI a különböző webes keresőmotorok lekérdezéséhez. Egy elvi gyűjteményből áll, amelyek mindegyike tudja, hogyan kell keresni egy adott weboldalt. További információ [: http://surfraw.org](http://surfraw.org).

- A támogatott webhelykereső szkriptek (elvi) listájának megjelenítése:

`surfraw -elvi`

- Megnyitja az elvi találati oldalát egy adott kereséshez a böngészőben:

`surfraw {{elvi}} "{{search_terms}}"`

- Megjeleníti az elvi leírását és annak konkrét beállításait:

`surfraw {{elvi}} -local-help`

- Keresés egy elvi segítségével, meghatározott opciókkal, és az eredményoldal megnyitása a böngészőben:

`surfraw {{elvi}} {{elvi_options}} "{{search_terms}}"`

- Az elvi találati oldalának URL-címének megjelenítése egy adott kereséshez:

`surfraw -print {{elvi}} "{{search_terms}}"`

- Keresés az alias használatával:

`sr {{elvi}} "{{search_terms}}"`

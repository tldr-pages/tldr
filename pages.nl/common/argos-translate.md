# argos-translate

> Een open-source offline vertaalbibliotheek en CLI-tool geschreven in Python.
> Meer informatie: <https://argos-translate.readthedocs.io/en/latest/source/cli.html>.

- Installeer vertaalparen voor vertaling van Spaans naar Engels:

`argospm install translate-es_en`

- Vertaal een tekst van het Spaans (`es`) naar het Engels (`en`) (Opmerking: alleen taalcodes van twee letters worden ondersteund):

`argos-translate --from-lang es --to-lang en {{un texto corto}}`

- Vertaal een tekstbestand van het Engels naar het Hindi:

`cat {{pad/naar/bestand.txt}} | argos-translate --from-lang en --to-lang hi`

- Toon alle geïnstalleerde vertaalparen:

`argospm list`

- Toon vertaalparen vanuit het Engels die beschikbaar zijn om te installeren:

`argospm search --from-lang en`

- Update geïnstalleerde taalpakketparen:

`argospm update`

- Vertaal van `ar` naar `ru` (Opmerking: dit vereist dat de vertaalparen `translate-ar_en` en `translate-en_ru` geïnstalleerd zijn):

`argos-translate --from-lang ar --to-lang ru {{صورة تساوي أكثر من ألف كلمة}}`

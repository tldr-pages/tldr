# helix

> Helix, een post-moderne tekst bewerker, welke verschillende modi beschikbaar stelt tot verschillende manieren van tekst manipulatie.
> Drukken op `<i>` begint invoegmodus. `<Esc>` begint normale modus, wat toegang geeft tot de Vim commando's.
> Meer informatie: <https://helix-editor.com>.

- Open een bestand:

`helix {{pad/naar/bestand}}`

- Open bestanden en toon ze naast elkaar:

`helix --vsplit {{pad/naar/bestand1 pad/naar/bestand2}}`

- Toon de tutorial om Helix te leren (of open het binnen Helix door op `<Esc>` te drukken en `<:>tutor<Enter>` te typen):

`helix --tutor`

- Pas het Helix thema aan:

`<:>theme {{thema_naam}}<Enter>`

- Opslaan en afsluiten:

`<:>wq<Enter>`

- Geforceerd afsluiten zonder op te slaan:

`<:>q!<Enter>`

- Maak de laatste verandering ongedaan:

`<u>`

- Zoek een patroon in het bestand (druk op `<n>`/`<N>` om naar de volgende/vorige overeenkomst te gaan):

`</>{{zoek_patroon}}<Enter>`

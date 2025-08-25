# rename

> Hernoem een bestand of groep van bestanden met een `regex`.
> WAARSCHUWING: Dit commando overschrijft bestanden zonder bevestiging, tenzij de dry-run optie gebruikt wordt.
> Opmerking: Deze pagina verwijst naar de Perl-versie, ook bekend als `file-rename`.
> Meer informatie: <https://manned.org/prename>.

- Vervang `van` met `naar` in de bestandsnamen van de opgegeven bestanden:

`rename 's/{{van}}/{{naar}}/' {{*.txt}}`

- Dry-run - toon welke veranderingen zouden plaatsvinden zonder ze uit te voeren:

`rename -n 's/{{van}}/{{naar}}/' {{*.txt}}`

- Verander de extensie:

`rename 's/\.{{oud}}$/\.{{nieuw}}/' {{*.txt}}`

- Verander naar kleine letters (gebruik `-f` in hoofdlettergevoelige bestandssystemen):

`rename {{[-f|--force]}} 'y/A-Z/a-z/' {{*.txt}}`

- Schrijf de eerste letter van elk woord in de naam met een hoofdletter:

`rename {{[-f|--force]}} 's/\b(\w)/\U$1/g' {{*.txt}}`

- Vervang spaties met underscores:

`rename 's/\s+/_/g' {{*.txt}}`

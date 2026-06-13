# git clean

> Verwijder bestanden die niet worden bijgehouden door Git uit de werkmap.
> Meer informatie: <https://git-scm.com/docs/git-clean>.

- Verwijder niet-bijgehouden bestanden interactief:

`git clean {{[-i|--interactive]}}`

- Toon welke bestanden verwijderd zouden worden zonder ze echt te verwijderen:

`git clean {{[-n|--dry-run]}}`

- Verwijder onmiddellijk alle niet-bijgehouden bestanden geforceerd:

`git clean {{[-f|--force]}}`

- Verwijder niet-bijgehouden mappen ([d]):

`git clean {{[-f|--force]}} -d`

- Verwijder alleen niet-bijgehouden bestanden die overeenkomen met specifieke paden of glob-patronen:

`git clean {{[-f|--force]}} -- {{pad/naar/map}} '{{*.ext}}'`

- Verwijder niet-bijgehouden bestanden, behalve die welke overeenkomen met de opgegeven patronen:

`git clean {{[-f|--force]}} {{[-e|--exclude]}} '{{*.ext}}' {{[-e|--exclude]}} {{pad/naar/map}}/`

- Verwijder niet-bijgehouden bestanden, inclusief genegeerde ([x]) bestanden (bestanden die worden genegeerd door `.gitignore` en `.git/info/exclude`):

`git clean {{[-f|--force]}} -x`

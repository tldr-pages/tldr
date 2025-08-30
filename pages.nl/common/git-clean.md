# git clean

> Verwijder bestanden die niet worden bijgehouden door Git uit de werkmap.
> Meer informatie: <https://git-scm.com/docs/git-clean>.

- Verwijder niet-bijgehouden bestanden:

`git clean`

- Verwijder niet-bijgehouden bestanden interactief:

`git clean {{[-i|--interactive]}}`

- Toon welke bestanden verwijderd zouden worden zonder ze echt te verwijderen:

`git clean {{[-n|--dry-run]}}`

- Verwijder niet-bijgehouden bestanden geforceerd:

`git clean {{[-f|--force]}}`

- Verwijder niet-bijgehouden mappen ([d]) geforceerd:

`git clean {{[-f|--force]}} -d`

- Verwijder niet-bijgehouden bestanden, inclusief genegeerde ([x]) bestanden (bestanden die worden genegeerd door `.gitignore` en `.git/info/exclude`):

`git clean -x`

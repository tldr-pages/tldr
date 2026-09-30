# crane mutate

> Wijzig image-labels en annotaties.
> De container moet naar een registry worden gepusht, en het manifest wordt daar bijgewerkt.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>.

- Stel nieuwe annotaties of labels in:

`crane mutate {{[-a|--annotation]}}/{{[-l|--label]}} {{annotation/label}}`

- Voeg een tarball toe, of stel het commando/de entrypoint/omgevingsvariabelen/exposed ports van een image in:

`crane mutate {{--append}}/{{--cmd}}/{{--entrypoint}}/{{[-e|--env]}}/{{--exposed-ports}} {{var1 var2 ...}}`

- Schrijf de resulterende image naar een nieuwe tarball:

`crane mutate {{[-o|--output]}} {{pad/naar/tarball}}`

- Stel het platform van de gewijzigde image in, in de vorm `os/arch/variant:osversion,platform`:

`crane mutate --set-platform {{platform_naam}}`

- Nieuwe tagreferentie die moet worden toegepast op de gewijzigde image:

`crane mutate {{[-t|--tag]}} {{tag_naam}}`

- Stel een nieuwe gebruiker in:

`crane mutate {{[-u|--user]}} {{gebruikersnaam}}`

- Stel een nieuwe werkmap in:

`crane mutate {{[-w|--workdir]}} {{pad/naar/werkmap}}`

- Toon de help:

`crane mutate {{[-h|--help]}}`

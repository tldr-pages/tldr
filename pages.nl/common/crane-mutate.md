# crane mutate

> Wijzig image-labels en annotaties.
> De container moet naar een registry worden gepusht, en het manifest wordt daar bijgewerkt.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>.

- Nieuwe annotaties om in te stellen (standaard []):

`crane mutate {{[-a|--annotation]}}/{{[-l|--label]}} {{annotation/label}}`

- Pad naar tarball/opdracht/entrypoint/omgeving variabele/exposed-ports om aan de image toe te voegen:

`crane mutate {{--append}}/{{--cmd}}/{{--entrypoint}}/{{[-e|--env]}}/{{--exposed-ports}} {{var1 var2 ...}}`

- Pad naar nieuwe tarball van de resulterende image:

`crane mutate {{[-o|--output]}} {{pad/naar/tarball}}`

- Repository in de vorm os/arch{{/variant}}{{:osversion}}{{,<platform>}} om de gewijzigde image te pushen:

`crane mutate --set-platform {{platform_naam}}`

- Nieuwe tagreferentie die moet worden toegepast op de gewijzigde image:

`crane mutate {{[-t|--tag]}} {{tag_naam}}`

- Nieuwe gebruiker in te stellen:

`crane mutate {{[-u|--user]}} {{gebruikersnaam}}`

- Nieuwe werk-map in te stellen:

`crane mutate {{[-w|--workdir]}} {{pad/naar/werk-map}}`

- Toon de help:

`crane mutate {{[-h|--help]}}`

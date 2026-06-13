# add-apt-repository

> Beheer `apt` repository-definities.
> Meer informatie: <https://manned.org/add-apt-repository>.

- Voeg een nieuwe `apt` repository toe:

`add-apt-repository {{repository_spec}}`

- Verwijder een `apt` repository:

`add-apt-repository {{[-r|--remove]}} {{repository_spec}}`

- Werk de pakketcache bij na het toevoegen van een repository:

`add-apt-repository --update {{repository_spec}}`

- Sta toe dat bronpakketten worden gedownload vanuit de repository:

`add-apt-repository {{[-s|--enable-source]}} {{repository_spec}}`

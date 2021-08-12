# git request-pull

> Generați o solicitare prin care solicitați proiectului din amonte să tragă modificări în arborele său.
> Mai multe informaţii: <https://git-scm.com/docs/git-request-pull>

- Produce o cerere care rezumă modificările dintre versiunea v1.1 și o ramură specificată:

`git request-pull {{v1.1}} {{https://example.com/project}} {{branch_name}}`

- Produce o cerere rezumând modificările dintre versiunea v0.1 pe sucursala `foo` și sucursala locală `bar”:

`git request-pull {{v0.1}} {{https://example.com/project}} {{foo:bar}}`

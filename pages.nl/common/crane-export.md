# crane export

> Exporteer het bestandssysteem van een containerimage als een tarball.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Schrijf de tarball naar `stdout`:

`crane export {{image_naam}} -`

- Schrijf de tarball naar een bestand:

`crane export {{image_naam}} {{pad/naar/tarball}}`

- Lees de image vanuit `stdin`:

`crane export - {{pad/naar/filenaam}}`

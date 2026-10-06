# crane push

> Stuur lokale image-inhoud naar een externe registry.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>.

- Stuur lokale image naar externe registry:

`crane push {{pad/naar/tarball}} {{image_naam}}`

- Schrijf een lijst van gepubliceerde image-referenties naar een bestand:

`crane push {{pad/naar/tarball}} {{image_naam}} --image-refs {{pad/naar/bestand}}`

- Stuur een verzameling images als een enkele index (vereist als pad meerdere images heeft):

`crane push {{pad/naar/tarball}} {{image_naam}} --index`

- Toon de help:

`crane push {{[-h|--help]}}`

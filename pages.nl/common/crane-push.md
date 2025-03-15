# crane push

> Stuur lokale image-inhoud naar een externe registry.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>.

- Stuur lokale image naar externe registry:

`crane push {{pad/naar/tarball}} {{image_naam}}`

- Pad naar bestand met lijst van gepubliceerde image-referenties:

`crane push {{pad/naar/tarball}} {{image_naam}} --image-refs {{pad/naar/filenaam}}`

- Stuur een verzameling images als een enkele index (vereist als pad meerdere images heeft):

`crane push {{pad/naar/tarball}} {{image_naam}} --index`

- Toon de help:

`crane push {{[-h|--help]}}`

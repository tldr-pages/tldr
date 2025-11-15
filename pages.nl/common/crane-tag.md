# crane tag

> Efficiënt taggen van een remote image zonder het te downloaden, wat verschilt van het `copy` commando.
> Het slaat de controles van laagbestaan over omdat we weten dat de manifest al bestaat, wat het iets sneller maakt.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

- Tag een remote image:

`crane tag {{image_naam}} {{tag_naam}}`

- Toon de help:

`crane tag {{[-h|--help]}}`

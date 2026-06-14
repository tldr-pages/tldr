# կռունկի հավելված

> Հրել պատկեր՝ հիմնված (ըստ ցանկության) բազային պատկերի վրա:.
> Ավելացնում է տրամադրված թարբոլիկների պարունակությունը պարունակող շերտեր:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>:.

- Հրել պատկերը հիմնված բազային պատկերի վրա.:

`crane append {{[-b|--base]}} {{image_name}}`

- Հրել պատկերը կցված շերտով tarball-ից.:

`crane append {{[-f|--new_layer]}} {{layer_name1 layer_name2 ...}}`

- Հրել պատկերը կցված շերտով նոր պիտակով.:

`crane append {{[-t|--new_tag]}} {{tag_name}}`

- Ստացված պատկերը մղեք նոր tarball.:

`crane append {{[-o|--output]}} {{path/to/tarball}}`

- Docker-ի փոխարեն օգտագործեք OCI տիպի լրատվամիջոցների դատարկ բազային պատկեր.:

`crane append --oci-empty-base`

- Նշեք ստացված պատկերը որպես հիմնական պատկերի վրա հիմնված.:

`crane append --set-base-image-annotations`

- Ցուցադրել օգնությունը.:

`crane append {{[-h|--help]}}`

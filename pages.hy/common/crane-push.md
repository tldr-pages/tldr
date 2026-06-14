# կռունկի հրում

> Տեղական պատկերի բովանդակությունը տեղափոխեք հեռավոր ռեեստր:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>:.

- Տեղական պատկերը մղեք հեռավոր ռեեստր.:

`crane push {{path/to/tarball}} {{image_name}}`

- Հրապարակված պատկերների հղումների ցանկով ֆայլի ուղի.:

`crane push {{path/to/tarball}} {{image_name}} --image-refs {{path/to/file}}`

- Հրել պատկերների հավաքածուն որպես մեկ ինդեքս (պահանջվում է, եթե ուղին ունի մի քանի պատկեր).:

`crane push {{path/to/tarball}} {{image_name}} --index`

- Ցուցադրել օգնությունը.:

`crane push {{[-h|--help]}}`

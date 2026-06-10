# m4b-գործիք

> Միավորել, բաժանել և կառավարել աուդիոգրքերի ֆայլերը գլուխներով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sandreas/m4b-tool>:.

- Ստեղծեք աուդիոգիրք աուդիո ֆայլերով մուտքագրման գրացուցակում.:

`m4b-tool merge {{path/to/input_directory}} {{[-o|--output-file]}}={{path/to/merged.m4b}}`

- Կազմեք գլուխներ՝ օգտագործելով մուտքային ֆայլերի անունները.:

`m4b-tool merge {{path/to/input_directory}} {{[-o|--output-file]}}={{path/to/merged.m4b}} --use-filenames-as-chapters`

- Աուդիոգիրքը բաժանեք առանձին ֆայլերի՝ ըստ գլուխների.:

`m4b-tool split {{path/to/audiobook.m4b}} {{[-o|--output-dir]}}={{path/to/output_directory}}`

- Աուդիոգիրքը բաժանեք MP3 ֆայլերի.:

`m4b-tool split {{path/to/audiobook.m4b}} --audio-format {{mp3}} {{[-o|--output-dir]}}={{path/to/output_directory}}`

- Կարգավորեք գլուխները՝ օգտագործելով լռության հայտնաբերումը.:

`m4b-tool chapters {{path/to/audiobook.m4b}} --adjust-by-silence`

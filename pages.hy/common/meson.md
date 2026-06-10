#մեզոն

> SCons-ի նման կառուցման համակարգ, որն օգտագործում է Python-ը որպես ճակատային լեզու, իսկ Ninja-ն՝ որպես շենքի հետին պլան:.
> Լրացուցիչ տեղեկություններ. <https://mesonbuild.com/Commands.html>:.

- Ստեղծեք նախագիծ լռելյայն արժեքներով.:

`meson init`

- Ստեղծեք C նախագիծ տվյալ անունով և տարբերակով.:

`meson init {{[-l|--language]}} c {{[-n|--name]}} {{myproject}} --version {{0.1}}`

- Կազմաձևեք `build` անունով գրացուցակը, նախնական արժեքներով կոմպիլյացիայի համար.:

`meson {{[build|setup build]}}`

- Կազմել նախագիծը.:

`meson compile -C {{path/to/build_directory}}`

- Գործարկել բոլոր թեստերը նախագծում.:

`meson test -C {{path/to/build_directory}}`

- Տեղադրեք նախագիծը `/usr/local`-ում՝:

`meson install -C {{path/to/build_directory}}`

- Ցուցադրել օգնությունը.:

`meson {{[-h|--help]}}`

- Ցուցադրման տարբերակը:

`meson {{[-v|--version]}}`

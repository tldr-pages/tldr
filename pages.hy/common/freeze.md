#սառեցնել

> Ստեղծեք կոդի և տերմինալի ելքի պատկերներ:.
> Աջակցվող ձևաչափերն են PNG, SVG և WebP:.
> Տես նաև՝ `silicon`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/charmbracelet/freeze#flags>:.

- Ստեղծեք ֆայլի հիման վրա կոդի պատկեր.:

`freeze {{path/to/file}}`

- Նշեք ելքի ուղին.:

`freeze {{path/to/file}} {{[-o|--output]}} {{path/to/output_image.png}}`

- Ստեղծեք տերմինալի ելքի պատկեր.:

`freeze {{[-x|--execute]}} {{command}}`

- Ինտերակտիվ կերպով հարմարեցրեք ելքային պատկերը.:

`freeze {{path/to/file}} {{[-i|--interactive]}}`

- Ընտրեք թեմա շարահյուսության ընդգծման համար.:

`freeze {{path/to/file}} {{[-t|--theme]}} {{dracula}}`

- Օգտագործեք հիմնական կազմաձևման ձևանմուշ.:

`freeze {{path/to/file}} {{[-c|--config]}} {{base|full|user}}`

- Գրեք տողերի համարների որոշակի շրջանակ.:

`freeze {{path/to/file}} --lines {{start}},{{end}}`

- Ցույց տալ տողերի համարները.:

`freeze {{path/to/file}} --show-line-numbers`

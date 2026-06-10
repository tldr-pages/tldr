# ng կազմաձևում

> Օգտագործեք JSON ուղու նշումը (camelCase) աշխատանքային տարածքի կամ նախագծի կազմաձևերը խմբագրելու համար, ինչպիսիք են կառուցման ընտրանքները:.
> Լրացուցիչ տեղեկություններ. <https://angular.dev/cli/config>:.

- Ցուցադրել բոլոր կազմաձևման արժեքները.:

`ng config`

- Ստացեք հատուկ կազմաձևման արժեք.:

`ng config projects.{{project_name}}.prefix`

- Սահմանեք կազմաձևման արժեքը.:

`ng config projects.{{project_name}}.prefix {{value}}`

- Անջատեք CLI-ի վերլուծությունը ամբողջ աշխարհում.:

`ng config cli.analytics disabled {{[-g|--global]}}`

- Սահմանեք գլոբալ կազմաձևման արժեք (զգույշ. սա ազդում է բոլոր Angular նախագծերի վրա).:

`ng config projects.{{project_name}}.prefix {{value}} {{[-g|--global]}}`

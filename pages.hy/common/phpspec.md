# phpspec

> Վարքագծի վրա հիմնված մշակման գործիք PHP-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://phpspec.net/en/stable/cookbook/console.html>:.

- Ստեղծեք հստակեցում դասի համար.:

`phpspec describe {{class_name}}`

- Գործարկեք բոլոր բնութագրերը «spec» գրացուցակում.:

`phpspec run`

- Գործարկել մեկ հստակեցում.:

`phpspec run {{path/to/class_specification_file}}`

- Գործարկել բնութագրերը՝ օգտագործելով հատուկ կազմաձևման ֆայլ.:

`phpspec run {{[-c|--config]}} {{path/to/configuration_file}}`

- Գործարկեք բնութագրերը՝ օգտագործելով հատուկ bootstrap ֆայլ.:

`phpspec run {{[-b|--bootstrap]}} {{path/to/bootstrap_file}}`

- Անջատել կոդերի ստեղծման հուշումները.:

`phpspec run --no-code-generation`

- Միացնել կեղծ վերադարձի արժեքները.:

`phpspec run --fake`

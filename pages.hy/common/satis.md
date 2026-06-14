#բավարար

> Satis ստատիկ կոմպոզիտորի պահեստի օգտակարությունը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/composer/satis>:.

- Նախաձեռնեք Satis կոնֆիգուրացիան.:

`satis init {{satis.json}}`

- Ավելացնել VCS պահոց Satis-ի կազմաձևին.:

`satis add {{repository_url}}`

- Կառուցեք ստատիկ ելքը կոնֆիգուրացիայից.:

`satis build {{satis.json}} {{path/to/output_directory}}`

- Ստեղծեք ստատիկ ելք՝ թարմացնելով միայն նշված պահոցը.:

`satis build --repository-url {{repository_url}} {{satis.json}} {{path/to/output_directory}}`

- Հեռացրեք անօգուտ արխիվային ֆայլերը.:

`satis purge {{satis.json}} {{path/to/output_directory}}`

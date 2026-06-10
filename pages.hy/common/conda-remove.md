# conda հեռացնել

> Հեռացրեք փաթեթները կոնդա միջավայրից:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/remove.html>:.

- Հեռացրեք `scipy`-ը ընթացիկ ակտիվ միջավայրից.:

`conda remove scipy`

- Հեռացրեք փաթեթների ցանկը նշված միջավայրից.:

`conda remove {{[-n|--name]}} {{environment_name}} {{package1 package2 ...}}`

- Հեռացրեք բոլոր փաթեթները և ինքնին միջավայրը.:

`conda remove {{[-n|--name]}} {{environment_name}} --all`

- Հեռացրեք բոլոր փաթեթները, բայց պահպանեք շրջակա միջավայրը.:

`conda remove {{[-n|--name]}} {{environment_name}} --all --keep-env`

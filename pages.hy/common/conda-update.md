# Conda թարմացում

> Թարմացրեք փաթեթները conda միջավայրում, ներառյալ Conda-ն:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/update.html>:.

- Թարմացրեք բոլոր փաթեթները ընթացիկ միջավայրում.:

`conda update {{[--all|--update-all]}}`

- Թարմացրեք որոշակի փաթեթ ընթացիկ միջավայրում.:

`conda update {{package_name}}`

- Թարմացրեք conda-ն բազային միջավայրում.:

`conda update {{[-n|--name]}} base conda`

- Թարմացրեք փաթեթները՝ անտեսելով ամրացված փաթեթները.:

`conda update --no-pin`

- Թարմացրեք փաթեթները անցանց ռեժիմում.:

`conda update --offline`

# conda ակտիվացնել

> Ակտիվացրեք կոնդա միջավայրը:.
> Տես նաև՝ `conda deactivate`:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/stable/dev-guide/deep-dives/activation.html>:.

- Ակտիվացրեք գոյություն ունեցող միջավայրը `myenv` անունով:

`conda activate myenv`

- Ակտիվացրեք գոյություն ունեցող միջավայրը, որը գտնվում է հատուկ ուղու վրա.:

`conda activate {{path/to/myenv}}`

- Կցեք `myenv` միջավայրը նախորդ միջավայրի վերևում՝ հասանելի դարձնելով գրադարանները/հրամանները/փոփոխականները երկուսից՝:

`conda activate --stack myenv`

- Սկսեք մաքուր միջավայր `myenv` առանց այն կուտակելու՝ դարձնելով նախորդ միջավայրի գրադարանները/հրամանները/փոփոխականները անհասանելի.:

`conda activate --no-stack myenv`

- Ցուցադրել օգնությունը.:

`conda activate {{[-h|--help]}}`

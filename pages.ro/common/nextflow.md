# nextflow

> Instrument pentru rularea conductelor de calcul. Folosit în principal pentru fluxurile de lucru bioinformatică.
> Mai multe informaţii: <https://www.nextflow.io>

- Rulați o conductă, utilizați rezultatele memorate în cache din rulările anterioare:

`nextflow run {{main.nf}} -resume`

- Rulați o versiune specifică a unui flux de lucru la distanță de la GitHub:

`nextflow run {{user/repo}} -revision {{release_tag}}`

- Rulați cu un director de lucru dat pentru fișiere intermediare, salvați raportul de execuție:

`nextflow run {{workflow}} -work-dir {{path/to/directory}} -with-report {{report.html}}`

- Afișează detaliile rulărilor anterioare în directorul curent:

`nextflow log`

- Eliminați fișierele cache și intermediare pentru o anumită rulare:

`nextflow clean -force {{run_name}}`

- Listează toate proiectele descărcate:

`nextflow list`

- Trageți cea mai recentă versiune a unui flux de lucru la distanță de la Bitbucket:

`nextflow pull {{user/repo}} -hub bitbucket`

- Actualizare Nextflow:

`nextflow self-update`

# trivy

> A konténerképek, fájlrendszerek és Git-tárházak sebezhetőségének, valamint a konfigurációs problémáknak a keresése. További információ: <https://github.com/aquasecurity/trivy>.

- Egy kép ellenőrzése:

`trivy image {{image:tag}}`

- A fájlrendszer vizsgálata sebezhetőségek és hibás konfigurációk után:

`trivy fs --security-checks {{vuln,config}} {{path/to/project_directory}}`

- Egy könyvtár vizsgálata hibás konfigurációk után:

`trivy config {{path/to/iac_directory}}`

- Kimenet generálása SARIF-sablonnal:

`trivy image --format {{template}} --template {{"@sarif.tpl"}} -o {{path/to/report.sarif}} {{image:tag}}`

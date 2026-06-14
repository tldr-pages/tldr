# սոնար-սկաներ

> Ընդհանուր սկաներ SonarQube նախագծերի համար, որոնք չեն օգտագործում կառուցման գործիքներ, ինչպիսիք են Maven, Gradle կամ Ant:.
> Լրացուցիչ տեղեկություններ. <https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner>:.

- Սկանավորեք նախագիծը կազմաձևման ֆայլով ձեր նախագծի արմատական գրացուցակում՝ `sonar-project.properties` անունով:

`sonar-scanner`

- Սկանավորեք նախագիծը՝ օգտագործելով կազմաձևման ֆայլը, բացի `sonar-project.properties`-ից:

`sonar-scanner {{[-D|--define]}} {{project.settings=myproject.properties}}`

- Տպել վրիպազերծման տեղեկատվությունը.:

`sonar-scanner {{[-X|--debug]}}`

- Ցուցադրել օգնությունը.:

`sonar-scanner {{[-h|--help]}}`

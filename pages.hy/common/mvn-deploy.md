# mvn տեղակայում

> Ավելացնել արտեֆակտ հեռավոր պահեստում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/mvn>:.

- Պատճենեք վերջնական արտեֆակտը `settings.xml` ֆայլում կազմաձևված հեռավոր պահոցում՝:

`mvn deploy`

- Պատճենեք արտեֆակտ, որը կառուցված չէ Maven-ի միջոցով հեռավոր պահեստում.:

`mvn deploy:deploy-file {{[-D|--define]}} url={{URLOfTheRemoteRepository}} {{[-D|--define]}} repositoryId={{ServerIdFromSettingsXML}} {{[-D|--define]}} file={{FileToBeDeployed}}`

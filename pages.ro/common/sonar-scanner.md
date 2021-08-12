# sonar-scanner

> SonarScanner este un scaner generic pentru proiectele SonarQube care nu utilizează instrumente de construire, cum ar fi Maven, Gradle sau Ant.
> Mai multe informaţii: <https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>

- Scanați un proiect cu fișier de configurare în directorul rădăcină al proiectului numit `sonar-project.properties`:

`sonar-scanner`

- Scanarea unui proiect folosind alt fișier de configurare decât `sonar-project.properties`:

`sonar-scanner -D{{project.settings=myproject.properties}}`

- Imprimați informații de ajutor:

`sonar-scanner -h`

- Imprimare informații de depanare:

`sonar-scanner -X`

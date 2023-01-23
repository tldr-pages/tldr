# sonar-scanner

> A SonarScanner egy általános szkenner a SonarQube projektekhez, amelyek nem használnak olyan építőeszközöket, mint a Maven, Gradle vagy Ant. További információ: <https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

- A projekt gyökérkönyvtárában lévő, `sonar-project.properties` nevű konfigurációs fájlal rendelkező projekt beolvasása:

`sonar-scanner`

- Projekt beolvasása a `sonar-project.properties` címtől eltérő konfigurációs fájlt használó projekt beolvasása :

`sonar-scanner -D{{project.settings=myproject.properties}}`

- Súgóinformációk nyomtatása:

`sonar-scanner -h`

- Hibakeresési információk nyomtatása:

`sonar-scanner -X`

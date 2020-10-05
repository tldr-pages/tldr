# sonar-scanner

> SonarScanner is a generic scanner for SonarQube for projects do not use any specific build tool like maven, gradle , etc.
> More information: <https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/>.

- Scan a project with configuration file in your project's root directory named `sonar-project.properties`:

`sonar-scanner`

- Scan a project using configuration file other than `sonar-project.properties`:

`sonar-scanner -D{{project.settings=myproject.properties}}`

- Print help information:

`sonar-scanner -h`

- Print debudgging information:

`sonar-scanner -X`

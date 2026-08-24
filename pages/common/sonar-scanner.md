# sonar-scanner

> A generic scanner for SonarQube projects that do not use build tools such as Maven, Gradle, or Ant.
> More information: <https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/sonarscanner>.

- Scan a project with configuration file in your project's root directory named `sonar-project.properties`:

`sonar-scanner`

- Scan a project using configuration file other than `sonar-project.properties`:

`sonar-scanner {{[-D|--define]}} {{project.settings=myproject.properties}}`

- Print debugging information:

`sonar-scanner {{[-X|--debug]}}`

- Display help:

`sonar-scanner {{[-h|--help]}}`

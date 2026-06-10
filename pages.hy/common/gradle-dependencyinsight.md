# gradle dependencyInsight

> Ցուցադրել Gradle նախագծի որոշակի կախվածության պատկերացում:.
> Լրացուցիչ տեղեկություններ. <https://docs.gradle.org/current/userguide/command_line_interface.html#reporting_dependencies>:.

- Ցույց տալ պատկերացում կոնկրետ կախվածության համար.:

`gradle dependencyInsight --dependency {{package_name}}`

- Ցույց տվեք որոշակի կոնֆիգուրացիայի կախվածության պատկերացում.:

`gradle dependencyInsight --dependency {{package_name}} --configuration {{configuration_name}}`

- Ցույց տալ պատկերացում կոնկրետ ենթանախագծի համար.:

`gradle :{{subproject}}:dependencyInsight --dependency {{package_name}}`

- Ցույց տվեք պատկերացում կախվածության ամբողջական ճանապարհով.:

`gradle dependencyInsight --dependency {{package_name}} {{[-i|--info]}}`

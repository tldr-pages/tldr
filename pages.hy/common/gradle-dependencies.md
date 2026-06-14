# gradle կախվածություն

> Ցուցադրել կախվածության ծառը Gradle նախագծի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_project_dependencies>:.

- Ցուցադրել բոլոր կախվածությունները.:

`gradle dependencies`

- Ցուցադրել կախվածությունը որոշակի կազմաձևման համար.:

`gradle dependencies --configuration {{implementation}}`

- Ցուցադրել կախվածությունը կոնկրետ ենթանախագծի համար.:

`gradle :{{subproject}}:dependencies`

- Ցուցադրել կախվածությունները և պահել ֆայլում.:

`gradle dependencies > {{path/to/dependencies.txt}}`

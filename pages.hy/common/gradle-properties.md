# gradle հատկություններ

> Ցուցադրել Gradle նախագծի հատկությունները:.
> Լրացուցիչ տեղեկություններ. <https://docs.gradle.org/current/userguide/command_line_interface.html#listing_project_properties>:.

- Ցուցադրել նախագծի բոլոր հատկությունները.:

`gradle properties`

- Ցուցադրել հատկությունները մանրամասն ելքով.:

`gradle properties {{[-i|--info]}}`

- Ցուցադրել հատկությունները կոնկրետ ենթանախագծի համար.:

`gradle :{{subproject}}:properties`

- Ցուցադրել հատուկ գույքի արժեքը.:

`gradle properties | grep {{property_name}}`

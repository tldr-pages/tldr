# gradle init

> Նախաձեռնեք նոր Gradle նախագիծը ինտերակտիվ կերպով:.
> Լրացուցիչ տեղեկություններ. <https://docs.gradle.org/current/userguide/build_init_plugin.html>:.

- Նախաձեռնեք նոր Gradle նախագիծը ինտերակտիվ կերպով.:

`gradle init`

- Նախաձեռնել որոշակի տեսակի նախագիծ.:

`gradle init --type {{basic|java-application|java-library|...}}`

- Նախաձեռնեք նախագիծ հատուկ DSL-ով.:

`gradle init --dsl {{groovy|kotlin}}`

- Նախաձեռնեք նախագիծ հատուկ թեստային շրջանակով.:

`gradle init --test-framework {{junit-jupiter|testng|spock}}`

- Նախաձեռնեք նախագիծն առանց ինտերակտիվ հուշումների.:

`gradle init --type {{java-application}} --dsl {{kotlin}} --test-framework {{junit-jupiter}}`

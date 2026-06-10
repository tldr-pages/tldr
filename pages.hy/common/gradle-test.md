# gradle թեստ

> Գործարկել թեստերը Gradle-ի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://docs.gradle.org/current/userguide/java_testing.html>:.

- Գործարկել բոլոր թեստերը.:

`gradle test`

- Գործարկել թեստերը մանրամասն ելքով.:

`gradle test {{[-i|--info]}}`

- Գործարկել հատուկ թեստային դաս.:

`gradle test --tests {{class_name}}`

- Կատարեք օրինակին համապատասխանող թեստեր.:

`gradle test --tests "{{pattern}}"`

- Վերագործարկեք թեստերը, նույնիսկ եթե արդիական են.:

`gradle test --rerun`

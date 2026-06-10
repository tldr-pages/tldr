# sbt

> Ստեղծեք գործիք Scala և Java նախագծերի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.scala-sbt.org/1.x/docs/>:.

- Սկսեք REPL (ինտերակտիվ կեղև).:

`sbt`

- Ստեղծեք նոր Scala նախագիծ GitHub-ում տեղակայված գոյություն ունեցող Giter8 ձևանմուշից.:

`sbt new {{scala/hello-world.g8}}`

- Կազմեք և գործարկեք բոլոր թեստերը.:

`sbt test`

- Ջնջել բոլոր ստեղծված ֆայլերը `target` գրացուցակում.:

`sbt clean`

- Կազմեք հիմնական աղբյուրները `src/main/scala` և `src/main/java` դիրեկտորիաներում.:

`sbt compile`

- Օգտագործեք sbt-ի նշված տարբերակը.:

`sbt -sbt-version {{version}}`

- Օգտագործեք հատուկ jar ֆայլ որպես sbt գործարկիչ.:

`sbt -sbt-jar {{path}}`

- Թվարկեք բոլոր sbt տարբերակները.:

`sbt -h`

# scala-cli

> Փոխազդել Scala ծրագրավորման լեզվի հետ:.
> Լրացուցիչ տեղեկություններ. <https://scala-cli.virtuslab.org/docs/overview/>:.

- Սկսեք REPL (ինտերակտիվ կեղև)՝ օգտագործելով հատուկ Scala և JVM տարբերակ.:

`scala-cli --scala {{3.1.0}} --jvm {{temurin:17}}`

- Կազմել և գործարկել Scala սցենարը.:

`scala-cli run {{path/to/script.scala}}`

- Կազմեք և փորձարկեք Scala սցենար.:

`scala-cli test {{path/to/script.scala}}`

- Ձևաչափեք Scala սցենարը՝ տեղում թարմացնելով ֆայլը.:

`scala-cli fmt {{path/to/script.scala}}`

- Ստեղծեք ֆայլեր IDE (VSCode և IntelliJ) աջակցության համար.:

`scala-cli setup-ide {{path/to/script.scala}}`

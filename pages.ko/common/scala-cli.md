# scala-cli

> Scala 프로그래밍 언어와 상호작용.
> 더 많은 정보: <https://scala-cli.virtuslab.org/docs/overview/>.

- 특정 Scala 버전과 JVM 버전을 사용하여 REPL(대화형 셸) 시작:

`scala-cli --scala {{3.1.0}} --jvm {{temurin:17}}`

- Scala 스크립트 컴파일 및 실행:

`scala-cli run {{경로/대상/스크립트.scala}}`

- Scala 스크립트 컴파일 및 테스트:

`scala-cli test {{경로/대상/스크립트.scala}}`

- Scala 스크립트의 형식을 맞추고 파일을 직접 업데이트:

`scala-cli fmt {{경로/대상/스크립트.scala}}`

- IDE 지원을 위한 파일 생성 (VSCode 및 IntelliJ):

`scala-cli setup-ide {{경로/대상/스크립트.scala}}`

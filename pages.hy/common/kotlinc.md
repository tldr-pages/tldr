# kotlinc

> Kotlin կազմող.
> Լրացուցիչ տեղեկություններ. <https://kotlinlang.org/docs/compiler-reference.html#common-options>:.

- Սկսեք REPL (ինտերակտիվ կեղև).:

`kotlinc`

- Կազմեք Kotlin ֆայլ.:

`kotlinc {{path/to/file.kt}}`

- Կազմեք մի քանի Kotlin ֆայլեր.:

`kotlinc {{path/to/file1.kt path/to/file2.kt ...}}`

- Կատարեք հատուկ Kotlin Script ֆայլ.:

`kotlinc -script {{path/to/file.kts}}`

- Կազմեք Kotlin ֆայլը ինքնուրույն պարունակվող jar ֆայլի մեջ, որը ներառում է Kotlin գործարկման գրադարանը.:

`kotlinc {{path/to/file.kt}} -include-runtime -d {{path/to/file.jar}}`

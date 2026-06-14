# cs java

> `java` և `java-home` հրամանները վերցնում և տեղադրում են JVM-ներ: `java` հրամանը նույնպես գործարկում է դրանք:.
> Լրացուցիչ տեղեկություններ. <https://get-coursier.io/docs/cli-java>:.

- Ցուցադրել Java տարբերակը՝ օգտագործելով սուրհանդակ.:

`cs java -version`

- Զանգահարեք հատուկ Java-ի տարբերակ մաքսային հատկություններով, օգտագործելով կուրսիեր.:

`cs java --jvm {{jvm_name}}:{{jvm_version}} -Xmx32m -X{{another_jvm_opt}} -jar {{path/to/jar_name.jar}}`

- Նշեք բոլոր հասանելի JVM-ները սուրհանդակային լռելյայն ինդեքսում.:

`cs java --available`

- Թվարկեք համակարգում տեղադրված բոլոր JVM-ները՝ իր սեփական գտնվելու վայրով.:

`cs java --installed`

- Սահմանեք հատուկ JVM որպես միանվագ կանխադրված shell օրինակի համար.:

`cs java --jvm {{jvm_name}}:{{jvm_version}} --env`

- Վերադարձեք փոփոխությունները լռելյայն JVM կարգավորումների համար.:

`eval "$(cs java --disable)"`

- Սահմանեք հատուկ JVM որպես լռելյայն ամբողջ համակարգի համար.:

`cs java --jvm {{jvm_name}}:{{jvm_version}} --setup`

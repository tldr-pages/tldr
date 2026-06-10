# jbang

> Հեշտությամբ ստեղծեք, խմբագրեք և գործարկեք միայն աղբյուրի վրա պարունակվող Java ծրագրեր:.
> Տես նաև՝ `java`:.
> Լրացուցիչ տեղեկություններ. <https://www.jbang.dev/documentation/jbang/latest/cli/jbang.html>:.

- Նախաձեռնեք պարզ Java դաս.:

`jbang init {{path/to/file.java}}`

- Նախաձեռնել Java դասը (օգտակար է սկրիպտավորման համար).:

`jbang init {{[-t|--template]}}={{cli}} {{path/to/file.java}}`

- Օգտագործեք `jshell`՝ REPL խմբագրիչում սկրիպտը և ցանկացած կախվածություն ուսումնասիրելու և օգտագործելու համար.:

`jbang run {{[-i|--interactive]}}`

- Ստեղծեք ժամանակավոր նախագիծ՝ IDE-ում սկրիպտը խմբագրելու համար.:

`jbang edit --open={{codium|code|eclipse|idea|netbeans|gitpod}} {{path/to/script.java}}`

- Գործարկեք Java կոդի հատված (Java 9 և ավելի ուշ).:

`{{echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'}} | jbang -`

- Գործարկել հրամանի տող հավելվածը.:

`jbang {{path/to/file.java}} {{command}} {{arg1 arg2 ...}}`

- Տեղադրեք սկրիպտ օգտատիրոջ `$PATH`-ում.:

`jbang app install --name {{command_name}} {{path/to/script.java}}`

- Տեղադրեք JDK-ի հատուկ տարբերակը, որը կօգտագործվի `jbang`-ով.:

`jbang jdk install {{version}}`

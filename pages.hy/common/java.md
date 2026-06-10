# java

> Java հավելվածի գործարկիչ:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/en/java/javase/25/docs/specs/man/java.html>:.

- Կատարեք Java `.class` ֆայլ, որը պարունակում է հիմնական մեթոդ՝ օգտագործելով միայն դասի անունը.:

`java {{classname}}`

- Կատարեք Java ծրագիր և օգտագործեք լրացուցիչ երրորդ կողմի կամ օգտագործողի կողմից սահմանված դասեր.:

`java -classpath {{path/to/classes1}}:{{path/to/classes2}}:. {{classname}}`

- Կատարեք `.jar` ծրագիր.:

`java -jar {{filename.jar}}`

- Գործարկեք `.jar` ծրագիր՝ վրիպազերծմամբ, որը սպասում է 5005 պորտին միանալուն:

`java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 -jar {{filename.jar}}`

- Ցուցադրել JDK, JRE և HotSpot տարբերակները.:

`java -version`

- Ցուցադրել օգնությունը.:

`java -help`

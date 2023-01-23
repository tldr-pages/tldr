# cs java

> A java és a java-home parancsok a JVM-ek letöltését és telepítését végzik. A java parancs futtatja is őket. További információ: <https://get-coursier.io/docs/cli-java>.

- A java verzió meghívása a coursier parancs segítségével:

`cs java -version`

- Egy adott java verzió meghívása egyéni tulajdonságokkal a coursier segítségével:

`cs java --jvm {{jvm_name}}:{{jvm_version}} -Xmx32m -X{{another_jvm_opt}} -jar {{path/to/jar_name.jar}}`

- Az összes elérhető JVM listázása a coursier alapértelmezett indexében:

`cs java --available`

- Az összes telepített JVM listázása a rendszerben a saját helyével:

`cs java --installed`

- Egy adott JVM beállítása egyszeri "alapértelmezettként" a héjpéldányhoz:

`cs java --jvm {{jvm_name}}:{{jvm_version}} --env`

- Az alapértelmezett JVM-beállítások módosításainak visszavonása:

`eval "$(cs java --disable)"`

- Egy adott JVM beállítása alapértelmezettként az egész rendszerre:

`cs java --jvm {{jvm_name}}:{{jvm_version}} --setup`

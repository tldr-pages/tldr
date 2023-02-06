# jenv

> Parancssori eszköz a "JAVA_HOME" környezeti változó kezelésére. További információ: <https://www.jenv.be/>.

- Java verzió hozzáadása a jEnv:

`jenv add {{path/to/jdk_home}}`

- Az aktuálisan használt JDK verziójának megjelenítése:

`jenv version`

- Az összes kezelt JDK megjelenítése:

`jenv versions`

- A globális JDK verzió beállítása:

`jenv global {{java_version}}`

- Az aktuális shell munkamenet JDK verziójának beállítása:

`jenv shell {{java_version}}`

- A jEnv bővítmény engedélyezése:

`jenv enable-plugin {{plugin_name}}`

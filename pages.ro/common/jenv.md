# jenv

> Instrument de linie de comandă pentru a gestiona variabila de mediu „JAVA_HOME”.
> Mai multe informaţii: <https://www.jenv.be/>

- Adăugați o versiune Java la JenV:

`jenv add {{path/to/jdk_home}}`

- Afișează versiunea curentă JDK utilizată:

`jenv version`

- Afișează toate JDK-urile gestionate:

`jenv versions`

- Setaţi versiunea globală JDK:

`jenv global {{java_version}}`

- Setaţi versiunea JDK pentru sesiunea de shell curentă:

`jenv shell {{java_version}}`

- Activează un plugin JenV:

`jenv enable-plugin {{plugin_name}}`

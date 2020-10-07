# jenv

> Command line tool to manage the "JAVA_HOME" environment variable.
> More information: <https://www.jenv.be/>.

- Add a java version to jEnv:

`jenv add {{path/to/jdk_home}}`

- Display the current JDK version used:

`jenv version`

- Display all managed JDKs:

`jenv versions`

- Set the global JDK version:

`jenv global {{java_version}}`

- Set the JDK version for the current shell session:

`jenv shell {{java_version}}`

- Enable a jEnv plugin:

`jenv enable-plugin {{plugin_name}}`

# jenv

> JEnv is a command line tool to help you forget how to set the "JAVA_HOME" environment variable.
> More information: <https://www.jenv.be/>.

- Add a java version to jEnv:

`jenv add {{path/to/jdk_home}}`

- Display current JDK version used:

`jenv version`

- Display all managed JDKs:

`jenv versions`

- Set the global JDK version:

`jenv global {{java version}}`

- Set JDK version for current shell session:

`jenv shell {{java_version}}`

- To enable a jEnv plugin:

`jenv enable-plugin {{plugin name}}`

#ջենվ

> Կառավարեք `$JAVA_HOME` միջավայրի փոփոխականը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/jenv/jenv>:.

- Ավելացրեք Java տարբերակ jEnv-ին.:

`jenv add {{path/to/jdk_home}}`

- Ցուցադրել օգտագործված JDK-ի ընթացիկ տարբերակը.:

`jenv version`

- Ցուցադրել բոլոր կառավարվող JDK-ները.:

`jenv versions`

- Սահմանեք գլոբալ JDK տարբերակը.:

`jenv global {{java_version}}`

- Սահմանեք JDK տարբերակը ընթացիկ shell նստաշրջանի համար.:

`jenv shell {{java_version}}`

- Միացնել jEnv հավելվածը.:

`jenv enable-plugin {{plugin_name}}`

# cs launch

> Launch an application from the name directly from one or more Maven dependencies without the need of installing it.
> More information: <https://get-coursier.io/docs/cli-launch>.

- Launch an application with the `--version` argument:

`cs launch {{application-name}} -- --version`

- Launch a specific version of `scalafmt-cli` with `-help`argument in it:

`cs launch org.scalameta::scalafmt-cli:2.3.2 -- --help`

- Launch a specific version of an application specifying which is the main file:

`cs launch {{groupId}}:{{artifactId}}:{{artifactVersion}} -M {{main-class-file}}`

- Launch an application specifying custom java options and a jvm memory options:

`cs launch --java-opt -D{{opt-name}}:{{opt-value}} --java-opt -X{{jvm-opt}} {{application-name}}`

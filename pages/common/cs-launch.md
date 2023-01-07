# cs launch

> Launch an application from the name directly from one or more Maven dependencies without the need of installing it.
> More information: <https://get-coursier.io/docs/cli-launch>.

- Launch a specific application with arguments:

`cs launch {{application_name}} -- {{arg1 arg2 ...}}`

- Launch a specific application version with arguments:

`cs launch {{application_name}}:{{application_version}} -- {{arg1 arg2 ...}}`

- Launch a specific version of an application specifying which is the main file:

`cs launch {{group_id}}:{{artifact_id}}:{{artifact_version}} --main-class {{path/to/main_class_file}}`

- Launch an application specifying custom java options and a jvm memory options:

`cs launch --java-opt -D{{opt-name}}:{{opt-value}} --java-opt -X{{jvm-opt}} {{application-name}}`

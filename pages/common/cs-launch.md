# cs launch

> Launch an application from the name directly from one or more Maven dependencies without the need of installing it.
> More information: <https://get-coursier.io/docs/cli-launch>.

- Launch a specific application with arguments:

`cs launch {{application_name}} -- {{argument1 argument2 ...}}`

- Launch a specific application version with arguments:

`cs launch {{application_name}}:{{application_version}} -- {{argument1 argument2 ...}}`

- Launch a specific version of an application specifying which is the main file:

`cs launch {{group_id}}:{{artifact_id}}:{{artifact_version}} --main-class {{path/to/main_class_file}}`

- Launch an application with specific java options and a jvm memory ones:

`cs launch --java-opt {{-Doption_name1:option_value1 -Doption_name2:option_value2 ...}} --java-opt {{-Xjvm_option1 -Xjvm_option2 ...}} {{application_name}}`

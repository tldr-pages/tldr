# cs launch

> 从 Maven 依赖中直接启动应用程序，无需安装。
> 更多信息：<https://get-coursier.io/docs/cli-launch>.

- 启动指定的应用程序并带有参数：

`cs launch {{application_name}} -- {{argument1 argument2 ...}}`

- 启动指定版本的应用程序并带有参数：

`cs launch {{application_name}}:{{application_version}} -- {{argument1 argument2 ...}}`

- 指定主文件来启动应用程序的特定版本：

`cs launch {{group_id}}:{{artifact_id}}:{{artifact_version}} --main-class {{path/to/main_class_file}}`

- 带有特定的 Java 选项和 JVM 内存选项启动应用程序：

`cs launch --java-opt {{-Doption_name1:option_value1 -Doption_name2:option_value2 ...}} --java-opt {{-Xjvm_option1 -Xjvm_option2 ...}} {{application_name}}`

# cs 启动

> 直接从 Maven 依赖中通过名称启动应用程序，无需安装。
> 更多信息：<https://get-coursier.io/docs/cli-launch>。

- 使用参数启动特定应用程序：

`cs launch {{application_name}} -- {{argument1 argument2 ...}}`

- 使用参数启动特定应用程序版本：

`cs launch {{application_name}}:{{application_version}} -- {{argument1 argument2 ...}}`

- 启动特定版本的应用程序，指定主文件：

`cs launch {{group_id}}:{{artifact_id}}:{{artifact_version}} --main-class {{path/to/main_class_file}}`

- 使用特定的 Java 选项和 JVM 内存选项启动应用程序：

`cs launch --java-opt {{-Doption_name1:option_value1 -Doption_name2:option_value2 ...}} --java-opt {{-Xjvm_option1 -Xjvm_option2 ...}} {{application_name}}`
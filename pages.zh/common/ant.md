# ant

> Apache Ant.
> 用于构建、管理基于Java的项目的工具.
> 详见: <https://ant.apache.org>.

- 使用默认的构建文件 `build.xml`构建一个项目:

`ant`

- 使用指定文件构建一个项目:

`ant -f {{buildfile.xml}}`

- Print information on possible targets for this project:

`ant -p`

- 打印调试信息:

`ant -d`

- Execute all targets that do not depend on fail target(s):

`ant -k`

# mvn

> Apache Maven：构建和管理基于Java的项目。
> 更多信息：<https://maven.apache.org>。

- 编译项目：

`mvn compile`

- 编译并以可分发格式打包编译后的代码，例如 `jar`：

`mvn package`

- 编译并打包，跳过单元测试：

`mvn package -DskipTests`

- 将构建的包安装到本地 Maven 仓库。（这也会调用编译和打包命令）：

`mvn install`

- 从目标目录删除构建产物：

`mvn clean`

- 先清理，然后调用打包阶段：

`mvn clean package`

- 清理并使用给定的构建配置文件打包代码：

`mvn clean -P {{profile}} package`

- 运行具有主方法的类：

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{argument1 argument2 ...}}"`
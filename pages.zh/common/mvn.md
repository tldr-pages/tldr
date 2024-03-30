# mvn

> Apache Maven.
> 用于构建和管理基于 Java 的项目的工具。
> 更多信息：<https://maven.apache.org>.

- 编译项目：

`mvn compile`

- 将编译后的代码打包成可分发格式，比如 `jar`：

`mvn package`

- 编译和打包，跳过单元测试：

`mvn package -DskipTests`

- 在本地 maven 存储库中安装构建的包（这也会调用 compile 和 package 命令）：

`mvn install`

- 从目标目录中删除构建工件，通常用来清理之前的编译结果：

`mvn clean`

- 执行清理操作，然后进行编译打包：

`mvn clean package`

- 清理然后使用给定的构建配置文件打包代码：

`mvn clean -P {{构建配置}} package`

- 使用 main 方法运行一个类：

`mvn exec:java -Dexec.mainClass="{{com.example.Main}}" -Dexec.args="{{参数1 参数2}}"`

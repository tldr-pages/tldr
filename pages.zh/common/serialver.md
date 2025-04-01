# serialver

> 返回类的 serialVersionUID。
> 默认情况下不设置安全管理器。
> 更多信息：<https://docs.oracle.com/en/java/javase/20/docs/specs/man/serialver.html>.

- 显示类的 serialVersionUID：

`serialver {{classnames}}`

- 显示以冒号分隔的类和资源列表的 serialVersionUID：

`serialver -classpath {{path/to/directory}} {{classname1:classname2:...}}`

- 使用 Java 应用程序启动器参考页面中的特定选项传递给 Java 虚拟机：

`serialver -Joption {{classnames}}`
# arthas-watch

> 函数执行数据观测。
> 另见 `arthas`, `arthas-trace`.
> 更多信息：<https://arthas.aliyun.com/en/doc/watch.html>.

- 在方法调用后观察，显示第一个参数和返回值，展开嵌套对象的 4 层：

`watch {{class-pattern}} {{method-pattern}} {{'{ params[0],returnObj }'}} -x 4`

- 在方法调用后观测，当第一个参数的值是 5 时，显示第二个参数和返回值，展开嵌套对象的 4 层：

`watch {{class-pattern}} {{method-pattern}} {{'{ params[1],returnObj }'}} {{'"5".equals(params[0])'}} -x 4`

- 在方法返回和异常后观测，显示第二个参数的 count 属性：

`watch {{class-pattern}} {{method-pattern}} {{'{ params[1].count }'}} -e -s`

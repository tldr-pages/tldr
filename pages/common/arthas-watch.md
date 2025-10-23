# arthas-watch

> Method invoke data observation.
> See also: `arthas`, `arthas-trace`.
> More information: <https://arthas.aliyun.com/en/doc/watch.html>.

- Observe the first parameter and return value of method, and expand the nested attributes of the object to 4 levels:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[0],returnObj }}}' -x 4`

- When the value of the first parameter of the method is 5, the second parameter and return value are output, and the object is expanded 4 layers:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[1],returnObj }}}' '{{"5".equals(params[0])}}' -x 4`

- When the method returns or an exception occurs, observe the count property of the second parameter:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[1].count }}}' -e -s`

# arthas-watch

> 메서드 호출 데이터를 관찰.
> 관련 항목: `arthas`, `arthas-trace`.
> 더 많은 정보: <https://arthas.aliyun.com/en/doc/watch.html>.

- 메서드의 첫 번째 매개변수와 반환 값을 관찰하고, 객체의 중첩된 속성을 4단계까지 확장하여 표시:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[0],returnObj }}}' -x 4`

- 메서드의 첫 번째 매개변수 값이 5일 때, 두 번째 매개변수와 반환 값을 출력하고, 객체를 4단계까지 확장:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[1],returnObj }}}' '{{"5".equals(params[0])}}' -x 4`

- 메서드가 반환되거나 예외가 발생할 때, 두 번째 매개변수의 count 속성을 관찰:

`watch {{class-pattern}} {{method-pattern}} '{{{ params[1].count }}}' -e -s`

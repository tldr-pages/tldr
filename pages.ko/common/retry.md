# retry

> 명령이 성공하거나 기준이 충족될 때까지 명령을 반복.
> 더 많은 정보: <https://github.com/minfrin/retry>.

- 명령이 성공할 때까지 재시도:

`retry {{명령}}`

- 명령이 성공할 때까지 n초마다 재시도:

`retry --delay={{n}} {{명령}}`

- n번 시도 후 포기:

`retry --times={{n}} {{명령}}`

# leave

> 출발할 시간이 되었을 때 알림을 설정.
> 알림을 제거하려면 `kill $(pidof leave)` 사용.
> 더 많은 정보: <https://www.freebsd.org/cgi/man.cgi?query=leave>.

- 지정된 시간에 알림 설정:

`leave {{출발_시간}}`

- 정오에 출발할 알림 설정:

`leave {{1200}}`

- 특정 시간 후에 알림 설정:

`leave +{{시간_량}}`

- 4시간 4분 후에 출발할 알림 설정:

`leave +{{0404}}`

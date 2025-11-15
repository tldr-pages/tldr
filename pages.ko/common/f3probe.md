# f3probe

> 위조 플래시 메모리가 있는지 블록 장치(예: 플래시 드라이브 또는 microSD 카드)를 조사.
> 참고: `f3read`, `f3write`, `f3fix`.
> 더 많은 정보: <https://github.com/AltraMayor/f3>.

- 블록 장치 조사:

`sudo f3probe {{경로/대상/블록_장치}}`

- 가능한 최소한의 RAM을 사용:

`sudo f3probe --min-memory {{경로/대상/블록_장치}}`

- 디스크 작업에 걸리는 시간:

`sudo f3probe --time-ops {{경로/대상/블록_장치}}`

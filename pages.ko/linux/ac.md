# ac

> 사용자가 얼마나 오랫동안 연결되어 있었는지에 대한 통계를 출력합니다.
> 더 많은 정보: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- 현재 사용자가 몇 시간 동안 연결되었는지 출력:

`ac`

- 사용자가 몇 시간 동안 연결되었는지 출력:

`ac {{[-p|--individual-totals]}}`

- 특정 사용자가 몇 시간 동안 연결되었는지 출력:

`ac {{[-p|--individual-totals]}} {{사용자명}}`

- 특정 사용자가 하루 동안 몇 시간 연결되었는지 출력(총합 포함):

`ac {{[-d|--daily-totals]}} {{[-p|--individual-totals]}} {{사용자명}}`

- 추가 세부 정보도 표시:

`ac --compatibility`

# rsstail

> RSS 피드를 위한 `tail`.
> 더 많은 정보: <https://manned.org/rsstail>.

- 주어진 URL의 피드를 표시하고 새 항목이 아래에 나타날 때까지 대기:

`rsstail -u {{URL}}`

- 피드를 역순으로 표시 (최신 항목이 아래에 위치):

`rsstail -r -u {{URL}}`

- 발행 날짜와 링크 포함:

`rsstail -pl -u {{URL}}`

- 업데이트 간격 설정:

`rsstail -u {{URL}} -i {{초_간격}}`

- 피드를 표시하고 종료:

`rsstail -1 -u {{URL}}`

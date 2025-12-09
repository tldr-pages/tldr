# pw-top

> 실시간으로 PipeWire 노드 및 장치 통계를 확인.
> 같이 보기: `pipewire`, `pw-dump`, `pw-cli`, `pw-profiler`.
> 더 많은 정보: <https://docs.pipewire.org/page_man_pw-top_1.html>.

- PipeWire 노드와 장치의 대화형 뷰 표시:

`pw-top`

- 원격 인스턴스 모니터링:

`pw-top --remote {{원격_이름}}`

- 대화형 모드 대신 주기적으로 정보 출력:

`pw-top --batch-mode`

- 특정 횟수만큼 주기적으로 정보 출력:

`pw-top --batch-mode --iterations {{3}}`

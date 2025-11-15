# pw-dump

> PipeWire의 현재 상태를 노드, 장치, 모듈, 포트 및 기타 객체 정보를 포함하여 JSON 형식으로 덤프.
> 같이 보기: `pw-mon`.
> 더 많은 정보: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- 기본 PipeWire 인스턴스의 현재 상태를 JSON 형식으로 출력:

`pw-dump`

- 현재 상태를 덤프하고, 변경 사항을 [m]onitoring하여 다시 출력:

`pw-dump --monitor`

- 원격 인스턴스의 현재 상태를 [r]emote하여 파일에 덤프:

`pw-dump --remote {{원격_이름}} > {{경로/대상/덤프_파일.json}}`

- [C]olor 설정 구성:

`pw-dump --color {{never|always|auto}}`

- 도움말 표시:

`pw-dump --help`

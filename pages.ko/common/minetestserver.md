# minetestserver

> 멀티플레이어 무한 세계 블록 샌드박스 서버.
> 그래픽 클라이언트인 `minetest`도 참고하세요.
> 더 많은 정보: <https://wiki.minetest.org/Setting_up_a_server>.

- 서버 시작:

`minetestserver`

- 사용 가능한 세계 목록 나열:

`minetestserver --world list`

- 지정된 세계 로드:

`minetestserver --world {{세계_이름}}`

- 사용 가능한 게임 ID 목록 나열:

`minetestserver --gameid list`

- 지정된 게임 사용:

`minetestserver --gameid {{게임_ID}}`

- 특정 포트로 수신 대기:

`minetestserver --port {{34567}}`

- 다른 데이터 백엔드로 마이그레이션:

`minetestserver --migrate {{sqlite3|leveldb|redis}}`

- 서버 시작 후 대화형 터미널 시작:

`minetestserver --terminal`

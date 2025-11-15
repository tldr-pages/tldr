# openttd

> Microprose 게임 "Transport Tycoon Deluxe"의 오픈 소스 클론.
> 더 많은 정보: <https://wiki.openttd.org/en/Manual/Command%20line>.

- 새 게임 시작:

`openttd -g`

- 시작 시 저장된 게임 불러오기:

`openttd -g {{경로/대상/파일}}`

- 지정된 창 해상도로 시작:

`openttd -r {{1920x1080}}`

- 사용자 정의 구성 파일로 시작:

`openttd -c {{경로/대상/파일}}`

- 선택된 비디오, 사운드, 음악 드라이버로 시작:

`openttd -v {{비디오_드라이버}} -s {{사운드_드라이버}} -m {{음악_드라이버}}`

- 백그라운드에서 포크된 전용 서버 시작:

`openttd -f -D {{호스트}}:{{포트}}`

- 비밀번호로 서버 참가:

`openttd -n {{호스트}}:{{포트}}#{{플레이어_이름}} -p {{비밀번호}}`

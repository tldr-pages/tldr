# eventcreate

> 이벤트 로그에 사용자 정의 항목을 생성.
> 이벤트 ID는 1에서 1000 사이의 숫자여야 함.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/eventcreate>.

- 로그에 주어진 ID(1-1000)로 새로운 이벤트 생성:

`eventcreate /t {{성공|오류|경고|정보}} /id {{id}} /d "{{메시지}}"`

- 특정 이벤트 로그에 이벤트 생성:

`eventcreate /l {{로그_이름}} /t {{유형}} /id {{id}} /d "{{메시지}}"`

- 특정 소스로 이벤트 생성:

`eventcreate /so {{소스_이름}} /t {{유형}} /id {{id}} /d "{{메시지}}"`

- 원격 컴퓨터의 이벤트 로그에 이벤트 생성:

`eventcreate /s {{호스트명}} /u {{사용자명}} /p {{비밀번호}} /t {{유형}} /id {{id}} /d "{{메시지}}"`

# w32tm

> w32time 시간 동기화 서비스를 쿼리하고 제어합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings>.

- 시간 동기화의 현재 상태 표시:

`w32tm /query /status /verbose`

- 시간 서버에 대한 시간 오프셋 그래프 표시:

`w32tm /stripchart /computer:{{시간_서버}}`

- 시간 서버에서 NTP 응답 표시:

`w32tm /stripchart /packetinfo /samples:1 /computer:{{시간_서버}}`

- 현재 사용되는 시간 서버의 상태 표시:

`w32tm /query /peers`

- w32time 서비스의 구성 표시 (관리자 권한으로 실행):

`w32tm /query /configuration`

- 강제 시간 재동기화를 즉시 실행 (관리자 권한으로 실행):

`w32tm /resync /force`

- w32time 디버그 로그를 파일에 쓰기 (관리자 권한으로 실행):

`w32tm /debug /enable /file:{{경로\대상\debug.log}} /size:{{10000000}} /entries:{{0-300}}`

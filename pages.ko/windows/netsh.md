# netsh

> Windows 네트워크 설정을 관리.
> `wlan`과 같은 일부 하위 명령은 각각 별도의 사용 문서를 제공.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/netsh>.

- helper Dynamic Link Library (DLL) 추가:

`netsh add helper {{경로\대상\파일.dll}}`

- 로드된 모든 helper DLL 목록 표시:

`netsh show helper`

- helper DLL 삭제:

`netsh delete helper {{경로\대상\파일.dll}}`

- 네트워크 구성 설정을 파일로 내보내기:

`netsh dump > {{경로\대상\출력_파일.txt}}`

- 추적에 사용할 수 있는 네트워크 인터페이스 목록 표시:

`netsh trace show interfaces`

- 쉘 종료:

`exit`

- 도움말 표시:

`netsh help`

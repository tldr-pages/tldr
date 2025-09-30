# net

> 네트워크 관련 설정을 보고 수정하는 시스템 유틸리티입니다.
> 더 많은 정보: <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>.

- 동기적으로 Windows 서비스 시작 또는 중지:

`net {{start|stop}} {{서비스}}`

- 현재 콘솔에서 SMB 공유 가능한지 확인:

`net use {{\\smb_shared_folder}} /USER:{{사용자명}}`

- 현재 SMB로 공유되는 폴더 표시:

`net share`

- SMB 공유를 사용하는 사용자 표시 (관리자 권한 콘솔에서 실행):

`net session`

- 로컬 보안 그룹의 사용자 표시:

`net localgroup "{{Administrators}}"`

- 로컬 보안 그룹에 사용자 추가 (관리자 권한 콘솔에서 실행):

`net localgroup "{{Administrators}}" {{사용자명}} /add`

- 하위 명령에 대한 도움말 표시:

`net help {{하위명령}}`

- 도움말 표시:

`net help`

# cleanmgr

> 컴퓨터 하드 디스크의 불필요한 파일을 정리.
> 최신 Windows 버전에서는 더 이상 권장되지 않고 "Storage Sense"로 대체됨.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cleanmgr>.

- 지정한 드라이브의 디스크 정리 실행:

`cleanmgr /d {{C}}`

- 모든 정리 항목을 기본 선택한 상태로 디스크 정리 실행:

`cleanmgr /d {{C}} /lowdisk`

- 사용자 확인 없이 모든 정리 작업 자동 수행:

`cleanmgr /d {{C}} /verylowdisk`

- 정리할 항목을 설정하고 지정한 프로필에 저장:

`cleanmgr /sageset:{{프로파일_번호}}`

- 이전에 저장한 프로필을 사용하여 디스크 정리 실행:

`cleanmgr /sagerun:{{프로파일_번호}}`

- Windows 업그레이드 후 남은 파일 정리:

`cleanmgr /autoclean`

- 이전 Windows 설치 파일 정리:

`cleanmgr /setup`

- 도움말 표시:

`cleanmgr /?`

# mount

> 네트워크 파일 시스템(NFS) 네트워크 공유를 마운트합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/mount>.

- 공유를 "Z" 드라이브 문자에 마운트:

`mount \\{{컴퓨터명}}\{{공유명}} {{Z:}}`

- 다음 사용 가능한 드라이브 문자에 공유 마운트:

`mount \\{{컴퓨터명}}\{{공유명}} *`

- 읽기 시간 제한을 초 단위로 설정 (기본값은 0.8, 0.9 또는 1에서 60까지 가능):

`mount -o timeout={{seconds}} \\{{컴퓨터명}}\{{공유명}} {{Z:}}`

- 공유를 마운트하고 실패 시 최대 10번 재시도:

`mount -o retry=10 \\{{컴퓨터명}}\{{공유명}} {{Z:}}`

- 대소문자 구분 강제 하고 공유 마운트:

`mount -o casesensitive \\{{컴퓨터명}}\{{공유명}} {{Z:}}`

- 익명 사용자로 공유 마운트:

`mount -o anon \\{{컴퓨터명}}\{{공유명}} {{Z:}}`

- 특정 마운트 유형을 사용하여 공유 마운트:

`mount -o mtype={{soft|hard}} \\{{컴퓨터명}}\{{공유명}} {{Z:}}`

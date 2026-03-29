# runas

> 다른 사용자로 프로그램을 실행.
> 더 많은 정보: <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11)>.

- 로컬 Administrator 사용자로 프로그램 실행:

`runas /user:.\Administrator "{{명령어}}"`

- 특정 사용자로 프로그램 실행:

`runas /user:{{도메인\사용자명} "{{명령어}}"`

- 사용자 프로필을 로드하지 ㅇ낳고 실행:

`runas /noprofile /user:{{도메인\사용자명}} "{{명령어}}"`

- 다른 사용자로 명령 프롬프트 실행:

`runas /user:{{도메인\사용자명}} cmd`

- 현재 사용자 환경 변수를 유지하면서 특정 사용자로 Notepad 실행 (따옴표 이스케이프 포함 파일 열기):

`runas /env /user:{{도메인\사용자명}} "notepad \"{{C:\경로\대상\파일.txt}}\""`

- 특정 사용자로 Active Directory Users and Computers 실행:

`runas /env /user:{{도메인\사용자명}} "mmc %windir%\system32\dsa.msc"`

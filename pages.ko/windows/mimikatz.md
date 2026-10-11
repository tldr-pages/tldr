# mimikatz

> Windows 자격 증명과 상호작용하고, 자격 증명 덤프, 토큰 조작 등의 작업을 수행.
> 관리자 권한이 필요하며 일반적으로 Windows에서 실행됨.
> 더 많은 정보: <https://github.com/gentilkiwi/mimikatz>.

- mimikatz를 대화형 모드로 실행:

`mimikatz`

- 디버그 권한 활성화(대부분의 작업에 필요):

`mimikatz "privilege::debug"`

- 메모리에서 평문 비밀번호, NTLM 해시 및 Kerberos 티켓 덤프:

`mimikatz "sekurlsa::logonpasswords"`

- 지정한 NTLM 해시로 Pass-the-Hash를 수행하고 명령 실행:

`mimikatz "sekurlsa::pth /user:{{사용자명}} /domain:{{도메인명}} /ntlm:{{해시}} /run:{{명령어}}"`

- 로컬 SAM 데이터베이스의 해시 덤프:

`mimikatz "lsadump::sam"`

- Kerberos 티켓을 추출하여 파일로 내보내기:

`mimikatz "kerberos::list /export"`

- [대화형] mimikatz 종료:

`exit`

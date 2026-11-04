# mimikatz process

> 프로세스 권한과 토큰을 관리.
> 더 많은 정보: <https://github.com/gentilkiwi/mimikatz>.

- 프로세스와 해당 토큰 목록 표시:

`mimikatz "process::list"`

- Mimikatz를 SYSTEM 권한의 프로세스로 승격:

`mimikatz "process::token /user:NT AUTHORITY\SYSTEM"`

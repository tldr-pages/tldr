# mimikatz crypto

> Windows 암호화 서비스와 인증서를 관리하며, 내보내기 불가로 표시된 인증서와 키도 목록을 조회하거나 내보낼 수 있음.
> 일반적으로 높은 권한이 필요하며, 특히 시스템 키에 접근할 때 관리자 권한이 필요.
> 더 많은 정보: <https://github.com/gentilkiwi/mimikatz>.

- 암호화 프로바이더 목록 표시:

`mimikatz "crypto::providers"`

- 암호화 프로바이더의 키 목록 표시:

`mimikatz "crypto::capi"`

- 인증서와 키 내보내기:

`mimikatz "crypto::certificates /export"`

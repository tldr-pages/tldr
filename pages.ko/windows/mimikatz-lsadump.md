# mimikatz lsadump

> Windows 로컬 보안 기관(LSA)에서 비밀 정보를 추출.
> SYSTEM 권한이 필요.
> 더 많은 정보: <https://github.com/gentilkiwi/mimikatz>.

- SAM 해시 덤프:

`mimikatz "lsadump::sam"`

- SECURITY 레지스트리 하이브에서 비밀 정보 추출:

`mimikatz "lsadump::secrets"`

- 캐시된 도메인 자격 증명 덤프:

`mimikatz "lsadump::cache"`

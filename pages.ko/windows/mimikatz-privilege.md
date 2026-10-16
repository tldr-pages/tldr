# mimikatz privilege

> Mimikatz 작업에 필요한 권한을 관리.
> 더 많은 정보: <https://github.com/gentilkiwi/mimikatz>.

- 디버그 권한 활성화(여러 모듈에서 필요):

`mimikatz "privilege::debug"`

- 현재 권한 상태 확인:

`mimikatz "privilege::whoami"`

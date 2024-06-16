# yaourt

> Arch Linux 유틸리티로 Arch User Repository(AUR)에서 패키지를 빌드합니다.
> 더 많은 정보: <https://linuxcommandlibrary.com/man/yaourt>.

- 모든 패키지 동기화 및 업데이트 (AUR 포함):

`yaourt -Syua`

- 새 패키지 설치 (AUR 포함):

`yaourt -S {{패키지}}`

- 패키지와 그 의존성 제거 (AUR 패키지 포함):

`yaourt -Rs {{패키지}}`

- 키워드로 패키지 데이터베이스 검색 (AUR 포함):

`yaourt -Ss {{검색어}}`

- 설치된 패키지, 버전 및 저장소 나열 (AUR 패키지는 'local' 저장소로 나열됨):

`yaourt -Q`

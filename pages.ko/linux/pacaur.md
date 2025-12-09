# pacaur

> Arch User Repository에서 패키지를 빌드하고 설치하기 위한 Arch Linux 유틸리티.
> 더 많은 정보: <https://github.com/rmarquis/pacaur#name>.

- 모든 패키지를 동기화하고 업데이트 (AUR 포함):

`pacaur -Syu`

- AUR 패키지만 동기화하고 업데이트:

`pacaur -Syua`

- 새 패키지 설치 (AUR 포함):

`pacaur -S {{패키지}}`

- 특정 패키지 및 의존성 제거 (AUR 패키지 포함):

`pacaur -Rs {{패키지}}`

- 패키지 데이터베이스에서 키워드 검색 (AUR 포함):

`pacaur -Ss {{키워드}}`

- 현재 설치된 모든 패키지 나열 (AUR 패키지 포함):

`pacaur -Qs`

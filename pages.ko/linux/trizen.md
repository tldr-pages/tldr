# trizen

> Arch Linux에서 Arch User Repository (AUR)로부터 패키지를 빌드하는 도구.
> 더 많은 정보: <https://github.com/trizen/trizen/blob/master/TRIZEN.md>.

- 모든 AUR 패키지를 동기화하고 업데이트:

`trizen -Syua`

- 새 패키지 설치:

`trizen -S {{패키지}}`

- 패키지 및 의존성 제거:

`trizen -Rs {{패키지}}`

- 패키지 데이터베이스에서 키워드 검색:

`trizen -Ss {{키워드}}`

- 패키지 정보 표시:

`trizen -Si {{패키지}}`

- 설치된 패키지 및 버전 나열:

`trizen -Qe`

# auracle

> Arch Linux의 사용자 저장소(AUR)와 상호작용하기 위한 명령줄 도구.
> 더 많은 정보: <https://github.com/falconindy/auracle/blob/master/man/auracle.1.pod>.

- 정규 표현식과 일치하는 AUR 패키지 표시:

`auracle search '{{정규_표현식}}'`

- 하나 이상의 AUR 패키지에 대한 정보 표시:

`auracle info {{패키지1 패키지2 ...}}`

- 하나 이상의 AUR 패키지에 대한 `PKGBUILD` 파일(빌드 정보) 표시:

`auracle show {{패키지1 패키지2 ...}}`

- 설치된 AUR 패키지의 업데이트 표시:

`auracle outdated`

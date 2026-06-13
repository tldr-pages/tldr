# ncu

> 패키지 종속성의 최신 버전을 찾고, 로컬 또는 전역적으로 오래된 npm 패키지를 확인.
> `ncu`는 `package.json`의 종속성 버전만 업데이트합니다. 새 버전을 설치하려면 이후에 `npm install`을 실행하세요.
> 더 많은 정보: <https://github.com/raineorshine/npm-check-updates>.

- 현재 디렉토리의 오래된 종속성 나열:

`ncu`

- 전역 `npm` 패키지 중 오래된 항목 나열:

`ncu --global`

- 현재 디렉토리의 모든 종속성 업그레이드:

`ncu --upgrade`

- 현재 디렉토리의 종속성을 대화형으로 업그레이드:

`ncu --interactive`

- 가장 높은 마이너 버전까지의 오래된 종속성 나열:

`ncu --target {{마이너_버전}}`

- 키워드 또는 정규 표현식과 일치하는 오래된 종속성 나열:

`ncu --filter {{키워드|/정규식/}}`

- 특정 섹션의 오래된 종속성만 나열:

`ncu --dep {{dev|optional|peer|prod|packageManager}}`

- 도움말 표시:

`ncu --help`

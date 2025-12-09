# eslint

> JavaScript 및 JSX용 플러그형 린팅 유틸리티.
> 더 많은 정보: <https://eslint.org/docs/latest/use/command-line-interface>.

- ESLint 구성파일 생성:

`eslint --init`

- 하나 이상의 파일 린팅:

`eslint {{경로/대상/파일1.js 경로/대상/파일2.js ...}}`

- 린트 문제 수정:

`eslint --fix`

- 지정된 구성 파일을 사용하는 린트:

`eslint -c {{경로/대상/구성_파일}} {{경로/대상/파일1.js 경로/대상/파일2.js}}`

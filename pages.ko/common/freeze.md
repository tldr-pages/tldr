# freeze

> 코드 및 터미널 출력 이미지를 생성하는 도구.
> 지원 형식은 PNG, SVG, WebP입니다.
> 관련 항목: `silicon`.
> 더 많은 정보: <https://github.com/charmbracelet/freeze#flags>.

- 파일 기반으로 코드 이미지 생성:

`freeze {{경로/대상/파일}}`

- 출력 경로 지정:

`freeze {{경로/대상/파일}} {{[-o|--output]}} {{경로/대상/출력_이미지.png}}`

- 터미널 출력 이미지를 생성:

`freeze {{[-x|--execute]}} {{명령어}}`

- 출력 이미지를 대화형으로 사용자 지정:

`freeze {{경로/대상/파일}} {{[-i|--interactive]}}`

- 문법 강조 테마 선택:

`freeze {{경로/대상/파일}} {{[-t|--theme]}} {{dracula}}`

- 기본 설정 템플릿 사용:

`freeze {{경로/대상/파일}} {{[-c|--config]}} {{base|full|user}}`

- 특정 줄 범위만 캡처:

`freeze {{경로/대상/파일}} --lines {{시작}},{{끝}}`

- 줄 번호 표시:

`freeze {{경로/대상/파일}} --show-line-numbers`

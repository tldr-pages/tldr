# typst

> Typst 파일을 PDF로 컴파일.
> 참고: 출력 위치 지정은 선택 사항입니다.
> 더 많은 정보: <https://github.com/typst/typst>.

- 주어진 디렉터리에 템플릿(예: `@preview/charged-ieee`)을 사용하여 새로운 Typst 프로젝트 초기화:

`typst init "{{템플릿}}" {{경로/대상/폴더}}`

- Typst 파일 컴파일:

`typst compile {{경로/대상/소스.typ}} {{경로/대상/출력.pdf}}`

- Typst 파일을 감시하고 변경 시 다시 컴파일:

`typst watch {{경로/대상/소스.typ}} {{경로/대상/출력.pdf}}`

- 시스템 및 주어진 디렉토리에서 발견 가능한 모든 글꼴 나열:

`typst --font-path {{경로/대상/폰트_디렉토리}} fonts`

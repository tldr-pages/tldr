# plantuml

> 일반 텍스트 언어로 UML 다이어그램을 작성하고 다양한 형식으로 렌더링.
> 더 많은 정보: <https://plantuml.com/en/command-line>.

- 다이어그램을 기본 형식(PNG)으로 렌더링:

`plantuml {{다이어그램1.puml}} {{다이어그램2.puml}}`

- 주어진 형식(예: `png`, `pdf`, `svg`, `txt`)으로 다이어그램 렌더링:

`plantuml -t {{형식}} {{다이어그램.puml}}`

- 디렉토리의 모든 다이어그램 렌더링:

`plantuml {{경로/대상/다이어그램}}`

- 출력 디렉토리에 다이어그램 렌더링:

`plantuml -o {{경로/대상/출력}} {{다이어그램.puml}}`

- 다이어그램의 소스 코드를 저장하지 않고 렌더링 (참고: `-nometadata` 옵션이 지정되지 않으면 기본적으로 저장됨):

`plantuml -nometadata {{다이어그램.png}} > {{다이어그램.puml}}`

- `plantuml` 다이어그램의 메타데이터에서 소스 코드 가져오기:

`plantuml -metadata {{다이어그램.png}} > {{다이어그램.puml}}`

- 구성 파일을 사용하여 다이어그램 렌더링:

`plantuml -config {{구성.cfg}} {{다이어그램.puml}}`

- 도움말 표시:

`plantuml -help`

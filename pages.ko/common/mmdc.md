# mmdc

> 도메인 특화 언어를 사용하는 다이어그램 생성 도구인 mermaid의 CLI.
> mermaid 정의 파일을 입력으로 받아 SVG, PNG 또는 PDF 파일을 출력으로 생성.
> 더 많은 정보: <https://mermaid-js.github.io/mermaid/>.

- 파일을 지정된 형식으로 변환 (파일 확장자에 따라 자동 결정):

`mmdc --input {{입력.mmd}} --output {{출력.svg}}`

- 차트의 테마 지정:

`mmdc --input {{입력.mmd}} --output {{출력.svg}} --theme {{forest|dark|neutral|default}}`

- 차트의 배경색 지정 (예: `lime`, `"#D8064F"` 또는 `transparent`):

`mmdc --input {{입력.mmd}} --output {{출력.svg}} --backgroundColor {{색상}}`

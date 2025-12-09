# quarto

> Pandoc 기반의 오픈 소스 과학 및 기술 출판 시스템.
> 더 많은 정보: <https://quarto.org/docs/reference/projects/options.html>.

- 새 프로젝트 생성:

`quarto create-project {{경로/대상/폴더}} --type {{book|default|website}}`

- 새 블로그 웹사이트 생성:

`quarto create-project {{경로/대상/폴더}} --type {{website}} --template {{blog}}`

- 입력 파일을 다양한 형식으로 렌더링:

`quarto render {{경로/대상/파일.[qmd|rmd|ipynb]}} --to {{html|pdf|docx}}`

- 문서나 웹사이트를 렌더링하고 미리보기:

`quarto preview {{경로/대상/폴더|경로/대상/파일}}`

- 문서나 프로젝트를 Quarto Pub, Github Pages, RStudio Connect 또는 Netlify에 게시:

`quarto publish {{quarto-pub|gh-pages|connect|netlify}}`

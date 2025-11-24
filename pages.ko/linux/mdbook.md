# mdbook

> Markdown 파일을 작성하여 온라인 책을 만듭니다.
> 더 많은 정보: <https://rust-lang.github.io/mdBook/cli/index.html>.

- 현재 디렉토리에 mdbook 프로젝트 생성:

`mdbook init`

- 특정 디렉토리에 mdbook 프로젝트 생성:

`mdbook init {{경로/대상/폴더}}`

- 생성된 책이 있는 디렉토리 정리:

`mdbook clean`

- <http://localhost:3000>에서 책 제공, 파일 변경 시 자동 빌드:

`mdbook serve`

- Markdown 파일 세트를 감시하고 파일이 변경될 때 자동으로 빌드:

`mdbook watch`

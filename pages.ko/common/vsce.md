# vsce

> Visual Studio Code 확장 관리자.
> 더 많은 정보: <https://github.com/microsoft/vscode-vsce>.

- 특정 게시자가 만든 모든 확장 나열:

`vsce list {{게시자}}`

- 확장을 주 버전, 부 버전 또는 패치 버전으로 게시:

`vsce publish {{major|minor|patch}}`

- 확장 취소 게시:

`vsce unpublish {{확장_ID}}`

- 현재 작업 디렉토리를 `.vsix` 파일로 패키징:

`vsce package`

- 확장과 관련된 메타데이터 표시:

`vsce show {{확장_ID}}`

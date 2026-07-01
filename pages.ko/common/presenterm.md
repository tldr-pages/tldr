# presenterm

> 마크다운 프레젠테이션을 터미널에서 슬라이드 형태로 표시하는 도구.
> 더 많은 정보: <https://mfontanini.github.io/presenterm/>.

- 프레젠테이션 표시:

`presenterm {{경로/대상/슬라이드.md}}`

- 지정한 테마로 프레젠테이션 표시:

`presenterm --theme {{dark|light|tokyonight-storm|...}} {{경로/대상/슬라이드.md}}`

- 사용 가능한 모든 테마 목록 표시:

`presenterm --list-themes`

- 프레젠테이션을 PDF로 내보내기:

`presenterm --export-pdf --output {{경로/대상/출력파일.pdf}} {{경로/대상/슬라이드.md}}`

- 코드 스니펫 실행 기능을 활성화하여 프레젠테이션 표시:

`presenterm --enable-snippet-execution {{경로/대상/슬라이드.md}}`

- 프레젠테이션 내용이 터미널 화면을 넘치지 않는지 검증:

`presenterm --validate-overflows {{경로/대상/슬라이드.md}}`

# rich

> 터미널에서 화려한 출력을 위한 도구 모음.
> 더 많은 정보: <https://github.com/Textualize/rich-cli>.

- 파일을 구문 강조와 함께 표시:

`rich {{경로/대상/파일.py}}`

- 줄 번호 및 들여쓰기 가이드 추가:

`rich {{경로/대상/파일.py}} --line-number --guides`

- 테마 적용:

`rich {{경로/대상/파일.py}} --theme {{monokai}}`

- 파일을 인터랙티브 페이지로 표시:

`rich {{경로/대상/파일.py}} --pager`

- URL에서 내용 표시:

`rich {{https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md}} --markdown --pager`

- 파일을 HTML로 내보내기:

`rich {{경로/대상/파일.md}} --export-html {{경로/대상/파일.html}}`

- 서식 태그, 사용자 정의 정렬 및 줄 너비를 사용하여 텍스트 표시:

`rich --print "{{Hello [green on black]Stylized[/green on black] [bold]World[/bold]}}" --{{left|center|right}} --width {{10}}`

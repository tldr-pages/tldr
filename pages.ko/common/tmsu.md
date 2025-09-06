# tmsu

> 파일에 태그를 붙이는 간단한 명령줄 도구.
> 더 많은 정보: <https://tmsu.org>.

- 특정 파일에 여러 태그 추가:

`tmsu tag {{경로/대상/파일.mp3}} {{music}} {{big-jazz}} {{mp3}}`

- 여러 파일에 태그 추가:

`tmsu tag --tags "{{music mp3}}" {{*.mp3}}`

- 지정된 파일의 태그 나열:

`tmsu tags {{*.mp3}}`

- 지정된 태그가 있는 파일 나열:

`tmsu files {{big-jazz}} {{music}}`

- 논리 표현식과 일치하는 태그가 있는 파일 나열:

`tmsu files "{{(year >= 1990 and year <= 2000)}} and {{grunge}}"`

- 기존 디렉토리에 tmsu 가상 파일 시스템 마운트:

`tmsu mount {{경로/대상/폴더}}`

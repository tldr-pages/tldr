# vhs

> 테이프 파일에서 터미널 GIF 생성.
> 더 많은 정보: <https://github.com/charmbracelet/vhs>.

- 테이프 파일 생성 (편집기를 사용하여 테이프 파일에 명령 추가):

`vhs new {{경로/대상/파일.tape}}`

- 테이프 파일에 입력 기록 (완료 후 셸을 종료하여 테이프 생성):

`vhs record > {{경로/대상/파일.tape}}`

- 특정 셸을 사용하여 테이프 파일에 입력 기록:

`vhs record --shell {{셸}} > {{경로/대상/파일.tape}}`

- 테이프 파일의 구문 검증:

`vhs validate {{경로/대상/파일.tape}}`

- 테이프 파일에서 GIF 생성:

`vhs < {{경로/대상/파일.tape}}`

- <https://vhs.charm.sh>에 GIF 게시 및 공유 가능한 URL 얻기:

`vhs publish {{경로/대상/파일.gif}}`

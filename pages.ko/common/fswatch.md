# fswatch

> 크로스 플랫폼 파일 변경 모니터.
> 더 많은 정보: <https://emcrisostomo.github.io/fswatch>.

- 파일 생성, 업데이트 또는 삭제 시 Bash 명령을 실행:

`fswatch {{경로/대상/파일}} | xargs {{[-n|--max-args]}} 1 {{bash_명령어}}`

- 하나 이상의 파일 또는 디렉터리를 감시:

`fswatch {{경로/대상/파일}} {{경로/대상/디렉토리}} {{path/to/another_directory/**/*.js}} | xargs {{[-n|--max-args]}} 1 {{bash_명령어}}`

- 변경된 파일의 절대 경로를 출력:

`fswatch {{경로/대상/디렉토리}} | xargs {{[-n|--max-args]}} 1 -I _ echo _`

- 이벤트 유형 별로 필터링:

`fswatch --event {{Updated|Deleted|Created}} {{경로/대상/디렉토리}} | xargs {{[-n|--max-args]}} 1 {{bash_명령어}}`

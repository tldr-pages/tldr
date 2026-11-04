# unhash

> 해시 테이블에 저장된 실행 파일 위치 등 항목 제거.
> 관련 항목: `hash`.
> 더 많은 정보: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- 해시 테이블에서 지정한 명령 제거:

`unhash {{명령어}}`

- 일반 별칭([a]liases)의 해시 항목 제거:

`unhash -a {{별칭}}`

- 접미사 별칭([s]uffix aliases)의 해시 항목 제거:

`unhash -s {{별칭}}`

- 셸 함수([f]unctions)의 해시 항목 제거:

`unhash -f {{함수}}`

- 디렉터리([d]irectories)의 해시 항목 제거:

`unhash -d {{디렉터리}}`

- 패턴과 일치하는([m]atches) 모든 함수의 해시 항목 제거:

`unhash -f -m "{{패턴}}"`

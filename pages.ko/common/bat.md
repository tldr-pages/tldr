# bat

> 파일들을 출력하고 연결. 구문 강조와 Git 통합을 가진`cat`클론.
> 더 많은 정보: <https://github.com/sharkdp/bat>.

- 파일 내용을 표준 출력으로 출력:

`bat {{file}}`

- 여러 파일을 대상 파일에 연결:

`bat {{file1}} {{file2}} > {{target_file}}`

- 대상 파일에 여러 파일을 추가:

`bat {{file1}} {{file2}} >> {{target_file}}`

- 모든 출력 라인 번호 매기기:

`bat -n {{file}}`

- json파일 구문 강조:

`bat --language json {{file.json}}`

- 지원되는 모든 언어 표시:

`bat --list-languages`

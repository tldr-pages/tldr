# git archive

> 트리에서 파일의 아카이브를 생성합니다.
> 더 많은 정보: <https://git-scm.com/docs/git-archive>.

- 현재 HEAD의 내용을 tar 아카이브로 생성하고 `stdout`에 출력:

`git archive {{[-v|--verbose]}} HEAD`

- Zip 형식을 사용하고 진행 상황을 자세히 보고:

`git archive {{[-v|--verbose]}} --format zip HEAD`

- Zip 아카이브를 특정 파일로 출력:

`git archive {{[-v|--verbose]}} {{[-o|--output]}} {{경로/대상/파일.zip}} HEAD`

- 특정 브랜치의 최신 커밋 내용을 tar 아카이브로 생성:

`git archive {{[-o|--output]}} {{경로/대상/파일.tar}} {{branch_name}}`

- 특정 디렉토리의 내용을 사용:

`git archive {{[-o|--output]}} {{경로/대상/파일.tar}} HEAD:{{경로/대상/폴더}}`

- 각 파일에 경로를 추가하여 특정 디렉토리에 아카이브:

`git archive {{[-o|--output]}} {{경로/대상/파일.tar}} --prefix {{경로/대상/폴더}}/ HEAD`

# typos

> 소스 코드의 맞춤법 오류를 찾고 수정.
> 더 많은 정보: <https://github.com/crate-ci/typos/blob/master/docs/reference.md>.

- 파일 또는 디렉터리에서 맞춤법 오류 검사:

`typos {{경로/대상/파일_또는_디렉터리}}`

- 파일 또는 디렉터리에서 오타를 자동으로 수정:

`typos {{[-w|--write-changes]}} {{경로/대상/파일_또는_디렉터리}}`

- 변경 사항을 적용하기 전에 미리보기:

`typos --diff {{경로/대상/파일_또는_디렉터리}}`

- 숨김 파일 및 디렉터리를 포함하여 검사:

`typos --hidden {{경로/대상/파일_또는_디렉터리}}`

- 지정한 glob 패턴과 일치하는 파일을 제외하고 검사:

`typos --exclude {{패턴}} {{경로/대상/파일_또는_디렉터리}}`

- 현재 설정을 지정한 파일에 출력:

`typos --dump-config {{경로/대상/typos.toml}}`

- 지원되는 모든 파일 유형 목록 표시:

`typos --type-list`

- 지정한 출력 형식으로 맞춤법 오류 표시 (기본값: `long`):

`typos --format {{brief|long|json|...}} {{경로/대상/파일_또는_디렉터리}}`

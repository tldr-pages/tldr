# rector

> PHP 5.3+ 코드를 업데이트하고 리팩토링하는 자동화 도구.
> 더 많은 정보: <https://github.com/rectorphp/rector>.

- 특정 디렉토리 처리:

`rector process {{경로/대상/폴더}}`

- 변경 사항을 적용하지 않고 디렉토리 처리 (드라이 런):

`rector process {{경로/대상/폴더}} --dry-run`

- 디렉토리를 처리하고 코딩 표준 적용:

`rector process {{경로/대상/폴더}} --with-style`

- 사용 가능한 레벨 목록 표시:

`rector levels`

- 특정 레벨로 디렉토리 처리:

`rector process {{경로/대상/폴더}} --level {{레벨_이름}}`

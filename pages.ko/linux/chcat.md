# chcat

> 파일의 SELinux 보안 카테고리 변경.
> 카테고리는 MCS (Multi-Category Security) 기반의 추가 접근 제어 수준 제공.
> 관련 항목: `chcon`, `semanage`.
> 더 많은 정보: <https://manned.org/chcat>.

- 사용 가능한 모든 카테고리 목록 표시:

`sudo chcat {{[-L|--list]}}`

- 파일에 카테고리 추가:

`sudo chcat +{{카테고리_이름}} {{경로/대상/파일}}`

- 파일에서 카테고리 제거:

`sudo chcat -- -{{카테고리_이름}} {{경로/대상/파일}}`

- 파일에 특정 카테고리 설정 (기존 카테고리 대체):

`sudo chcat {{카테고리_이름1,카테고리_이름2,...}} {{경로/대상/파일}}`

- 파일 카테고리 표시:

`ls {{[-Z|--context]}} {{경로/대상/파일}}`

- 파일의 모든 카테고리 제거:

`sudo chcat {{[-d|--delete]}} {{경로/대상/파일}}`

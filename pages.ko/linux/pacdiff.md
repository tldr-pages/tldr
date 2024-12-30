# pacdiff

> `pacman`에 의해 생성된 `.pacorig`, `.pacnew`, `.pacsave` 파일을 관리하는 도구.
> 더 많은 정보: <https://manned.org/pacdiff>.

- 인터랙티브 모드에서 유지 관리가 필요한 파일 검토:

`pacdiff`

- sudo와 sudoedit를 사용하여 파일 제거 및 병합:

`pacdiff --sudo`

- 유지 관리가 필요한 파일을 검토하고, `(O)덮어쓰기` 시 원본의 `.bak`업 생성:

`pacdiff --sudo --backup`

- 특정 편집기를 사용하여 설정 파일을 보고 병합 (기본값은 `vim -d`):

`DIFFPROG={{편집기}} pacdiff`

- `pacman` 데이터베이스 대신 `locate`를 사용하여 설정 파일 스캔:

`pacdiff --locate`

- 도움말 표시:

`pacdiff --help`

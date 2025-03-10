# useradd

> 새 사용자 생성.
> 같이 보기: `users`, `userdel`, `usermod`.
> 더 많은 정보: <https://manned.org/useradd>.

- 새 사용자 생성:

`sudo useradd {{사용자명}}`

- 특정 사용자 ID로 새 사용자 생성:

`sudo useradd {{[-u|--uid]}} {{ID}} {{사용자명}}`

- 특정 셸로 새 사용자 생성:

`sudo useradd {{[-s|--shell]}} {{경로/대상/셸}} {{사용자명}}`

- 추가 그룹에 속하는 새 사용자 생성 (공백 없이 작성):

`sudo useradd {{[-G|--groups]}} {{그룹1,그룹2,...}} {{사용자명}}`

- 기본 홈 디렉터리를 가진 새 사용자 생성:

`sudo useradd {{[-m|--create-home]}} {{사용자명}}`

- 템플릿 디렉터리 파일로 채워진 홈 디렉터리를 가진 새 사용자 생성:

`sudo useradd {{[-k|--skel]}} {{경로/대상/템플릿_디렉터리}} {{[-m|--create-home]}} {{사용자명}}`

- 홈 디렉터리 없이 새 시스템 사용자 생성:

`sudo useradd {{[-r|--system]}} {{사용자명}}`

# gh skyline

> GitHub 기여 기록을 기반으로 3D 모델 생성.
> 기본적으로, 현재 디렉터리에 `{사용자명}-{연도}-github-skyline.stl` 파일 생성.
> 더 많은 정보: <https://github.com/github/gh-skyline>.

- 현재 연도와 인증된 사용자를 기준으로 skyline STL 파일 생성:

`gh skyline`

- 특정 사용자와 연도를 기준으로 skyline 생성:

`gh skyline {{[-u|--user]}} {{사용자명}} {{[-y|--year]}} {{year}}`

- 특정 사용자에 대해 여러 연도 범위의 skyline 생성:

`gh skyline {{[-u|--user]}} {{사용자명}} {{[-y|--year]}} {{시작_연도}}-{{종료_연도}}`

- 사용자의 가입 연도부터 현재까지 전체 skyline 생성:

`gh skyline {{[-u|--user]}} {{사용자명}} {{[-f|--full]}}`

- 디버그 로깅 활성화:

`gh skyline {{[-d|--debug]}}`

- 출력 STL 파일 경로 지정하여 skyline 생성:

`gh skyline {{[-o|--output]}} {{경로/대상/출력_파일.stl}}`

- 특정 사용자의 GitHub 프로필을 브라우저에서 열기:

`gh skyline {{[-u|--user]}} {{사용자명}} {{[-w|--web]}}`

- 도움말 표시:

`gh skyline {{[-h|--help]}}`

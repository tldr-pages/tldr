# brew tap

> Homebrew formula 저장소를 추가. 인자를 지정하지 않으면, 설치된 모든 tap 목록을 출력.
> 더 많은 정보: <https://docs.brew.sh/Manpage#tap-options-userrepo-url>.

- 설치된 Homebrew tap 목록 출력:

`brew tap`

- GitHub에 호스팅된 Git 저장소 추가(tap):

`brew tap {{github_사용자명}}/{{github_저장소_이름}}`

- GitHub 외부에 호스팅된 Git 저장소 추가(tap):

`brew tap {{사용자명}}/{{저장소_이름}} {{git_clone_url}}`

- GitLab에 호스팅된 저장소 tap 추가:

`brew tap {{사용자명}}/{{저장소_이름}} https://gitlab.com/{{사용자명}}/{{저장소_이름}}.git`

- 도움말 표시:

`brew tap {{[-h|--help]}}`

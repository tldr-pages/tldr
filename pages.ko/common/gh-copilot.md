# gh copilot

> GitHub Copilot과 상호작용.
> 참고: 현재는 `copilot` 명령으로 대체되어 deprecated 상태.
> 더 많은 정보: <https://github.com/github/gh-copilot#usage>.

- 설명을 기반으로 명령어 추천:

`gh copilot suggest "{{git 설치}}"`

- Git 명령어 추천:

`gh copilot suggest {{[-t|--target]}} git "{{Undo the most recent local commits}}"`

- 명령어 설명:

`gh copilot explain "{{traceroute example.com}}"`

- Bash용 쉘 별칭 생성:

`echo 'eval "$(gh copilot alias -- bash)"' >> ~/.bashrc`

- Zsh용 쉘 별칭 생성:

`echo 'eval "$(gh copilot alias -- zsh)"' >> ~/.zshrc`

- 옵션 설정:

`gh copilot config`

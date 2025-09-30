# fisher

> Fish-shell 플러그인 관리자인 Fisher.
> 이름별로 플러그인을 설치하거나 번들 설치의 경우 관리되는 'fishfile'에서 플러그인을 설치.
> 더 많은 정보: <https://github.com/jorgebucaran/fisher>.

- 하나 이상의 플러그인을 설치:

`fisher {{플러그인1}} {{플러그인2}}`

- GitHub 요점에서 플러그인을 설치:

`fisher {{gist_url}}`

- 선호하는 편집기로 'fishfile'을 수동으로 편집하고 여러 플러그인을 설치:

`{{editor}} ~/.config/fish/fishfile; fisher`

- 설치된 플러그인 목록:

`fisher ls`

- 플러그인 업데이트:

`fisher update`

- 하나 이상의 플러그인을 제거:

`fisher remove {{플러그인1}} {{플러그인2}}`

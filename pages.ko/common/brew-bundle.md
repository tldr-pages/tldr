# brew bundle

> Homebrew, Homebrew Cask 및 Mac App Store용 번들러.
> 더 많은 정보: <https://docs.brew.sh/Manpage#bundle-subcommand>.

- 현재 경로의 Brewfile에서 패키지를 설치:

`brew bundle`

- 특정 경로의 특정 Brewfile에서 패키지를 설치:

`brew bundle --file {{경로/대상/파일}}`

- 설치된 모든 패키지에서 Brewfile을 생성:

`brew bundle dump`

- Brewfile에 나열되지 않은 모든 공식을 제거:

`brew bundle cleanup --force`

- Brewfile에 설치하거나 업그레이드할 항목이 있는지 확인:

`brew bundle check`

- Brewfile의 모든 항목을 나열:

`brew bundle list --all`

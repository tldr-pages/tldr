# brew uninstall

> Homebrew formula/cask를 제거.
> 나중에 사용하지 않는 의존성을 제거하려면, `brew autoremove`를 사용.
> 더 많은 정보: <https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->.

- formula/cask를 설치 삭제:

`brew uninstall {{formula|cask}}`

- cask를 제거하고 관련 파일을 모두 제거:

`brew uninstall --zap {{cask}}`

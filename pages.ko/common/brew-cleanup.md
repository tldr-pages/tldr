# brew cleanup

> 모든 formulas와 casks에 대해 오래된 잠금 파일과 오래된 다운로드 파일을 제거.
> 더 많은 정보: <https://docs.brew.sh/Manpage#cleanup-options-formulacask->.

- 모든 formula/cask에 대해 오래된 잠금 파일과 오래된 다운로드 파일을 제거:

`brew cleanup`

- 특정 formula/cask에 대해 오래된 잠금 파일과 오래된 다운로드 파일을 제거:

`brew cleanup {{formula|cask}}`

- 실제 삭제하지 않고, 제거될 항목을 표시:

`brew cleanup {{[-n|--dry-run]}}`

- 도움말 표시:

`brew cleanup {{[-h|--help]}}`

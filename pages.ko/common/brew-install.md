# brew install

> Homebrew formuale이나 cask를 설치.
> 더 많은 정보: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- formuale/cask 설치:

`brew install {{formula|cask}}`

- 소스에서 formuale을 빌드하고 설치 (의존성은 여전히 병에서 설치):

`brew install {{[-s|--build-from-source]}} {{formula}}`

- 매니페스트를 다운로드하고, 설치될 항목을 인쇄하지만 실제로는 아무것도 설치하지 않음:

`brew install {{[-n|--dry-run]}} {{formula|cask}}`

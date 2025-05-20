# nix build

> Nix 표현식을 빌드합니다 (가능할 경우 캐시에서 다운로드).
> 같이 보기: 전통적인 Nix 표현식 빌드에 대한 `nix-build`, flakes에 대한 정보는 `nix flake`.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-build.html>.

- nixpkgs에서 패키지를 빌드하고 결과를 `./result`에 심볼릭 링크:

`nix build {{nixpkgs#pkg}}`

- 현재 디렉토리의 flake에서 패키지를 빌드하고 빌드 로그를 표시:

`nix build -L {{.#pkg}}`

- 특정 디렉토리의 flake에서 기본 패키지 빌드:

`nix build {{./경로/대상/폴더}}`

- `result` 심볼릭 링크를 생성하지 않고 패키지를 빌드하며 대신 저장소 경로를 `stdout`에 출력:

`nix build --no-link --print-out-paths`

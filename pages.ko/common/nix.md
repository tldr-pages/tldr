# nix

> 패키지 관리를 신뢰성 있고, 재현 가능하며, 선언적으로 만드는 강력한 패키지 관리자.
> `nix`는 실험적이며 실험적 기능 사용을 활성화해야 합니다. 안정적인 인터페이스를 원하면 `tldr nix classic`을 참조하세요.
> `build`, `develop`, `flake`, `registry`, `profile`, `search`, `repl`, `store`, `edit`, `why-depends` 등의 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix>.

- `nix` 명령 활성화:

`mkdir {{[-p|--parents]}} ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- nixpkgs에서 이름이나 설명으로 패키지 검색:

`nix search nixpkgs {{검색어}}`

- nixpkgs에서 지정한 패키지가 사용 가능한 셸 시작:

`nix shell {{nixpkgs#패키지1 nixpkgs#패키지2 nixpkgs#패키지3 ...}}`

- nixpkgs에서 일부 패키지를 영구적으로 설치:

`nix profile install {{nixpkgs#패키지1 nixpkgs#패키지2 nixpkgs#패키지3 ...}}`

- Nix 저장소에서 사용하지 않는 경로 제거하여 공간 확보:

`nix store gc`

- Nix 표현식을 평가하기 위한 대화형 환경 시작:

`nix repl`

- 특정 하위 명령에 대한 도움말 표시:

`nix help {{하위_명령}}`

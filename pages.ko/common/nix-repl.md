# nix repl

> Nix 표현식을 평가하기 위한 대화형 환경 시작.
> Nix 표현식 언어에 대한 설명은 <https://nixos.org/manual/nix/stable/language/index.html>을 참고하세요.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-repl.html>.

- Nix 표현식을 평가하기 위한 대화형 환경 시작:

`nix repl`

- 플레이크(예: `nixpkgs`)의 모든 패키지를 스코프로 불러오기:

`:lf {{nixpkgs}}`

- 표현식에서 패키지 빌드:

`:b {{표현식}}`

- 표현식에서 패키지를 사용할 수 있는 셸 시작:

`:u {{표현식}}`

- 표현식에서 패키지의 종속성을 사용할 수 있는 셸 시작:

`:s {{표현식}}`

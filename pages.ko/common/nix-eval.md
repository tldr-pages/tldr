# nix eval

> Nix 표현식을 평가하고 결과를 `stdout`에 출력.
> 더 많은 정보: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-eval.html>.

- 현재 디렉터리의 Nix flake 속성을 평가:

`nix eval .#{{속성}}`

- 주어진 Nix 표현식 평가:

`nix eval --expr '{{자신의_표현식}}'`

- 지정한 파일의 Nix 표현식 평가:

`nix eval --file {{경로/대상/파일}}`

- nixpkgs에서 지정한 패키지의 store 경로 출력:

`nix eval {{nixpkgs#pkg}} --raw`

- GitHub의 flake에서 속성 평가:

`nix eval {{github:owner/repo#attributes}}`

- 지정한 패키지를 인수로 전달하여 람다 함수 평가:

`nix eval {{nixpkgs#pkg}} --apply '{{lambda_함수}}'`

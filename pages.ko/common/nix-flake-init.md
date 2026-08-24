# nix flake init

> 템플릿을 사용하여 현재 디렉터리에 flake를 생성.
> 더 많은 정보: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-init.html>.

- 기본 템플릿으로 현재 디렉터리에 새로운 flake 생성:

`nix flake init`

- 지정한 템플릿으로 새로운 flake 생성 (`nix flake show`에서 템플릿 정보 확인 가능):

`nix flake init {{[-t|--template]}} templates#{{자신의_템플릿}}`

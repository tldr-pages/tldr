# nix run

> Nix 플레이크에서 애플리케이션 실행.
> 같이 보기: 플레이크에 대한 정보는 `nix flake`.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-run.html>.

- 현재 디렉토리의 플레이크에서 기본 애플리케이션 실행:

`nix run`

- nixpkgs에서 패키지 이름과 일치하는 명령 실행 (해당 패키지의 다른 명령을 원하면 `tldr nix3 shell` 참조):

`nix run nixpkgs#{{패키지}}`

- 제공된 인수와 함께 명령 실행:

`nix run nixpkgs#{{vim}} -- {{경로/대상/파일}}`

- 원격 저장소에서 실행:

`nix run {{원격_이름}}:{{소유자}}/{{레포}}`

- 특정 태그, 리비전 또는 브랜치를 사용하여 원격 저장소에서 실행:

`nix run {{원격_이름}}:{{소유자}}/{{레포}}/{{참조}}`

- 하위 디렉토리와 프로그램을 지정하여 원격 저장소에서 실행:

`nix run "{{원격_이름}}:{{소유자}}/{{레포}}?dir={{디렉토리_이름}}#{{앱}}"`

- GitHub 풀 리퀘스트의 플레이크 실행:

`nix run github:{{소유자}}/{{레포}}/pull/{{번호}}/head`

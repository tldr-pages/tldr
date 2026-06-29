# nh

> Nix/NixOS 생태계를 위한 현대적인 헬퍼 유틸리티 도구.
> `os`, `home`, `clean`, `search` 등의 하위 명령어는 각각 별도의 사용법 문서를 제공.
> 더 많은 정보: <https://github.com/nix-community/nh#usage>.

- 지정한 NixOS flake 설정을 빌드하고 적용:

`nh os switch {{경로/대상/flake}}`

- 지정한 Home Manager flake 설정을 빌드하고 적용:

`nh home switch {{경로/대상/flake}}`

- 지정한 nix-darwin flake 설정을 빌드하고 적용:

`nh darwin switch {{경로/대상/flake}} {{[-H|--hostname]}} {{호스트}}`

- Nix store의 모든 가비지와 GC Root를 정리:

`nh clean all {{[-a|--ask]}}`

- Nixpkgs에서 패키지 검색:

`nh search {{이름}}`

- 지정한 쉘의 자동완성 스크립트 생성:

`nh completions {{쉘}}`

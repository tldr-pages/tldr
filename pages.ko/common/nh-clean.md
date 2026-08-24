# nh clean

> Nix 프로필을 정리하고 사용되지 않거나 더 이상 참조되지 않는 Nix store 경로 삭제.
> 생성된 세대는 `nix-env --list-generations` 또는 `nh os info`를 사용하여 확인 가능.
> 더 많은 정보: <https://github.com/nix-community/nh#usage>.

- 정리 계획을 확인한 후, 모든 프로필을 정리하고 가비지 컬렉션 수행:

`nh clean all {{[-a|--ask]}}`

- 현재 사용자의 최신 프로필을 지정한 개수만 유지하고 나머지 프로필 삭제:

`nh clean user {{[-k|--keep]}} {{숫자}}`

- 특정 프로필을 정리하고 가비지 컬렉션 수행:

`nh clean profile {{경로/대상/프로필}}`

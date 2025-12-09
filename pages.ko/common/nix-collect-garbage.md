# nix-collect-garbage

> 사용되지 않거나 접근할 수 없는 nix 저장소 경로 삭제.
> 세대는 `nix-env --list-generations` 명령어로 나열할 수 있습니다.
> 더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>.

- 각 프로필의 현재 세대에서 사용되지 않는 모든 저장소 경로 삭제:

`nix-collect-garbage --delete-old`

- 오래된 저장소 경로 삭제 시뮬레이션:

`nix-collect-garbage --delete-old --dry-run`

- 30일보다 오래된 모든 저장소 경로 삭제:

`nix-collect-garbage --delete-older-than 30d`

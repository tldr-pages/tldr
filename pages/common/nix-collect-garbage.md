# nix-collect-garbage

> Delete unused and unreachable nix store paths.
> Generations can be listed using `nix-env --list-generations`.
> More information: <https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>.

- Delete all store paths unused by current generations of each profile:

`sudo nix-collect-garbage --delete-old`

- Simulate the deletion of old store paths:

`sudo nix-collect-garbage --delete-old --dry-run`

- Delete all store paths older than 30 days:

`sudo nix-collect-garbage --delete-older-than 30d`

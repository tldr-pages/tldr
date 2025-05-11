# nix store

> Manipulate the Nix store.
> See also: `nix-store`.
> More information: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-store.html>.

- Collect garbage, i.e. remove unused paths to reduce space usage:

`nix store gc`

- Hard-link identical files together to reduce space usage:

`nix store optimise`

- Delete a specific store path (most be unused):

`nix store delete {{/nix/store/...}}`

- List a contents of the store path, on a remote store:

`nix store --store {{https://cache.nixos.org}} ls {{/nix/store/...}}`

- Show the differences in versions between two store paths, with their respective dependencies:

`nix store diff-closures {{/nix/store/...}} {{/nix/store/...}}`

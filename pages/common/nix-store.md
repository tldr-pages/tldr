# nix-store

> Manipulate or query the Nix store.
> Not to be confused with `nix store` (see `tldr nix3 store`).

- Collect garbage, i.e. remove unused paths to reduce space usage:

`nix-store --gc`

- Hard-link identical files together to reduce space usage:

`nix-store --optimise`

- Delete a specific store path (most be unused):

`nix-store --delete {{/nix/store/...}}`

- Show all dependencies of a store path (package), in a tree format:

`nix-store --query --tree {{/nix/store/...}}`

- Calculate the total size of a certain store path with all the dependencies:

`du -cLsh $(nix-store --query --references {{/nix/store/...}})`

- Show all dependents of a particular store path:

`nix-store --query --referrers {{/nix/store/...}}`

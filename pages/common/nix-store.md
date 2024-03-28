# nix-store

> Manipulate or query the Nix store.
> See also: `nix3 store`.
> More information: <https://nixos.org/manual/nix/stable/command-ref/nix-store.html>.

- Collect garbage, such as removing unused paths:

`nix-store --gc`

- Hard-link identical files together to reduce space usage:

`nix-store --optimise`

- Delete a specific store path (must be unused):

`nix-store --delete {{/nix/store/...}}`

- Show all dependencies of a store path (package), in a tree format:

`nix-store --query --tree {{/nix/store/...}}`

- Calculate the total size of a certain store path with all the dependencies:

`du -cLsh $(nix-store --query --references {{/nix/store/...}})`

- Show all dependents of a particular store path:

`nix-store --query --referrers {{/nix/store/...}}`

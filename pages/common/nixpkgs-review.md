# nixpkgs-review

> Review pull requests in the NixOS packages repository (nixpkgs).
> After a successful build, a `nix-shell` with all built packages is started.
> More information: <https://github.com/Mic92/nixpkgs-review#usage>.

- Build changed packages in the specified pull request:

`nixpkgs-review pr {{pr_number|pr_url}}`

- Build changed packages and post a comment with a report (requires setting up a token in `hub`, `gh`, or the `GITHUB_TOKEN` environment variable):

`nixpkgs-review pr --post-result {{pr_number|pr_url}}`

- Build changed packages and print a report:

`nixpkgs-review pr --print-result {{pr_number|pr_url}}`

- Build changed packages in a local commit:

`nixpkgs-review rev {{HEAD}}`

- Build changed packages that haven't been committed yet:

`nixpkgs-review wip`

- Build changed packages that have been staged:

`nixpkgs-review wip --staged`

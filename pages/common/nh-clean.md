# nh clean

> Clean Nix profiles and delete unused and unreachable nix store paths.
> Generations can be listed using `nix-env --list-generations` or `nh os info`.
> More information: <https://github.com/nix-community/nh#usage>.

- Ask for clean up plan confirmation, clean all profiles and collect garbage:

`nh clean all {{[-a|--ask]}}`

- Keep a specified number of the most recent profiles for the current user and clean the remaining profiles:

`nh clean user {{[-k|--keep]}} {{number}}`

- Clean a specific profile and collect garbage:

`nh clean profile {{path/to/profile}}`

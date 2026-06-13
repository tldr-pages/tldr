# nh search

> Search for packages in Nixpkgs.
> More information: <https://github.com/nix-community/nh#usage>.

- Search for a package in Nixpkgs, limiting results:

`nh search {{[-l|--limit]}} {{number}} {{name}}`

- Search for a package in a specified Nixpkgs channel:

`nh search {{[-c|--channel]}} {{nixos-unstable}} {{name}}`

- Search for a package in Nixpkgs, showing supported platforms for each package:

`nh search {{[-P|--platforms]}} {{name}}`

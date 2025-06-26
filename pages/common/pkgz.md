# pkgz

A fast, extensible CLI package manager written in Crystal.  
Supports unified package management across Apt, Flatpak, Pacstall, Pacman, Paru, DNF, and BSD package systems.

- `pkgz install <app>`  
  Installs the app from the first enabled source where it’s found.

- `pkgz remove <app>`  
  Attempts to remove the app from all enabled sources.

- `pkgz update`  
  Runs update commands on all enabled sources.

- `pkgz search <app>`  
  Searches across all enabled sources and lists matches.

- `pkgz --version`  
  Prints the current pkgz version.

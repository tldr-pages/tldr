# pkgz

A fast, extensible CLI package manager written in Crystal.  
Supports unified package management across Apt, Flatpak, Pacstall, Pacman, Paru, DNF, and BSD package systems.

---

## Configuration

`pkgz` loads configuration from:

  ~/.config/pkgz/config.toml

If this file does not exist, pkgz will exit with a sample config you can create manually.

Example config.toml:
```toml
  [elevator]
  command = "sudo" or "doas"

  [sources]
  apt = true
  nala = false
  flatpak = true
  paru = false
  pacman = false
  dnf = false
  pacstall = true
  freebsd = false
  freebsd_ports = false
  openbsd = false
  openbsd_ports = false
```
- The `elevator.command` option controls which privilege escalation command pkgz uses.
- The `[sources]` section enables or disables each package source backend.

---

## Privilege Elevation

- pkgz tries to detect the elevation command by reading the config.
- If no config or no elevator command is set, pkgz falls back to detecting if `doas` is available.
- If not, it uses `sudo` as the default.

---

## Supported Package Sources

pkgz supports multiple package sources via classes that implement the `Source` abstract interface:

- Apt (Debian/Ubuntu)
- Nala (front-end for Apt)
- Flatpak (sandboxed Linux apps)
- Pacman (Arch Linux)
- Paru (Arch User Repository)
- DNF (Fedora)
- Pacstall (Universal package manager for Linux)
- FreeBSD pkg and FreeBSD Ports
- OpenBSD pkg_add and OpenBSD Ports

Each source implements methods for:

- Checking if a package is available (`available?`)
- Installing, removing, updating, and searching packages

---

## Basic Commands

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

---

## Example Usage

```bash
pkgz install neovim
pkgz remove firefox
pkgz update
pkgz search chromium


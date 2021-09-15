# aura

> The Aura Package Manager: A secure, multilingual package manager for Arch Linux and the AUR.
> More information: <https://github.com/fosskers/aura>.

- Search for packages from the repos and AUR:

`aura -As --both {{package_name|search_regex}}`

- Display a package's PKGBUILD:

`aura -Ap {{package_name}}`

- Update all AUR packages in a verbose mode and remove all make dependencies:

`aura -Akuax`

- Install a package from the AUR:

`aura -A {{package_name}}`

- Hotedit the PKGBUILD before installtion of a package from the AUR (text editor should be set in /etc/aura.conf):

`aura -A --hotedit {{package_name}}`

- Analyse all locally installed AUR packages for vulnerabilities:

`aura -Pa`

- Analyse all local PKGBUILD file:

`aura -Pf {{PKGBUILD_FIlE}}`

- Install a package from the system repos:

`aura -S {{package_name}}`

- Update all system repo packages:

`aura -Syu`

- Clear aura package cache:

`aura -Cv`

- Downgrade a package from the package cache:

`aura -C {{package_name}}`

- View the install / upgrade history of a package:

`aura -Li {{package_name}}`

- Remove an installed package and both its dependencies:

`aura -Rs {{package_name}}`

- List all orphan packages (installed as dependencies but not required by any package):

`aura -O`

- Uninstall all orphan packages:

`aura -Oj`

- Mark packages as explicitly installed to avoid it's accidental deletion as an orphan package:

`aura -Oa {{package_names}}`

# stow

> Manager Symlink.
> Adesea folosit pentru a gestiona dotfiles.
> Mai multe informaţii: <https://www.gnu.org/software/stow>

- Symlink toate fișierele recursiv la un anumit director:

`stow --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Ștergeți linkurile simbolice recursiv dintr-un anumit director:

`stow --delete --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Simulați pentru a vedea cum ar fi rezultatul:

`stow --simulate --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Ștergeți și resymlink:

`stow --restow --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Excludeți fișierele care se potrivesc unei expresii regulate:

`stow --ignore={{regular_expression}} --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

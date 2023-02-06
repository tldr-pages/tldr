# stow

> Symlink manager. Gyakran használják a dotfiles kezelésére. További információ: <https://www.gnu.org/software/stow>.

- Az összes fájlt rekurzívan egy adott könyvtárba linkeli:

`stow --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Symlinkek törlése rekurzívan egy adott könyvtárból:

`stow --delete --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Szimulálja, hogy lássa, milyen lenne az eredmény:

`stow --simulate --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Törlés és újraminktálás:

`stow --restow --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

- Szabályos kifejezésnek megfelelő fájlok kizárása:

`stow --ignore={{regular_expression}} --target={{path/to/target_directory}} {{file1 directory1 file2 directory2}}`

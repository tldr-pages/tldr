# xdg-user-dirs-update

> Az XDG felhasználói könyvtárak frissítése. További információ: <https://manned.org/xdg-user-dirs-update>.

- Az XDG DESKTOP könyvtárának módosítása a megadott könyvtárra (abszolút értékűnek kell lennie):

`xdg-user-dirs-update --set DESKTOP "{{path/to/directory}}"`

- Az eredményt a megadott dry-run-fájlba írja a `user-dirs.dirs` fájl helyett:

`xdg-user-dirs-update --dummy-output "{{path/to/dry_run_file}}" --set {{xdg_user_directory}} "{{path/to/directory}}"`

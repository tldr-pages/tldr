# xdg-user-dirs-update

> Actualizați directoarele utilizatorilor XDG.
> Mai multe informaţii: <https://manpages.ubuntu.com/manpages/bionic/man1/xdg-user-dirs-update.1.html>

- Schimbați directorul DESKTOP al XDG în directorul specificat (trebuie să fie absolut):

`xdg-user-dirs-update --set DESKTOP "{{path/to/directory}}"`

- Scrieți rezultatul în fișierul uscat specificat în locul fișierului `user-dirs.dirs`:

`xdg-user-dirs-update --dummy-output "{{path/to/dry_run_file}}" --set {{xdg_user_directory}} "{{path/to/directory}}"`

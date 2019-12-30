# xdg-user-dirs-update

> Update XDG user directories.
> More information: <https://manpages.ubuntu.com/manpages/bionic/man1/xdg-user-dirs-update.1.html>.

- Change XDG's DESKTOP directory to the specified directory (must be absolute):

`xdg-user-dirs-update --set DESKTOP "{{path/to/directory}}"`

- Write the result to the specified dry-run-file instead of the `user-dirs.dirs` file:

`xdg-user-dirs-update --dummy-output "{{path/to/dry_run_file}}" --set {{xdg_user_directory}} "{{path/to/directory}}"`

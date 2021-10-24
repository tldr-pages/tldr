# emacs

> The extensible, customizable, self-documenting, real-time display editor.
> See also `emacsclient`.
> More information: <https://www.gnu.org/software/emacs>.

- Start Emacs and open a file:

`emacs {{path/to/file}}`

- Open a file at a specified line number:

`emacs +{{line_number}} {{path/to/file}}`

- Start Emacs in console mode (without an X window):

`emacs --no-window-system`

- Start an Emacs server in the background (accessible via `emacsclient`):

`emacs --daemon`

- Stop a running Emacs server and all its instances, asking for confirmation on unsaved files:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Save a file in Emacs:

`Ctrl + X, Ctrl + S`

- Quit Emacs:

`Ctrl + X, Ctrl + C`

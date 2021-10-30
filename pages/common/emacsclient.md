# emacsclient

> Open files in an existing Emacs server.
> See also `emacs`.
> More information: <https://www.emacswiki.org/emacs/EmacsClient>.

- Open a file in an existing Emacs server (using GUI if available):

`emacsclient {{path/to/file}}`

- Open a file in console mode (without an X window):

`emacsclient --no-window-system {{path/to/file}}`

- Open a file in a new Emacs window:

`emacsclient --create-frame {{path/to/file}}`

- Evaluate a command, printing the output to stdout, and then quit:

`emacsclient --eval '({{command}})'`

- Specify an alternative editor in case no Emacs server is running:

`emacsclient --alternate-editor {{editor}} {{path/to/file}}`

- Stop a running Emacs server and all its instances, asking for confirmation on unsaved files:

`emacsclient --eval '(save-buffers-kill-emacs)'`

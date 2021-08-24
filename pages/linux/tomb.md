# tomb

> Manage encrypted storage directories that can be safely transported and hidden in a filesystem.
> More information: <https://www.dyne.org/software/tomb/>.

- Create a new tomb with an initial size of 100 MB:

`tomb dig -s {{100}} {{encrypted_directory.tomb}}`

- Create a new key file that can be used to lock a tomb; user will be prompted for a password for the key:

`tomb forge {{encrypted_directory.tomb.key}}`

- Forcefully create a new key, even if the tomb isn't allowing key forging (due to swap):

`tomb forge {{encrypted_directory.tomb.key}} -f`

- Initialize and lock an empty tomb using a key made with `forge`:

`tomb lock {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- Mount a tomb (by default in `/media`) using its key, making it usable as a regular filesystem directory:

`tomb open {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- Close a tomb (fails if the tomb is being used by a process):

`tomb close {{encrypted_directory.tomb}}`

- Forcefully close all open tombs, killing any applications using them:

`tomb slam all`

- List all open tombs:

`tomb list`

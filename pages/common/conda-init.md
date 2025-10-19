# conda init

> Initialize conda for shell interaction.
> Most shells need to be closed and restarted for changes to take effect.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/init.html>.

- Initialize a specific shell (if none is specified, defaults to `bash` for UNIX and `powershell` for Windows):

`conda init {{zsh|bash|powershell|fish|tcsh|xonsh}}`

- Initialize all available shells:

`conda init --all`

- Initialize conda for all users on the system:

`conda init --system`

- Don't initialize conda for the current user:

`conda init --no-user`

- Add `condabin/` directory to PATH:

`conda init --condabin`

- Undo effects of the last `conda init`:

`conda init --reverse`

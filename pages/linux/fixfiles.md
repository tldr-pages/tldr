# fixfiles

> Fix file SELinux security contexts.
> More information: <https://manned.org/fixfiles>.

- If specified with onboot, this fixfiles will record the current date in the `/.autorelabel` file, so that it can be used later to speed up labeling. If used with restore, the restore will only affect files that were modified today:

`fixfiles -B`

- [F]orce reset of context to match `file_context` for customizable files:

`fixfiles -F`

- Clear `/tmp` directory without confirmation:

`fixfiles -f`

- Use the [R]pm database to discover all files within specific packages and restore the file contexts:

`fixfiles -R {{rpm_package_name1,rpm_package_name2 ...}}`

- Run a diff on the `PREVIOUS_FILECONTEXT` file to the [C]urrently installed one, and restore the context of all affected files:

`fixfiles -C PREVIOUS_FILECONTEXT`

- Only act on files created after a specific date which will be passed to find `--newermt` command:

`fixfiles -N {{YYYY-MM-DD HH:MM}}`

- Bind [M]ount filesystems before relabeling them, this allows fixing the context of files or directories that have been mounted over:

`fixfiles -M`

- Modify [v]erbosity from progress to verbose and run `restorecon` with `-v` instead of `-p`:

`fixfiles -v`

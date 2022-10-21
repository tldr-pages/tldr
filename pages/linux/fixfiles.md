# fixfiles

> Fix file SELinux security contexts.
> More information: <https://manned.org/fixfiles>.

- If specified with onboot, this fixfiles will record the current date in the /.autorelabel file, so that it can be used later to speed up labeling. If used with restore, the restore will only affect files that were modified today:

`fixfiles -B`

- Force reset of context to match file_context for customizable files:

`fixfiles -F`

- Clear /tmp directory with out prompt for removal:

`fixfiles -f`

- Use the rpm database to discover all files within the specified packages and restore the file contexts:

`fixfiles -R rpmpackagename[,rpmpackagename...]`

- Run a diff on  the PREVIOUS_FILECONTEXT file to the currently installed one, and restore the context of all affected files:

`fixfiles -C PREVIOUS_FILECONTEXT`

- Only act on files created after the specified date.  Date must be specified in "YYYY-MM-DD HH:MM" format.  Date field will be passed to find --newermt command:

`fixfiles -N time`

- Bind mount filesystems before relabeling them, this allows fixing the context of files or directories that have been mounted over:

`fixfiles -M`

- Modify verbosity from progress to verbose. (Run restorecon with -v instead of -p):

`fixfiles -v`

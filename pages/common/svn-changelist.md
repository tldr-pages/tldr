# svn changelist

> Associate a changelist with a set of files.
> More information: <https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn.c.changelist>.

- Add files to a changelist, creating the changelist if it does not exist:

`svn {{[cl|changelist]}} {{changelist_name}} {{path/to/file1 path/to/file2 ...}}`

- Remove files from a changelist:

`svn {{[cl|changelist]}} --remove {{path/to/file1 path/to/file2 ...}}`

- Remove the whole changelist at once:

`svn {{[cl|changelist]}} --remove {{[-R|--recursive]}} --changelist {{changelist_name}} .`

- Add the contents of a space-separated list of directories to a changelist:

`svn {{[cl|changelist]}} {{[-R|--recursive]}} {{changelist_name}} {{path/to/directory1 path/to/directory2 ...}}`

- Commit a changelist:

`svn commit --changelist {{changelist_name}}`

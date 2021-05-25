# svn changelist

> Associate a changelist with a set of files.
> More information: <http://svnbook.red-bean.com/en/1.7/svn.advanced.changelists.html>.

- Add files to a changelist, creating the changelist if it does not exist:

`svn changelist {{changelist_name}} {{path/to/file1}} {{path/to/file2}}`

- Remove files from a changelist:

`svn changelist --remove {{path/to/file1}} {{path/to/file2}}`

- Remove the whole changelist at once:

`svn changelist --remove --recursive --changelist {{changelist_name}} .`

- Add the contents of a space-separated list of directories to a changelist:

`svn changelist --recursive {{changelist_name}} {{path/to/directory1}} {{path/to/directory2}}`

- Commit a changelist:

`svn commit --changelist {{changelist_name}}`

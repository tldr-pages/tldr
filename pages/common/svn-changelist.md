# svn changelist

> Associate a changelist with a set of files.
> More information: <https://subversion.apache.org>.

- Add files to a [new] changelist:

`svn changelist {{changelist_name}} [{{FILE_PATH}}]`

- Remove files from a changelist:

`svn changelist --changelist {{changelist_name}} --remove [{{FILE_PATH}}]`

- Remove the whole changelist at once:

`svn changelist --changelist {{changelist_name}} -R --remove .`

- Add a whole folder to a changelist:

`svn changelist -R {{changelist_name}} [{{PATH}}]`

- Commit a changelist:

`svn commit --changelist {{changelist_name}}`

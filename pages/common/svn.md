# svn

> Subversion client tool.
> More information: <https://svnbook.red-bean.com/en/1.7/svn-book.html#svn.ref.svn>.

- Check out a working copy from a repository:

`svn {{[co|checkout]}} {{file:///path/to/repository}}`

- Bring changes from the repository into the working copy:

`svn {{[up|update]}}`

- Put files and directories under version control, scheduling them for addition to repository. They will be added in next commit:

`svn add {{path/to/file_or_directory}}`

- Send changes from your working copy to the repository:

`svn {{[ci|commit]}} {{[-m|--message]}} {{commit_log_message}} {{path/to/directory}}`

- Display changes from the last 10 revisions, showing modified files for each revision:

`svn log {{[-vl|--verbose --limit]}} {{10}}`

- Display help:

`svn {{[h|help]}}`

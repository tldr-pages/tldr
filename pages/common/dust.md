# dust

> Dust gives you an instant overview of which directories are using disk space:.
> More information: <https://github.com/bootandy/dust>.

- show the current directory's information:

`dust`

- show the information of A and B directories in the current directory:

`dust A B`

- show only 30 directories instead of showing default number of directories:

`dust -n 30`

- show 3 levels of subdirectories

`dust -d 3`

- reverse order of output, with root at the lowest

`dust -r`

- ignore all files and directories with the name 'ignore':

`dust -X ignore`

- do not show percentages or draw ASCII bars

`dust -b`

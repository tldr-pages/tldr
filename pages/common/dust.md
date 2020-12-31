# dust

> Dust gives you an instant overview of which directories are using disk space:.
> More information: <https://github.com/bootandy/dust>.

- Display information for the current directory:

`dust`

- Show the information of A and B directories in the current directory:

`dust A B`

- Show only 30 directories instead of showing default number of directories:

`dust -n 30`

- Show 3 levels of subdirectories:

`dust -d 3`

- Severse order of output, with root at the lowest:

`dust -r`

- Ignore all files and directories with the name 'ignore':

`dust -X ignore`

- Do not show percentages or draw ASCII bars:

`dust -b`

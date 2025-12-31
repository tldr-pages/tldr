# lxc-ls

> List Linux containers.
> More information: <https://linuxcontainers.org/lxc/manpages/man1/lxc-ls.1.html>.

- List all containers:

`sudo lxc-ls`

- List active containers (including frozen and running):

`sudo lxc-ls --active`

- List only frozen containers:

`sudo lxc-ls --frozen`

- List only stopped containers:

`sudo lxc-ls --stopped`

- List containers in a fancy, column-based output:

`sudo lxc-ls {{[-f|--fancy]}}`

- Display help:

`lxc-ls {{[-?|--help]}}`

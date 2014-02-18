#chmod

> Change the permissions for a file
> Mode is three number which define permissions for owner, group, and others respectively.
> Each number represents the execute, read, and write via binary representation
> Ex: mode = 754
>   Permission -> R W E
>              U  1 1 1 = 111%b = 7
>              G  1 0 1 = 101%b = 5
>              O  1 0 0 = 100%b = 4
>   User type -^

- Change permissions of a file

`chmod {{mode}} {{target}}`

- Change permissions of files and directories recursively

`chmod -r {{mode}} {{target}}`

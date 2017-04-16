# SELinux

> NSA Security-Enhanced Linux

- Check SELinux status
 
`sestatus`

- Set SELinux to enforcing

`setenforce {{Enforcing}}`

- Set SELinux to permissive

`setenforce {{Permissive}}`

- Check a file's SELinux context

`ls -Z {{file}}`

- Change a file's SELinux context
 
`chcon -v --type={{context}} {{file}}`

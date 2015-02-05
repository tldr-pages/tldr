# SELinux

> NSA Security-Enhanced Linux

- Check SELinux status
 
`sestatus`

- Change SELinux enforcing status

`setenforce {{enforcing|permissive}}`

- Check a file's SELinux context

`ls -Z {{file}}`

- Change a file's SELinux context
 
`chcon -v --type={{context}} {{file}}`

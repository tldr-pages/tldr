# selinuxenabled

> Check whether SELinux is enabled.
> Returns exit code 0 if SELinux is enabled, and 1 if it is not.
> See also: `getenforce`, `setenforce`, `sestatus`.
> More information: <https://manned.org/selinuxenabled>.

- Check if SELinux is enabled (no output; check exit code with `echo $?`):

`selinuxenabled`

- Check if SELinux is enabled and print the result:

`selinuxenabled && echo "SELinux is enabled" || echo "SELinux is disabled"`

- Use in a shell script to conditionally execute commands:

`if selinuxenabled; then echo "SELinux is running"; fi`

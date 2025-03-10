# semanage permissive

> Manage persistent SELinux permissive domains.
> Note that this effectively makes the process unconfined. For long-term use, it is recommended to configure SELiunx properly.
> See also: `semanage`, `getenforce`, `setenforce`.
> More information: <https://manned.org/semanage-permissive>.

- List all process types (a.k.a domains) that are in permissive mode:

`sudo semanage permissive {{[-l|--list]}}`

- Set permissive mode for a domain:

`sudo semanage permissive {{[-a|--add]}} {{httpd_t}}`

- Unset permissive mode for a domain:

`sudo semanage permissive {{[-d|--delete]}} {{httpd_t}}`

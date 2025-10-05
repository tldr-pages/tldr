# sesearch

> Search SELinux policy rules.
> Part of the `setools` package.
> See also: `seinfo`, `semodule`.
> More information: <https://manned.org/sesearch>.

- Search for all allow rules:

`sesearch --allow`

- Search for rules related to a specific type:

`sesearch --allow {{[-t|--target]}} {{httpd_t}}`

- Search for rules related to a specific source type:

`sesearch --allow {{[-s|--source]}} {{user_t}}`

- Search for rules that allow a specific class and permission:

`sesearch --allow {{[-c|--class]}} {{file}} {{[-p|--perm]}} {{read}}`

- Search for rules with a specific target type and class:

`sesearch --allow {{[-t|--target]}} {{shadow_t}} {{[-c|--class]}} {{file}}`

- Display more detailed information about matched rules:

`sesearch --allow {{[-t|--target]}} {{httpd_t}} {{[-v|--verbose]}}`

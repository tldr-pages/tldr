# sesearch

> Search SELinux policy rules.
> Part of the `setools` package.
> See also: `seinfo`, `semodule`.
> More information: <https://manned.org/sesearch>.

- Search for all allow rules:

`sesearch --allow`

- Search for rules related to a specific type:

`sesearch --allow -t {{httpd_t}}`

- Search for rules related to a specific source type:

`sesearch --allow -s {{user_t}}`

- Search for rules that allow a specific class and permission:

`sesearch --allow -c {{file}} -p {{read}}`

- Search for rules with a specific target type and class:

`sesearch --allow -t {{shadow_t}} -c {{file}}`

- Display more detailed information about matched rules:

`sesearch --allow -t {{httpd_t}} -v`

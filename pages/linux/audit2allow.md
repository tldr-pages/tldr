# audit2allow

> Generate SELinux policy allow rules from audit logs.
> Part of the `policycoreutils-python-utils` package.
> See also: `audit2why`, `ausearch`, `semodule`.
> More information: <https://manned.org/audit2allow>.

- Generate allow rules from recent audit denials and display them:

`sudo audit2allow {{[-a|--all]}}`

- Generate allow rules from a specific audit log file:

`sudo audit2allow {{[-i|--input]}} {{path/to/audit.log}}`

- Generate a policy module from recent audit denials:

`sudo audit2allow {{[-a|--all]}} {{[-M|--module]}} {{module_name}}`

- Explain why SELinux denials occurred (same as `audit2why`):

`sudo audit2allow {{[-a|--all]}} --why`

- Display detailed information around generated messages:

`sudo audit2allow {{[-a|--all]}} {{[-e|--explain]}}`

- Use installed macros to generate a reference policy:

`sudo audit2allow {{[-a|--all]}} {{[-R|--reference]}}`

- Generate allow rules for a specific service:

`sudo ausearch {{[-m|--message]}} avc {{[-c|--comm]}} {{service_name}} | audit2allow {{[-M|--module]}} {{policy_name}}`

- Enable verbose output mode:

`sudo audit2allow {{[-a|--all]}} {{[-v|--verbose]}}`

# audit2allow

> Scan logs for messages pertaining to denied permissions.
> Generate a report of Type Enforcement (TE) rules that might allow successful operations.
> See also: `audit2why`.
> More information: <https://manned.org/audit2allow>.

- Show all generated messages in audit and message logs:

`audit2allow {{[-a|--all]}}`

- Show all generated messages since last boot:

`audit2allow {{[-b|--boot]}}`

- Display detailed information around generated messages:

`audit2allow {{[-e|--explain]}}`

- Enable verbose output mode:

`audit2allow {{[-v|--verbose]}}`

- Use installed macros to generate a reference policy:

`audit2allow {{[-R|--reference]}}`

- Specify a policy file for further analysis:

`audit2allow {{[-p|--policy]}} {{path/to/policyfile}}`

- Limit analysis to messages with a type specified in `regex`:

`audit2allow {{[-t|--type]}} {{type_regex}}`

- Display help:

`audit2allow {{[-h|--help]}}`

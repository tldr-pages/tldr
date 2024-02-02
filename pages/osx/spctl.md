# spctl

> Manage the security assessment policy subsystem.
> Utility for managing Gatekeeper in macOS.
> More information: <https://keith.github.io/xcode-man-pages/SPCTL.8.html>.

- Turn off Gatekeeper:

`spctl --master-disable`

- Add a rule to allow an application to run (labeling of rule is optional):

`spctl --add --label {{rule_name}} {{path/to/file}}`

- Turn on Gatekeeper:

`spctl --master-enable`

- List all rules on the system:

`spctl --list`

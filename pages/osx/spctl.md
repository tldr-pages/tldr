# spctl

> Manage the security assessment policy subsystem.
> Utility for managing Gatekeeper in macOS.
> More information: <https://www.unix.com/man-page/osx/8/SPCTL/>.

- Turn off Gatekeeper:

`spctl --master-disable`

- Add a rule to allow an application to run (labeling of rule is optional):

`spctl --add --label "{{rule_name}}" {{path/to/file}}`

- Turn on Gatekeeper:

`spctl --master-enable`

- List all rules on the system:

`spctl --list`

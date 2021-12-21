# spctl

> Manage the security assessment policy subsystem.
> Utility for managing Gatekeeper in OS X
> More information: <https://www.unix.com/man-page/osx/8/SPCTL/>.

- Turn off gatekeeper:

`spctl --master-disable`

- Add a rule to allow an application to run (Labeling of rule is optional):

`spctl --add --label "RuleName" {{path/to/file}}`

- Turn on gatekeeper:

`spctl --master-enable`

- List all rules on the system:

`spctl --list`

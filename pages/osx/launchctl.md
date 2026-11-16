# launchctl

> Control Apple's `launchd` service manager for agents and daemons.
> Service targets combine a domain (e.g. `gui/$(id -u)` or `system`) with the plist's `Label`.
> More information: <https://keith.github.io/xcode-man-pages/launchctl.1.html>.

- Load an agent into the current user's GUI login domain:

`launchctl bootstrap gui/$(id -u) {{path/to/agent.plist}}`

- Load a system-wide daemon:

`sudo launchctl bootstrap system {{path/to/daemon.plist}}`

- Display information about the current user's GUI login domain, including its services:

`launchctl print gui/$(id -u)`

- Display the status of a specific user agent:

`launchctl print gui/$(id -u)/{{service_label}}`

- Start or restart a loaded user agent immediately:

`launchctl kickstart -k gui/$(id -u)/{{service_label}}`

- Send a termination signal to a running user agent (it may restart depending on its configuration):

`launchctl kill SIGTERM gui/$(id -u)/{{service_label}}`

- Unload a user agent from the current GUI login domain:

`launchctl bootout gui/$(id -u)/{{service_label}}`

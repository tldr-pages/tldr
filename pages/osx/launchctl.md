# launchctl

> Control Apple's `launchd` manager for launch daemons (system-wide services) and launch agents (per-user programs).
> `launchd` loads XML-based `*.plist` files placed in the appropriate locations, and runs the corresponding commands according to their defined schedule.
> Note: `bootstrap`, `bootout` and `kickstart` replace the deprecated `load`, `unload` and `start`. Jobs are identified by a target of a domain plus the service label, e.g. `gui/501/local.example.agent` or `system/local.example.daemon`.
> More information: <https://keith.github.io/xcode-man-pages/launchctl.1.html>.

- Load a user-specific agent into the GUI domain of the current user, so it is loaded at login:

`launchctl bootstrap gui/{{uid}} ~/Library/LaunchAgents/{{my_script}}.plist`

- Load a system-wide daemon, so it is loaded at boot even if no user logs in:

`sudo launchctl bootstrap system /Library/LaunchDaemons/{{system_daemon}}.plist`

- Show all loaded agents and daemons, with the PID of the ones currently running and the last exit code:

`launchctl list`

- Unload a currently loaded agent, e.g. to make changes:

`launchctl bootout gui/{{uid}}/{{label}}`

- Manually run a loaded agent or daemon, even if it is not the right time:

`launchctl kickstart gui/{{uid}}/{{label}}`

- Restart a loaded service, killing the running instance first:

`launchctl kickstart -k gui/{{uid}}/{{label}}`

- Manually send a signal to the process of a loaded service, if it is running:

`launchctl kill {{signal_name}} gui/{{uid}}/{{label}}`

- Enable a service that has been disabled, so it can be loaded again:

`launchctl enable gui/{{uid}}/{{label}}`

# launchctl

> Control Apple's `launchd` manager for launch daemons (system-wide services) and launch agents (per-user programs).
> `launchd` loads XML-based `*.plist` files placed in the appropriate locations, and runs the corresponding commands according to their defined schedule.
> More information: <https://manned.org/launchctl>.

- Activate a user-specific agent to be loaded into `launchd` whenever the user logs in:

`launchctl load ~/Library/LaunchAgents/{{my_script}}.plist`

- Activate an agent which requires root privileges to run and/or should be loaded whenever any user logs in (note the absence of `~` in the path):

`sudo launchctl load /Library/LaunchAgents/{{root_script}}.plist`

- Activate a system-wide daemon to be loaded whenever the system boots up (even if no user logs in):

`sudo launchctl load /Library/LaunchDaemons/{{system_daemon}}.plist`

- Show all loaded agents/daemons, with the PID if the process they specify is currently running, and the exit code returned the last time they ran:

`launchctl list`

- Unload a currently loaded agent, e.g. to make changes (note: the plist file is automatically loaded into `launchd` after a reboot and/or logging in):

`launchctl unload ~/Library/LaunchAgents/{{my_script}}.plist`

- Manually run a known (loaded) agent/daemon, even if it is not the right time (note: this command uses the agent's label, rather than the filename):

`launchctl start {{script_file}}`

- Manually kill the process associated with a known agent/daemon, if it is running:

`launchctl stop {{script_file}}`

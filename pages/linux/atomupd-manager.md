# atomupd-manager

> Manage SteamOS updates.
> More information: <https://github.com/evlaV/atomupd-daemon>.

- Check for available updates:

`sudo atomupd-manager check`

- Update to a specific image:

`sudo atomupd-manager update`

- Print the current tracked update channel:

`atomupd-manager tracked-branch`

- List available update channels:

`atomupd-manager list-branches`

- Switch to a specific update channel:

`sudo atomupd-manager switch-branch {{stable|beta|preview|rc|bc|pc|main}}`

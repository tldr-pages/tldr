# waydroid

> Waydroid is a container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu.
> Documentation: <https://docs.waydro.id/>.
> More information: <https://waydro.id/>.

- Start Waydroid:

`waydroid`

- Initialize Waydroid (required on first run or after reinstalling Android):

`waydroid init`

- Install a new Android app from file:

`waydroid app install {{path/to/file.apk}}`

- Launch an Android app by its package name:

`waydroid app launch {{com.example.app}}`

- Start or stop the Waydroid session:

`waydroid session {{start/stop}}`

- Manage the Waydroid Container:

`waydroid container {{start/stop/restart/freeze/unfreeze}}`

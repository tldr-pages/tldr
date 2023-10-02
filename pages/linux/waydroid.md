# waydroid

> A container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu.
> More information: <https://docs.waydro.id>.

- Start Waydroid:

`waydroid`

- Initialize Waydroid (required on first run or after reinstalling Android):

`waydroid init`

- Install a new Android app from a file:

`waydroid app install {{path/to/file.apk}}`

- Launch an Android app by its package name:

`waydroid app launch {{com.example.app}}`

- Start or stop the Waydroid session:

`waydroid session {{start|stop}}`

- Manage the Waydroid container:

`waydroid container {{start|stop|restart|freeze|unfreeze}}`

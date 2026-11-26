# waydroid

> A container-based approach to boot a full Android system on a regular Linux system like Ubuntu.
> More information: <https://docs.waydro.id/usage/waydroid-command-line-options>.

- Start Waydroid:

`waydroid show-full-ui`

- Initialize Waydroid (required on first run or after reinstalling Android):

`sudo waydroid init`

- Check the container status:

`waydroid status`

- Install a new Android app from a file:

`waydroid app install {{path/to/file}}.apk`

- Start or stop the Waydroid session:

`waydroid session {{start|stop}}`

- Manage the Waydroid container:

`sudo waydroid container {{start|stop|restart|freeze|unfreeze}}`

- Open Waydroid shell:

`sudo waydroid shell`

- Adjust Waydroid window dimensions:

`waydroid prop set persist.waydroid.{{width|height}} {{number}}`

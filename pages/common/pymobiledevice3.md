# pymobiledevice3

> Interact with a connected iDevice (iPhone, iPad, ...).
> More information: <https://github:com/doronz88/pymobiledevice3>.

- List connected devices:

`pymobiledevice3 usbmux list`

- Print information on connected device:

`pymobiledevice3 lockdown info`

- View all syslog lines (including debug messages):

`pymobiledevice3 syslog live`

- Filter out only messages containing the word "SpringBoard":

`pymobiledevice3 syslog live -m SpringBoard`

- Restart device:

`pymobiledevice3 diagnostics restart`

- Pull all crash reports from device:

`pymobiledevice3 crash pull /path/to/crashes`

- Manage the media directory:

`pymobiledevice3 afc shell`

- List all installed applications and their details:

`pymobiledevice3 apps list`

- List query only a specific set os apps:

`pymobiledevice3 apps query BUNDLE_ID1 BUNDLE_ID2`

- Create a TCP tunnel from your HOST to the device:

`pymobiledevice3 usbmux forward HOST_PORT DEVICE_PORT [-d]`

- Create a full backup of the device:

`pymobiledevice3 backup2 backup --full DIRECTORY`

- Restore a given backup:

`pymobiledevice3 backup2 restore DIRECTORY`

- Perform a software update by a given IPSW file/url:

`pymobiledevice3 restore update -i /path/to/ipsw | url`

- Get interactive JavaScript shell on any open tab:

`pymobiledevice3 webinspector js-shell`

- List currently opened tabs is device's browser:

`pymobiledevice3 webinspector opened-tabs`

- Get interactive JavaScript shell on new remote automation tab:

`pymobiledevice3 webinspector js-shell --automation`

- Launch an automation session to view a given URL:

`pymobiledevice3 webinspector launch URL`

- Get a a selenium-like shell:

`pymobiledevice3 webinspector shell`

- Mount the DDI (DeveloperDiskImage) (**Required for some of the :developer commands**):

`pymobiledevice3 mounter auto-mount`

- Simulate a `lat long` location (iOS < 17.0):

`pymobiledevice3 developer simulate-location set -- lat long`

- Simulate a `lat long` location (iOS >= 17.0):

`pymobiledevice3 developer dvt simulate-location set -- lat long`

- Clear the simulated location:

`pymobiledevice3 developer dvt simulate-location clear`

- Take a screenshot from the device:

`pymobiledevice3 developer dvt screenshot /path/to/screen:png`

- View detailed process list (including ppid, uid, guid, sandboxed, etc):

`pymobiledevice3 developer dvt sysmon process single`

- Kill a process:

`pymobiledevice3 developer dvt kill PID`

- List files in a given directory (un-chrooted):

`pymobiledevice3 developer dvt ls PATH`

- Launch an app by its bundle name:

`pymobiledevice3 developer dvt launch com:apple:mobilesafari`

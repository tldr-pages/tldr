# idevicecrashreport

> Retrieve crash reports from an iOS device.
> More information: <https://manned.org/idevicecrashreport>.

- Retrieve crash reports and move them to a specified directory:

`idevicecrashreport {{path/to/directory}}`

- Retrieve crash reports without removing them from the device:

`idevicecrashreport --keep {{path/to/directory}}`

- Extract crash reports into separate `.crash` files:

`idevicecrashreport --extract {{path/to/directory}}`

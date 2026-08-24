# toolbox rmi

> Remove Toolbx images.
> See also: `toolbox rm`.
> More information: <https://manned.org/toolbox-rmi>.

- Remove one or more Toolbx image:

`toolbox rmi {{image_name1 image_name2 ...}}`

- Remove all Toolbx images:

`toolbox rmi {{[-a|--all]}}`

- Force the removal of a Toolbx image which is currently being used by a container (the container will be removed as well):

`toolbox rmi {{[-f|--force]}} {{image_name}}`

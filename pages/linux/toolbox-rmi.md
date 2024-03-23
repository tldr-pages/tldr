# toolbox rmi

> Remove `toolbox` images.
> See also: `toolbox rm`.
> More information: <https://manned.org/toolbox-rmi.1>.

- Remove one or more `toolbox` image:

`toolbox rmi {{image_name1 image_name2 ...}}`

- Remove all `toolbox` images:

`toolbox rmi --all`

- Force the removal of a `toolbox` image which is currently being used by a container (the container will be removed as well):

`toolbox rmi --force {{image_name}}`

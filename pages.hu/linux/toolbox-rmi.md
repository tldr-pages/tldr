# toolbox rmi

> Egy vagy több `toolbox` kép eltávolítása. Lásd még: `toolbox rm`. További információ: <https://manned.org/toolbox-rmi.1>.

- A `toolbox` kép eltávolítása:

`toolbox rmi {{image_name}}`

- Az összes `toolbox` kép eltávolítása:

`toolbox rmi --all`

- Egy olyan `toolbox` kép eltávolításának kikényszerítése, amelyet jelenleg egy konténer használ (a konténer is eltávolításra kerül):

`toolbox rmi --force {{image_name}}`

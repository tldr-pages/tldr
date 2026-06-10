# chown

> Փոխել ֆայլերի և գրացուցակների օգտագործողի և խմբի սեփականությունը:.
> Տես նաև՝ `chgrp`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>:.

- Փոխել ֆայլի/տեղեկատուի սեփականատեր օգտագործողին.:

`sudo chown {{user}} {{path/to/file_or_directory}}`

- Փոխեք ֆայլի/տեղեկատուի սեփականատեր օգտագործողին և խմբին.:

`sudo chown {{user}}:{{group}} {{path/to/file_or_directory}}`

- Փոխեք սեփականատեր օգտվողին և խմբին, որպեսզի երկուսն էլ ունենան `user` անունը:

`sudo chown {{user}}: {{path/to/file_or_directory}}`

- Փոխեք ֆայլի խումբը մի խմբի, որին պատկանում է ներկայիս օգտվողը.:

`chown :{{group}} {{path/to/file_or_directory}}`

- Ռեկուրսիվ կերպով փոխել գրացուցակի սեփականատիրոջը և դրա բովանդակությունը.:

`sudo chown {{[-R|--recursive]}} {{user}} {{path/to/directory}}`

- Փոխել խորհրդանշական հղման սեփականատիրոջը.:

`sudo chown {{[-h|--no-dereference]}} {{user}} {{path/to/symlink}}`

- Փոխեք ֆայլի/տեղեկատուի սեփականատիրոջը՝ հղումային ֆայլին համապատասխանելու համար.:

`sudo chown --reference {{path/to/reference_file}} {{path/to/file_or_directory}}`

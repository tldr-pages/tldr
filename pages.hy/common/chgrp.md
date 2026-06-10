# chgrp

> Փոխել ֆայլերի և գրացուցակների խմբային սեփականությունը:.
> Տես նաև՝ `chown`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html>:.

- Փոխել ֆայլի/տեղեկատուի սեփականատիրոջ խումբը.:

`chgrp {{group}} {{path/to/file_or_directory}}`

- Ռեկուրսիվ կերպով փոխել գրացուցակի սեփականատիրոջ խումբը և դրա բովանդակությունը.:

`chgrp {{[-R|--recursive]}} {{group}} {{path/to/directory}}`

- Փոխեք խորհրդանշական հղման սեփականատերերի խումբը.:

`chgrp {{[-h|--no-dereference]}} {{group}} {{path/to/symlink}}`

- Փոխեք ֆայլի/տեղեկատուի սեփականատիրոջ խումբը՝ հղումային ֆայլին համապատասխանելու համար.:

`chgrp --reference {{path/to/reference_file}} {{path/to/file_or_directory}}`

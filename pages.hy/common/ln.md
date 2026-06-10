# ln

> Ստեղծեք հղումներ դեպի ֆայլեր և գրացուցակներ:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html>:.

- Ստեղծեք խորհրդանշական հղում դեպի ֆայլ կամ գրացուցակ.:

`ln {{[-s|--symbolic]}} /{{path/to/file_or_directory}} {{path/to/symlink}}`

- Ստեղծեք խորհրդանշական հղում՝ կապված այն վայրի հետ, որտեղ գտնվում է հղումը.:

`ln {{[-s|--symbolic]}} {{path/to/file_or_directory}} {{path/to/symlink}}`

- Գոյություն ունեցող խորհրդանշական հղումը վերագրեք՝ մեկ այլ ֆայլ մատնանշելու համար.:

`ln {{[-sf|--symbolic --force]}} /{{path/to/new_file}} {{path/to/symlink}}`

- Ստեղծեք կոշտ հղում դեպի ֆայլ.:

`ln /{{path/to/file}} {{path/to/hardlink}}`

# git միաձուլում-մեկ-ֆայլ

> Լուծել մեկ ֆայլի միաձուլումը չնչին միաձուլումից հետո:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-merge-one-file>:.

- Լուծեք ֆայլի միաձուլման պարզ կոնֆլիկտ.:

`git merge-one-file {{path/to/file}}`

- Օգտագործեք որպես օգնական ֆայլի միաձուլման ինդեքսում.:

`git merge-index git-merge-one-file {{path/to/file}}`

- Կառավարեք երկուական ֆայլի միաձուլումը.:

`git merge-one-file -p {{path/to/file}}`

- Կիրառել կարդալ-ծառից հետո սկրիպտային միաձուլման մեջ.:

`git read-tree -m {{branch1}} {{branch2}} && git merge-index git-merge-one-file {{path/to/file}}`

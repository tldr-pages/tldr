# git միաձուլում

> Միավորել մասնաճյուղերը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-merge>:.

- Միավորեք մասնաճյուղերը ձեր ընթացիկ մասնաճյուղում.:

`git merge {{branch_name1 branch_name2 ...}}`

- Խմբագրել միաձուլման հաղորդագրությունը.:

`git merge {{[-e|--edit]}} {{branch_name}}`

- Միավորել մասնաճյուղը և ստեղծել միաձուլման հանձնառություն.:

`git merge --no-ff {{branch_name}}`

- Պատճենեք ճյուղի վիճակը աշխատանքային ծառի մեջ և բեմադրեք այն (Նշում. Օգտագործեք `git commit` փաստացի commit-ը ստեղծելու համար):

`git merge --squash {{branch_name}}`

- Հակամարտությունների դեպքում դադարեցնել միաձուլումը.:

`git merge --abort`

- Միաձուլել՝ օգտագործելով հատուկ ռազմավարություն.:

`git merge {{[-s|--strategy]}} {{strategy}} {{[-X|--strategy-option]}} {{strategy_option}} {{branch_name}}`

# git update-ref

> Git հրամանը Git refs ստեղծելու, թարմացնելու և ջնջելու համար:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-update-ref>:.

- Ջնջել ref, որն օգտակար է առաջին commit-ի փափուկ վերակայման համար.:

`git update-ref -d {{HEAD}}`

- Թարմացրեք ref-ը հաղորդագրությամբ.:

`git update-ref -m {{message}} {{HEAD}} {{4e95e05}}`

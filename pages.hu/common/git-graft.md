# git graft

> Egy adott ág commitjainak egyesítése egy másik ágba, és a forráság törlése. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-graft>.

- A célágban nem szereplő összes commit beolvasztása a forráságból a célágba, és a forráság törlése:

`git graft {{source_branch}} {{target_branch}}`

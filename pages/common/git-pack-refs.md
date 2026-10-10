# git pack-refs

> Pack branches and tags into a single file to improve repository performance.
> More information: <https://git-scm.com/docs/git-pack-refs>.

- Pack all tags and references that are already packed (branches are left as loose files):

`git pack-refs`

- Pack all references, including branches:

`git pack-refs --all`

- Pack all references without removing the original loose files:

`git pack-refs --all --no-prune`

- Pack only references matching a pattern:

`git pack-refs --include "{{refs/heads/*}}"`

- Pack all references except those matching a pattern:

`git pack-refs --all --exclude "{{refs/tags/*}}"`

- Pack references only if needed (e.g. when there are too many loose references):

`git pack-refs --auto`

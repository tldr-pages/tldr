# git summary

> Run grep as directed but replace the given files with the pattern.
> Works only on git tracked files
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sed>.

- Replace the string 'this' with 'that':

`git sed 'this' 'that'`

- Replace the string and then commit the resulting changes with a standard commit message:

`git sed -c 'this' 'that'`

- Replace the string passing regex flags to `sed` :

`git sed -f g 'this' 'that'`

- Replace the string only in the given pathspec:

`git sed 'this' 'that' -- lake/`

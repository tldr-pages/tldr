# git release

> Git-címke létrehozása egy kiadáshoz. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-release>.

- Létrehoz egy kiadást, és közzéteszi azt:

`git release {{tag_name}}`

- Létrehoz és tol egy aláírt kiadást:

`git release {{tag_name}} -s`

- Üzenettel ellátott kiadás létrehozása és pusholása:

`git release {{{tag_name}}} -m "{{message}}"`

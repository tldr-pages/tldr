# git-sh-i18n

> Internationalization helpers for Git shell scripts. Source this library to use `gettext` wrappers.
> Typically used inside Git's own shell scripts and not invoked directly.
> More information: <https://git-scm.com/docs/git-sh-i18n>.

- Source the library in a POSIX shell to make translation helpers available in the current process:

`sh -c '. "$(git --exec-path)/git-sh-i18n"; gettext "{{Hello, world}}"'`

- Interpolate variables within translatable strings using `eval_gettext` (note the escaped `$` to avoid early expansion):

`sh -c 'name={{Alice}}; . "$(git --exec-path)/git-sh-i18n"; eval_gettext "{{Hi, \$name}}"'`

- Print a formatted, translatable message with `gettext_printf`:

`sh -c '. "$(git --exec-path)/git-sh-i18n"; gettext_printf "{{%s files updated}}\n" {{3}}'`

- Run with a different locale (standard gettext environment variables apply):

`LANG={{es_ES.UTF-8}} sh -c '. "$(git --exec-path)/git-sh-i18n"; gettext "{{Commit}}"'`

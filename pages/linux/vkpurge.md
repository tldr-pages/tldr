# vkpurge

> List or remove old kernel versions left behind by `xbps`.
> The `version` arguments support shell globs.
> More information: <https://man.voidlinux.org/vkpurge.8>.

- List all removable kernel versions (or those matching `version` if the argument is specified):

`vkpurge list {{version}}`

- Remove all unused kernels:

`vkpurge rm all`

- Remove kernel versions matching `version`:

`vkpurge rm {{version}}`

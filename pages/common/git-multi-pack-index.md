# git multi-pack-index

> Manage a multi-pack-index file, which indexes objects across multiple packfiles to speed up object lookups.
> More information: <https://git-scm.com/docs/git-multi-pack-index>.

- Write a multi-pack-index file covering all packfiles in the repository:

`git multi-pack-index write`

- Write a multi-pack-index file along with a reachability bitmap:

`git multi-pack-index write --bitmap`

- Verify the contents of the multi-pack-index file:

`git multi-pack-index verify`

- Combine small packfiles into a new packfile until reaching a specific total size:

`git multi-pack-index repack --batch-size {{100m}}`

- Delete packfiles that no longer contain any objects referenced by the multi-pack-index:

`git multi-pack-index expire`

- Write a multi-pack-index file for a specific object directory:

`git multi-pack-index --object-dir {{path/to/objects}} write`

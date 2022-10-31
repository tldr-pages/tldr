# git pull

> Create/Merge feature branch.
> Feature branchs obey the format feature/<name>
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-feature>.

- Start a new feature branch:

`git feature {{feature_name}}`

- Finish the feature with --no-ff merge:

```bash
git checkout {{main_branch}}
git feature finish {{feature_name}}
```
- Finish the feature with --squash merge:

```bash
git checkout {{main_branch}}
git feature finish --squash {{feature_name}}
```

- Publish a feature to remote repository:

`git feature {{feature_name}} -r {{remote_name}}`

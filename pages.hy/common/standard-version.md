# ստանդարտ-տարբերակ

> Ավտոմատացրեք տարբերակները և փոփոխության մատյանների ստեղծումը՝ SemVer-ի և Conventional Commits-ի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/conventional-changelog/standard-version>:.

- Թարմացրեք փոփոխության log ֆայլը և նշեք թողարկումը.:

`standard-version`

- Նշեք թողարկումն առանց տարբերակի հարվածելու.:

`standard-version --first-release`

- Թարմացրեք փոփոխության մատյանը և նշեք ալֆա թողարկումը.:

`standard-version --prerelease alpha`

- Թարմացրեք փոփոխության մատյանը և նշեք թողարկման որոշակի տեսակ.:

`standard-version --release-as {{major|minor|patch}}`

- Նշեք թողարկումը՝ թույլ չտալով, որ կեռիկներն ստուգվեն կատարման քայլի ընթացքում.:

`standard-version --no-verify`

- Նշեք թողարկումը, որը կատարում է բոլոր փուլային փոփոխությունները, ոչ միայն ֆայլերը, որոնց վրա ազդում են `standard-version`-ը:

`standard-version --commit-all`

- Թարմացրեք որոշակի փոփոխության ֆայլ և նշեք թողարկումը.:

`standard-version --infile {{path/to/file.md}}`

- Ցուցադրել թողարկումը, որը կկատարվեր առանց դրանք կատարելու.:

`standard-version --dry-run`

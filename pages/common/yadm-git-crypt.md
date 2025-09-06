# yadm git-crypt

> Git Crypt enables transparent encryption and decryption of files in a git repository.
> See also: `git-crypt`.
> More information: <https://github.com/AGWA/git-crypt>.

- Initialize repo to use Git Crypt:

`yadm git-crypt init`

- Share the repository using GPG:

`yadm git-crypt add-gpg-user {{user_id}}`

- After cloning a repository with encrypted files, unlock them:

`yadm git-crypt unlock`

- Export a symmetric secret key:

`yadm git-crypt export-key {{path/to/key_file}}`

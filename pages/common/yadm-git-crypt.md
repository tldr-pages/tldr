# yadm git-crypt

> If `git-crypt` is installed, this command allows you to pass options directly to it.
> With the environment configured to use the yadm repository.
> Git Crypt enables transparent encryption and decryption of files in a git repository.
> More information: <https://github.com/AGWA/yadm>.

- Initialize repo to use git crypt:

`yadm git-crypt init`

- Share the repository with others (or with yourself) using GPG:

`yadm git-crypt add-gpg-user {{USER_ID}}`

- After cloning a repository with encrypted files, unlock with:

`yadm git-crypt unlock`

- Export a symmetric secret key:

`yadm git-crypt export-key {{/path/to/key_file}}`
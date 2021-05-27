# Making a Pull Request

Most people submit pull requests to the tldr-pages project
[using GitHub's web interface][pr-howto].

If you prefer, you can do most of the process using the command line instead.
The overall process should look somewhat like this:

1. Fork the tldr-pages/tldr repository on the GitHub web interface.

2. Clone your fork locally:
  `git clone https://github.com/{{your_username}}/tldr.git && cd tldr`

3. Create a feature branch, e.g. named after the command you plan to edit:
  `git checkout -b {{branch_name}}`

4. Make your changes (edit existing files or create new ones)

5. Commit the changes (following the [commit message guidelines][commit-msg]):
  `git commit --all -m "{{commit_message}}"`

6. Push the commit(s) to your fork:
  `git push origin {{branch_name}}`

7. Go to the GitHub page for your fork and click the green "pull request" button.

Please only send related changes in the same pull request.
Typically a pull request will include changes in a single file.
(Exceptions are [occasionally acceptable][mass-changes].)

[pr-howto]: ../CONTRIBUTING.md#submitting-a-pull-request
[commit-msg]: ../CONTRIBUTING.md#commit-message
[mass-changes]: https://github.com/tldr-pages/tldr/pulls?&q=is:pr+is:merged+label:"mass+changes"

# Updating your fork

Forks aren't updated automatically and in order to avoid merge conflicts it should be done manually and regularly. This is possible via the GitHub web interface by pressing `Fetch upstream` and `Fetch and merge` on the fork:
![Fetch and merge button in GitHub](https://user-images.githubusercontent.com/50295997/119873818-393e2000-bf25-11eb-8a0a-b804c293439b.png).

Alternatively it can also be done using Git in the terminal:

```bash
git checkout main
git remote add upstream https://tldr-pages/tldr.git # only run this if you don't already have the upstream remote for https://github.com/tldr-pages/tldr.git
git fetch upstream main
git rebase upstream/main
git push --force # not needed if you only want to update your local repository
```

# Changing the email of your last commit

If the email that you used for a commit isn't added to your GitHub account, you can either add it [here](https://github.com/settings/emails) or change the email of your last commit with the following commands:

```bash
git commit --amend --author="Name <new.email@example.com>"
git push --force
```

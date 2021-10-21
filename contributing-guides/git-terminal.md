# Opening a Pull Request

Most people submit pull requests to the tldr-pages project
[using GitHub's web interface][pr-howto].

If you prefer, you can do most of the process using the command-line instead.
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

7. Go to the GitHub page for your fork and click the green "Compare & pull request" button.

Please only send related changes in the same pull request.
Typically a pull request will include changes in a single file.
(Exceptions are [occasionally acceptable][mass-changes].)

[pr-howto]: ../CONTRIBUTING.md#submitting-a-pull-request
[commit-msg]: ../CONTRIBUTING.md#commit-message
[mass-changes]: https://github.com/tldr-pages/tldr/pulls?&q=is:pr+is:merged+label:"mass+changes"

# Updating your fork

Forks of GitHub repositories aren't updated automatically. To keep your fork up-to-date with the latest changes and avoid merge conflicts, you should update it regularly.

There are two ways to update your fork.

1. Via the GitHub web interface. Click `Fetch upstream` and then `Fetch and merge` on the fork as shown below:

![Fetch and merge button in GitHub](../images/github-fetch-and-merge-button.png)

2. Using Git in the terminal:

```bash
git checkout main
git remote add upstream https://github.com/tldr-pages/tldr.git  # only run if you don't already have the upstream remote (check with "git remote -v")
git fetch upstream main
git rebase upstream/main     # in case you have any merge conflicts, click the link below to see how to resolve them
git push --force-with-lease  # not needed if you only want to update your local repository
```
[How to resolve merge conflicts](https://docs.github.com/en/github/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)

# Changing the email of your last commit

If the email that you used for the last commit isn't associated with your GitHub account, you can either add it [here](https://github.com/settings/emails) or change the email of the commit with the following commands:

```bash
git commit --amend --author="Your Name <new.email@example.com>"
git push --force-with-lease
```

# Changing the email of any commit(s)

Let's take this commit history as an example:

| Commit Hash | Author Email
|---|---
| A | wrong@example.org
| B | correct@example.org
| C | correct@example.org
| D | wrong@example.org
| E | correct@example.org
| F (HEAD) | correct@example.org

To change the email of commits A and D, run

```bash
git reset A
git commit --amend --author="Your Name <correct@example.org>"
git cherry-pick B^..D # re-apply commits B to D
git commit --amend --author="Your Name <correct@example.org>"
git cherry-pick E^..HEAD
git push --force-with-lease
```

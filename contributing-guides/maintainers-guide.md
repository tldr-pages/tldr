# Maintainer's guide

The following guidelines are meant to provide a general basis
for the behavior expected of tldr-pages maintainers.

> [!NOTE]
> This text is a living standard;
> That is, it's is meant to *describe* the project's maintenance practices rather than *prescribe* them.
> As a maintainer, you're expected to refer to it for clarification
> About the collaborative workflows of the project,
> but also to propose changes to it
> that you feel would make it more useful
> as a guideline for current and future maintainers.

## I. Responding to Contributions

- When responding to issues or pull requests,
  remember that you're temporarily the face of the tldr-pages project.
  **Be welcoming and friendly**, and if you don't know how to answer,
  mention other maintainers who might provide input.

- **Help keep the project responsive**.
  New discussion threads (issues or pull requests)
  should ideally receive a response within three days.
  You can respond yourself
  or ask other members to provide their thoughts/opinions.
  In addition, if possible, try to hang around in the
  [Matrix chat room](https://matrix.to/#/#tldr-pages:matrix.org)
  regularly as well, or at least show up every now and then.

- **Know when and how to say no**.
  Occasionally ,requests or contributions need to be declined,
  at least in their current form.
  The project has established several guidelines to handle special cases
  — get familaiarize yourself with them, and reference them when necessary.
  Be polite yet firm: it saves everyone's time and patience
  to make expectations clear early.

- Always remember to **thank every contribution**,
  even if their contribution cannot be accepted - especially in those cases.
  Remember that
  [every form of contribution](https://github.com/all-contributors/all-contributors)
  (pull request, feature request, bug report, etc.)
  is a voluntary gift of time offered to the tldr-pages project
  by someone who cares about it,
  so make sure it's clear that we don't take it for granted.

- Whenever possible, **keep the entire contribution process web-based**
  to ensure it is accessible and straightforward.
  If you're comfortable with Git, consider offering to perform
  interactive rebases or other command-line operations
  on behalf of contributors,
  or assisting them if they want to do it themselves.

## II. Handling PRs

- Pull requests should be merged once they
  (1) **Pass the automated tests** GitHub Actions and CLA signing verification.
  (2) Have all **review comments addressed** and resolved.
  (3) Receive **approval from two maintainers** (the second maintainer can merge immediately after approving).

- It's recommended to wait for a few hours before merging a Pull request that add new English pages. This is to allow other maintainers to review the changes and provide feedback.

- If a Pull request is non-English and there are automatic reviewers added via [CODEOWNERS](https://github.com/tldr-pages/tldr/blob/main/.github/CODEOWNERS), the PR at least needs one approval from one of the CODEOWNERS.
    - If a PR fails to get a review from one of the CODEOWNERS after a few days, the first maintainer should ping the CODEOWNERS for review.
    - If it still lingers around for **over 10 days without an approval from one of the CODEOWNERS**, the PR can be merged if it has two approvals.
    - If it only has one approval, please read the next point.

- If a PR fails to get a review from a second maintainer after a few days,
  the first maintainer should ping others for review.
    - If it still lingers around for **over a week without a second maintainer’s approval**, the first maintainer (if Owner) can go ahead and merge it.
    Otherwise, a message can be sent in the chatroom asking other maintainers to review the PR.

- If the only issues holding up a merge are **trivial fixes**
  (typos, syntax errors, etc.), and the author doesn't respond in a day or two,
  **maintainers can make the necessary changes themselves**,
  and proceed with the merge process.

- If a PR **stops getting feedback from the submitter** for more than a month,
  any maintainer can choose to take over the PR
  and make the necessary changes to get the content ready for merging.

- During the review process, make sure that contributors, especially new ones,
  are not **overwhelmed with too many change requests**.
  Be mindful of signs of fatigue (less enthusiastic responses, slower reactions),
  and relax review standards if necessary — minor issues can always be fixed later.

- For pull requests with major/breaking/architectural changes that are **not ready to be merged**, it is suggested to label them with the `decision` label and discuss the changes with the other maintainers in the chatroom.

- When merging PRs, use the **merge strategy that produces a clean Git history**:
  If there's a single commit in the PR,
  or if the multiple commits are not semantically independent changes,
  use the `Squash and merge` method.
  (Don't forget to clean up the body of the squashed commit message.)
  If instead, the PR author took the time to craft
  individual, informative messages for each commit,
  then use the `Rebase and merge` method,
  to honor that work and preserve the history of the changes.
  For less clear-cut cases, a simple heuristic you can follow
  is that if there are more "dirty" commits than "clean" commits,
  then prefer squash, else do a rebase.

- It is suggested to clean up the commit message when merging a PR. For small commits, use:

  ```txt
  page-name: a short description of the change

  Co-authored-by: ...
  ```

  If you think a more descriptive message is needed, use asterisks:

  ```txt
  page-name: a short description of the change

  * some more information
  * ...

  ---------

  Co-authored-by: ...
  ```

- It is suggested to preserve the `Co-authored-by` message when cleaning the body of a squashed commit message unless the change done was trivial.

- Although having push access allows committing directly to the repository to all branches (except the main branch),
  please **create pull requests for all of your changes**.
  This ensures that the entire process that regular contributors go through
  is also exposed to maintainers,
  who can then identify and address bottlenecks or inconveniences.
  Similarly, **avoid merging your own PRs** unless approved by other maintainers.

- At the last week of October, all applicable PRs that wouldn't get merged
 in time can be labelled as `hacktoberfest-accepted`.

## III. Transparency

- All non-confidential requests or mail made on behalf of the project
 should be documented as an issue with the [archive](https://github.com/tldr-pages/tldr/issues?q=label%3Aarchive) label
  and must be communicated with other maintainers.
- All repository/organization settings changes must be documented as an issue with the [archive](https://github.com/tldr-pages/tldr/issues?q=label%3Aarchive) label.

## IV. Handling failing actions and CLA checks

- While merging multiple pull requests at the same time there is a chance that the deploy step might fail in the GitHub Actions workflow. In such cases, the maintainer should only **re-run** the workflow of the recently merged commit (to prevent previous commits from overwriting assets).
- If the CLA check is frozen at the message "Status waiting to be reported", it is recommended to close and reopen the pull requests to retrigger the check (and notify the contributor about the same).

For reference to see if a contributor has signed the CLA, visit the dashboard at <https://cla-assistant.io/>.

## V. Creating a client specification release

### Pre-requisites

- Ensure client specification changes are discussed with the other maintainers and community members in GitHub and chatroom, and the changes have been agreed upon and enough time has been provided for everyone to review the changes.
- Tag all client spec PRs under a [milestone](https://github.com/tldr-pages/tldr/milestones) for ease of release.
- Ensure [GPG signing](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key) has been setup for your account.
- It is suggested to prepare the release notes to add to the client specification release in advance.
    - The release notes should mention pending breaking architectural changes from previous client specifications (if any).
    - Along with the changelog, the release notes must explain the client specification changes in detail along with examples (if any).

### Steps

1. Merge all applicable PRs that modify the client specification and ensure they are documented in the [CHANGELOG section of client specification](/CLIENT-SPECIFICATION.md#changelog).
2. Bump the version to the upcoming release (in the client specification file) and inform other maintainers in the chatroom about the release.
3. Clone the repository locally to your device:

```sh
git clone https://github.com/tldr-pages/tldr
```

4. Cross check the additions, version and changelog details in the client specification file.
5. Create a signed tag using the command

```sh
git tag -s vX.Y.Z
```

> [!NOTE]\
> Replace `X.Y.Z` with the client specification version.

> [!TIP]\
> If any commits are merged after the client specification file's version bump commit and before tagging, when creating the tag
> you can use the command: `git tag -s vX.Y.Z <commit hash>` (i.e. `git tag -s v2.3 3b17800`) to tag a older commit.

6. Verify the created signed tag's details using the command:

```sh
git tag -v vX.Y.Z
```

7. Now, push the tag to the repository using the command:

```sh
git push origin vX.Y.Z
```

8. Verify the tag's creation [here](https://github.com/tldr-pages/tldr/tags) and then navigate to the [releases](https://github.com/tldr-pages/tldr/releases) tab and draft a new release.
9. Choose the tag you just pushed and add the release notes prepared previously along with an appropriate release title and then enable the "Create a discussion for this release" option.
10. Now publish the release and proceed with the below post-release steps.

### Post-release steps

- Once the release is published, [view the workflow run of `copy-release-assets.yml`](https://github.com/tldr-pages/tldr/actions/workflows/copy-release-assets.yml) and after its successful completion ensure the assets are copied from the previous release.
- Notify the [social media managers](https://github.com/tldr-pages/access#social-media-accounts) to post about the client specification release on Mastodon and other platforms to inform the wider community about the release.

## VI. Periodic Maintenance Tasks

To maintain the quality and relevance of the tldr-pages project, maintainers are encouraged to regularly perform the following tasks:

- **Monitor software updates** — Regularly check if the tools documented in tldr-pages have been updated — especially those introducing breaking changes. Update relevant pages accordingly and, where appropriate, encourage contributors to do the same.

- **Validate external links** — Periodically check that all links across the documentation and pages are functional. Consider using https://github.com/tldr-pages/tldr-maintenance/issues/129 for link-checking pages and other automated link-checking tools to detect broken URLs for documentation. Then replace or remove any broken links.

- **Update client status on the wiki** — Ensure the list of clients in the project's [Wiki](https://github.com/tldr-pages/tldr/wiki) reflects their current development status (active, inactive, deprecated). Reach out to maintainers of clients when needed for status updates.

- **Track and document new clients** — Look out for new tldr clients being developed. When appropriate, add them to the Wiki or relevant documentation, and encourage their maintainers to follow the project’s conventions and style guidelines.

- **Revise CONTRIBUTING.md and the Style Guide** — Make sure that [`CONTRIBUTING.md`](https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md) and the [Style Guide](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/style-guide.md) reflect current conventions. If community conventions shift, update these documents to guide future contributions.

- **Maintain collaborators and Org members list** — Periodically review the list of collaborators and organization members. Remove inactive members and onboard new contributors who have demonstrated consistent involvement. Document any changes using an issue with the `community` label.

- **Manage "Let's document" and translation requests** — Monitor and update issues labeled as `let's document` or language-specific translation requests. While these are often maintained by issue authors, there’s room for improvement through automation — for example, updating issue status based on milestones or completed PRs.

- **Review translated pages** — Check the [tldr-maintenance repository](https://github.com/tldr-pages/tldr-maintenance/issues/127) for issues or inconsistencies with translated pages.

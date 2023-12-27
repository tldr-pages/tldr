# Maintainer's guide

The following guidelines are meant to provide a general basis
for the behavior expected of tldr-pages maintainers.

> [!NOTE]
> This text is a living standard;
> that is, it is meant to *describe* the project's maintenance practices,
> rather than *prescribe* them.
> As a maintainer, you're expected to refer to it for clarification
> about the collaborative workflows of the project,
> but also to propose changes to it
> that you feel would make it more useful
> as a guideline for current and future maintainers.

## I. Responding to contributions

- When responding to issues or pull requests,
  remember that you're temporarily the face of the tldr-pages project.
  **Be welcoming and friendly**, and if you don't know how to answer,
  ping other maintainers who you think might have a say.

- **Help keep the project responsive**.
  New discussion threads (issues or pull requests)
  should receive a response within 3 days, ideally.
  You can respond yourself
  or ask other members to provide their thoughts/opinions.
  In addition, if possible, try to hang around in the
  [Matrix chat room](https://matrix.to/#/#tldr-pages:matrix.org)
  regularly as well, or at least show up every now and then.

- **Know when and how to say no**.
  Sometimes requests or contributions need to be declined,
  at least in their current form.
  The project has developed multiple guidelines over time to handle edge cases
  — get acquainted with them, and point them out when necessary.
  Be polite, but firm: it saves everyone's time and patience
  to make expectations clear early.

- Always remember to **thank every contribution**,
  even when it can't be accepted (in fact, especially then).
  Keep in mind that
  [every form of contribution](https://github.com/all-contributors/all-contributors)
  (pull request, feature request, bug report, etc.)
  is a voluntary gift of time offered to the tldr-pages project
  by someone who cares about it,
  so make sure it's clear that we don't take it for granted.

- Try to **keep the entire contribution process web-based**, if possible,
  to ensure it is accessible and straightforward.
  If you're comfortable with Git, consider offering to perform
  interactive rebases or other command-line operations
  on behalf of contributors,
  or assisting them if they want to do it themselves.

## II. Handling PRs

- PRs should be merged once they
  (1) **pass the automated tests** (GitHub Actions, CLA signing, etc.),
  (2) have the **review comments addressed**,
  (3) get **approved reviews by two maintainers** (the second maintainer can merge immediately after approving).

- It is suggested to wait for a few hours before merging a pull request with new additions to English pages. This is to allow other maintainers to review the changes and provide feedback.

- If a PR fails to get a review from a second maintainer after a few days,
  the first maintainer should ping others for review. If it still lingers around
  for **over a week without a second maintainer’s approval**,
  the first maintainer (if Owner) can go ahead and merge it. Otherwise, a message
  can be sent in the chatroom asking other maintainers to review the PR.

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

  ```
  page-name: a short description of the change

  Co-authored-by: ...
  ```
  if you think a more descriptive message is needed, use asterisks:
  ```
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

- All non-confidential requests/mail made/sent on behalf of the project
 should be documented as an issue with the [archive](https://github.com/tldr-pages/tldr/issues?q=label%3Aarchive) label
  and must be communicated with other maintainers.
- All repository/organization settings changes must be documented as an issue with the [archive](https://github.com/tldr-pages/tldr/issues?q=label%3Aarchive) label.

## IV. Handling failing actions and CLA checks

- While merging multiple pull requests at the same time there is a chance that the deploy step might fail in the GitHub Actions workflow. In such cases, the maintainer should only **re-run** the workflow of the commit which was last merged (to prevent overwriting of assets by previous commits).
- If the CLA check is frozen at the message "Status waiting to be reported", it is recommended to close and reopen the pull requests to retrigger the check (and notify the contributor about the same).

For reference to see if a contributor has signed the CLA, visit the dashboard at <https://cla-assistant.io/>.

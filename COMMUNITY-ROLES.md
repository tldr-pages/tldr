# Community roles

The following guidelines aim to keep the project vibrant and responsive,
by ensuring a **smooth transition flow between community roles** —
from newcomer, to occasional contributor, to regular contributor, to maintainer.
This way, the project should be able to adapt dynamically and flexibly
to the natural variations in availability and interest of its contributors,
improving long-term resilience, reducing the risk of burnout, and avoiding
[single points of failure](https://en.wikipedia.org/wiki/Bus_factor).

To this end, rather than _assigning_ roles and tasks to people,
these guidelines aim to **recognize the work that people already do**.
Everyone is therefore encouraged to get involved
and contribute to the project in whatever way they prefer,
and we will strive to **get barriers out of the way** of these contributions.

To ensure that these role transitioning processes are
straightforward, transparent, predictable, and impartial,
the metrics used are objective, easy to check, and explicitly described below.
(That's not to say they're hard-set rules:
exceptions can always be considered, via open community discussion.)


## When to change roles

- **Regular contributors should be added as collaborators in the repository.**
  Specifically: once a contributor has had _5 non-trivial pull requests merged_
  (see `https://github.com/tldr-pages/tldr/commits?author=<username>`)
  on a repository under the tldr-pages organization,
  they should be invited to become
  a **collaborator** in that repository.
  This means they will be able to push commits to that repository,
  as well as merge PRs, label and close issues, among other things.

- **Repository collaborators who regularly perform maintenance tasks should be added as organization members.**
  (Maintenance work means facilitating contributions by other people,
  which in this project typically consists in reviewing and/or merging PRs.)
  Specifically: once a repository collaborator has _merged at least 10 PRs_
  (see `https://github.com/tldr-pages/tldr/commits?committer=<username>`)
  and submitted at least _5 non-trivial reviews to PRs_
  (see `https://github.com/tldr-pages/tldr/pulls?q=reviewed-by:<username>`),
  which can overlap with the 10 they merged themselves,
  they should be invited to become a
  [**member**](https://github.com/orgs/tldr-pages/people)
  of the tldr-pages organization.
  This means they will be able to
  push commits to all of the organization's repositories,
  merge PRs, label and close issues, among other things.
  > [!NOTE]
  > All members of the tldr-pages organization
  > must make their membership public.

- **Organization members who remain active for a while should become organization owners.**
  Specifically: members of the tldr-pages organization
  who remain _active for at least 6 months_
  (see [`MAINTAINERS.md`](MAINTAINERS.md#organization-members))
  should be invited to become an
  [**owner**](https://help.github.com/articles/permission-levels-for-an-organization/)
  of the tldr-pages organization.
  This means they will be able to add people to the organization,
  manage all the organization's repositories, configure integrations, etc.

- **These roles are temporary, and that's OK.**
  People's interests and availability naturally change over time,
  so the project should regularly update the list of people in each role,
  in order to accurately reflect the active team managing the project
  (and to avoid conveying an undue sense of obligation
  on people whose priorities have shifted.)
  Specifically: If an organization member becomes _inactive for over 6 months_,
  their membership status should be equally deactivated.
  (They should nevertheless remain as collaborators
  in the repositories on which they have been active in the past.)
  Again, this is and merely a reflection
  of their actual involvement with the project,
  not a demotion or punishment.
  Indeed, if they return to active participation in the project,
  they should be added back to the organization, to reflect that fact.


## How to change roles

> [!NOTE]
> This section is aimed at owners in the tldr-pages organization
> (i.e. the group of people who are able to perform these changes).

If you notice a contributor being particularly active,
review their recent contributions to check whether a role transition is due,
according to the criteria defined in the previous section.
If a role change is warranted, **open a new issue proposing that role change**,
using one of the template messages below as a base.

### Adding new collaborators

1. Open an issue with the following message template (edit it as appropriate):

   ```
   Hi, @username! You seem to be enjoying contributing to the tldr-pages project.
   You now have had five distinct pull requests merged (<!-- REPLACE THIS WITH LINKS TO THE RELEVANT PRs -->)!
   That qualifies you to become a collaborator in this repository, as explained in our [community roles documentation](https://github.com/tldr-pages/tldr/blob/main/COMMUNITY-ROLES.md).

   As a collaborator, you will have commit access to the repository.
   That means you can merge pull requests, label and close issues, and perform various other maintenance tasks that are needed here and there.
   Of course, all of this is voluntary — you're welcome to contribute to the project in whatever ways suit your liking.

   If you do decide to start performing maintenance tasks, though, we only ask you to get familiar with the [maintainer's guide](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/maintainers-guide.md).

   So, what do you say? Can we add you as a collaborator?

   Either way, thanks for all your work so far!
   ```

2. Once they acknowledge the message, and if they accept the invitation,
   go to https://github.com/tldr-pages/tldr/settings/collaboration
   and add them to the repository as collaborator with write permissions.

3. Open a PR adding their name to the "Repository collaborators" section
   in [MAINTAINERS.md](MAINTAINERS.md#repository-collaborators).
   Make sure to include `Closes #<issue number>` in the PR description.
   The issue will then be automatically closed once the PR is merged.

### Adding new organization members

1. Open an issue with the following message template (edit it as appropriate):

   ```
   Hi, @username! After joining as a collaborator in the repository, you have been regularly performing maintenance tasks (<!-- REPLACE THIS WITH LINKS TO THE RELEVANT ISSUES AND/OR PRs -->).
   Thank you for that!
   According to our [community roles documentation](https://github.com/tldr-pages/tldr/blob/main/COMMUNITY-ROLES.md), you've now met the thresholds to be effectively considered an active maintainer of the project.
   To publicly acknowledge that fact, we'd like to add you to the tldr-pages organization.

   If you accept the invitation, we ask you to make your membership public, and (in case you don't already) start hanging out in our [Matrix chat room](https://matrix.to/#/#tldr-pages:matrix.org).
   Additionally, consider subscribing to the notifications from the various repositories under the [tldr-pages organization](https://github.com/tldr-pages).
   As one of the public faces of the tldr-pages project, it's also especially important that you follow and encourage the [project
   governance principles](https://github.com/tldr-pages/tldr/blob/main/GOVERNANCE.md).

   How does that sound? Are you up for it?
   ```

2. Once they acknowledge the message, and if they accept the invitation,
   go to https://github.com/orgs/tldr-pages/people
   and add them to the organization as a member.

3. Open a PR moving their name to the "Organization members" section
   in [MAINTAINERS.md](MAINTAINERS.md#organization-members).
   Make sure to include `Closes #<issue number>` in the PR description.
   The issue will then be automatically closed once the PR is merged.

### Adding new organization owners

1. Open an issue with the following message template (edit it as appropriate):

   ```
   Hi, @username! You've been an active tldr-pages organization member for over 6 months.
   Thanks for sticking around this far and helping out!
   According to our [community roles documentation](https://github.com/tldr-pages/tldr/blob/main/COMMUNITY-ROLES.md), you're now eligible for becoming an owner in the organization.

   That means you will, from now on, be part of the team responsible for performing role changes (like this one!) in the community.
   When performing such role transitions, make sure to follow the process described in the [COMMUNITY-ROLES.md](https://github.com/tldr-pages/tldr/blob/main/COMMUNITY-ROLES.md) document.

   Is that OK with you? Let us know!

   Either way, thanks so much for all the work you've done so far. You rock!
   ```

2. Once they acknowledge the message, and if they accept the invitation,
   go to https://github.com/orgs/tldr-pages/people
   and change their role from "member" to "owner".

3. Open a PR moving their name to the "Organization owners" section
   in [MAINTAINERS.md](MAINTAINERS.md#organization-owners).
   Make sure to include `Closes #<issue number>` in the PR description.
   The issue will then be automatically closed once the PR is merged.

### Removing inactive organization members

1. Open an issue with the following message template (edit it as appropriate):

   ```
   Hi, @username! As you know, our [community roles documentation](https://github.com/tldr-pages/tldr/blob/main/COMMUNITY-ROLES.md) defines processes for keeping the list of organization members in sync with the actual maintenance team.
   Since you haven't been active in the project for a while now, we'll be relieving you from the maintainer responsibilities.

   In practice, not much will change on your side, since you'll remain a collaborator in the repos you have been active in.
   That means **you will keep the ability to commit, merge PRs, label and close issues, etc.**, whenever you feel so inclined.
   If you don't, that's all right too!
   Every bit of work you already did for the tldr-pages project was a voluntary gift of your time to this community, which is deeply appreciated.
   Your efforts have contributed to a project which helps hundreds of people every day — be proud of it!

   And of course, you're welcome back anytime as an active maintainer, if you so choose — in which case, just let us know and we'll re-add you to the organization, in accordance to the principles of our governance guidelines.
   In any case, we wish you the best of luck in your new endeavors!
   ```

2. Once they acknowledge the message (or after two weeks without any reaction),
   go to https://github.com/orgs/tldr-pages/people, click the gear icon in their row,
   and select the "Convert to outside collaborator" menu entry.

3. Open a PR moving their name to the "Past organization members" section
   in [MAINTAINERS.md](MAINTAINERS.md).
   Make sure to include `Closes #<issue number>` in the PR description.
   The issue will then be automatically closed once the PR is merged.

## Who can change roles
Any member of the community can (and is encouraged to) propose role changes
by following the process outlined [above](#how-to-change-roles).
[Owners of the tldr-pages organization](MAINTAINERS.md#organization-owners)
can then perform the actual role changes.

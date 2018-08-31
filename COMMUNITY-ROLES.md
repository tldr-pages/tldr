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
  on a repository under the tldr-pages organization,
  they should be invited to become
  a **collaborator** in that repository.
  This means they will be able to push commits to that repository,
  as well as merge PRs, label and close issues, among other things.

- **Collaborators who perform maintenance tasks should be made org members.**
  (Maintenance work is understood as facilitating contributions by other people,
  which in this project consists primarily of reviewing and/or merging PRs.)
  Specifically: once a repository collaborator has _merged at least 10 PRs_
  and submitted at least _5 non-trivial reviews to PRs_
  (either the same or different ones)
  they should be invited to become a
  [**member**](https://github.com/orgs/tldr-pages/people)
  of the tldr-pages organization.
  This means they will be able to
  push commits to all of the organization's repositories,
  merge PRs, label and close issues, among other things.
  _Note_: All members of the tldr-pages organization
  must make their membership public.

- **Maintainers who have been helping out for a while should become org owners.**
  Specifically: members of the tldr-pages organization
  who remain _active for at least 6 months_
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

*Note: this section is aimed at owners in the tldr-pages organization
(i.e. the group of people who are able to perform these changes).*

If you notice a contributor being particularly active,
review their recent contributions to check whether a role transition is due,
according to the criteria defined in the previous section.
If a role change is warranted, **open a new issue proposing that role change**,
using one of the template messages below as a base.

### For adding new collaborators

Open an issue with the following message:

> Hi, \@username(s)! You seem to be enjoying contributing to the tldr-pages project.
You now have had five distinct pull requests merged (\[LINKS TO THE RELEVANT PRs]),
which qualifies you to become a collaborator in this repository,
as explained in our
\[governance guidelines](https://github.com/tldr-pages/tldr/blob/master/GOVERNANCE.md).
>
> As a collaborator, you will have commit access
and can therefore merge pull requests from others, label and close issues,
and perform various other maintenance tasks that are needed here and there.
Of course, all of this is voluntary
— you're welcome to contribute to the project in whatever ways suit your liking.
>
> If you do decide to start performing maintenance tasks, though,
we only ask you to get familiar with the
\[maintainer's guide](https://github.com/tldr-pages/tldr/blob/master/contributing-guides/maintainers-guide.md).
>
> Thanks for all your work so far!

Once they acknowledge the message,
go to https://github.com/tldr-pages/tldr/settings/collaboration
and add them to the repository as collaborator with write permissions.

### For adding new organization members

Open an issue with the following message:

> Hi, \@username(s)! After joining as a collaborator in the repository,
you have been regularly performing maintenance tasks. Thank you for that!
According to
\[GOVERNANCE.md](https://github.com/tldr-pages/tldr/blob/master/GOVERNANCE.md),
you've now met the thresholds to be effectively considered
an active maintainer of the project (\[LINKS TO THE RELEVANT PRs]).
To publicly acknowledge that fact, we'll add you to the tldr-pages organization.
>
> If you accept the invitation, we ask you to make your membership public,
and (in case you don't already) start hanging out in our Gitter chat room.
You'll now be one of the public faces of the tldr-pages project.
Welcome aboard!

Once they acknowledge the message,
go to https://github.com/orgs/tldr-pages/people
and add them to the organization as a member.

### For adding new organization owners:

Open an issue with the following message:

> Hi, \@username(s)! You've been an active tldr-pages org member for over 6 months.
Thanks for sticking around this far and helping out!
According to
\[GOVERNANCE.md](https://github.com/tldr-pages/tldr/blob/master/GOVERNANCE.md),
you're now eligible for becoming an owner of the organization.
>
> That means you will, from now on, be part of the team
responsible for performing role changes (like this one!) in the community.
Before performing such role transitions, make sure to review the
\[COMMUNITY-ROLES.md](https://github.com/tldr-pages/tldr/blob/master/COMMUNITY-ROLES.md)
document.
>
> Thanks for all the work you've done so far. You rock!

Once they acknowledge the message,
go to https://github.com/orgs/tldr-pages/people
and change their role from "member" to "owner".

Afterwards, add their name to the list of current organization owners below.

### For removing inactive organization members:

Open an issue with the following message:

> Hi, @username(s)! As you know, our
\[governance guidelines](https://github.com/tldr-pages/tldr/blob/master/GOVERNANCE.md)
define processes for keeping the list of organization members
in sync with the actual maintenance team.
Since you haven't been active in the project for a while now,
we'll be moving you to the status of former maintainer.
>
> In practice, not much will change on your side,
since you'll remain a collaborator in the repos you have been active in,
so \*\*you will keep the ability to commit, merge PRs, label and close issues, etc.\*\*,
if you feel so inclined. But even if you don't,
keep in mind that every bit of work you already did for the tldr-pages project
was a voluntary gift of your time to this community.
Your efforts have contributed to a project
which helps hundreds of people every day — be proud of it!
>
> And of course, you're welcome back anytime as a maintainer, if you so choose
— in which case we'll re-add you to the organization,
as is also described in the guidelines.
In any case, we wish you the best of luck in your new endeavors!

Once they acknowledge the message (or after a week without any reaction),
go to https://github.com/orgs/tldr-pages/people, click the gear icon in their row,
and select the "Convert to outside collaborator" menu entry.

Afterwards, edit this file to move their name to the "Past owners" section below.

Finally, once the membership changes are complete and the lists are updated,
close the issue opened to track this process.


## Who can change roles

### Current owners

The following people are the current owners of the tldr-pages organization,
have admin access to all of its repositories,
and are responsible for performing role changes in the community.

- Romain Prieto ([@rprieto](https://github.com/rprieto)):
  created the the project on [8 December 2013](https://github.com/tldr-pages/tldr/commit/11264d9)
- Agniva De Sarker ([@agnivade](https://github.com/agnivade)):
  [27 September 2016](https://gitter.im/tldr-pages/tldr?at=57eaedefe4e41c6a4afc2f47) — present
- Starbeamrainbowlabs ([@sbrl](https://github.com/sbrl)):
  [23 April 2017](https://gitter.im/tldr-pages/tldr?at=58fc6fce3e27cac331b5c397) — present

### Past owners

The following people used to be owners in the tldr-pages organization,
and have reduced their participation or otherwise moved on to other projects.
Their contributions and dedication have ensured the success of the tldr project,
and for that they'll always be appreciated.

- Igor Shubovych ([@igorshubovych](https://github.com/igorshubovych)):
  until [18 January 2018](https://github.com/tldr-pages/tldr/issues/1878#issuecomment-358610454)
- Ruben Vereecken ([@rubenvereecken](https://github.com/rubenvereecken)):
  until [18 January 2018](https://github.com/tldr-pages/tldr/issues/1878#issuecomment-358610454)
- Felix Yan ([@felixonmars](https://github.com/felixonmars)):
  until [18 January 2018](https://github.com/tldr-pages/tldr/issues/1878#issuecomment-358610454)
- Dan Zimmerman ([@danzimm](https://github.com/danzimm)):
  until [18 January 2018](https://github.com/tldr-pages/tldr/issues/1878#issuecomment-358610454)
- Eduardo Gurgel ([@edgurgel](https://github.com/edgurgel)):
  until [18 January 2018](https://github.com/tldr-pages/tldr/issues/1878#issuecomment-358610454)
- Arvid Gerstmann ([@Leandros](https://github.com/Leandros)):
  until [18 January 2018](https://github.com/tldr-pages/tldr/issues/1878#issuecomment-358610454)
- Leandro Ostera ([@ostera](https://github.com/ostera)):
  until [18 January 2018](https://github.com/tldr-pages/tldr/issues/1878#issuecomment-358610454)
- Waldir Pimenta ([@waldyrious](https://github.com/waldyrious)): until [26 August 2018](https://github.com/tldr-pages/tldr/issues/2257)

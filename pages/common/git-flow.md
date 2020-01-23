# git flow

> A collection of Git extensions to provide high-level repository operations for Vincent Driessen's branching model.
> More information: <https://github.com/nvie/gitflow>.

- Initialize it inside an existing git repository:

`git flow init`

- Start developing a new feature. It creates a new branch based on develop:

`git flow feature start {{feature}}`

- Finish development on a feature branch, merging it into the `develop` branch and deleting it:

`git flow feature finish {{feature}}`

- Publish a feature to the remote server so others can work on it too:

`git flow feature publish {{feature}}`

- Get a feature published by another user:

`git flow feature pull origin <feature>`

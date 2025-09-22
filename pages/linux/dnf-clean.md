# dnf clean

> Perform cleanup of temporary files kept for Red Hat-based repositories.
> More information: <https://dnf.readthedocs.io/en/latest/command_ref.html#clean-command>.

- Remove cache files generated from the repository metadata:

`dnf clean dbcache`

- Mark the repository metadata as expired:

`dnf clean expire-cache`

- Remove repository metadata:

`dnf clean metadata`

- Remove any cached packages from the system:

`dnf clean packages`

- Clean up all DNF repository specific metadata and cached files (all of the above):

`dnf clean all`

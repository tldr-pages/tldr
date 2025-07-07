# dnf builddep

> Install dependencies to build a given package. 
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf changelog`, `dnf config-manager`, `dnf copr`, `dnf debug`, `dnf debuginfo-install`, `dnf download`, `dnf generate_completion_cache`, `dnf groups-manager`, `dnf leaves`, `dnf local`, `dnf migrate`, `dnf modulesync`, `dnf needs-restarting`, `dnf post-transaction-actions`, `dnf repoclosure`, `dnf repodiff`, `dnf repograph`, `dnf repomanage`, `dnf reposync`, `dnf show-leaves`, `dnf system-upgrade`, `dnf versionlock`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/builddep.html>.

- Install dependencies for a given package:

`dnf builddep {{path/to/specification.spec}}`

- Install dependencies for a given package but ignore unavailable:

`dnf builddep --skip-unavailable {{path/to/specification.spec}}`

- Define the RPM macro to a given expression:

`dnf builddep {{[-D|--define]}} '{{expression}}'`

- Define an argument for a `.spec` file path:

`dnf builddep --spec {{argument}}`

- Define an argument for a `.rpm` file path:

`dnf builddep --srpm {{argument}}`

- Display help:

`dnf builddep --help-cmd`

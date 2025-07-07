# dnf builddep

> Install dependencies to build a given package.
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf`.
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

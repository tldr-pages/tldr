# rpmbuild

> RPM Package Build tool.
> More information: <https://manned.org/man/rpmbuild>.

- Build binary and source packages:

`rpmbuild -ba {{path/to/spec_file}}`

- Build a binary package without source package:

`rpmbuild -bb {{path/to/spec_file}}`

- Specify additional variables when building a package:

`rpmbuild -bb {{path/to/spec_file}} --define "{{variable1}} {{value1}}" --define "{{variable2}} {{value2}}"`

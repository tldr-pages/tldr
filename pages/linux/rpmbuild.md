# rpmbuild

> RPM Package Build tool.

- Build binary and source packages:

`rpmbuild -ba {{spec file}}`

- Build a binary package without source package:

`rpmbuild -bb {{spec file}}`

- Pass variables when building package:

`rpmbuild -bb {{spec file}}  --define "{{variable1}} {{value1}}" --define "{{variable2 value2}}"`

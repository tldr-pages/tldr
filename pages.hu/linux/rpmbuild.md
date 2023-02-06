# rpmbuild

> RPM csomagkészítő eszköz. További információ: <https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/>.

- Bináris és forráscsomagok építése:

`rpmbuild -ba {{path/to/spec_file}}`

- Bináris csomag építése forráscsomag nélkül:

`rpmbuild -bb {{path/to/spec_file}}`

- További változók megadása a csomag építése során:

`rpmbuild -bb {{path/to/spec_file}} --define "{{variable1}} {{value1}}" --define "{{variable2}} {{value2}}"`

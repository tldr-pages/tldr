# rpmbuild

> Instrumentul Creare pachete RPM.
> Mai multe informaţii: <https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/>

- Construiți pachete binare și sursă:

`rpmbuild -ba {{path/to/spec_file}}`

- Construiți un pachet binar fără pachet sursă:

`rpmbuild -bb {{path/to/spec_file}}`

- Specificați variabile suplimentare atunci când construiți un pachet:

`rpmbuild -bb {{path/to/spec_file}} --define "{{variable1}} {{value1}}" --define "{{variable2}} {{value2}}"`

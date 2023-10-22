# virt-xml-validate

> Validate `libvirt` XML files against a schema.
> If a schema is not specified, the schema is determined by the root element in the XML file.
> More information: <https://libvirt.org/manpages/virt-xml-validate.html>.

- Validate an XML file against a specific schema:

`virt-xml-validate {{path/to/file.xml}} {{schema}}`

- Validate the domain XML against the domain schema:

`virt-xml-validate {{path/to/domain.xml}} domain`

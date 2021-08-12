# dget

> Descărcați pachete Debian.
> Mai multe informaţii: <https://manpages.debian.org/dget>

- Descărcați un pachet binar:

`dget {{package_name}}`

- Descărcaţi şi extrageţi o sursă de pachete din fişierul său `.dsc`:

`dget {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

- Descărcaţi o sursă de pachete tarball din fişierul său `.dsc`, dar nu o extrageţi:

`dget -d {{http://deb.debian.org/debian/pool/main/h/haskell-tldr/haskell-tldr_0.4.0-2.dsc}}`

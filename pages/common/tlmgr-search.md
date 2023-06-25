# tlmgr search

> Search for TeX Live packages using (Perl) regular expressions.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Search for a package name and descriptions of all locally installed packages from a specific regular expression:

`tlmgr search "{{regular_expression}}"`

- Search for all file names of all locally installed packages from a regular expression:

`tlmgr search --file "{{regular_expression}}"`

- Search for all file names, package names, and descriptions of all locally installed packages from a regular expression:

`tlmgr search --all "{{regular_expression}}"`

- Search the TeX Live database, instead of the local installation:

`tlmgr search --global "{{regular_expression}}"`

- Restrict the matches for package names and descriptions (but not for file names) to whole words:

`tlmgr search --all --word "{{regular_expression}}"`

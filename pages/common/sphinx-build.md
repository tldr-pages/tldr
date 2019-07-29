# sphinx-build

> Generates documentation from the files in sourcedir and places it in the outputdir.
> More information: <http://www.sphinx-doc.org/en/master/man/sphinx-build.html>.

- Build documentation as "epub" and put it in "builddir":

`sphinx-build -b {{html|epub|text|...}} {{path/to/source_dir}} {{path/to/build_dir}}`

- Build documentations intended for readthedocs.io:

`pip install -U sphinx sphinx-rtd-theme ; sphinx-build -b {{html}} {{path/to/docs_dir}} {{path/to/builddir}}`

- Common builders:

`html dirhtml singlehtml htmlhelp qthelp devhelp epub applehelp latex man texinfo text gettext doctest linkcheck xml pseudoxml`

# twine

> Twine is a utility for publishing Python packages on PyPI.
> Subcommands such as `twine upload` have their own usage documentation.
> More information: <https://twine.readthedocs.io>.

- Upload to the Test PyPI [r]epository and verify things look right:

`twine upload -r testpypi dist/*`

- Upload to PyPI:

`twine upload dist/*`

- Specify [u]sername and [p]assword while uploading to PyPI:

`twine upload -u {{username}} -p {{password}} dist/*`

- Upload to an alternative repository url:

`twine upload --repository-url {{repository_url}} dist/*`

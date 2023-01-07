# twine

> Utility for publishing Python packages on PyPI.
> More information: <https://twine.readthedocs.io/en/stable/#commands>.

- Upload to PyPI:

`twine upload dist/*`

- Upload to the Test PyPI [r]epository to verify things look right:

`twine upload -r testpypi dist/*`

- Upload to PyPI with a specified [u]sername and [p]assword:

`twine upload -u {{username}} -p {{password}} dist/*`

- Upload to an alternative repository URL:

`twine upload --repository-url {{repository_url}} dist/*`

- Check that your distribution's long description should render correctly on PyPI:

`twine check dist/*`

- Upload using a specific pypirc configuration file:

`twine upload --config-file {{configuration_file}} dist/*`

- Continue uploading files if one already exists (only valid when uploading to PyPI):

`twine upload --skip-existing dist/*`

- Upload to PyPI showing detailed information:

`twine upload --verbose dist/*`

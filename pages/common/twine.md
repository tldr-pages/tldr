# twine

> Utility for publishing Python packages on PyPI.
> More information: <https://twine.readthedocs.io>.

- Upload to PyPI:

`twine upload dist/*`

- Upload to the Test PyPI [r]epository and verify things look right:

`twine upload -r testpypi dist/*`

- Upload to PyPI with a specified [u]sername and [p]assword:

`twine upload -u {{username}} -p {{password}} dist/*`

- Upload to an alternative repository URL:

`twine upload --repository-url {{repository_url}} dist/*`

- Check that your distribution’s long description should render correctly on PyPI:

`twine check dist/*`

- Upload with a specific pypirc configuration file (<https://packaging.python.org/en/latest/specifications/pypirc>):

`twine upload --config-file {{config_file}} dist/*`

- Continue uploading files if one already exists. (Only valid when uploading to PyPI. Other implementations may not support this.):

`twine upload --skip-existing dist/*`

- Display extra verbosity during upload:

`twine upload --verbose dist/*`

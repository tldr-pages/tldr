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

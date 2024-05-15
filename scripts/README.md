# Scripts

The current directory contains useful scripts used/to use with `tldr` pages.

## Summary

This section contains a summary of the scripts available in this directory. For more information about each script, please refer to the header of each script.

- [pdf](pdf/README.md) directory contains the `render.py` and `build-pdf.sh` script and related resources to generate a PDF document of tldr-pages for a specific language or platform (or both).
- [build.sh](build.sh) script builds the ZIP archives of the `pages` directory.
- [build-index.sh](build-index.sh) script builds the index of available pages.
- [check-pr.sh](check-pr.sh) script checks the pages syntax and performs various checks on the PR.
- [deploy.sh](deploy.sh) script deploys the ZIP and PDF archives to the static website repository.
- [send-to-bot.py](send-to-bot.py) is a Python script that send the build or tests output to tldr-bot.
- [set-alias-page.py](set-alias-page.py) is a Python script to generate or update alias pages.
- [set-more-info-link.py](set-more-info-link.py) is a Python script to generate or update more information links across pages.
- [set-page-title.py](set-page-title.py) is a Python script to update the title across pages.
- [test.sh](test.sh) script runs some basic tests on every PR/commit to make sure that the pages are valid and that the code is formatted correctly.
- [wrong-filename.sh](wrong-filename.sh) script checks the consistency between the filenames and the page title.
- [update-command.py](update-command.py) is a Python script to update the common contents of a command example across all languages.

## Compatibility

The below table shows the compatibility of user-executable scripts with different platforms.

| Script | Linux | macOS (`osx`) | Windows |
| ------ | ----- | ----- | ------- |
| [render.py](pdf/render.py) | ✅ | ✅ | ✅ |
| [build-pdf.sh](pdf/build-pdf.sh) | ✅ | ✅ | ❌ |
| [build.sh](build.sh) | ✅ | ✅ | ❌ |
| [set-alias-pages.py](set-alias-pages.py) | ✅ | ✅ | ✅ |
| [set-more-info-link.py](set-more-info-link.py) | ✅ | ✅ | ✅ |
| [set-page-title.py](set-page-title.py) | ✅ | ✅ | ✅ |
| [wrong-filename.sh](wrong-filename.sh) | ✅ | ❌ | ❌ |
| [update-command.py](update-command.py) | ✅ | ✅ | ✅ |

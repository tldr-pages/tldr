# gcloud components update

> Update all installed components of Google Cloud CLI to the latest version or a specified version.

More information: [Google Cloud CLI Documentation](https://cloud.google.com/sdk/gcloud/reference/components/update)

- Update all components to the latest version:

  ```bash
  gcloud components update
  ```

- Update all components to a specific version (e.g., 1.2.3):

  ```bash
  gcloud components update --version=1.2.3
  ```

- Check the current version of Google Cloud CLI:

  ```bash
  gcloud version
  ```

- List all available components and their versions:

  ```bash
  gcloud components list
  ```

- Update components without confirmation (useful for automation scripts):

  ```bash
  gcloud components update --quiet
  ```
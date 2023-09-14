# linode-cli object-storage

> Command-line interface to manage Linode Object Storage via `linode-cli`.

- List all Object Storage buckets:

`linode-cli object-storage buckets list`

- Create a new Object Storage bucket:

`linode-cli object-storage buckets create --cluster [cluster-id] --label [bucket-label]`

- Delete an Object Storage bucket:

`linode-cli object-storage buckets delete [cluster-id] [bucket-label]`

- List Object Storage cluster regions:

`linode-cli object-storage clusters list`

- List access keys for Object Storage:

`linode-cli object-storage keys list`

- Create a new access key for Object Storage:

`linode-cli object-storage keys create --label [label]`

- Revoke an access key for Object Storage:

`linode-cli object-storage keys revoke [access-key-id]`

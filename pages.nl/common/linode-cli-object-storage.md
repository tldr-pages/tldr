# linode-cli object-storage

> Beheer Linode Object Storage.
> Bekijk ook: `linode-cli`.
> Meer informatie: <https://www.linode.com/docs/products/tools/cli/guides/object-storage/>.

- Toon alle Object Storage buckets:

`linode-cli object-storage buckets list`

- Maak een nieuwe Object Storage bucket:

`linode-cli object-storage buckets create --cluster {{cluster_id}} --label {{bucket_label}}`

- Verwijder een Object Storage bucket:

`linode-cli object-storage buckets delete {{cluster_id}} {{bucket_label}}`

- Toon alle Object Storage cluster regio's:

`linode-cli object-storage clusters list`

- Toon alle access keys voor Object Storage:

`linode-cli object-storage keys list`

- Maak een nieuw access key voor Object Storage:

`linode-cli object-storage keys create --label {{label}}`

- Trek een access key terug voor Object Storage:

`linode-cli object-storage keys revoke {{access_key_id}}`

# exo storage

> Manage the Exoscale Simple Object Storage (SOS) service.
> More information: <https://community.exoscale.com/product/storage/object-storage/>.

- Create a new SOS bucket:

`exo storage mb {{bucket_name}}`

- Upload a file to a bucket:

`exo storage put {{file_path}} {{bucket_name}}/{{prefix/}}`

- List the objects within a bucket:

`exo storage ls {{bucket_name}}`

- Simulate the download of an object from a bucket:

`exo storage get {{bucket_name}}/{{object_key}} {{local_path}} --dry-run`

- Manage the metadata of an object:

`exo storage metadata add {{bucket_name}}/{{object_key}} {{key=value}}`

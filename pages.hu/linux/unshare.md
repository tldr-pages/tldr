# unshare

> Parancs végrehajtása új, felhasználó által meghatározott névterekben. További információ: <https://www.kernel.org/doc/html/latest/userspace-api/unshare.html>.

- Parancs végrehajtása a csatlakoztatott hálózatokhoz való hozzáférés megosztása nélkül:

`unshare --net {{command}} {{command_arguments}}`

- Parancs végrehajtása gyermekfolyamatként, csatlakoztatások, folyamatok vagy hálózatok megosztása nélkül:

`unshare --mount --pid --net --fork {{command}} {{command_arguments}}`

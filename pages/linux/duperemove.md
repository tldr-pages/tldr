# duperemove

> Finds duplicate file system extents and optionally schedule them for deduplication.
> An extent is small part of a file inside the file system.
> On some file systems one extent can be referenced multiple times, when parts of the content of the files are identical.
> More information: <https://markfasheh.github.io/duperemove/>.

- Search for duplicate extents in a directory and show them:

`duperemove -r {{path/to/directory}}`

- Deduplicate duplicate extents on a Btrfs or XFS (experimental) file system:

`duperemove -r -d {{path/to/directory}}`

- Use a hash file to store extent hashes (less memory usage and can be reused on subsequent runs):

`duperemove -r -d --hashfile={{path/to/hashfile}} {{path/to/directory}}`

- Limit I/O threads (for hashing and dedupe stage) and CPU threads (for duplicate extent finding stage):

`duperemove -r -d --hashfile={{path/to/hashfile}} --io-threads={{N}} --cpu-threads={{N}} {{path/to/directory}}`

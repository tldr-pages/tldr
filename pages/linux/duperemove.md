# duperemove

> Finds duplicate extends and optionally schedule them for deduplication.
> More information: <https://markfasheh.github.io/duperemove/>.

- Search for duplicate extends in a directory and show them:

`duperemove -r {{directory}}`

- Deduplicate duplicate extends on a Btrfs or XFS (experimental) file system:

`duperemove -r -d {{directory}}`

- Use a hash file to store extend hashes (less memory usage and can be reused on subsequent runs):

`duperemove -r -d --hashfile={{hashfile}} {{directory}}`

- Limit I/O threads (for hashing and dedupe stage) and CPU threads (for duplicate extend finding stage):

`duperemove -r -d --hashfile={{hashfile}} --io-threads={{N}} --cpu-threads={{N}} {{directory}}`

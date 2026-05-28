# b4 shazam

> Retrieve and apply patches from a public-inbox archive directly to the current Git tree.
> More information: <https://b4.docs.kernel.org/en/latest/maintainer/am-shazam.html>.

- Retrieve patches from a thread and apply them directly to the current branch:

`b4 shazam {{message_id}}`

- Retrieve patches and create a `FETCH_HEAD` for merging (like a pull request):

`b4 shazam {{[-H|--make-fetch-head]}} {{message_id}}`

- Retrieve patches and automatically merge using the cover letter as the merge commit message:

`b4 shazam {{[-M|--merge]}} {{message_id}}`

- Retrieve patches, add your `Signed-off-by` and `Link:` trailers, then merge:

`b4 shazam {{[-slM|--add-my-sob --add-link --merge]}} {{message_id}}`

- Retrieve patches and start interactive conflict resolution when applicable:

`b4 shazam {{[-H|--make-fetch-head]}} --resolve {{message_id}}`

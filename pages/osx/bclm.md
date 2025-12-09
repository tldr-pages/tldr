# bclm

> Set a custom charge limit on MacBooks.
> More information: <https://github.com/zackelia/bclm#usage>.

- Set the charge limit to about 80% (for Intel machines, the battery charge level may be slightly lower than the set value):

`sudo bclm write {{77}}`

- Read the current charge limit:

`bclm read`

- Keep the charge limit after rebooting/smc reset:

`sudo bclm persist`

- Remove the persistent charge limit:

`sudo bclm unpersist`

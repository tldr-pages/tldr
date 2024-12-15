# bclm

> Set a custom charge limit on MacBooks.
> More information: <https://github.com/zackelia/bclme>.

- Set the charge limit to 80% (battery charge level may be slightly lower than set value for Intel machines):

`sudo bclm write {{77}}`

- Read the current charge limit:

`bclm read`

- Keep the charge limit after reboot/smc reset:

`sudo bclm persist`

- Remove the persisting charge limit:

`sudo bclm unpersist`

# bclm

> Set a custom chrage limit on MacBooks.
> More information: <https://github.com/zackelia/bclme>.

- Install the wrapper:

`brew tap zackelia/formulae && brew install bclm`

- Set the charge limit to 80% (battery charge level may be slightly lower than set value for intel machines):

`sudo bclm write 77`

- Read the current charge limit:

`bclm read`

- Keep the charge limit after reboot/smc reset:

`sudo bclm persist`

- Remove the persisting charge limit:

`sudo bclm unpersist`

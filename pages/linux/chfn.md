# chfn

> Update `finger` info for a user.
> More information: <https://manned.org/chfn>.

- Update a user's "Name" field in the output of `finger`:

`chfn {{[-f|--full-name]}} {{new_display_name}} {{username}}`

- Update a user's "Office Room Number" field for the output of `finger`:

`chfn {{[-o|--office]}} {{new_office_room_number}} {{username}}`

- Update a user's "Office Phone Number" field for the output of `finger`:

`chfn {{[-p|--office-phone]}} {{new_office_telephone_number}} {{username}}`

- Update a user's "Home Phone Number" field for the output of `finger`:

`chfn {{[-h|--home-phone]}} {{new_home_telephone_number}} {{username}}`

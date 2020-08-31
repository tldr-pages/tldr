# nodemon

> automatically restart node application when watched files are changed.
> More information: <https://www.npmjs.com/package/nodemon/>.

- Watch a spesific file for reloads:

`nodemon --inspect filename.js`

- manually restart nodemon (note nodemon must already be active for this to work):

`rs`

- ignore spesific files

`nodemon --ignore filename.js`

- use any node argument in nodemon

`nodemon yournodeargument`

- monitor non node files

`nodemon --exec "python --verbose" filename.py`

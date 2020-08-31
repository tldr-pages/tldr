# nodemon

> Automatically restart node application when watched files are changed.
> More information: <https://www.npmjs.com/package/nodemon/>.

- Watch a spesific file for reloads:

`nodemon --inspect filename.js`

- Manually restart nodemon (note nodemon must already be active for this to work):

`rs`

- Ignore spesific files:

`nodemon --ignore filename.js`

- Use any node argument in nodemon:

`nodemon yournodeargument`

- Monitor non node files:

`nodemon --exec "python --verbose" filename.py`

var os = require('os');
var util = require('util');

exports.url = function(command) {
  if (process.env.NODE_ENV == 'development') {
      return 'http://localhost:3000/pages/' + osGroup() + '/' + command + '.md';
  } else {
      return 'http://raw.github.com/rprieto/tldr/master/pages/' + osGroup() + '/' + command + '.md';
  }
}

function osGroup() {
  if (os.platform() == 'darwin') {
    return 'osx';
  } else {
    return 'unsupported';
  }
}

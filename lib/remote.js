var os   = require('os');
var util = require('util');
var env  = require('./env');

exports.url = function(command) {
  if (env.test) {
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

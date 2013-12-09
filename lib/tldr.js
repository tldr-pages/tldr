var util    = require('util');
var request = require('./request');
var output  = require('./output');

exports.get = function(command) {
  request.get(command, function(err, body) {
    if (err) {
      util.error('ERROR: ' + err);
      process.exit(1);
    } else {
      util.puts(output.fromMarkdown(body));
    }
  });
};

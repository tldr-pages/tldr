var util     = require('util');
var resolver = require('./resolver');
var output   = require('./output');

exports.get = function(command, options) {
  resolver.get(command, options, function(err, body) {
    if (err) {
      util.error('ERROR: ' + err);
      process.exit(1);
    } else {
      util.puts(output.fromMarkdown(body));
    }
  });
};

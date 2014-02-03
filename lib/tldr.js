var resolver = require('./resolver');
var output   = require('./output');

exports.get = function(command, options) {
  resolver.get(command, options, function(err, body) {
    if (err) {
      console.error('ERROR: ' + err);
      process.exit(1);
    } else {
      console.log(output.fromMarkdown(body));
    }
  });
};

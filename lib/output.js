var markit = require('markit');
var colors = require('ansicolors');
var styles = require('ansistyles');

exports.fromMarkdown = function(markdown) {
  var r = new markit.Renderer();

  // automatically created by new lines
  r.paragraph = function(text) {
    return text;
  };

  // high-level command description
  r.list = function(body, ordered) {
    return body + '\n';
  }
  
  r.listitem = function(text) {
    return '  ' + styles.italic(styles.bright(text)) + '\n';
  };

  // description for each example
  r.header = function(text, level) {
    if (level == 2) {
      return colors.green('  - ' + text) + '\n';
    } else {
      return '';
    }
  };

  // example code
  r.codespan = function(code, lang) {
    return '  ' + colors.white('  ' + colors.bgBlack(code)) + '\n\n';
  };
  
  return markit(markdown, {renderer: r});
};

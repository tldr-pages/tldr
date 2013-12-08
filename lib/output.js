var markit = require('markit');
var colors = require('ansicolors');
var styles = require('ansistyles');

var allElements = [
  'blockcode', 'blockhtml', 'blockquote', 'codespan', 'emphasis',
  'header', 'hrule', 'image', 'linebreak', 'link', 'list', 'listitem',
  'paragraph', 'strikethrough', 'strong', 'table', 'tablecell', 'tablerow'];

exports.fromMarkdown = function(markdown) {

  var r = new markit.Renderer();

  // ignore all syntax by default
  allElements.forEach(function(e) {
    r[e] = function() { return ''; }
  });

  // paragraphs just pass through (automatically created by new lines)
  r.paragraph = function(text) {
    return text;
  };

  // lists = high-level command description
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

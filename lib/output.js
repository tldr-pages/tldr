var markit = require('markit');
var unhtml = require('unhtml');
var colors = require('ansicolors');
var styles = require('ansistyles');

var TOKEN_REGEX = /\{\{(.*?)\}\}/g;

var COMMAND_BACKGROUND = 'bgBlack';
var COMMAND_FOREGROUND = 'red';
var COMMAND_TOKENS     = 'white';

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

  //
  // High-level description
  //

  r.blockquote = function(text) {
    text = text.replace('\n', '\n  ')
    return '  ' + styles.italic(text);
  };

  //
  // Examples
  //

  r.list = function(body, ordered) {
    return '\n\n' + body + '\n';
  }
  
  r.listitem = function(text) {
    return '  - ' + text + '\n';
  };

  r.codespan = function(code, lang) {
    var highlighted = code.replace(TOKEN_REGEX, highlightToken);
    return '    ' + colors[COMMAND_BACKGROUND](colors[COMMAND_FOREGROUND](highlighted)) + '';
  };

  return '\n' + unhtml(markit(markdown, {renderer: r})) + '\n';

};

function highlightToken(match, capture) {
  return colors.open[COMMAND_TOKENS] + capture + colors.open[COMMAND_FOREGROUND];
}

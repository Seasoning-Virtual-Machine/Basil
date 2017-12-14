grammar Basil;

options {
    language=Python3;
}

/*
 * Parser Rules
 */

program: code + EOF;
code: line+;

line: (line_number (expression_statement (NEWLINE expression_statement?)*)) | COMMENT;

line_number: NUMBER;
expression_statement: expression | statement;

statement: end_statement;
end_statement: END;

expression: arith_expr;
arith_expr: NUMBER ((PLUS | MINUS | TIMES | DIV) NUMBER)+;

/*
 * Lexer Rules
 */

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
EQUALS: '=';

NEWLINE: '\n';
END: 'END';

COMMENT: ['] ~[\r\n]* -> skip;
SPACE: [ \t\r\n] -> skip;

STRING: ["] ~["\r\n]* ["];

LETTERS: ([a-z] | [A-Z])+;
NUMBER: [0-9]+;
BOOLEAN: 'TRUE' | 'FALSE';

WS: [ \t\r\n\f]+ -> skip;
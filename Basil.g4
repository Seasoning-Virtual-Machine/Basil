grammar Basil;

options {
    language=Python3;
}

/*
 * Parser Rules
 */

code: line + EOF;

line: (line_number (expression | statement)) | COMMENT;

line_number: NUMBER;

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

END: 'END';

COMMENT: ['] ~[\r\n]* -> skip;
SPACE: [ \t\r\n] -> skip;

STRING: ["] ~["\r\n]* ["];

LETTERS: ([a-z] | [A-Z])+;
NUMBER: [0-9]+;
BOOLEAN: 'TRUE' | 'FALSE';

WS: [ \t\r\n\f]+ -> skip;
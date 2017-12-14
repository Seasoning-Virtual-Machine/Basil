grammar Basil;

options {
    language=Python3;
}

/*
 * Parser Rules
 */

arith_expr: NUMBER ((PLUS | MINUS | TIMES | DIV) NUMBER)+;

/*
 * Lexer Rules
 */

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';

END: 'END';

COMMENT: '\'' -> skip;
SPACE: [ \t\r\n] -> skip;

STRING: ["] ~["\r\n]* ["];

LETTERS: [a-z] | [A-Z] +;
NUMBER: [0-9] +;
BOOLEAN: 'TRUE' | 'FALSE';
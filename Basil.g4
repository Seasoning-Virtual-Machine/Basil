grammar Basil;

options {
    language=Python3;
}

/*
 * Parser Rules
 */

program: code+ END;
code: (line_number line (SEMICOLON line)*)+;

line: expression | statement | COMMENT;

line_number: NUMBER;

statement: assignment_statement | print_statement | input_statement | end_statement;
assignment_statement: LET ID EQUAL NUMBER;
print_statement: PRINT (STRING | NUMBER | BOOLEAN | expression)?;
input_statement: INPUT;
end_statement: END;

expression: arithmetic_expression;
arithmetic_expression: NUMBER ((PLUS | MINUS | TIMES | DIV) NUMBER)+;

/*
 * Lexer Rules
 */

PRINT: 'PRINT';
INPUT: 'INPUT';
LET: 'LET';

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
EQUAL: '=';

SEMICOLON: ';';
NEWLINE: '\n';
END: 'END';

COMMENT: ['] ~[\r\n]* -> skip;
SPACE: [ \t\r\n] -> skip;

STRING: ["] ~["\r\n]* ["];

LETTERS: ([a-z] | [A-Z])+;
NUMBER: [0-9]+;
BOOLEAN: 'TRUE' | 'FALSE';
ID: [a-z]+;

WS: [ \t\r\n\f]+ -> skip;
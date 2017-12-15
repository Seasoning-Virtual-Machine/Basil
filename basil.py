import antlr4
from BasilLexer import BasilLexer
from BasilListener import BasilListener
from BasilParser import BasilParser

import io


class BasilCompiler(BasilListener):
    def __init__(self, asm: io.FileIO):
        self.asm = asm
        self.arithmetic_operators = []

    def enterLine(self, ctx:BasilParser.LineContext):
        print(ctx.getText())

    def enterArithmetic_expression(self, ctx: BasilParser.Arithmetic_expressionContext):
        for item in ctx.getChildren():
            # print(item)

            if str(item).isnumeric():
                self.asm.write("PUSH,{},".format(item))

            elif str(item) in ["+", "-", "*", "/"]:
                self.arithmetic_operators.append(item)

    def exitArithmetic_expression(self, ctx: BasilParser.Arithmetic_expressionContext):
        for item in self.arithmetic_operators:
            if str(item) == "+":
                self.asm.write("ADD,")

            elif str(item) == "-":
                self.asm.write("SUB,")

            elif str(item) == "*":
                self.asm.write("MUL,")

            elif str(item) == "/":
                self.asm.write("DIV,")

        self.arithmetic_operators = []

    def enterStatement(self, ctx: BasilParser.StatementContext):
        text = ctx.getText().strip("0123456789 ")
        other = ctx.getText().strip(text)

        if text == "END":
            self.asm.write("HALT")

        elif text == "PRINT":
            self.asm.write("PRINT,{},".format(other))

        elif text == "INPUT":
            self.asm.write("IN,")


if __name__ == "__main__":
    lexer = BasilLexer(antlr4.FileStream("example.bas"))
    stream = antlr4.CommonTokenStream(lexer)
    parser = BasilParser(stream)
    tree = parser.code()

    with open("temp.sasm", "w") as asm:
        compile_ = BasilCompiler(asm)
        walker = antlr4.ParseTreeWalker()
        walker.walk(compile_, tree)

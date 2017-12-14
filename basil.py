import antlr4
from BasilLexer import BasilLexer
from BasilListener import BasilListener
from BasilParser import BasilParser

import io


class BasilCompiler(BasilListener):
    def __init__(self, asm: io.FileIO):
        self.asm = asm
        self.arithmetic_operators = []

    def enterArith_expr(self, ctx: BasilParser.Arith_exprContext):
        for item in ctx.getChildren():
            # print(item)

            if str(item).isnumeric():
                self.asm.write("PUSH,{},".format(item))

            elif str(item) in ["+", "-", "*", "/"]:
                self.arithmetic_operators.append(item)

    def exitArith_expr(self, ctx: BasilParser.Arith_exprContext):
        for item in self.arithmetic_operators:
            if str(item) == "+":
                self.asm.write("ADD,")

            elif str(item) == "-":
                self.asm.write("SUB,")

            elif str(item) == "*":
                self.asm.write("MUL")

            elif str(item) == "/":
                self.asm.write("DIV")

        self.arithmetic_operators = []

    def enterStatement(self, ctx: BasilParser.StatementContext):
        if ctx.getText() == "END":
            self.asm.write("HALT")


if __name__ == "__main__":
    lexer = BasilLexer(antlr4.FileStream("example.bas"))
    stream = antlr4.CommonTokenStream(lexer)
    parser = BasilParser(stream)
    tree = parser.code()

    with open("temp.sasm", "w") as asm:
        compile_ = BasilCompiler(asm)
        walker = antlr4.ParseTreeWalker()
        walker.walk(compile_, tree)

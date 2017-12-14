import antlr4
from BasilLexer import BasilLexer
from BasilListener import BasilListener
from BasilParser import BasilParser

import io


class BasilCompiler(BasilListener):
    def __init__(self, asm: io.FileIO):
        self.asm = asm

    def enterArith_expr(self, ctx: BasilParser.Arith_exprContext):
        for item in ctx.NUMBER():
            # print(item)
            self.asm.write("PUSH,{},".format(item))

    def enterStatement(self, ctx:BasilParser.StatementContext):
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

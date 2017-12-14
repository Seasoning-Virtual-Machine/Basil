import antlr4
from BasilLexer import BasilLexer
from BasilListener import BasilListener
from BasilParser import BasilParser


class BasilCompiler(BasilListener):
    def enterLine(self, ctx: BasilParser.LineContext):
        print(ctx.getText())


if __name__ == "__main__":
    lexer = BasilLexer(antlr4.FileStream("example.bas"))
    stream = antlr4.CommonTokenStream(lexer)
    parser = BasilParser(stream)
    tree = parser.code()
    compile_ = BasilCompiler()
    walker = antlr4.ParseTreeWalker()
    walker.walk(compile_, tree)

# Generated from python/MicroC.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



from MicroCCompiler.compiler.SymbolTable import SymbolTable
from MicroCCompiler.compiler.Scope import Scope
from MicroCCompiler.ast.IntLitNode import IntLitNode
from MicroCCompiler.ast.FloatLitNode import FloatLitNode
from MicroCCompiler.ast.AssignNode import AssignNode
from MicroCCompiler.ast.VarNode import VarNode
from MicroCCompiler.ast.WriteNode import WriteNode
from MicroCCompiler.ast.ReadNode import ReadNode
from MicroCCompiler.ast.ReturnNode import ReturnNode
from MicroCCompiler.ast.CondNode import CondNode
from MicroCCompiler.ast.StatementListNode import StatementListNode
from MicroCCompiler.ast.ASTNode import ASTNode
from MicroCCompiler.ast.BinaryOpNode import BinaryOpNode
from MicroCCompiler.ast.UnaryOpNode import UnaryOpNode
from MicroCCompiler.ast.IfStatementNode import IfStatementNode
from MicroCCompiler.ast.WhileNode import WhileNode



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\"")
        buf.write("\u00dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\7\34\u00a5\n\34\f\34\16")
        buf.write("\34\u00a8\13\34\3\35\6\35\u00ab\n\35\r\35\16\35\u00ac")
        buf.write("\3\36\7\36\u00b0\n\36\f\36\16\36\u00b3\13\36\3\36\3\36")
        buf.write("\6\36\u00b7\n\36\r\36\16\36\u00b8\3\37\3\37\7\37\u00bd")
        buf.write("\n\37\f\37\16\37\u00c0\13\37\3\37\3\37\3 \3 \3 \3 \7 ")
        buf.write("\u00c8\n \f \16 \u00cb\13 \3 \3 \3 \3 \3 \3!\6!\u00d3")
        buf.write("\n!\r!\16!\u00d4\3!\3!\3\"\3\"\3#\3#\3\u00c9\2$\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C\2E\2\3\2\5\3\2$$\5")
        buf.write("\2\13\f\17\17\"\"\4\2C\\c|\2\u00e1\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\3G\3\2\2")
        buf.write("\2\5I\3\2\2\2\7P\3\2\2\2\tR\3\2\2\2\13V\3\2\2\2\r\\\3")
        buf.write("\2\2\2\17a\3\2\2\2\21c\3\2\2\2\23e\3\2\2\2\25g\3\2\2\2")
        buf.write("\27i\3\2\2\2\31n\3\2\2\2\33t\3\2\2\2\35{\3\2\2\2\37~\3")
        buf.write("\2\2\2!\u0083\3\2\2\2#\u0089\3\2\2\2%\u008b\3\2\2\2\'")
        buf.write("\u008d\3\2\2\2)\u0090\3\2\2\2+\u0093\3\2\2\2-\u0096\3")
        buf.write("\2\2\2/\u0099\3\2\2\2\61\u009b\3\2\2\2\63\u009d\3\2\2")
        buf.write("\2\65\u009f\3\2\2\2\67\u00a1\3\2\2\29\u00aa\3\2\2\2;\u00b1")
        buf.write("\3\2\2\2=\u00ba\3\2\2\2?\u00c3\3\2\2\2A\u00d2\3\2\2\2")
        buf.write("C\u00d8\3\2\2\2E\u00da\3\2\2\2GH\7=\2\2H\4\3\2\2\2IJ\7")
        buf.write("u\2\2JK\7v\2\2KL\7t\2\2LM\7k\2\2MN\7p\2\2NO\7i\2\2O\6")
        buf.write("\3\2\2\2PQ\7?\2\2Q\b\3\2\2\2RS\7k\2\2ST\7p\2\2TU\7v\2")
        buf.write("\2U\n\3\2\2\2VW\7h\2\2WX\7n\2\2XY\7q\2\2YZ\7c\2\2Z[\7")
        buf.write("v\2\2[\f\3\2\2\2\\]\7o\2\2]^\7c\2\2^_\7k\2\2_`\7p\2\2")
        buf.write("`\16\3\2\2\2ab\7*\2\2b\20\3\2\2\2cd\7+\2\2d\22\3\2\2\2")
        buf.write("ef\7}\2\2f\24\3\2\2\2gh\7\177\2\2h\26\3\2\2\2ij\7t\2\2")
        buf.write("jk\7g\2\2kl\7c\2\2lm\7f\2\2m\30\3\2\2\2no\7r\2\2op\7t")
        buf.write("\2\2pq\7k\2\2qr\7p\2\2rs\7v\2\2s\32\3\2\2\2tu\7t\2\2u")
        buf.write("v\7g\2\2vw\7v\2\2wx\7w\2\2xy\7t\2\2yz\7p\2\2z\34\3\2\2")
        buf.write("\2{|\7k\2\2|}\7h\2\2}\36\3\2\2\2~\177\7g\2\2\177\u0080")
        buf.write("\7n\2\2\u0080\u0081\7u\2\2\u0081\u0082\7g\2\2\u0082 \3")
        buf.write("\2\2\2\u0083\u0084\7y\2\2\u0084\u0085\7j\2\2\u0085\u0086")
        buf.write("\7k\2\2\u0086\u0087\7n\2\2\u0087\u0088\7g\2\2\u0088\"")
        buf.write("\3\2\2\2\u0089\u008a\7/\2\2\u008a$\3\2\2\2\u008b\u008c")
        buf.write("\7>\2\2\u008c&\3\2\2\2\u008d\u008e\7>\2\2\u008e\u008f")
        buf.write("\7?\2\2\u008f(\3\2\2\2\u0090\u0091\7@\2\2\u0091\u0092")
        buf.write("\7?\2\2\u0092*\3\2\2\2\u0093\u0094\7?\2\2\u0094\u0095")
        buf.write("\7?\2\2\u0095,\3\2\2\2\u0096\u0097\7#\2\2\u0097\u0098")
        buf.write("\7?\2\2\u0098.\3\2\2\2\u0099\u009a\7@\2\2\u009a\60\3\2")
        buf.write("\2\2\u009b\u009c\7,\2\2\u009c\62\3\2\2\2\u009d\u009e\7")
        buf.write("\61\2\2\u009e\64\3\2\2\2\u009f\u00a0\7-\2\2\u00a0\66\3")
        buf.write("\2\2\2\u00a1\u00a6\5C\"\2\u00a2\u00a5\5C\"\2\u00a3\u00a5")
        buf.write("\5E#\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("8\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\5E#\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad:\3\2\2\2\u00ae\u00b0\5E#\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b4\u00b6\7\60\2\2\u00b5\u00b7\5E#\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9<\3\2\2\2\u00ba\u00be\7$\2\2")
        buf.write("\u00bb\u00bd\n\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3")
        buf.write("\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1")
        buf.write("\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c2\7$\2\2\u00c2")
        buf.write(">\3\2\2\2\u00c3\u00c4\7\61\2\2\u00c4\u00c5\7,\2\2\u00c5")
        buf.write("\u00c9\3\2\2\2\u00c6\u00c8\13\2\2\2\u00c7\u00c6\3\2\2")
        buf.write("\2\u00c8\u00cb\3\2\2\2\u00c9\u00ca\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc")
        buf.write("\u00cd\7,\2\2\u00cd\u00ce\7\61\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\b \2\2\u00d0@\3\2\2\2\u00d1\u00d3\t\3\2\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7")
        buf.write("\b!\2\2\u00d7B\3\2\2\2\u00d8\u00d9\t\4\2\2\u00d9D\3\2")
        buf.write("\2\2\u00da\u00db\4\62;\2\u00dbF\3\2\2\2\13\2\u00a4\u00a6")
        buf.write("\u00ac\u00b1\u00b8\u00be\u00c9\u00d4\3\b\2\2")
        return buf.getvalue()


class MicroCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    IDENTIFIER = 27
    INT_LITERAL = 28
    FLOAT_LITERAL = 29
    STR_LITERAL = 30
    COMMENT = 31
    WS = 32

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'string'", "'='", "'int'", "'float'", "'main'", "'('", 
            "')'", "'{'", "'}'", "'read'", "'print'", "'return'", "'if'", 
            "'else'", "'while'", "'-'", "'<'", "'<='", "'>='", "'=='", "'!='", 
            "'>'", "'*'", "'/'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", 
            "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", 
                  "COMMENT", "WS", "LETTER", "DIGIT" ]

    grammarFileName = "MicroC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def setSymbolTable(self, st: SymbolTable):
      self.st = st

    def getSymbolTable(self) -> SymbolTable:
      return self.st

    def setAST(self, node: ASTNode):
      self.ast = node

    def getAST(self) -> ASTNode:
      return self.ast



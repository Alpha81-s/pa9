# Generated from python/MicroC.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO



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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write("\u00f8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3@\n\3\3\4\3\4\3\4\3\4\5\4F\n\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\5\bZ\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\nj\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13v\n\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0084\n\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00b1\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00cb\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00da\n\25\f\25")
        buf.write("\16\25\u00dd\13\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u00e8\n\26\f\26\16\26\u00eb\13\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32")
        buf.write("\2\4(*\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\2\5\3\2\24\31\3\2\32\33\4\2\23\23\34\34\2\u00ef")
        buf.write("\2\64\3\2\2\2\4?\3\2\2\2\6E\3\2\2\2\bG\3\2\2\2\nI\3\2")
        buf.write("\2\2\fN\3\2\2\2\16Y\3\2\2\2\20[\3\2\2\2\22i\3\2\2\2\24")
        buf.write("u\3\2\2\2\26\u0083\3\2\2\2\30\u0085\3\2\2\2\32\u008b\3")
        buf.write("\2\2\2\34\u0091\3\2\2\2\36\u0095\3\2\2\2 \u00b0\3\2\2")
        buf.write("\2\"\u00b2\3\2\2\2$\u00ca\3\2\2\2&\u00cc\3\2\2\2(\u00d0")
        buf.write("\3\2\2\2*\u00de\3\2\2\2,\u00ec\3\2\2\2.\u00f1\3\2\2\2")
        buf.write("\60\u00f3\3\2\2\2\62\u00f5\3\2\2\2\64\65\5\4\3\2\65\66")
        buf.write("\5\20\t\2\66\67\b\2\1\2\67\3\3\2\2\289\5\n\6\29:\5\4\3")
        buf.write("\2:@\3\2\2\2;<\5\f\7\2<=\5\4\3\2=@\3\2\2\2>@\3\2\2\2?")
        buf.write("8\3\2\2\2?;\3\2\2\2?>\3\2\2\2@\5\3\2\2\2AB\5\n\6\2BC\5")
        buf.write("\6\4\2CF\3\2\2\2DF\3\2\2\2EA\3\2\2\2ED\3\2\2\2F\7\3\2")
        buf.write("\2\2GH\7\35\2\2H\t\3\2\2\2IJ\5\16\b\2JK\5\b\5\2KL\7\3")
        buf.write("\2\2LM\b\6\1\2M\13\3\2\2\2NO\7\4\2\2OP\5\b\5\2PQ\7\5\2")
        buf.write("\2QR\7 \2\2RS\7\3\2\2ST\b\7\1\2T\r\3\2\2\2UV\7\6\2\2V")
        buf.write("Z\b\b\1\2WX\7\7\2\2XZ\b\b\1\2YU\3\2\2\2YW\3\2\2\2Z\17")
        buf.write("\3\2\2\2[\\\7\6\2\2\\]\7\b\2\2]^\7\t\2\2^_\7\n\2\2_`\7")
        buf.write("\13\2\2`a\5\22\n\2ab\7\f\2\2bc\b\t\1\2c\21\3\2\2\2de\5")
        buf.write("\24\13\2ef\5\22\n\2fg\b\n\1\2gj\3\2\2\2hj\b\n\1\2id\3")
        buf.write("\2\2\2ih\3\2\2\2j\23\3\2\2\2kl\5\26\f\2lm\7\3\2\2mn\b")
        buf.write("\13\1\2nv\3\2\2\2op\5 \21\2pq\b\13\1\2qv\3\2\2\2rs\5\"")
        buf.write("\22\2st\b\13\1\2tv\3\2\2\2uk\3\2\2\2uo\3\2\2\2ur\3\2\2")
        buf.write("\2v\25\3\2\2\2wx\5\36\20\2xy\b\f\1\2y\u0084\3\2\2\2z{")
        buf.write("\5\30\r\2{|\b\f\1\2|\u0084\3\2\2\2}~\5\32\16\2~\177\b")
        buf.write("\f\1\2\177\u0084\3\2\2\2\u0080\u0081\5\34\17\2\u0081\u0082")
        buf.write("\b\f\1\2\u0082\u0084\3\2\2\2\u0083w\3\2\2\2\u0083z\3\2")
        buf.write("\2\2\u0083}\3\2\2\2\u0083\u0080\3\2\2\2\u0084\27\3\2\2")
        buf.write("\2\u0085\u0086\7\r\2\2\u0086\u0087\7\t\2\2\u0087\u0088")
        buf.write("\5\b\5\2\u0088\u0089\7\n\2\2\u0089\u008a\b\r\1\2\u008a")
        buf.write("\31\3\2\2\2\u008b\u008c\7\16\2\2\u008c\u008d\7\t\2\2\u008d")
        buf.write("\u008e\5(\25\2\u008e\u008f\7\n\2\2\u008f\u0090\b\16\1")
        buf.write("\2\u0090\33\3\2\2\2\u0091\u0092\7\17\2\2\u0092\u0093\5")
        buf.write("(\25\2\u0093\u0094\b\17\1\2\u0094\35\3\2\2\2\u0095\u0096")
        buf.write("\5\b\5\2\u0096\u0097\7\5\2\2\u0097\u0098\5(\25\2\u0098")
        buf.write("\u0099\b\20\1\2\u0099\37\3\2\2\2\u009a\u009b\7\20\2\2")
        buf.write("\u009b\u009c\7\t\2\2\u009c\u009d\5,\27\2\u009d\u009e\7")
        buf.write("\n\2\2\u009e\u009f\7\13\2\2\u009f\u00a0\5\22\n\2\u00a0")
        buf.write("\u00a1\7\f\2\2\u00a1\u00a2\b\21\1\2\u00a2\u00b1\3\2\2")
        buf.write("\2\u00a3\u00a4\7\20\2\2\u00a4\u00a5\7\t\2\2\u00a5\u00a6")
        buf.write("\5,\27\2\u00a6\u00a7\7\n\2\2\u00a7\u00a8\7\13\2\2\u00a8")
        buf.write("\u00a9\5\22\n\2\u00a9\u00aa\7\f\2\2\u00aa\u00ab\7\21\2")
        buf.write("\2\u00ab\u00ac\7\13\2\2\u00ac\u00ad\5\22\n\2\u00ad\u00ae")
        buf.write("\7\f\2\2\u00ae\u00af\b\21\1\2\u00af\u00b1\3\2\2\2\u00b0")
        buf.write("\u009a\3\2\2\2\u00b0\u00a3\3\2\2\2\u00b1!\3\2\2\2\u00b2")
        buf.write("\u00b3\7\22\2\2\u00b3\u00b4\7\t\2\2\u00b4\u00b5\5,\27")
        buf.write("\2\u00b5\u00b6\7\n\2\2\u00b6\u00b7\7\13\2\2\u00b7\u00b8")
        buf.write("\5\22\n\2\u00b8\u00b9\7\f\2\2\u00b9\u00ba\b\22\1\2\u00ba")
        buf.write("#\3\2\2\2\u00bb\u00bc\5\b\5\2\u00bc\u00bd\b\23\1\2\u00bd")
        buf.write("\u00cb\3\2\2\2\u00be\u00bf\7\t\2\2\u00bf\u00c0\5(\25\2")
        buf.write("\u00c0\u00c1\7\n\2\2\u00c1\u00c2\b\23\1\2\u00c2\u00cb")
        buf.write("\3\2\2\2\u00c3\u00c4\5&\24\2\u00c4\u00c5\b\23\1\2\u00c5")
        buf.write("\u00cb\3\2\2\2\u00c6\u00c7\7\36\2\2\u00c7\u00cb\b\23\1")
        buf.write("\2\u00c8\u00c9\7\37\2\2\u00c9\u00cb\b\23\1\2\u00ca\u00bb")
        buf.write("\3\2\2\2\u00ca\u00be\3\2\2\2\u00ca\u00c3\3\2\2\2\u00ca")
        buf.write("\u00c6\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb%\3\2\2\2\u00cc")
        buf.write("\u00cd\7\23\2\2\u00cd\u00ce\5(\25\2\u00ce\u00cf\b\24\1")
        buf.write("\2\u00cf\'\3\2\2\2\u00d0\u00d1\b\25\1\2\u00d1\u00d2\5")
        buf.write("*\26\2\u00d2\u00d3\b\25\1\2\u00d3\u00db\3\2\2\2\u00d4")
        buf.write("\u00d5\f\3\2\2\u00d5\u00d6\5\62\32\2\u00d6\u00d7\5*\26")
        buf.write("\2\u00d7\u00d8\b\25\1\2\u00d8\u00da\3\2\2\2\u00d9\u00d4")
        buf.write("\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc)\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00df\b\26\1\2\u00df\u00e0\5$\23\2\u00e0\u00e1\b\26\1")
        buf.write("\2\u00e1\u00e9\3\2\2\2\u00e2\u00e3\f\3\2\2\u00e3\u00e4")
        buf.write("\5\60\31\2\u00e4\u00e5\5$\23\2\u00e5\u00e6\b\26\1\2\u00e6")
        buf.write("\u00e8\3\2\2\2\u00e7\u00e2\3\2\2\2\u00e8\u00eb\3\2\2\2")
        buf.write("\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea+\3\2\2")
        buf.write("\2\u00eb\u00e9\3\2\2\2\u00ec\u00ed\5(\25\2\u00ed\u00ee")
        buf.write("\5.\30\2\u00ee\u00ef\5(\25\2\u00ef\u00f0\b\27\1\2\u00f0")
        buf.write("-\3\2\2\2\u00f1\u00f2\t\2\2\2\u00f2/\3\2\2\2\u00f3\u00f4")
        buf.write("\t\3\2\2\u00f4\61\3\2\2\2\u00f5\u00f6\t\4\2\2\u00f6\63")
        buf.write("\3\2\2\2\f?EYiu\u0083\u00b0\u00ca\u00db\u00e9")
        return buf.getvalue()


class MicroCParser ( Parser ):

    grammarFileName = "MicroC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'string'", "'='", "'int'", "'float'", 
                     "'main'", "'('", "')'", "'{'", "'}'", "'read'", "'print'", 
                     "'return'", "'if'", "'else'", "'while'", "'-'", "'<'", 
                     "'<='", "'>='", "'=='", "'!='", "'>'", "'*'", "'/'", 
                     "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_var_decls = 2
    RULE_ident = 3
    RULE_var_decl = 4
    RULE_str_decl = 5
    RULE_base_type = 6
    RULE_function = 7
    RULE_statements = 8
    RULE_statement = 9
    RULE_base_stmt = 10
    RULE_read_stmt = 11
    RULE_print_stmt = 12
    RULE_return_stmt = 13
    RULE_assign_stmt = 14
    RULE_if_stmt = 15
    RULE_while_stmt = 16
    RULE_primary = 17
    RULE_unaryminus_expr = 18
    RULE_expr = 19
    RULE_term = 20
    RULE_cond = 21
    RULE_cmpop = 22
    RULE_mulop = 23
    RULE_addop = 24

    ruleNames =  [ "program", "decls", "var_decls", "ident", "var_decl", 
                   "str_decl", "base_type", "function", "statements", "statement", 
                   "base_stmt", "read_stmt", "print_stmt", "return_stmt", 
                   "assign_stmt", "if_stmt", "while_stmt", "primary", "unaryminus_expr", 
                   "expr", "term", "cond", "cmpop", "mulop", "addop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    IDENTIFIER=27
    INT_LITERAL=28
    FLOAT_LITERAL=29
    STR_LITERAL=30
    COMMENT=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    def setSymbolTable(self, st: SymbolTable):
      self.st = st

    def getSymbolTable(self) -> SymbolTable:
      return self.st

    def setAST(self, node: ASTNode):
      self.ast = node

    def getAST(self) -> ASTNode:
      return self.ast



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._function = None # FunctionContext

        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def function(self):
            return self.getTypedRuleContext(MicroCParser.FunctionContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MicroCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.decls()
            self.state = 51
            localctx._function = self.function()
            self.setAST(localctx._function.node);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def str_decl(self):
            return self.getTypedRuleContext(MicroCParser.Str_declContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = MicroCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.var_decl()
                self.state = 55
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.str_decl()
                self.state = 58
                self.decls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def var_decls(self):
            return self.getTypedRuleContext(MicroCParser.Var_declsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decls" ):
                listener.enterVar_decls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decls" ):
                listener.exitVar_decls(self)




    def var_decls(self):

        localctx = MicroCParser.Var_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decls)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.var_decl()
                self.state = 64
                self.var_decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MicroCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = MicroCParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MicroCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = MicroCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            localctx._base_type = self.base_type()
            self.state = 72
            localctx._ident = self.ident()
            self.state = 73
            self.match(MicroCParser.T__0)
            self.st.addVariable(localctx._base_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ident = None # IdentContext
            self.val = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def STR_LITERAL(self):
            return self.getToken(MicroCParser.STR_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_str_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_decl" ):
                listener.enterStr_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_decl" ):
                listener.exitStr_decl(self)




    def str_decl(self):

        localctx = MicroCParser.Str_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_str_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MicroCParser.T__1)
            self.state = 77
            localctx._ident = self.ident()
            self.state = 78
            self.match(MicroCParser.T__2)
            self.state = 79
            localctx.val = self.match(MicroCParser.STR_LITERAL)
            self.state = 80
            self.match(MicroCParser.T__0)
            self.st.addVariable(Scope.Type.STRING, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), (None if localctx.val is None else localctx.val.text));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None


        def getRuleIndex(self):
            return MicroCParser.RULE_base_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_type" ):
                listener.enterBase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_type" ):
                listener.exitBase_type(self)




    def base_type(self):

        localctx = MicroCParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_base_type)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(MicroCParser.T__3)
                localctx.t =  Scope.Type.INT
                pass
            elif token in [MicroCParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(MicroCParser.T__4)
                localctx.t =  Scope.Type.FLOAT
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._statements = None # StatementsContext

        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MicroCParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MicroCParser.T__3)
            self.state = 90
            self.match(MicroCParser.T__5)
            self.state = 91
            self.match(MicroCParser.T__6)
            self.state = 92
            self.match(MicroCParser.T__7)
            self.state = 93
            self.match(MicroCParser.T__8)
            self.state = 94
            localctx._statements = self.statements()
            self.state = 95
            self.match(MicroCParser.T__9)
            localctx.node =  localctx._statements.node
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._statement = None # StatementContext
            self.s = None # StatementsContext

        def statement(self):
            return self.getTypedRuleContext(MicroCParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = MicroCParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statements)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__10, MicroCParser.T__11, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__15, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                localctx._statement = self.statement()
                self.state = 99
                localctx.s = self.statements()
                localctx.node =  StatementListNode(localctx._statement.node, localctx.s.node.getStatements())
                pass
            elif token in [MicroCParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                localctx.node =  StatementListNode()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._base_stmt = None # Base_stmtContext
            self._if_stmt = None # If_stmtContext
            self._while_stmt = None # While_stmtContext

        def base_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Base_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MicroCParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MicroCParser.While_stmtContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MicroCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__10, MicroCParser.T__11, MicroCParser.T__12, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                localctx._base_stmt = self.base_stmt()
                self.state = 106
                self.match(MicroCParser.T__0)
                localctx.node =  localctx._base_stmt.node
                pass
            elif token in [MicroCParser.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                localctx._if_stmt = self.if_stmt()
                localctx.node =  localctx._if_stmt.node
                pass
            elif token in [MicroCParser.T__15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                localctx._while_stmt = self.while_stmt()
                localctx.node =  localctx._while_stmt.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._assign_stmt = None # Assign_stmtContext
            self._read_stmt = None # Read_stmtContext
            self._print_stmt = None # Print_stmtContext
            self._return_stmt = None # Return_stmtContext

        def assign_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Assign_stmtContext,0)


        def read_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Read_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_base_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_stmt" ):
                listener.enterBase_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_stmt" ):
                listener.exitBase_stmt(self)




    def base_stmt(self):

        localctx = MicroCParser.Base_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_base_stmt)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                localctx._assign_stmt = self.assign_stmt()
                localctx.node =  localctx._assign_stmt.node
                pass
            elif token in [MicroCParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                localctx._read_stmt = self.read_stmt()
                localctx.node =  localctx._read_stmt.node
                pass
            elif token in [MicroCParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                localctx._print_stmt = self.print_stmt()
                localctx.node =  localctx._print_stmt.node
                pass
            elif token in [MicroCParser.T__12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                localctx._return_stmt = self.return_stmt()
                localctx.node =  localctx._return_stmt.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_read_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_stmt" ):
                listener.enterRead_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_stmt" ):
                listener.exitRead_stmt(self)




    def read_stmt(self):

        localctx = MicroCParser.Read_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_read_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MicroCParser.T__10)
            self.state = 132
            self.match(MicroCParser.T__6)
            self.state = 133
            localctx._ident = self.ident()
            self.state = 134
            self.match(MicroCParser.T__7)
            localctx.node =  ReadNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = MicroCParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MicroCParser.T__11)
            self.state = 138
            self.match(MicroCParser.T__6)
            self.state = 139
            localctx._expr = self.expr(0)
            self.state = 140
            self.match(MicroCParser.T__7)
            localctx.node =  WriteNode(localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = MicroCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MicroCParser.T__12)
            self.state = 144
            localctx._expr = self.expr(0)
            localctx.node =  ReturnNode(localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._expr = None # ExprContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = MicroCParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            localctx._ident = self.ident()
            self.state = 148
            self.match(MicroCParser.T__2)
            self.state = 149
            localctx._expr = self.expr(0)
            localctx.node =  AssignNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))), localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext
            self.ts = None # StatementsContext
            self.es = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MicroCParser.StatementsContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = MicroCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(MicroCParser.T__13)
                self.state = 153
                self.match(MicroCParser.T__6)
                self.state = 154
                localctx._cond = self.cond()
                self.state = 155
                self.match(MicroCParser.T__7)
                self.state = 156
                self.match(MicroCParser.T__8)
                self.state = 157
                localctx._statements = self.statements()
                self.state = 158
                self.match(MicroCParser.T__9)
                localctx.node =  IfStatementNode(localctx._cond.node, StatementListNode(None, localctx._statements.node.getStatements()), None)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(MicroCParser.T__13)
                self.state = 162
                self.match(MicroCParser.T__6)
                self.state = 163
                localctx._cond = self.cond()
                self.state = 164
                self.match(MicroCParser.T__7)
                self.state = 165
                self.match(MicroCParser.T__8)
                self.state = 166
                localctx.ts = self.statements()
                self.state = 167
                self.match(MicroCParser.T__9)
                self.state = 168
                self.match(MicroCParser.T__14)
                self.state = 169
                self.match(MicroCParser.T__8)
                self.state = 170
                localctx.es = self.statements()
                self.state = 171
                self.match(MicroCParser.T__9)
                localctx.node =  IfStatementNode(localctx._cond.node, StatementListNode(None, localctx.ts.node.getStatements()), StatementListNode(None, localctx.es.node.getStatements()))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = MicroCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MicroCParser.T__15)
            self.state = 177
            self.match(MicroCParser.T__6)
            self.state = 178
            localctx._cond = self.cond()
            self.state = 179
            self.match(MicroCParser.T__7)
            self.state = 180
            self.match(MicroCParser.T__8)
            self.state = 181
            localctx._statements = self.statements()
            self.state = 182
            self.match(MicroCParser.T__9)
            localctx.node =  WhileNode(localctx._cond.node, StatementListNode(localctx._statements.node))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._expr = None # ExprContext
            self._unaryminus_expr = None # Unaryminus_exprContext
            self.il = None # Token
            self.fl = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def unaryminus_expr(self):
            return self.getTypedRuleContext(MicroCParser.Unaryminus_exprContext,0)


        def INT_LITERAL(self):
            return self.getToken(MicroCParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MicroCParser.FLOAT_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = MicroCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primary)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                localctx._ident = self.ident()
                localctx.node =  VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)))
                pass
            elif token in [MicroCParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(MicroCParser.T__6)
                self.state = 189
                localctx._expr = self.expr(0)
                self.state = 190
                self.match(MicroCParser.T__7)
                localctx.node =  localctx._expr.node
                pass
            elif token in [MicroCParser.T__16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                localctx._unaryminus_expr = self.unaryminus_expr()
                localctx.node =  localctx._unaryminus_expr.node
                pass
            elif token in [MicroCParser.INT_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                localctx.il = self.match(MicroCParser.INT_LITERAL)
                localctx.node =  IntLitNode((None if localctx.il is None else localctx.il.text))
                pass
            elif token in [MicroCParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                localctx.fl = self.match(MicroCParser.FLOAT_LITERAL)
                localctx.node =  FloatLitNode((None if localctx.fl is None else localctx.fl.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unaryminus_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_unaryminus_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryminus_expr" ):
                listener.enterUnaryminus_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryminus_expr" ):
                listener.exitUnaryminus_expr(self)




    def unaryminus_expr(self):

        localctx = MicroCParser.Unaryminus_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unaryminus_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MicroCParser.T__16)
            self.state = 203
            localctx._expr = self.expr(0)
            localctx.node =  UnaryOpNode(localctx._expr.node, '-')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self._term = None # TermContext
            self._addop = None # AddopContext

        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def addop(self):
            return self.getTypedRuleContext(MicroCParser.AddopContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            localctx._term = self.term(0)
            localctx.node =  localctx._term.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 210
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 211
                    localctx._addop = self.addop()
                    self.state = 212
                    localctx._term = self.term(0)
                    localctx.node =  BinaryOpNode(localctx.e1.node, localctx._term.node, (None if localctx._addop is None else self._input.getText(localctx._addop.start,localctx._addop.stop))) 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.t1 = None # TermContext
            self._primary = None # PrimaryContext
            self._mulop = None # MulopContext

        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def mulop(self):
            return self.getTypedRuleContext(MicroCParser.MulopContext,0)


        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            localctx._primary = self.primary()
            localctx.node =  localctx._primary.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                    localctx.t1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 224
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 225
                    localctx._mulop = self.mulop()
                    self.state = 226
                    localctx._primary = self.primary()
                    localctx.node =  BinaryOpNode(localctx.t1.node, localctx._primary.node, (None if localctx._mulop is None else self._input.getText(localctx._mulop.start,localctx._mulop.stop))) 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self._cmpop = None # CmpopContext
            self.e2 = None # ExprContext

        def cmpop(self):
            return self.getTypedRuleContext(MicroCParser.CmpopContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MicroCParser.ExprContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = MicroCParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            localctx.e1 = self.expr(0)
            self.state = 235
            localctx._cmpop = self.cmpop()
            self.state = 236
            localctx.e2 = self.expr(0)
            localctx.node = CondNode(localctx.e1.node, localctx.e2.node, (None if localctx._cmpop is None else self._input.getText(localctx._cmpop.start,localctx._cmpop.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_cmpop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmpop" ):
                listener.enterCmpop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmpop" ):
                listener.exitCmpop(self)




    def cmpop(self):

        localctx = MicroCParser.CmpopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_cmpop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MicroCParser.T__17) | (1 << MicroCParser.T__18) | (1 << MicroCParser.T__19) | (1 << MicroCParser.T__20) | (1 << MicroCParser.T__21) | (1 << MicroCParser.T__22))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)




    def mulop(self):

        localctx = MicroCParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__23 or _la==MicroCParser.T__24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)




    def addop(self):

        localctx = MicroCParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__16 or _la==MicroCParser.T__25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expr_sempred
        self._predicates[20] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         





// Generated from /Users/mckinnec/github/fa2024-595-step3-cbpmckinney/java/MicroC.g4 by ANTLR 4.13.1


package compiler;

import java.util.List;
import java.util.LinkedList;
import ast.*;


import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MicroCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		IDENTIFIER=25, INT_LITERAL=26, FLOAT_LITERAL=27, STR_LITERAL=28, COMMENT=29, 
		WS=30;
	public static final int
		RULE_program = 0, RULE_decls = 1, RULE_var_decls = 2, RULE_ident = 3, 
		RULE_var_decl = 4, RULE_str_decl = 5, RULE_base_type = 6, RULE_function = 7, 
		RULE_statements = 8, RULE_statement = 9, RULE_base_stmt = 10, RULE_read_stmt = 11, 
		RULE_print_stmt = 12, RULE_return_stmt = 13, RULE_assign_stmt = 14, RULE_while_stmt = 15, 
		RULE_primary = 16, RULE_unaryminus_expr = 17, RULE_expr = 18, RULE_term = 19, 
		RULE_cond = 20, RULE_cmpop = 21, RULE_mulop = 22, RULE_addop = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "decls", "var_decls", "ident", "var_decl", "str_decl", "base_type", 
			"function", "statements", "statement", "base_stmt", "read_stmt", "print_stmt", 
			"return_stmt", "assign_stmt", "while_stmt", "primary", "unaryminus_expr", 
			"expr", "term", "cond", "cmpop", "mulop", "addop"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'string'", "'='", "'int'", "'float'", "'main'", "'('", 
			"')'", "'{'", "'}'", "'read'", "'print'", "'return'", "'while'", "'-'", 
			"'<'", "'<='", "'>='", "'=='", "'!='", "'>'", "'*'", "'/'", "'+'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", "COMMENT", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MicroC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


	     private SymbolTable st; //Symbol table for the program
	     private ASTNode ast; //AST for the program

	     public void setSymbolTable(SymbolTable st) {
	          this.st = st;
	     }

	     public SymbolTable getSymbolTable() {
	          return st;
	     }

	     public ASTNode getAST() {
	          return ast;
	     }


	public MicroCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public FunctionContext function;
		public DeclsContext decls() {
			return getRuleContext(DeclsContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			decls();
			setState(49);
			((ProgramContext)_localctx).function = function();
			ast = ((ProgramContext)_localctx).function.node;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclsContext extends ParserRuleContext {
		public Var_declContext var_decl() {
			return getRuleContext(Var_declContext.class,0);
		}
		public DeclsContext decls() {
			return getRuleContext(DeclsContext.class,0);
		}
		public Str_declContext str_decl() {
			return getRuleContext(Str_declContext.class,0);
		}
		public DeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decls; }
	}

	public final DeclsContext decls() throws RecognitionException {
		DeclsContext _localctx = new DeclsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_decls);
		try {
			setState(59);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(52);
				var_decl();
				setState(53);
				decls();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				str_decl();
				setState(56);
				decls();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_declsContext extends ParserRuleContext {
		public Var_declContext var_decl() {
			return getRuleContext(Var_declContext.class,0);
		}
		public Var_declsContext var_decls() {
			return getRuleContext(Var_declsContext.class,0);
		}
		public Var_declsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decls; }
	}

	public final Var_declsContext var_decls() throws RecognitionException {
		Var_declsContext _localctx = new Var_declsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_var_decls);
		try {
			setState(65);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(61);
				var_decl();
				setState(62);
				var_decls();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MicroCParser.IDENTIFIER, 0); }
		public IdentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ident; }
	}

	public final IdentContext ident() throws RecognitionException {
		IdentContext _localctx = new IdentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ident);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_declContext extends ParserRuleContext {
		public Base_typeContext base_type;
		public IdentContext ident;
		public Base_typeContext base_type() {
			return getRuleContext(Base_typeContext.class,0);
		}
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl; }
	}

	public final Var_declContext var_decl() throws RecognitionException {
		Var_declContext _localctx = new Var_declContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_var_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			((Var_declContext)_localctx).base_type = base_type();
			setState(70);
			((Var_declContext)_localctx).ident = ident();
			setState(71);
			match(T__0);
			st.addVariable(((Var_declContext)_localctx).base_type.t, (((Var_declContext)_localctx).ident!=null?_input.getText(((Var_declContext)_localctx).ident.start,((Var_declContext)_localctx).ident.stop):null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Str_declContext extends ParserRuleContext {
		public IdentContext ident;
		public Token val;
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode STR_LITERAL() { return getToken(MicroCParser.STR_LITERAL, 0); }
		public Str_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_str_decl; }
	}

	public final Str_declContext str_decl() throws RecognitionException {
		Str_declContext _localctx = new Str_declContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_str_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(T__1);
			setState(75);
			((Str_declContext)_localctx).ident = ident();
			setState(76);
			match(T__2);
			setState(77);
			((Str_declContext)_localctx).val = match(STR_LITERAL);
			setState(78);
			match(T__0);
			st.addVariable(Scope.Type.STRING, (((Str_declContext)_localctx).ident!=null?_input.getText(((Str_declContext)_localctx).ident.start,((Str_declContext)_localctx).ident.stop):null), (((Str_declContext)_localctx).val!=null?((Str_declContext)_localctx).val.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Base_typeContext extends ParserRuleContext {
		public Scope.Type t;
		public Base_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_base_type; }
	}

	public final Base_typeContext base_type() throws RecognitionException {
		Base_typeContext _localctx = new Base_typeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_base_type);
		try {
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(81);
				match(T__3);
				((Base_typeContext)_localctx).t =  Scope.Type.INT;
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(83);
				match(T__4);
				((Base_typeContext)_localctx).t =  Scope.Type.FLOAT;
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public StatementListNode node;
		public StatementsContext statements;
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(T__3);
			setState(88);
			match(T__5);
			setState(89);
			match(T__6);
			setState(90);
			match(T__7);
			setState(91);
			match(T__8);
			setState(92);
			((FunctionContext)_localctx).statements = statements();
			setState(93);
			match(T__9);
			((FunctionContext)_localctx).node =  ((FunctionContext)_localctx).statements.node;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementsContext extends ParserRuleContext {
		public StatementListNode node;
		public StatementContext statement;
		public StatementsContext s;
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public StatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statements; }
	}

	public final StatementsContext statements() throws RecognitionException {
		StatementsContext _localctx = new StatementsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_statements);
		try {
			setState(101);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				((StatementsContext)_localctx).statement = statement();
				setState(97);
				((StatementsContext)_localctx).s = statements();
				((StatementsContext)_localctx).node =  new StatementListNode(((StatementsContext)_localctx).statement.node, ((StatementsContext)_localctx).s.node);
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				((StatementsContext)_localctx).node =  new StatementListNode();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementNode node;
		public Base_stmtContext base_stmt;
		public Base_stmtContext base_stmt() {
			return getRuleContext(Base_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statement);
		try {
			setState(111);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
			case T__11:
			case T__12:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				((StatementContext)_localctx).base_stmt = base_stmt();
				setState(104);
				match(T__0);
				((StatementContext)_localctx).node =  ((StatementContext)_localctx).base_stmt.node;

				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 2);
				{
				setState(108);
				while_stmt();

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Base_stmtContext extends ParserRuleContext {
		public StatementNode node;
		public Assign_stmtContext assign_stmt;
		public Read_stmtContext read_stmt;
		public Print_stmtContext print_stmt;
		public Return_stmtContext return_stmt;
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public Read_stmtContext read_stmt() {
			return getRuleContext(Read_stmtContext.class,0);
		}
		public Print_stmtContext print_stmt() {
			return getRuleContext(Print_stmtContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public Base_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_base_stmt; }
	}

	public final Base_stmtContext base_stmt() throws RecognitionException {
		Base_stmtContext _localctx = new Base_stmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_base_stmt);
		try {
			setState(125);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				((Base_stmtContext)_localctx).assign_stmt = assign_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).assign_stmt.node;
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 2);
				{
				setState(116);
				((Base_stmtContext)_localctx).read_stmt = read_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).read_stmt.node;
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 3);
				{
				setState(119);
				((Base_stmtContext)_localctx).print_stmt = print_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).print_stmt.node;
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 4);
				{
				setState(122);
				((Base_stmtContext)_localctx).return_stmt = return_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).return_stmt.node;
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Read_stmtContext extends ParserRuleContext {
		public ReadNode node;
		public IdentContext ident;
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Read_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_stmt; }
	}

	public final Read_stmtContext read_stmt() throws RecognitionException {
		Read_stmtContext _localctx = new Read_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_read_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(T__10);
			setState(128);
			match(T__6);
			setState(129);
			((Read_stmtContext)_localctx).ident = ident();
			setState(130);
			match(T__7);
			((Read_stmtContext)_localctx).node =  new ReadNode(new VarNode((((Read_stmtContext)_localctx).ident!=null?_input.getText(((Read_stmtContext)_localctx).ident.start,((Read_stmtContext)_localctx).ident.stop):null)));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_stmtContext extends ParserRuleContext {
		public WriteNode node;
		public ExprContext expr;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Print_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_stmt; }
	}

	public final Print_stmtContext print_stmt() throws RecognitionException {
		Print_stmtContext _localctx = new Print_stmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_print_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			match(T__11);
			setState(134);
			match(T__6);
			setState(135);
			((Print_stmtContext)_localctx).expr = expr(0);
			setState(136);
			match(T__7);
			((Print_stmtContext)_localctx).node =  new WriteNode(((Print_stmtContext)_localctx).expr.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Return_stmtContext extends ParserRuleContext {
		public ReturnNode node;
		public ExprContext expr;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_return_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(T__12);
			setState(140);
			((Return_stmtContext)_localctx).expr = expr(0);
			((Return_stmtContext)_localctx).node =  new ReturnNode(((Return_stmtContext)_localctx).expr.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assign_stmtContext extends ParserRuleContext {
		public AssignNode node;
		public IdentContext ident;
		public ExprContext expr;
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			((Assign_stmtContext)_localctx).ident = ident();
			setState(144);
			match(T__2);
			setState(145);
			((Assign_stmtContext)_localctx).expr = expr(0);
			((Assign_stmtContext)_localctx).node =  new AssignNode(new VarNode((((Assign_stmtContext)_localctx).ident!=null?_input.getText(((Assign_stmtContext)_localctx).ident.start,((Assign_stmtContext)_localctx).ident.stop):null)), ((Assign_stmtContext)_localctx).expr.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class While_stmtContext extends ParserRuleContext {
		public WhileNode node;
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(T__13);
			setState(149);
			match(T__6);
			setState(150);
			cond();
			setState(151);
			match(T__7);
			setState(152);
			match(T__8);
			setState(153);
			statements();
			setState(154);
			match(T__9);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public ExpressionNode node;
		public IdentContext ident;
		public ExprContext expr;
		public Unaryminus_exprContext unaryminus_expr;
		public Token il;
		public Token fl;
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Unaryminus_exprContext unaryminus_expr() {
			return getRuleContext(Unaryminus_exprContext.class,0);
		}
		public TerminalNode INT_LITERAL() { return getToken(MicroCParser.INT_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(MicroCParser.FLOAT_LITERAL, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_primary);
		try {
			setState(171);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(156);
				((PrimaryContext)_localctx).ident = ident();
				((PrimaryContext)_localctx).node =  new VarNode((((PrimaryContext)_localctx).ident!=null?_input.getText(((PrimaryContext)_localctx).ident.start,((PrimaryContext)_localctx).ident.stop):null));
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(159);
				match(T__6);
				setState(160);
				((PrimaryContext)_localctx).expr = expr(0);
				setState(161);
				match(T__7);
				((PrimaryContext)_localctx).node =  ((PrimaryContext)_localctx).expr.node;
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 3);
				{
				setState(164);
				((PrimaryContext)_localctx).unaryminus_expr = unaryminus_expr();
				((PrimaryContext)_localctx).node =  ((PrimaryContext)_localctx).unaryminus_expr.node;
				}
				break;
			case INT_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(167);
				((PrimaryContext)_localctx).il = match(INT_LITERAL);
				((PrimaryContext)_localctx).node =  new IntLitNode((((PrimaryContext)_localctx).il!=null?((PrimaryContext)_localctx).il.getText():null));
				}
				break;
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 5);
				{
				setState(169);
				((PrimaryContext)_localctx).fl = match(FLOAT_LITERAL);
				((PrimaryContext)_localctx).node =  new FloatLitNode((((PrimaryContext)_localctx).fl!=null?((PrimaryContext)_localctx).fl.getText():null));
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Unaryminus_exprContext extends ParserRuleContext {
		public ExpressionNode node;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Unaryminus_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryminus_expr; }
	}

	public final Unaryminus_exprContext unaryminus_expr() throws RecognitionException {
		Unaryminus_exprContext _localctx = new Unaryminus_exprContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_unaryminus_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(T__14);
			setState(174);
			expr(0);

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExpressionNode node;
		public ExprContext e1;
		public TermContext term;
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public AddopContext addop() {
			return getRuleContext(AddopContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(178);
			((ExprContext)_localctx).term = term(0);
			((ExprContext)_localctx).node =  ((ExprContext)_localctx).term.node;
			}
			_ctx.stop = _input.LT(-1);
			setState(188);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					_localctx.e1 = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(181);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(182);
					addop();
					setState(183);
					((ExprContext)_localctx).term = term(0);

					}
					} 
				}
				setState(190);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public ExpressionNode node;
		public TermContext t1;
		public PrimaryContext primary;
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public MulopContext mulop() {
			return getRuleContext(MulopContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		return term(0);
	}

	private TermContext term(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermContext _localctx = new TermContext(_ctx, _parentState);
		TermContext _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_term, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(192);
			((TermContext)_localctx).primary = primary();
			((TermContext)_localctx).node =  ((TermContext)_localctx).primary.node;
			}
			_ctx.stop = _input.LT(-1);
			setState(202);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new TermContext(_parentctx, _parentState);
					_localctx.t1 = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_term);
					setState(195);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(196);
					mulop();
					setState(197);
					((TermContext)_localctx).primary = primary();

					}
					} 
				}
				setState(204);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondContext extends ParserRuleContext {
		public CondNode node;
		public ExprContext e1;
		public ExprContext e2;
		public CmpopContext cmpop() {
			return getRuleContext(CmpopContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_cond);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			((CondContext)_localctx).e1 = expr(0);
			setState(206);
			cmpop();
			setState(207);
			((CondContext)_localctx).e2 = expr(0);

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CmpopContext extends ParserRuleContext {
		public CmpopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cmpop; }
	}

	public final CmpopContext cmpop() throws RecognitionException {
		CmpopContext _localctx = new CmpopContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_cmpop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4128768L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MulopContext extends ParserRuleContext {
		public MulopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mulop; }
	}

	public final MulopContext mulop() throws RecognitionException {
		MulopContext _localctx = new MulopContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_mulop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			_la = _input.LA(1);
			if ( !(_la==T__21 || _la==T__22) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AddopContext extends ParserRuleContext {
		public AddopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addop; }
	}

	public final AddopContext addop() throws RecognitionException {
		AddopContext _localctx = new AddopContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_addop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			_la = _input.LA(1);
			if ( !(_la==T__14 || _la==T__23) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 18:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 19:
			return term_sempred((TermContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean term_sempred(TermContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001e\u00d9\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001<\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002B\b\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003"+
		"\u0006V\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0003\bf\b\b\u0001\t\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0003\tp\b\t\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n~\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0003\u0010\u00ac\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0005\u0012\u00bb\b\u0012\n\u0012"+
		"\f\u0012\u00be\t\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013"+
		"\u00c9\b\u0013\n\u0013\f\u0013\u00cc\t\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0000\u0002$&\u0018\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"$&(*,.\u0000\u0003\u0001\u0000\u0010\u0015\u0001\u0000\u0016\u0017"+
		"\u0002\u0000\u000f\u000f\u0018\u0018\u00cf\u00000\u0001\u0000\u0000\u0000"+
		"\u0002;\u0001\u0000\u0000\u0000\u0004A\u0001\u0000\u0000\u0000\u0006C"+
		"\u0001\u0000\u0000\u0000\bE\u0001\u0000\u0000\u0000\nJ\u0001\u0000\u0000"+
		"\u0000\fU\u0001\u0000\u0000\u0000\u000eW\u0001\u0000\u0000\u0000\u0010"+
		"e\u0001\u0000\u0000\u0000\u0012o\u0001\u0000\u0000\u0000\u0014}\u0001"+
		"\u0000\u0000\u0000\u0016\u007f\u0001\u0000\u0000\u0000\u0018\u0085\u0001"+
		"\u0000\u0000\u0000\u001a\u008b\u0001\u0000\u0000\u0000\u001c\u008f\u0001"+
		"\u0000\u0000\u0000\u001e\u0094\u0001\u0000\u0000\u0000 \u00ab\u0001\u0000"+
		"\u0000\u0000\"\u00ad\u0001\u0000\u0000\u0000$\u00b1\u0001\u0000\u0000"+
		"\u0000&\u00bf\u0001\u0000\u0000\u0000(\u00cd\u0001\u0000\u0000\u0000*"+
		"\u00d2\u0001\u0000\u0000\u0000,\u00d4\u0001\u0000\u0000\u0000.\u00d6\u0001"+
		"\u0000\u0000\u000001\u0003\u0002\u0001\u000012\u0003\u000e\u0007\u0000"+
		"23\u0006\u0000\uffff\uffff\u00003\u0001\u0001\u0000\u0000\u000045\u0003"+
		"\b\u0004\u000056\u0003\u0002\u0001\u00006<\u0001\u0000\u0000\u000078\u0003"+
		"\n\u0005\u000089\u0003\u0002\u0001\u00009<\u0001\u0000\u0000\u0000:<\u0001"+
		"\u0000\u0000\u0000;4\u0001\u0000\u0000\u0000;7\u0001\u0000\u0000\u0000"+
		";:\u0001\u0000\u0000\u0000<\u0003\u0001\u0000\u0000\u0000=>\u0003\b\u0004"+
		"\u0000>?\u0003\u0004\u0002\u0000?B\u0001\u0000\u0000\u0000@B\u0001\u0000"+
		"\u0000\u0000A=\u0001\u0000\u0000\u0000A@\u0001\u0000\u0000\u0000B\u0005"+
		"\u0001\u0000\u0000\u0000CD\u0005\u0019\u0000\u0000D\u0007\u0001\u0000"+
		"\u0000\u0000EF\u0003\f\u0006\u0000FG\u0003\u0006\u0003\u0000GH\u0005\u0001"+
		"\u0000\u0000HI\u0006\u0004\uffff\uffff\u0000I\t\u0001\u0000\u0000\u0000"+
		"JK\u0005\u0002\u0000\u0000KL\u0003\u0006\u0003\u0000LM\u0005\u0003\u0000"+
		"\u0000MN\u0005\u001c\u0000\u0000NO\u0005\u0001\u0000\u0000OP\u0006\u0005"+
		"\uffff\uffff\u0000P\u000b\u0001\u0000\u0000\u0000QR\u0005\u0004\u0000"+
		"\u0000RV\u0006\u0006\uffff\uffff\u0000ST\u0005\u0005\u0000\u0000TV\u0006"+
		"\u0006\uffff\uffff\u0000UQ\u0001\u0000\u0000\u0000US\u0001\u0000\u0000"+
		"\u0000V\r\u0001\u0000\u0000\u0000WX\u0005\u0004\u0000\u0000XY\u0005\u0006"+
		"\u0000\u0000YZ\u0005\u0007\u0000\u0000Z[\u0005\b\u0000\u0000[\\\u0005"+
		"\t\u0000\u0000\\]\u0003\u0010\b\u0000]^\u0005\n\u0000\u0000^_\u0006\u0007"+
		"\uffff\uffff\u0000_\u000f\u0001\u0000\u0000\u0000`a\u0003\u0012\t\u0000"+
		"ab\u0003\u0010\b\u0000bc\u0006\b\uffff\uffff\u0000cf\u0001\u0000\u0000"+
		"\u0000df\u0006\b\uffff\uffff\u0000e`\u0001\u0000\u0000\u0000ed\u0001\u0000"+
		"\u0000\u0000f\u0011\u0001\u0000\u0000\u0000gh\u0003\u0014\n\u0000hi\u0005"+
		"\u0001\u0000\u0000ij\u0006\t\uffff\uffff\u0000jk\u0006\t\uffff\uffff\u0000"+
		"kp\u0001\u0000\u0000\u0000lm\u0003\u001e\u000f\u0000mn\u0006\t\uffff\uffff"+
		"\u0000np\u0001\u0000\u0000\u0000og\u0001\u0000\u0000\u0000ol\u0001\u0000"+
		"\u0000\u0000p\u0013\u0001\u0000\u0000\u0000qr\u0003\u001c\u000e\u0000"+
		"rs\u0006\n\uffff\uffff\u0000s~\u0001\u0000\u0000\u0000tu\u0003\u0016\u000b"+
		"\u0000uv\u0006\n\uffff\uffff\u0000v~\u0001\u0000\u0000\u0000wx\u0003\u0018"+
		"\f\u0000xy\u0006\n\uffff\uffff\u0000y~\u0001\u0000\u0000\u0000z{\u0003"+
		"\u001a\r\u0000{|\u0006\n\uffff\uffff\u0000|~\u0001\u0000\u0000\u0000}"+
		"q\u0001\u0000\u0000\u0000}t\u0001\u0000\u0000\u0000}w\u0001\u0000\u0000"+
		"\u0000}z\u0001\u0000\u0000\u0000~\u0015\u0001\u0000\u0000\u0000\u007f"+
		"\u0080\u0005\u000b\u0000\u0000\u0080\u0081\u0005\u0007\u0000\u0000\u0081"+
		"\u0082\u0003\u0006\u0003\u0000\u0082\u0083\u0005\b\u0000\u0000\u0083\u0084"+
		"\u0006\u000b\uffff\uffff\u0000\u0084\u0017\u0001\u0000\u0000\u0000\u0085"+
		"\u0086\u0005\f\u0000\u0000\u0086\u0087\u0005\u0007\u0000\u0000\u0087\u0088"+
		"\u0003$\u0012\u0000\u0088\u0089\u0005\b\u0000\u0000\u0089\u008a\u0006"+
		"\f\uffff\uffff\u0000\u008a\u0019\u0001\u0000\u0000\u0000\u008b\u008c\u0005"+
		"\r\u0000\u0000\u008c\u008d\u0003$\u0012\u0000\u008d\u008e\u0006\r\uffff"+
		"\uffff\u0000\u008e\u001b\u0001\u0000\u0000\u0000\u008f\u0090\u0003\u0006"+
		"\u0003\u0000\u0090\u0091\u0005\u0003\u0000\u0000\u0091\u0092\u0003$\u0012"+
		"\u0000\u0092\u0093\u0006\u000e\uffff\uffff\u0000\u0093\u001d\u0001\u0000"+
		"\u0000\u0000\u0094\u0095\u0005\u000e\u0000\u0000\u0095\u0096\u0005\u0007"+
		"\u0000\u0000\u0096\u0097\u0003(\u0014\u0000\u0097\u0098\u0005\b\u0000"+
		"\u0000\u0098\u0099\u0005\t\u0000\u0000\u0099\u009a\u0003\u0010\b\u0000"+
		"\u009a\u009b\u0005\n\u0000\u0000\u009b\u001f\u0001\u0000\u0000\u0000\u009c"+
		"\u009d\u0003\u0006\u0003\u0000\u009d\u009e\u0006\u0010\uffff\uffff\u0000"+
		"\u009e\u00ac\u0001\u0000\u0000\u0000\u009f\u00a0\u0005\u0007\u0000\u0000"+
		"\u00a0\u00a1\u0003$\u0012\u0000\u00a1\u00a2\u0005\b\u0000\u0000\u00a2"+
		"\u00a3\u0006\u0010\uffff\uffff\u0000\u00a3\u00ac\u0001\u0000\u0000\u0000"+
		"\u00a4\u00a5\u0003\"\u0011\u0000\u00a5\u00a6\u0006\u0010\uffff\uffff\u0000"+
		"\u00a6\u00ac\u0001\u0000\u0000\u0000\u00a7\u00a8\u0005\u001a\u0000\u0000"+
		"\u00a8\u00ac\u0006\u0010\uffff\uffff\u0000\u00a9\u00aa\u0005\u001b\u0000"+
		"\u0000\u00aa\u00ac\u0006\u0010\uffff\uffff\u0000\u00ab\u009c\u0001\u0000"+
		"\u0000\u0000\u00ab\u009f\u0001\u0000\u0000\u0000\u00ab\u00a4\u0001\u0000"+
		"\u0000\u0000\u00ab\u00a7\u0001\u0000\u0000\u0000\u00ab\u00a9\u0001\u0000"+
		"\u0000\u0000\u00ac!\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005\u000f\u0000"+
		"\u0000\u00ae\u00af\u0003$\u0012\u0000\u00af\u00b0\u0006\u0011\uffff\uffff"+
		"\u0000\u00b0#\u0001\u0000\u0000\u0000\u00b1\u00b2\u0006\u0012\uffff\uffff"+
		"\u0000\u00b2\u00b3\u0003&\u0013\u0000\u00b3\u00b4\u0006\u0012\uffff\uffff"+
		"\u0000\u00b4\u00bc\u0001\u0000\u0000\u0000\u00b5\u00b6\n\u0001\u0000\u0000"+
		"\u00b6\u00b7\u0003.\u0017\u0000\u00b7\u00b8\u0003&\u0013\u0000\u00b8\u00b9"+
		"\u0006\u0012\uffff\uffff\u0000\u00b9\u00bb\u0001\u0000\u0000\u0000\u00ba"+
		"\u00b5\u0001\u0000\u0000\u0000\u00bb\u00be\u0001\u0000\u0000\u0000\u00bc"+
		"\u00ba\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000\u0000\u0000\u00bd"+
		"%\u0001\u0000\u0000\u0000\u00be\u00bc\u0001\u0000\u0000\u0000\u00bf\u00c0"+
		"\u0006\u0013\uffff\uffff\u0000\u00c0\u00c1\u0003 \u0010\u0000\u00c1\u00c2"+
		"\u0006\u0013\uffff\uffff\u0000\u00c2\u00ca\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c4\n\u0001\u0000\u0000\u00c4\u00c5\u0003,\u0016\u0000\u00c5\u00c6"+
		"\u0003 \u0010\u0000\u00c6\u00c7\u0006\u0013\uffff\uffff\u0000\u00c7\u00c9"+
		"\u0001\u0000\u0000\u0000\u00c8\u00c3\u0001\u0000\u0000\u0000\u00c9\u00cc"+
		"\u0001\u0000\u0000\u0000\u00ca\u00c8\u0001\u0000\u0000\u0000\u00ca\u00cb"+
		"\u0001\u0000\u0000\u0000\u00cb\'\u0001\u0000\u0000\u0000\u00cc\u00ca\u0001"+
		"\u0000\u0000\u0000\u00cd\u00ce\u0003$\u0012\u0000\u00ce\u00cf\u0003*\u0015"+
		"\u0000\u00cf\u00d0\u0003$\u0012\u0000\u00d0\u00d1\u0006\u0014\uffff\uffff"+
		"\u0000\u00d1)\u0001\u0000\u0000\u0000\u00d2\u00d3\u0007\u0000\u0000\u0000"+
		"\u00d3+\u0001\u0000\u0000\u0000\u00d4\u00d5\u0007\u0001\u0000\u0000\u00d5"+
		"-\u0001\u0000\u0000\u0000\u00d6\u00d7\u0007\u0002\u0000\u0000\u00d7/\u0001"+
		"\u0000\u0000\u0000\t;AUeo}\u00ab\u00bc\u00ca";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
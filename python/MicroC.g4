grammar MicroC;

@header {

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
}

@members {
def setSymbolTable(self, st: SymbolTable):
  self.st = st

def getSymbolTable(self) -> SymbolTable:
  return self.st

def setAST(self, node: ASTNode):
  self.ast = node

def getAST(self) -> ASTNode:
  return self.ast
}
program : decls function {self.setAST($function.node);};

/* Declarations */
decls : var_decl decls
      | str_decl decls
	 | /* empty */ ;

var_decls : var_decl var_decls 
          | /* empty */ ;

/* Identifiers and types */		  
ident : IDENTIFIER ;
		  
var_decl : base_type ident ';' {self.st.addVariable($base_type.t, $ident.text);};

str_decl : 'string' ident '=' val= STR_LITERAL ';' {self.st.addVariable(Scope.Type.STRING, $ident.text, $val.text);};

base_type returns [Scope.Type t]: 'int' {$t = Scope.Type.INT;}| 'float' {$t = Scope.Type.FLOAT;};

/* Functions */

function returns [StatementListNode node] : 'int' 'main' '(' ')' '{' statements '}' {$node = $statements.node;};
		 		 
/* Statements */
		 
statements returns [StatementListNode node] : statement s=statements {$node = StatementListNode($statement.node, $s.node.getStatements());}
            | /* empty */ {$node = StatementListNode();};
			
statement returns [StatementNode node] : base_stmt ';' {$node = $base_stmt.node;}
		  | if_stmt {$node = $if_stmt.node;} 
		  | while_stmt {$node = $while_stmt.node;} ; /* FILL IN FOR STEP 3 */
		  
base_stmt returns [StatementNode node] : assign_stmt {$node = $assign_stmt.node;}
          | read_stmt {$node = $read_stmt.node;}
		| print_stmt {$node = $print_stmt.node;}
		| return_stmt {$node = $return_stmt.node;};
		 
read_stmt returns [ReadNode node] : 'read' '(' ident ')' {$node = ReadNode(VarNode($ident.text));} ;

print_stmt returns [WriteNode node] : 'print' '(' expr ')' {$node = WriteNode($expr.node);};

return_stmt returns [ReturnNode node] : 'return' expr {$node = ReturnNode($expr.node);};

assign_stmt returns [AssignNode node] : ident '=' expr {$node = AssignNode(VarNode($ident.text), $expr.node);};

// I don't think we can put None here.  
// What about break/continue statements?
if_stmt returns [IfStatementNode node]: 'if' '(' cond ')' '{' statements '}' {$node = IfStatementNode($cond.node, StatementListNode(None, $statements.node.getStatements()), None);}  // put None for then part?
      | 'if' '(' cond ')' '{' ts=statements '}' 'else' '{' es=statements '}' {$node = IfStatementNode($cond.node, StatementListNode(None, $ts.node.getStatements()), StatementListNode(None, $es.node.getStatements()));}; // Can we do this?  Would this also allow for stuff like elif?

while_stmt returns [WhileNode node] : 'while' '(' cond ')' '{' statements '}' {$node = WhileNode($cond.node, StatementListNode($statements.node));}  ; /* FILL IN FOR STEP 3 */
	 
/* Expressions */

primary returns [ExpressionNode node] : ident {$node = VarNode($ident.text);}
        | '(' expr ')' {$node = $expr.node;}
        | unaryminus_expr {$node = $unaryminus_expr.node;}
        | il = INT_LITERAL {$node = IntLitNode($il.text);}
        | fl = FLOAT_LITERAL {$node = FloatLitNode($fl.text);};

unaryminus_expr returns [ExpressionNode node] : '-' expr {$node = UnaryOpNode($expr.node, '-');}; 
		 
expr returns [ExpressionNode node] : term {$node = $term.node;}
     | e1 = expr addop term {$node = BinaryOpNode($e1.node, $term.node, $addop.text);};
	 
term returns [ExpressionNode node] : primary {$node = $primary.node;}
     | t1 = term mulop primary {$node = BinaryOpNode($t1.node, $primary.node, $mulop.text);};
	   	   
cond returns [CondNode node] : e1=expr cmpop e2=expr {$node = CondNode($e1.node, $e2.node, $cmpop.text);} ; /* FILL IN FOR STEP 3 */

cmpop : '<' | '<=' | '>=' | '==' | '!=' | '>' ;

mulop : '*' | '/' ;

addop : '+' | '-' ;

/* Tokens */

IDENTIFIER : LETTER (LETTER | DIGIT)* ;

INT_LITERAL : DIGIT+;

FLOAT_LITERAL : DIGIT* '.' DIGIT+;

STR_LITERAL : '"' (~('"'))* '"' ;

COMMENT : '/*' .*? '*/' -> skip;

WS : [ \t\n\r]+ -> skip;

fragment LETTER : ('a'..'z' | 'A'..'Z') ;

fragment DIGIT : ('0'..'9') ;

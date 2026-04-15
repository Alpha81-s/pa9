from platform import node
import sys
import os

from .CodeObject import CodeObject
from .InstructionList import InstructionList
from .instructions import *
from ..compiler import *
from ..ast import *
from ..ast.visitor.AbstractASTVisitor import AbstractASTVisitor

class CodeGenerator(AbstractASTVisitor):

  def __init__(self):
    self.intRegCount = 0
    self.floatRegCount = 0
    self.intTempPrefix = 't'
    self.floatTempPrefix = 'f'
    self.numCtrlStructs = 0


  def getIntRegCount(self):
    return self.intRegCount

  def getFloatRegCount(self):
    return self.floatRegCount




  def postprocessVarNode(self, node: VarNode) -> CodeObject:
    sym = node.getSymbol()

    co = CodeObject(sym)
    co.lval = True
    co.type = node.getType()

    return co


  
  def postprocessIntLitNode(self, node: IntLitNode) -> CodeObject:

    co = CodeObject()

    temp = self.generateTemp(Scope.Type.INT)
    val = node.getVal()
    # LI t2, 5
    co.code.append(Li(temp, val))
    co.temp = temp
    co.lval = False
    co.type = node.getType()


    return co


  def postprocessFloatLitNode(self, node: FloatLitNode) -> CodeObject:
    '''
    This will look a lot like the int literal node above
    Minor difference: use FImm instead of Li
    '''
    co = CodeObject()


    temp = self.generateTemp(Scope.Type.FLOAT)
    val = node.getVal()
    # LI t2, 5
    co.code.append(FImm(temp, val))
    co.temp = temp
    co.lval = False
    co.type = node.getType()

    return co



  def postprocessBinaryOpNode(self, node: BinaryOpNode, left: CodeObject, right: CodeObject) -> CodeObject:
    '''
    Step 0: Create new code object
    Step 1: Get code from left child and rvalify if needed
    Step 2: Add left code
    Step 3: Get code from right child and rvalify if needed
    Step 4: Add right code
    Step 5: Generate binary operation code using left/right's temps
    Step 6: Update code object's fields
    Step 7: Return it
    '''

    co = CodeObject()
    newcode = CodeObject()

  
    optype = str(node.op) # Get string corresponding to the operation (+, -, *, /)

    
    if left.lval == True:
      left = self.rvalify(left) # create new code object, fix this, this is bad?
    
    co.code.extend(left.code)

   
    if right.lval == True:
      right = self.rvalify(right)
    
    co.code.extend(right.code)
  
    if left.type != right.type:
      print("Incompatible types in binary operation!\n")
    
    if left.type == Scope.Type.INT:
      #print("Processing binop with INTs")
      newtemp = self.generateTemp(Scope.Type.INT)
      if optype == "OpType.ADD":
        newcode = Add(left.temp, right.temp, newtemp)
      elif optype == "OpType.SUB":
        newcode = Sub(left.temp, right.temp, newtemp)
      elif optype == "OpType.MUL":
        newcode = Mul(left.temp, right.temp, newtemp)
      elif optype == "OpType.DIV":
        newcode = Div(left.temp, right.temp, newtemp)
      else:
        print("Bad operation in binop!\n")


    elif left.type == Scope.Type.FLOAT:
      newtemp = self.generateTemp(Scope.Type.FLOAT)
      if optype == "OpType.ADD":
        newcode = FAdd(left.temp, right.temp, newtemp)
      elif optype == "OpType.SUB":
        newcode = FSub(left.temp, right.temp, newtemp)
      elif optype == "OpType.MUL":
        newcode = FMul(left.temp, right.temp, newtemp)
      elif optype == "OpType.DIV":
        newcode = FDiv(left.temp, right.temp, newtemp)
      else:
        print("Bad operation in binop!\n")

    else:
      print("Bad type in binary op!\n")

    co.code.append(newcode)
    co.lval = False
    co.temp = newtemp
    co.type = left.type
    #print(newcode)
    return co



  def postprocessUnaryOpNode(self, node: UnaryOpNode, expr: CodeObject) -> CodeObject:
    '''
    Unary Op Node would be telling us to do -(expr)
    Step 1: Generate blank code object
    Step 2: Get code for expr and rvalify if necessary
    Step 3: Add expr code after rvalifying
    Step 4: Generate instruction to negate 
    Step 5: Update temp/lval of resulting code object
    Step 6: Return it
    '''

    co = CodeObject()  # Step 0
    
    if expr.lval:
      expr = self.rvalify(expr)

    co.code.extend(expr.code) # Add in all the code required to get expr after rvalifying


    if expr.type == Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(Neg(src=expr.temp, dest=temp))
      

    elif expr.type == Scope.Type.FLOAT:
      temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(FNeg(src=expr.temp, dest=temp))

    else:
      raise Exception("Non int/float type in unary op!")

    co.type = expr.type
    co.temp = temp
    co.lval = False 

    return co
  






  def postprocessAssignNode(self, node: AssignNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()

    assert(left.lval is True)
    assert(left.isVar() is True)

    if right.lval:
      right = self.rvalify(right)

    co.code.extend(right.code)

    address = self.generateAddrFromVariable(left)
    temp = self.generateTemp(Scope.Type.INT) 
    co.code.append(La(temp, address))

    if left.type == Scope.Type.INT:
      co.code.append(Sw(right.temp, temp, '0'))
    elif left.type == Scope.Type.FLOAT:
      co.code.append(Fsw(right.temp, temp, '0'))
    else:
      raise Exception("Bad type in assign node")

    co.type = left.type
    co.temp = right.temp
    co.lval = False 

    return co



  def postprocessStatementListNode(self, node: StatementListNode, statements: list) -> CodeObject:
    co = CodeObject()

    for subcode in statements:
      co.code.extend(subcode.code)

    co.type = None
    return co


	
  def postprocessReadNode(self, node: ReadNode, var: CodeObject) -> CodeObject:

    co = CodeObject()

    assert(var.isVar())

    if var.type is Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(GetI(temp))
      address = self.generateAddrFromVariable(var)
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp2, address))
      co.code.append(Sw(temp, temp2, '0'))

    elif var.type is Scope.Type.FLOAT:
      # put stuff here
      temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(GetF(temp))
      address = self.generateAddrFromVariable(var)
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp2, address))
      co.code.append(Fsw(temp, temp2, '0'))

    else:
      raise Exception("Bad type in read node")


    return co


  def postprocessWriteNode(self, node: WriteNode, expr: CodeObject) -> CodeObject:

    co = CodeObject()

    if expr.type is Scope.Type.INT:
      if expr.lval:
        expr = self.rvalify(expr)

      co.code.extend(expr.code)
      co.code.append(PutI(expr.temp))

    elif expr.type is Scope.Type.FLOAT:
      if expr.lval:
        expr = self.rvalify(expr)

      co.code.extend(expr.code)
      co.code.append(PutF(expr.temp))

    else:
      assert(expr.isVar())
      
      address = self.generateAddrFromVariable(expr)
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp, address))
      co.code.append(PutS(temp))

    return co

  
  def postprocessReturnNode(self, node: ReturnNode, retExpr: CodeObject) -> CodeObject:

    co = CodeObject()

    if retExpr.lval is True:
      retExpr = self.rvalify(retExpr)

    co.code.extend(retExpr.code)
    co.code.append(Halt())
    co.type = None
    return co


  
  def generateTemp(self, t: Scope.Type) -> str:

    if t == Scope.Type.INT:
      s = self.intTempPrefix + str(self.intRegCount)
      self.intRegCount += 1
      return s
    elif t == Scope.Type.FLOAT:
      s = self.floatTempPrefix + str(self.floatRegCount)
      self.floatRegCount += 1
      return s
    else:
      raise Exception("Generating temp for bad type")


  def postprocessCondNode(self, node: CondNode, left: CodeObject, right: CodeObject) -> CodeObject:
    '''
    NEW:
    '''
    co = CodeObject()
    temp = self.generateTemp(Scope.Type.INT)
    True_lab = "condtrue_" + temp
    Done_lab = "conddone_" + temp

    if left.lval:
      left = self.rvalify(left)
    co.code.extend(left.code)
    if right.lval:
      right =  self.rvalify(right)
    co.code.extend(right.code)

    optype = str(node.getOp()).upper()


    if left.type == Scope.Type.INT:


      co.code.append(Li(temp, '0'))

      if "!=" in optype or "NE" in optype:
        co.code.append(Bne(left.temp, right.temp, True_lab))
      elif "<=" in optype or "LE" in optype:  
        co.code.append(Bgt(left.temp, right.temp, True_lab))
      elif ">=" in optype or "GE" in optype:
        co.code.append(Blt(left.temp, right.temp, True_lab))
      elif "==" in optype or "EQ" in optype:
        co.code.append(Beq(left.temp, right.temp, True_lab))
      elif "<" in optype or "LT" in optype:
        co.code.append(Blt(left.temp, right.temp, True_lab))
      elif ">" in optype or "GT" in optype:
        co.code.append(Bgt(left.temp, right.temp, True_lab))
      else:
        raise Exception("Bad optype in cond node")
      
      co.code.append(J(Done_lab))
      co.code.append(Label(True_lab))
      co.code.append(Li(temp, '1'))
      co.code.append(Label(Done_lab))

    elif left.type == Scope.Type.FLOAT:
     if "==" in optype or "EQ" in optype:
        co.code.append(Feq(left.temp, right.temp, True_lab))
     elif "<=" in optype or "LE" in optype:  
        co.code.append(Fle(left.temp, right.temp, True_lab))
     elif ">=" in optype or "GE" in optype:
        co.code.append(Fle(right.temp, left.temp, True_lab))
     elif "!=" in optype or "NE" in optype:
        temp2 = self.generateTemp(Scope.Type.INT)
        True_lab = "condtrue_" + temp
        Done_lab = "conddone_" + temp

        co.code.append(Feq(left.temp, right.temp, temp2))
        co.code.append(Li(temp, '0'))
        co.code.append(Beq(temp2, 'x0', True_lab))
        co.code.append(J(Done_lab))
        co.code.append(Label(True_lab))
        co.code.append(Li(temp, '1'))
        co.code.append(Label(Done_lab))

     elif "<" in optype or "LT" in optype:
        co.code.append(Flt(left.temp, right.temp, True_lab))
     elif ">" in optype or "GT" in optype:
        co.code.append(Flt(right.temp, left.temp, True_lab))

     else:
        raise Exception("Bad optype in cond node")
     
    else:
      raise Exception("Bad type in cond node")
    
    co.temp = temp
    co.lval = False 
    co.type = Scope.Type.INT

    return co




  def postprocessIfStatementNode(self, node: IfStatementNode, cond: CodeObject, tlist: CodeObject, elist: CodeObject) -> CodeObject:
    '''
    NEW
    '''
    self._incrnumCtrlStruct()
    labelnum = self._getnumCtrlStruct()
    
    co = CodeObject()
    
    else_lab = self._generateElseLabel(labelnum)
    done_lab = self._generateDoneLabel(labelnum)

    co.code.extend(cond.code)

    if elist is None:
      co.code.append(Beq(cond.temp, "x0", done_lab))
      co.code.extend(tlist.code)
      co.code.append(Label(done_lab))
    else:
      co.code.append(Beq(cond.temp, "x0", else_lab))
      co.code.extend(tlist.code)
      co.code.append(J(done_lab))
      co.code.append(Label(else_lab))
      co.code.extend(elist.code)
      co.code.append(Label(done_lab))

    return co

  def postprocessWhileNode(self, node: WhileNode, cond: CodeObject, wlist:
  CodeObject) -> CodeObject:
    ''' 
    NEW
    '''
    self._incrnumCtrlStruct()
    labelnum = self._getnumCtrlStruct()
    co = CodeObject()

    loop_lab = self._generateLoopLabel(labelnum)
    done_lab = self._generateDoneLabel(labelnum)

    co.code.append(Label(loop_lab))
    co.code.extend(cond.code)
    co.code.append(Beq(cond.temp, "x0", done_lab))
    co.code.extend(wlist.code)
    co.code.append(J(loop_lab))
    co.code.append(Label(done_lab))

    return co


  def rvalify(self, lco : CodeObject) -> CodeObject:

    assert(lco.lval is True)
    assert(lco.isVar() is True)
    
    co = CodeObject()

    address = self.generateAddrFromVariable(lco)
    temp1 = self.generateTemp(Scope.Type.INT) # Addresses are always ints
    temp2 = self.generateTemp(Scope.Type.INT)
    co.code.append(La(temp1, address)) # Load address (global only)

    if lco.type is Scope.Type.INT:
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(Lw(temp2, temp1, '0'))

    elif lco.type is Scope.Type.FLOAT:
      temp2 = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(Flw(temp2, temp1, '0'))

    else:
      raise Exception("Bad type in rvalify!")

    co.type = lco.type
    co.lval = False
    co.temp = temp2


    return co






  def generateAddrFromVariable(self, lco: CodeObject) -> str:
    '''
    Changed type to return string.
    This function is responsible for returning the string that has the address of the variable.
    Right now it can only handle global variables.
    For globals: addresses are raw hex, e.g. 0x20000000
    Locals will be a number relative to the frame pointer
    '''

    assert(lco.isVar() is True)

    symbol = lco.getSTE()   # Get symbol from symbol table
    address = str(symbol.getAddress()) # Get address of variable

    return address
    


  def _incrnumCtrlStruct(self):
    self.numCtrlStructs += 1

  def _getnumCtrlStruct(self) -> int:
    return self.numCtrlStructs
  
  def _generateThenLabel(self, num: int) -> str:
    return "then_"+str(num)

  def _generateElseLabel(self, num: int) -> str:
    return "else_"+str(num)

  def _generateLoopLabel(self, num: int) -> str:
    return "loop_"+str(num)

  def _generateDoneLabel(self, num: int) -> str:
    return "out_"+str(num)


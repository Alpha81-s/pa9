from .Instruction import Instruction, OpCode

class FMv(Instruction):
  def __init__(self, src: str, dest: str):
    super().__init__()
    self.src1 = src # Original had src1 on the right hand side
    self.dest = dest
    self.oc = OpCode.FMVS

  def __init__(self):
    return str(self.oc) + " " + self.dest + " " + self.src1

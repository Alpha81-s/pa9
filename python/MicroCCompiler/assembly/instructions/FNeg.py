from .Instruction import Instruction, OpCode

class FNeg(Instruction):
  def __init__(self, src: str, dest: str):
    super().__init__()
    self.src1 = src
    self.dest = dest
    self.oc = OpCode.FNEGS

  def __str__(self):
    return str(self.oc) + " " + self.dest + ", " + self.src1  # original didn't have str() for the self.oc nor "return"

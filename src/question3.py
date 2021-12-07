from utils import *
from logic2 import *


x = Symbol("x")
y = Symbol("y")
enemies = Symbol("enemies((x), (y))")
hates1 = Symbol("hates((x), (y))")
hates2 = Symbol("hates((y), (x)")

# print(knowledge_for_question1.formula())
knowledge_for_question1 = And(Implication(enemies, And(hates1, hates2)))
#------------------------------------------------------------------------


p = Symbol("p(x)")
q = Symbol("q(x)")
r = Symbol("r(x)")

knowledge_for_question2 = And(Implication(p , And(q, r)))


from logic2 import *



# in English : Carrots color are orange
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge_for_question1 = And(Implication(carrots, orange))

print(knowledge_for_question1.formula())  
#---------------------------------------------------



# in English : " if person is vegetarian , person likes carrots "
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like = Symbol("like")
like_person_carrots = Symbol("like(x, carrots)")
knowledge_for_question2 = And(Implication(vegetarian, like_person_carrots))

print(knowledge_for_question2.formula())  
#---------------------------------------------------


# in English : " student pass if he studies hard "
pass_exam = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_for_question3 = Implication(study_hard, pass_exam)

print(knowledge_for_question3.formula())  
#---------------------------------------------------


# in English : " who will pass? "
Pass = Symbol("? pass(who)")
knowledge_for_question4 = And(Pass)

print(knowledge_for_question4.formula())  
#---------------------------------------------------


# in English : "professor teaches Course "
teaches = Symbol(" teaches(professor, Course)")
knowledge_for_question5 = And(teaches)

 # print the output formula of knowledge base
print(knowledge_for_question5.formula())  
#---------------------------------------------------
# in English : " if x & y are enemies, x hate y and x fight y "
x = Symbol("x")
y = Symbol("y")
enemies = Symbol("enemies((x), (y))")
hates = Symbol("hates((x), (y))")
fight = Symbol("fight({x}, (y))")
knowledge_for_question6 = And(Implication(enemies, And(hates, fight)))

print(knowledge_for_question6.formula()) 

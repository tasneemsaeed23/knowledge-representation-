

# Import libraries
import aima.utils
import aima.logic
# The main entry point for this module
def main():
    
    Array = []
    
    Array.append(aima.utils.expr("Healthy(John)"))
    Array.append(aima.utils.expr("Wealthy(jia)"))
    Array.append(aima.utils.expr("Wealthy(John)"))
    Array.append(aima.utils.expr("Man(John)"))
    Array.append(aima.utils.expr("Woman(Jia)"))
    Array.append(aima.utils.expr("(Wealthy(x) & Healthy(x)) ==> Traveler(x)"))
    Array.append(aima.utils.expr("traveler(x) ==> travel(x)") 
    
    # Create a first-order logic knowledge base (tasneem) with Array
    tasneem = aima.logic.FolKB(Array)
    
    # Get information from the knowledge base with ask
    travel = tasneem.ask(aima.utils.expr('Traveler(x)'))
    wealthy = tasneem.ask(aima.utils.expr('Wealthy(x)'))
    healthy = tasneem.ask(aima.utils.expr('Healthy(x)'))
    # Print answers
    print('Who can travel?')
    print(travel)
    print()
    print('who are wealthy?')
    print(wealthy)
    print()
    print('who are healthy?')
    print(healthy)
    print()
    
# Tell python to run main method
if __name__ == "__main__": main()
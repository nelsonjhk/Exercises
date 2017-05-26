"""
evalLoop takes in the user's input and evaluates it with the python interpreter. It'll do this until
the user types "done," and returns the value of the last evaluated expression.
"""
import sys

def eval_loop():
    last_expression = ""
    done = False
    while not done: 
        expression = input("Enter your expression: ")
        if expression.lower() == 'done':
            done = True
            return last_expression
        else:
            try: 
                last_expression = eval(expression)
                print(last_expression)
            except NameError:
                print("Oops! Looks like that's not a valid Python3 expression. Try again.")
            except: 
                print("Something went wrong. Terminating program.")
                done = True

if __name__ == "__main__":
    eval_loop()

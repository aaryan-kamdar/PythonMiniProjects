import time 
import numpy as np

operators=["+","-","*"]
min_operand=3
max_operand=12
TOTAL_PROBLEMS=10

def generate_problem():
    left=np.random.randint(min_operand,max_operand)
    right=np.random.randint(min_operand,max_operand)
    operator=np.random.choice(operators)
    expr=str(left)+" " + str(operator) +" "+ str(right) 
    print(expr)
    answer=eval(expr)
    return expr,answer
wrong=0
start_time=time.time()
for i in range(TOTAL_PROBLEMS):

    expr,answer=generate_problem()
    while True:
        guess=int(input(f"Problem {i+1} : {expr}"))
        if guess==answer:
            break
        wrong+=1

end_time=time.time()
total_time=end_time-start_time
print(f"{round(total_time,2)} seconds")




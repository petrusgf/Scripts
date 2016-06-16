# Function BIG O
def sum1(n):
    final_sum = 0
    
    for x in range(n+1):
        final_sum += x
        
    return final_sum
#Testing to know how many time spent in a def (Change sum1 for def name)    
if __name__ == '__main__':
    import timeit    
    print(timeit.timeit("sum1(10)", setup="from __main__ import sum1"))

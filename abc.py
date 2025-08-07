#******************************************************************************
# abc.py
#******************************************************************************
# Eduardo E





# GCD function 


def gcd(m, n):
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return m




def is_prime(a):
    # Initialize counter to count the number of multiples
    counter = 0
    #loop to count number of multiples up to the number itself
    for number in range(1,a+1):
        if a%number == 0:
            counter += 1
            
    #if the number ain't one and it has 2 multiples only, it is prime
    if a>1 and counter == 2:
        return True
    

def radical(a,b,c):
    #turn arguments into a list, initialize an empty list for found primes, and another list to put the unique values
    argument = [a,b,c]
    primes = []
    unique_primes = []
    #double loop evaluates the multiples of the arguments and adds them to the primes list if prime
    for element in argument:
        for number in range(1,element + 1):
            if element%number == 0 and is_prime(number):
                primes.append(number)
                
    #take into account only the unique values            
    for prime in primes:
        if  prime not in unique_primes:
            unique_primes.append(prime)
    #multiply all the unique primes        
    answer = 1
    for value in unique_primes:
        answer *= value
    
    return answer
#open the file
number_file = open('ab.txt', 'r')
#initiate cpunter for when the GCD =1 and when (GCD =1 and radical > c)
GCD1_counter = 0
GCD_radical_count = 0

#loop trough the file line by line 
for line in number_file:
    #slit the line and use the numbers
    data = line.split()
    num1 = int(data[0])
    num2 = int(data[1])
    num3 = num1 + num2
    GCD = gcd(num1,num2)
    if GCD == 1:
        GCD1_counter += 1
        result = radical(num1,num2,num3)
        print(f'a: {data[0]}, b: {data[1]}, GCD: {GCD} c: {num3}, Radical: {result}')
        if result > num3:
            GCD_radical_count += 1
    else:
        print(f'a: {data[0]}, b: {data[1]}, GCD: {GCD}')

#print the times the abc conjecture was true as a probability
print(GCD_radical_count/GCD1_counter)
        

        

                



    

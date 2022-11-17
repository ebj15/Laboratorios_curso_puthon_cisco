num = 0
def is_prime(num):
    for i in range(2,num):
        print(i)
        i = num % 2
        if i == 0:                
            return False
print(is_prime(7))
#
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")


  



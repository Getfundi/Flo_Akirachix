def add(a,b):
   answer=a+b
   return answer



def subtract(a,b):
	# print('subtracting',a,b)
	answer=a-b
	return answer


def multiply(a,b):
	answer=a*b
	return answer


def divide(a,b):
	answer=a/b
	return answer
	if a<=0:
		print(a,"cannot be zero")
		return
	elif b<=0:
		print(b,"cannot be zero")
		return
	else:
		print("dividing",a,"and",b)
		answer(a/b)
		return answer
			



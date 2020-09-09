# 내가 생각했던 것 > 코드 돌아가지 않음.. 
def is_vaild(string):
  new_list = []
  dic = {'[':']','{':'}','(':')'}  
  for i in range(len(string)): 
    if string[i] == "(" or string[i] == "{" or string[i] == "[": 
    elif string[i] == ")" or string[i] == "}" or string[i] == "]":
      if len(new_list) == 0:                                     
        return false  
      else:         
        n = new_list.pop()     
         if dic[n] == ')' or dic[n] == '}' or dic[n] == ']':
          return true

# model_solution
def is_valid(string):
    	left = ['(', '{', '['] 
	right = [')', '}', ']'] 
	stack = [] 
	for letter in string:
		if letter in left: 
			stack.append(letter) 
		elif letter in right: 
			if len(stack) <= 0: 
				return False
			if left.index(stack.pop()) != right.index(letter):
				return False
	return len(stack) == 0
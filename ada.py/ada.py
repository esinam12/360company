def calculate (action, firstNumber, secondNumber):
  if action == "multiply":
     result = firstNumber * secondNumber
     return result
    

  if action == "add" :
     result = firstNumber + secondNumber
     return result

  elif action == "divide" :
      result = firstNumber // secondNumber
      return result    


calcResult = calculate("multiply", 20, 4)
calcResult = calculate("add", calcResult, 5)
calcResult = calculate("divide", calcResult, 5)



print("theResultis ",calcResult) 



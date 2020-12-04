#############################
# Dev. by: Nesma Abdelnaby
# Date: 25.Nov.2020
#############################

#make lists to append every income or expenditure to it
list_of_income = []
list_of_expenditure = []
#initiate variables
total_income = 0
total_expenditure = 0
current_balance = 0
total_income =0
max_income =0
income_from_user=0

#warning function to use later
def warning_msg():
  print("WARNING : your Expenditures are more than your balance !!!")

#calculate balance function with 2 decimal numbers
def calculating_balance():
  current_balance = total_income-total_expenditure
  if(current_balance>0):
    print("your balance is : ",round(current_balance,2))
  else:
    print("your balance is : ",0)

  return current_balance

#greeting
print("Hello there, welcome to Cash Flow Manager!")

#make while loop with if conditions to help the customer calculate his cash flow
while(True):
  #ask the user which operation he wants to do
  user_need = input("\nPLEASE CHOOSE OPERATION:\nadd income (+) \nadd expenditure (-) \nsee current Balance (b) \nsee a summary (s) \nexit (x)\n  ")

  
  #take the income from the user and append it to the list of income then sum all incomes
  if(user_need == "+"):
    try:
      income_from_user = float(input( "Enter your income please : "))
      list_of_income.append(income_from_user)
      total_income = sum(list_of_income)
    except:
      print("It's not a number !!")

      
  #take the expenditure from the user and append it to the list of expenditure then sum all expenditure
  elif(user_need == "-"):
    #calculate and print the current balance before deducting expenditure
    current_balance_check = calculating_balance()
    try:
      expenditure_from_user = float(input("Enter your expenditure please :"))
      if(expenditure_from_user > round(current_balance_check,2)):
        warning_msg()
        print("you have only : ", round(current_balance_check,2))
      else:
        list_of_expenditure.append(expenditure_from_user)
        total_expenditure = sum(list_of_expenditure)
    except:
      print("It's not a number !!")
     

  #calculate the current balance and print it
  elif(user_need == "b"):
    calculating_balance()
    
    

  #calculate the summery 
  elif( user_need == "s"):

    #handle if there are no income entries yet
    if(list_of_income ==[]):
      total_income =0
      max_income =0
    else:
      total_income = sum(list_of_income)
      max_income = max(list_of_income)
    
    #handle if there are no exp. entries yet
    if(list_of_expenditure ==[]):
      total_expenditure =0
      max_expenditure =0
    else:
      total_expenditure = sum(list_of_expenditure)
      max_expenditure = max(list_of_expenditure)

    #handle expenditure and balance percentage if total income is 0
    if (total_income ==0):
      expenditure_percentage = 0
      balance_percentage = 0
    else:
      current_balance = total_income-total_expenditure
      expenditure_percentage = (total_expenditure/total_income)*100
      balance_percentage = (current_balance/total_income)*100

    

    #print summery
    print("\n>> SUMMERY <<")
    print("Total Income : ", round(total_income,2))
    print("Total Expenditure : ", round(total_expenditure,2))
    print("remaining Balance", round(current_balance,2))
    print("% expenditure of total income : ",round(expenditure_percentage,2) , "%")
    print("% balance of total income : ", round(balance_percentage,2), "%")
    print("max single expenditure : ",round(max_expenditure,2))
    print("max single income : ",round(max_income,2))

  #exit the loop
  elif( user_need == "x"):
    print("thanx for using Cash Flow Manager :)")
    break

  #warn the user if he put something else
  else:
    print("Invalid input!!")
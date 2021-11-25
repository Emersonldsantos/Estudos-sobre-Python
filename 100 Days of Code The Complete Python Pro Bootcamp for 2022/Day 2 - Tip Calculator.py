'''Instructions
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪'''

##########################RESOLUÇÃO##################################

print('Welcome to the tip calculator')
#Solicitação de preenchimento das seguintes informações:
#    -total da conta
#    -quantas pessoas irão pagar
#    -quanto desejam pagar de gorjeta
# A partir do preenchimento das informações solicitadas acima, poderemos calcular o valor da conta a ser pago por cada pessoa presente.
bill = float(input('What was the total bill?')) #Total da conta

people = int(input('How many people to split the bill?')) #Quantidade de Pessoas

tip = int(input('How much tip would you like to give? 10, 12, or 15?')) #Qual o percentual de gorjeta deseja pagar

# Criação dos condicionais para cálculo do total da conta junto com o percentual de gorjeta que desejam pagar.
if tip == 10:
  bill *= 1.1
elif tip == 12:
  bill *= 1.12
else:
  bill *= 1.15

#Divisão do total da conta por cada pessoa presente.
pay = bill / people
#Print do quanto cada um deve pagar
print('Each person should pay: $' + str(round(pay,2)))

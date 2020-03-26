carros = ( "uno" , "Doblo", "Toro", 2 )

for car in carros:
    print( car )

print("\n ----- \n")
for cont in range( len(carros) ):
# Python 2.x
    print( 'Posicao: {0} Carro:  {1}'.format( cont,  carros[cont] ) )    

# Python 3.x    
#   print( "Posicao: " , cont , " - Carro:  " ,  carros[cont] ) #


#imprimindo a tupla ordenada
frutas = ( "Laranja", "Banana", "Melancia")
print( sorted(frutas) )
print( frutas )


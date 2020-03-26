pessoa = {
    "nome" : "Maria" ,
    "idade" : 25 ,
    "altura" : 1.68 , 
    "temFilhos" : False ,
    "filho" : None
}
print( pessoa )

pessoa["nome"] = "Julia"

print( pessoa ) 

pessoa["email"] = "j@mail.com"

print( pessoa )

del pessoa["email"]

print( pessoa )

pessoa2 = {
    "nome" : "Joao" ,
    "idade" : 50 ,
    "altura" : 1.75 , 
    "temFilhos" : True ,
    "filho" : pessoa
}

print( pessoa2 )
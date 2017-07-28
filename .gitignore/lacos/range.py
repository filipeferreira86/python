#Range tem um sintaxe complicada, sendo inicio e fim, sendo fim não incluido
#O ultimo numero é a quantidade a ser adicionada a cada passada
#Neste caso ele inicia no zero, nossa lista fica com 0, 2, 4, 6, 8
#Isto pq o 10 não entra na lista pois é o ultimo
# neste caso então temos 0, (0+2) 2, (2+2) 4, (4+2) 6, (6+2) 8, (8+2) comoo resultado é 10 não inclui
print(list(range(0, 10, 2)))
# Troy Tural 404
# TP2: Exercise 1c

#Cette ligne nous indique que la variable "stars" qui sont les petits points vont commencer a 11
stars = 11
#While va faire que le rest du code va s`effectuer tant que le nombre de point n`est pas 0 (11 a 1)
while stars != 0:
    #Cette ligne va afficher les points de chaque ligne
    print('*' * stars)
    #Cette ligne va faire que le nombre de point minimale dans une ligne va etre 1 (donc le code arretera lorsqu`il restera 1 point
    stars -= 1

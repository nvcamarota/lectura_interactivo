"""
CLUB DE LECTURA INTERACTIVO
Formas parte de un club de lectura que clasifica libros según las preferencias de las lectoras:
1) Romance y finales felices: recomienda "Orgullo y prejuicio"
2) Aventuras y héroes valientes: sugiere "Harry Potter"
3) Misterios: elige "Sherlock Holmes"
4) Otro género: recomienda "Explora nuevas historias"

Escribe un programa que tome la opción del usuario y muestre la recomendación correspondiente.
"""

preferencia = input("¿Qué tipo de género de libro te gusta más?\n- Romance.\n- Finales Felices.\n- Aventura.\n- Héroes valientes.\n- Misterio.\n- Otro.\n\nTu respuesta: ").capitalize()

romance = preferencia == "Romance" or preferencia == "Finales felices"
aventura = preferencia == "Aventura" or preferencia == "Heroes valientes"
misterio = preferencia == "Misterio"
otro = preferencia == "Otro"

mensaje_romance = "Te recomendamos leer 'Orgullo y prejuicio' ♥"
mensaje_aventura = "Te recomendamos leer la saga de 'Harry Potter' ♥"
mensaje_misterio = "Te recomendamos leer 'Sherlock Holmes' ♥"
mensaje_otro = "Te recomendamos leer 'Explora nuevas historias' ♥"
mensaje_final = "No tenemos libros de ese género que podamos recomendarte. Lo sentimos."

if romance == True:
    print(mensaje_romance)
elif aventura == True:
    print(mensaje_aventura)
elif misterio == True:
    print(mensaje_misterio)
elif otro == True:
    print(mensaje_otro)
else:
    print(mensaje_final)
    
print()
print("Gracias por usar nuestro servicio. Te esperamos nuevamente ♥")
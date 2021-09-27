#Definition of variables
titanic = [
    ["Braund, Mr. Owen Harris",0,3,"masculino",22],
    ["Cumings, Mrs. John Bradley (Florence Briggs Thayer)",1,1,"femenino",38],
    ["Heikkinen, Miss. Laina",1,3,"femenino",26],
    ["Futrelle, Mrs. Jacques Heath (Lily May Peel)",1,1,"femenino",35],
    ["Allen, Mr. William Henry",0,3,"masculino",35],
    ["Saundercock, Mr. William Henry",0,3,"masculino",20],
    ["McCarthy, Mr. Timothy J", 0,1,"masculino",54],
    ["Palsson, Master. Gosta Leonard",0,3,"masculino",2],
    ["Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",1,3,"femenino",27],
    ["Nasser, Mrs. Nicholas (Adele Achem)",1,2,"femenino",14],
    ["Sandstrom, Miss. Marguerite Rut",1,3,"femenino",4]
];
average = 0;
survivorsClass1 = 0;
survivorsClass2 = 0;
survivorsClass3 = 0;

#Body of algorithm
for r in titanic:
    average += r[4];
    if r[2] == 1:
        survivorsClass1 += 1
    if r[2] == 2:
        survivorsClass2 += 1
    if r[2] == 3:
        survivorsClass3 += 1


average = average/len(titanic);
print("El promedio de edad de las personas que viajaban en el barco es de: " + str(average));
print("La cantidad de sobrevivientes que viajaba en la clase "+ "1" + "es de: " + str(survivorsClass1));
print("La cantidad de sobrevivientes que viajaba en la clase "+ "2" + "es de: " + str(survivorsClass2));
print("La cantidad de sobrevivientes que viajaba en la clase "+ "3" + "es de: " + str(survivorsClass3));
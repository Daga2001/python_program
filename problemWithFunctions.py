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

#Body of algorithm

#functions

#Una función para determinar la cantidad de viajeros en el barco.
def travelersAverage():
    travelers = 0;
    counter = 0;
    for i in titanic:
        counter = counter + 1;
        travelers += i[4];
    return travelers/counter;

#Determina el numero de sobrevivientes del accidente de acuerdo a su clase
def numberOfSurvivorOfClass(nClass):
    survivors = 0;
    for i in titanic:
        if i[2] == nClass and i[1] == 1:
            survivors += 1;
    return survivors;

print("El promedio de edad de las personas que viajaban en el barco es de: " + str(travelersAverage()));
print("La cantidad de sobrevivientes que viajaba en la clase "+ "1" + " es de: " + str(numberOfSurvivorOfClass(1)));
print("La cantidad de sobrevivientes que viajaba en la clase "+ "2" + " es de: " + str(numberOfSurvivorOfClass(2)));
print("La cantidad de sobrevivientes que viajaba en la clase "+ "3" + " es de: " + str(numberOfSurvivorOfClass(3)));
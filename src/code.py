import numpy as np
import updated_client as server
import random as random

key='qwOvHsUHfZQuWPRigKhWDvOmI2jCrx9JPwTeLsYUpcaiidLv8E'
num_coefficientWeights=11   #no_of_coefficients for a soln i.e no of genes in a chromosome

soln_per_population=10    #no_of_solutions for a population i.e no of chromosomes
num_of_parents_selected=(soln_per_population/2)         # no of parents selected is 5 since we retain the previous best 5 parents as they will be useful if current generated soln is worst than previous

parents_from_initial_population=[]

def Calc_initialPopulatin(Error_initial_population):
    for it in range(soln_per_population):
        Error_initial_population.append(server.get_errors(key,initial_population[it].tolist()))
        Error_initial_population[it].append(it)
        Error_initial_population[it].append(Error_initial_population[it][0]*3.5+Error_initial_population[it][1]*6.5)
    Error_initial_population=np.array(Error_initial_population)
    return Error_initial_population

def Parents_Selection(parents_from_initial_population,Error_initial_population):
    parents_from_initial_population=Error_initial_population[np.argsort(Error_initial_population[:, 3])]
    return parents_from_initial_population

def Crossover(parents_from_initial_population):
    first_generation=[]
    for i in range(int(soln_per_population/2)):
        temp=[]
        for j in range(num_coefficientWeights):
            temp.append(initial_population[int(parents_from_initial_population[i][2])][j])
        first_generation.append(temp)

    for i in range(int(soln_per_population/2)):
        temp=[]
        temp.append(-10)
        for j in range(5):
            temp.append(first_generation[i][j+1])
        for j in range(5):
            temp.append(first_generation[(i+1)%5][j+6])
        # for j in range(2):
            # temp.append(first_generation[(i+2)%5][j+5])    
        # for j in range(2):
            # temp.append(first_generation[(i+3)%5][j+7])
        # for j in range(2):
            # temp.append(first_generation[(i+4)%5][j+9])
        first_generation.append(temp)
    return first_generation

def Mutation(initial_population):
    num=random.randint(4,6)
    i=0
    for i in range(num): 
        a=random.randint(1,9)
        b=random.randint(1,10)
        initial_population[a][b]=(initial_population[a][b]+initial_population[a][b]*random.uniform(-0.3,0.3))%10
    return initial_population

def ErrorCalcAndPrinting(Error_first_generation):
    for i in range(soln_per_population):
        # print(first_generation[i])    
        Error_first_generation.append(server.get_errors(key,first_generation[i]))
        # print("res: "+str(Error_first_generation[i]))
        Error_first_generation[i].append(i)
        Error_first_generation[i].append(Error_first_generation[i][0]*3.5+Error_first_generation[i][1]*6.5)
    return Error_first_generation

temp1=np.array([-10.0, 4.06805041404064, -0.09, 0.054, -3.86000157715883e-07, 2.901944449494161e-07, -6.93409e-09, -6.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -3.430100176902565e-15])
temp2=np.array([-10.0, 4.56805041404064, -0.09, 0.054, -3.86000157715883e-07, 2.901944449494161e-07, -6.93409e-09, -6.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -4.730100176902565e-15])
temp3=np.array([-10, 3.6732405419386582, -0.09, 0.054, -3.86000157715883e-07, 2.901944449494161e-07, -6.93409e-09, -6.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -3.430100176902565e-15])
temp4=np.array([-10.0, 4.56805041404064, -0.09, 0.054, -3.86000157715883e-07, 2.901944449494161e-07, -6.93409e-09, -6.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -4.730100176902565e-15])
temp5=np.array([-10.0, 4.56805041404064, -0.09, 0.054, -3.86000157715883e-10, 2.901944449494161e-07, -6.93409e-09, -7.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -4.730100176902565e-15])
temp6=np.array([-10.0, 5.968050414040641, -0.05, 0.054, -3.86000157715883e-10, 2.901944449494161e-07, -6.93409e-09, -7.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -4.730100176902565e-15])
temp7=np.array([-10, 4.06805041404064, -0.09, 0.054, -3.86000157715883e-07, 2.901944449494161e-07, -6.93409e-09, -7.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -4.730100176902565e-15])
temp8=np.array([-10, 4.56805041404064, -0.09, 0.054, -3.86000157715883e-07, 2.901944449494161e-07, -6.93409e-09, -7.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -3.430100176902565e-15])
temp9=np.array([-10, 4.56805041404064, -0.09, 0.054, -3.86000157715883e-10, 2.901944449494161e-07, -6.93409e-09, -6.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -4.730100176902565e-15])
temp10=np.array([-10, 5.968050414040641, -0.05, 0.054, -3.86000157715883e-07, 2.901944449494161e-07, -6.93409e-09, -6.00985565299179e-10, 3.488006383229681e-12, 4.551492499340711e-14, -4.730100176902565e-15])

initial_population=np.array([temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,temp10])

Error_initial_population=[]
Error_initial_population = Calc_initialPopulatin(Error_initial_population)
parents_from_initial_population=[]
parents_from_initial_population=Parents_Selection(parents_from_initial_population,Error_initial_population)
print("\n")
print("Pool size: 10")
print("Fitness function: TrailError*3.5+ValidationError*6.5")
print("Crossover: Diagonal MultiParent Crossover")
print("Mutations: Few elements in the vector will be increased or decreased by 30%,of its value\n")
print("Now the Genetic Algorithm Starts:\n")
print("Initial Population along with their Train and Validation errors: ")
here=0
for here in range(len(initial_population)):
    print(initial_population[here])
    print("Train Error:",Error_initial_population[here][0])
    print("Validation Error:",Error_initial_population[here][1])
TotalIterations=4
for iterations in range(TotalIterations):
    print("\nAfter applying the fitness function,the vectors selected for crossover are:")
    here=0
    for here in range(int(len(parents_from_initial_population)/2)):
        print(initial_population[int(parents_from_initial_population[here][2])])

    first_generation=Crossover(parents_from_initial_population)
    print("\nThe vectors obtained after performing the crossover are:")
    here=0
    for here in range(len(first_generation)):
        print(first_generation[here])

    initial_population=first_generation
    initial_population=Mutation(initial_population)
    print("\nThe vectors obtained after performing Mutation are:")
    here=0
    for here in range(len(initial_population)):
        print(initial_population[here])

    print("\n============================================================================================")
    print("============================================================================================")
        
    Error_first_generation=[]
    Error_first_generation=ErrorCalcAndPrinting(Error_first_generation)
    if(iterations+1<TotalIterations):
        print("\n Next Generation")
        print("\nInitial population of Generation",(iterations+1)," along with the Train and Validation errors are:")
    else:
        print("\nNow the iterations are completed(i.e ",iterations+1," iterations are completed), and below are the resulted vectors along with Train and Validation errors:")
    here=0
    for here in range(len(initial_population)):
        print(initial_population[here])
        print("Train Error: ",Error_first_generation[here][0])
        print("Validation Error: ",Error_first_generation[here][1])
    
    Error_first_generation=np.array(Error_first_generation)
    parents_from_initial_population=Parents_Selection(parents_from_initial_population,Error_first_generation)
  
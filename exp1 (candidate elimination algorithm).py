#this is the candidate elimination algorithm

import csv #we import the required library that is csv
with open("job_data.csv") as file: #opening the csv as file 
    data = list(csv.reader(file)) 
# Separate header and training data
header = data[0]  #gets the header that is [CGPA,Skills,Internship,Job]
training_data = data[1:]  # gets the traing data , that is everything except the header file
# Initialize S and G
S = ['Ø'] * (len(header) - 1)  #this initialises the s with 'Ø'
G = ['?'] * (len(header) - 1)  #this initialiss the g with '?' as [?,?,?]
print("Initial S:", S)
print("Initial G:", G)
print("-" * 40)
# Process each example
for row in training_data:    #traverses through the traing data 
    attributes = row[:-1]  #takes everything except the last element like [[High,No,Yes]
    label = row[-1]  #takes the last element like [High,No,Yes,No] as no 
    if label == "Yes": # Positive example
        for i in range(len(S)):  #takes 3 as raange since that is the length of s
            if S[i] == 'Ø':   
                S[i] = attributes[i] #if it passes the if block it takes the value of attributes such as high for 0 and so on
            elif S[i] != attributes[i]:  #if it doesnt cross the if block it goes to this block which checks if s[i] is same as attributes of i 
                S[i] = '?'  #it fills with ?
    else: # Negative example takes the no as input 
        for i in range(len(G)):     #takes the g this time instead of s as its an negative example 
            if G[i] == '?' and S[i] != attributes[i]:  
                G[i] = S[i]
    print("Example:", row)  
    print("S =", S) 
    print("G =", G)
    print("-" * 40)
print("Final S:", S)  #prints the final s 
print("Final G:", G) #prints the final g 



#the csv file (job_data.csv) is as below 
CGPA,Skills,Internship,Job
High,Yes,Yes,Yes
High,Yes,No,Yes
Low,Yes,Yes,No
High,No,Yes,No

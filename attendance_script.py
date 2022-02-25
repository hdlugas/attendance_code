# This script is used to count attendance points for online synchronous courses.
#
# Instructions: Direct the students to message the word 'here' in the zoom chat. This will
# ensure that their name shows up in the text file of the chat. This script imports four
# text files (one for each day my course met), and records whether the student was in 
# attendance each day. 
# 
# For my course in particular, students must have attended 3 of 4 weekly class sessions
# to get full attendance credit. To award these points accordingly, I simply look at the output of this script


import numpy as np


name_vec = ['student1','student2','student3']

count_1 = np.zeros((len(name_vec)))
count_2 = np.zeros((len(name_vec)))
count_3 = np.zeros((len(name_vec)))
count_4 = np.zeros((len(name_vec)))
count_final = np.zeros((len(name_vec)))



#import attendance records
file1 = open("/home/hunter/attendance_records/monday.txt","r")
file2 = open("/home/hunter/attendance_records/tuesday.txt","r")
file3 = open("/home/hunter/attendance_records/wednesday.txt","r")
file4 = open("/home/hunter/attendance_records/thursday.txt","r")
readfile1 = file1.read()
readfile2 = file2.read()
readfile3 = file3.read()
readfile4 = file4.read()


for i in range(0,len(name_vec)):
    if name_vec[i] in readfile1: 
        count_1[i] = 1

for i in range(0,len(name_vec)):
    if name_vec[i] in readfile2: 
        count_2[i] = 1

for i in range(0,len(name_vec)):
    if name_vec[i] in readfile3: 
        count_3[i] = 1

for i in range(0,len(name_vec)):
    if name_vec[i] in readfile4: 
        count_4[i] = 1


for i in range(0,len(name_vec)):
    count_final[i] = count_1[i] + count_2[i] + count_3[i] + count_4[i]


for i in range(0,len(name_vec)):
    print(name_vec[i],'attended', int(count_final[i]),'of 4 weekly class sessions')


# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:54:03 2022

@author: user
"""

import pandas as pd
import csv
import numpy as np
import statistics as st
import scipy
from scipy.stats import skew
from scipy import signal
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.preprocessing import StandardScaler
import seaborn as sns

#Εισαγωγή δεδομένων
p1 = pd.read_csv("activity_recongition/Participant_1.csv")
p2 = pd.read_csv("activity_recongition/Participant_2.csv")
p3 = pd.read_csv("activity_recongition/Participant_3.csv")
p4 = pd.read_csv("activity_recongition/Participant_4.csv")
p5 = pd.read_csv("activity_recongition/Participant_5.csv")
p6 = pd.read_csv("activity_recongition/Participant_6.csv")
p7 = pd.read_csv("activity_recongition/Participant_7.csv")
p8 = pd.read_csv("activity_recongition/Participant_8.csv")
p9 = pd.read_csv("activity_recongition/Participant_9.csv")
p10 = pd.read_csv("activity_recongition/Participant_10.csv")

'''Παρατηρούμε ότι τα δεδομένα σε κάθε πίνακα συμμετέχοντα έχουν τύπο δεδομένων object
Επιλέγουμε από κάθε συμμετέχοντα μονο τις στήλες που δίνουν το τρισδιάστατο σήμα του 
επιταχυνσιόμετρου(Αx, Ay, Az) που αντιστοιχεί στη θέση “right pocket”, δηλαδή τις στήλες 
15, 16, 17 και αφήνουμε και την πρώτη γραμμή που περιέχει τα ονόματα Αx, Ay και Az για να 
μπορέσουμε στην συνέχεια να κάνουμε πράξεις.'''
P1=p1.iloc[1:,15:18]
P2=p2.iloc[1:,15:18]
P3=p3.iloc[1:,15:18]
P4=p4.iloc[1:,15:18]
P5=p5.iloc[1:,15:18]
P6=p6.iloc[1:,15:18]
P7=p7.iloc[1:,15:18]
P8=p8.iloc[1:,15:18]
P9=p9.iloc[1:,15:18]
P10=p10.iloc[1:,15:18]

#αλλάζουμε τον τύπο δεδομένων των καταγραφών σε πραγματικούς αριθμούς
P1=P1.astype(float)
P2=P2.astype(float)
P3=P3.astype(float)
P4=P4.astype(float)
P5=P5.astype(float)
P6=P6.astype(float)
P7=P7.astype(float)
P8=P8.astype(float)
P9=P9.astype(float)
P10=P10.astype(float)

# Μετατρέπουμε το τρισδιάστατο σήμα του επιταχυνσιομέτρου σε μονοδιάστατο παίρνοντας
#το μέτρο του διανύσματος επιτάχυνσης σε κάθε συμμετέχοντα
PP1=np.sqrt((P1.iloc[:,0]**2)+(P1.iloc[:,1]**2)+(P1.iloc[:,2]**2))
PP2=np.sqrt((P2.iloc[:,0]**2)+(P2.iloc[:,1]**2)+(P2.iloc[:,2]**2))
PP3=np.sqrt((P3.iloc[:,0]**2)+(P3.iloc[:,1]**2)+(P3.iloc[:,2]**2))
PP4=np.sqrt((P4.iloc[:,0]**2)+(P4.iloc[:,1]**2)+(P4.iloc[:,2]**2))
PP5=np.sqrt((P5.iloc[:,0]**2)+(P5.iloc[:,1]**2)+(P5.iloc[:,2]**2))
PP6=np.sqrt((P6.iloc[:,0]**2)+(P6.iloc[:,1]**2)+(P6.iloc[:,2]**2))
PP7=np.sqrt((P7.iloc[:,0]**2)+(P7.iloc[:,1]**2)+(P7.iloc[:,2]**2))
PP8=np.sqrt((P8.iloc[:,0]**2)+(P8.iloc[:,1]**2)+(P8.iloc[:,2]**2))
PP9=np.sqrt((P9.iloc[:,0]**2)+(P9.iloc[:,1]**2)+(P9.iloc[:,2]**2))
PP10=np.sqrt((P10.iloc[:,0]**2)+(P10.iloc[:,1]**2)+(P10.iloc[:,2]**2))

#Οι τιμές μέτρου που είναι πάνω από 1000 αντιστοιχούν σε σφάλματα του αισθητήρα.
#Αντικαθιστούμε τις τιμές αυτές με την προηγούμενη τιμή του αισθητήρα.
matrix_lengthPP1 = len(PP1) #Oρίζουμε το μήκος των πινάκων
matrix_lengthPP2 = len(PP2)
matrix_lengthPP3 = len(PP3)
matrix_lengthPP4 = len(PP4)
matrix_lengthPP5 = len(PP5)
matrix_lengthPP6 = len(PP6)
matrix_lengthPP7 = len(PP7)
matrix_lengthPP8  = len(PP8)
matrix_lengthPP9 = len(PP9)
matrix_lengthPP10 = len(PP10)

for i in range(matrix_lengthPP1):
    if PP1[i+1]>1000:
        PP1[i]=PP1[i-1]
for i in range(matrix_lengthPP2):
    if PP2[i+1]>1000:
        PP2[i]=PP2[i-1]
for i in range(matrix_lengthPP3):
    if PP3[i+1]>1000:
        PP3[i]=PP3[i-1]
for i in range(matrix_lengthPP4):
    if PP4[i+1]>1000:
        PP4[i]=PP4[i-1]
for i in range(matrix_lengthPP5):
    if PP5[i+1]>1000:
        PP5[i]=PP5[i-1]
for i in range(matrix_lengthPP6):
    if PP6[i+1]>1000:
        PP6[i]=PP6[i-1]
for i in range(matrix_lengthPP7):
    if PP7[i+1]>1000:
        PP7[i]=PP7[i-1]
for i in range(matrix_lengthPP8):
    if PP8[i+1]>1000:
        PP8[i]=PP8[i-1]
for i in range(matrix_lengthPP9):
    if PP9[i+1]>1000:
        PP9[i]=PP9[i-1]
for i in range(matrix_lengthPP10):
    if PP10[i+1]>1000:
        PP10[i]=PP10[i-1]
        
#Kάνουμε έλεγχο
PP1.loc[PP1>1000]
PP2.loc[PP2>1000]
PP3.loc[PP3>1000]
PP4.loc[PP4>1000]
PP5.loc[PP5>1000]
PP6.loc[PP6>1000]
PP7.loc[PP7>1000]
PP8.loc[PP8>1000]
PP9.loc[PP9>1000]
PP10.loc[PP10>1000]
PP1

#Παίρνουμε την στήλη που αντιστοιχεί στη δραστηριότητα που εκτελείται
last1=p1.iloc[1:,69] 

#Παίρνουμε τον πίνακα με το μέτρο του διανύσματος επιτάχυνσης του κάθε Participant και 
#στην τελευταία στήλη αντιστοιχούμε τη δραστηριότητα που εκτελείται
A= pd.concat([PP1,PP2,PP3,PP4,PP5,PP6,PP7,PP8,PP9,PP10,last1], axis=1)
A.iloc[:,10]

'''Θέλουμε να επιλέξουμε παράθυρα 20 δευτερολέπτων του σήματος, με βήμα 1 δευτερόλεπτο.
Το δείγμα μας έχει ρυθμό (rate) 50 samples per second δηλαδή συχνότητα f=50 Hz aρα  η 
χρονική απόσταση μεταξύ των δειγμάτων υπολογίζεται απο τον τύπο f=1/T => T=1/50=0.02 sec .
Συνεπ΄ως τα δείγματα που συλλέγονται σε 20 sec ειναι 20/0.02=1000 δείγματα και το βήμα 
είναι 50 δείγματα. Επιλέγω λοιπόν τα παράθυρα 
Mε Αi ονομάζω τον πίνακα που κάθε γράμμη του θα περιέχει τα χαρακτηριστικά που 
εξάγονται απο κάθε παράθυρο του Participant i
Χρησιμοποιώ τον μετρητη m για να βάλω τιμε΄ς σε κάθε παράθυρο των Αi
για το βήμα θα ξεκινήσω απο το i=0 και με βημα 50 θα παω μεχρι το 62999-1000+1=621000 
Αρχικά θα δούμε πόσα παράθυρα έχουμε'''

M=[]
for i in range(0,62001,50):
    M.append(i)
len(M)

'''Άρα έχουμε 1241 παράθυρα για κάθε Participant
1η στήλη κάθε Participant: Μεση Τιμη
2η //     //     //     :Τυπική απόκλιση των τιμών του παραθύρου
3η //     //     //     :Ασυμμετρία κατανομής - skewness
4η //     //     //     :Μέγιστη τιμή
5η //     //     //     :Ελάχιστη τιμή 
6η //     //     //     :Διαφορά μεταξύ μέγιστης και ελάχιστης τιμής 
7η //     //     //     :Εκτίμηση ισχύος φάσματος με τη μέθοδο του Welch
Ταυτοχρονα κάνουμε και Κανονικοποίηση
Έτσι, η StandardScaler() θα κανονικοποιήσει τα χαρακτηριστικά μεμωνομένα
έτσι ώστε κάθε στήλη/χαρακτηριστικό να έχει μ = 0 και σ = 1.'''
scale = StandardScaler()

A0=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([np.mean(PP1.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
A01=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([np.std(PP1.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
A02=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP1.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
A03=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP1.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
A04=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP1.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
A05=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP1.iloc[i:1000+i])-min(PP1.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])

'''Για την ισχύ φάσματος
Εμείς θα επιλέξουμε την συχνότητα που έχουμε την μέγιστη ισχύ φάσματος
δηλαδή σε κάθε παράθυρο διαλέγω απί τον πρώτο πίνακα που μας δίνει η μέθοδος Welch (δηλαδή τον 
πίνακα με τις συχνότητες των δειγμάτων στα επικαλυπτ΄ωμενα τμήματα) τη συχνότητα που αντιστοιχεί 
στον δείκτη εκείνον που αντιστοιχεί στην τιμή που ο δεύτερος πίνακας
εμφανίζει το μεγαλύτερο φάσμα ισχύος '''

A06=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP1.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP1.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP1.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
                 
a0= pd.concat([A0,A01,A02,A03,A04,A05,A06], axis=1)
a0

'''Σε κάθε παράθυρο αντιστοιχίζουμε μία δραστηριότητα που είναι η δραστηριότητα με την
πλειοψηφία στα δείγματα που περιέχονται στο παράθυρο.
Για να το κάνουμε αυτο χρησιμοποιούμε την εντολή value_counts().idxmax()'''

last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
last2
a1= pd.concat([A0,A01,A02,A03,A04,A05,A06,last2], axis=1)
a1

#2ος Participant
B0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP2.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
B1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP2.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
B2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP2.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
B3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP2.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
B4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP2.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
B5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP2.iloc[i:1000+i])-min(PP2.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
B6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP2.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP2.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP2.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a2= pd.concat([B0,B1,B2,B3,B4,B5,B6,last2], axis=1)
a2

#3ος Participant
C0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP3.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
C1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP3.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
C2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP3.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
C3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP3.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
C4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP3.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
C5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP3.iloc[i:1000+i])-min(PP3.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
C6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP3.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP3.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP3.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a3= pd.concat([C0,C1,C2,C3,C4,C5,C6,last2], axis=1)
a3

#4ος Participant
D0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP4.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
D1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP4.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
D2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP4.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
D3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP4.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
D4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP4.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
D5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP4.iloc[i:1000+i])-min(PP4.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
D6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP4.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP4.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP4.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a4= pd.concat([D0,D1,D2,D3,D4,D5,D6,last2], axis=1)
a4

#5ος Participant
E0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP5.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
E1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP5.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
E2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP5.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
E3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP5.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
E4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP5.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
E5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP5.iloc[i:1000+i])-min(PP5.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
E6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP5.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP5.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP5.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a5= pd.concat([E0,E1,E2,E3,E4,E5,E6,last2], axis=1)
a5

#6ος Participant
F0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP6.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
F1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP6.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
F2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP6.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
F3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP6.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
F4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP6.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
F5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP6.iloc[i:1000+i])-min(PP6.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
F6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP6.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP6.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP6.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a6= pd.concat([F0,F1,F2,F3,F4,F5,F6,last2], axis=1)
a6

#7ος Participant
G0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP7.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
G1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP7.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
G2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP7.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
G3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP7.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
G4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP7.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
G5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP7.iloc[i:1000+i])-min(PP7.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
G6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP7.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP7.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP7.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a7= pd.concat([G0,G1,G2,G3,G4,G5,G6,last2], axis=1)
a7

#8ος Participant
I0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP8.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
I1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP8.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
I2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP8.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
I3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP8.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
I4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP8.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
I5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP8.iloc[i:1000+i])-min(PP8.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
I6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP8.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP8.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP8.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a8= pd.concat([I0,I1,I2,I3,I4,I5,I6,last2], axis=1)
a8

#9ος Participant
J0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP9.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
J1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP9.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
J2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP9.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
J3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP9.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
J4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP9.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
J5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP9.iloc[i:1000+i])-min(PP9.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
J6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP9.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP9.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP9.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a9= pd.concat([J0,J1,J2,J3,J4,J5,J6,last2], axis=1)
a9

#10ος Participant
K0= pd.DataFrame(scale.fit_transform( pd.concat([pd.DataFrame([np.mean(PP10.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True) ), columns=['Mean'])
K1=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([st.pstdev(PP10.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Std'])
K2=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([skew(PP10.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Skew'])
K3=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP10.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Max'])
K4=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([min(PP10.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Min'])
K5=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([max(PP10.iloc[i:1000+i])-min(PP10.iloc[i:1000+i])]) for i in range(0,62001,50)],
          ignore_index=True)),columns=['Max-Min'])
K6=pd.DataFrame(scale.fit_transform(pd.concat([pd.DataFrame([scipy.signal.welch(PP10.iloc[i:1000+i], fs=50)[0][np.where( scipy.signal.welch(PP10.iloc[i:1000+i], fs=50)[1]== max(scipy.signal.welch(PP10.iloc[i:1000+i], 50)[1]))[0][0]]]) for i in range(0,62001,50)],
          ignore_index=True)), columns=['Welch'])
last2=pd.concat([pd.DataFrame([last1.iloc[i:1000+i].value_counts().idxmax()], columns=['Activity']) for i in range(0,62001,50)],
          ignore_index=True)
a10= pd.concat([K0,K1,K2,K3,K4,K5,K6,last2], axis=1)
a10

'''Σε κάθε έναν από τους πίνακες προσθέτω μια στήλη που δηλώνει σε ποιον συμμετέχοντα
    ανήκουν τα δεδομένα.'''    
a1['Participant']='Participant 1'
a2['Participant']='Participant 2'
a3['Participant']='Participant 3'
a4['Participant']='Participant 4'
a5['Participant']='Participant 5'
a6['Participant']='Participant 6'
a7['Participant']='Participant 7'
a8['Participant']='Participant 8'
a9['Participant']='Participant 9'
a10['Participant']='Participant 10'


'''LOSO ΕΚΠΑΙΔΕΥΣΗ
    Βάζω τα δεδομένα όλων των Particpants σε ένα ενιαίο dataframe.'''
dframe = pd.concat([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10],axis=0)

'''Πρώτα θα μετατρέψω το κατηγορικό διάνυσμα στόχων (string) σε μορφή που να μπορεί να 
   εισαχθεί στα SVM. Αντιστοιχίζω σε κάθε δραστηριότητα έναν αριθμό από το 1 ως το 7.
   ΄΄Ετσι, walking=1, standing=2, jogging=3, sitting=4, biking=5, upstairs=6, downstairs=7.
   Το ίδιο θα κάνω και με τους Participants.'''
dframe['Activity'] = dframe['Activity'].replace('walking',1)
dframe['Activity'] = dframe['Activity'].replace('standing',2)
dframe['Activity'] = dframe['Activity'].replace('jogging',3)  
dframe['Activity'] = dframe['Activity'].replace('sitting',4)
dframe['Activity'] = dframe['Activity'].replace('biking',5)
dframe['Activity'] = dframe['Activity'].replace('upstairs',6)
dframe['Activity'] = dframe['Activity'].replace('downstairs',7)

dframe['Participant'] = dframe['Participant'].replace('Participant 1',1)
dframe['Participant'] = dframe['Participant'].replace('Participant 2',2)
dframe['Participant'] = dframe['Participant'].replace('Participant 3',3)
dframe['Participant'] = dframe['Participant'].replace('Participant 4',4)
dframe['Participant'] = dframe['Participant'].replace('Participant 5',5)
dframe['Participant'] = dframe['Participant'].replace('Participant 6',6)
dframe['Participant'] = dframe['Participant'].replace('Participant 7',7)
dframe['Participant'] = dframe['Participant'].replace('Participant 8',8)
dframe['Participant'] = dframe['Participant'].replace('Participant 9',9)
dframe['Participant'] = dframe['Participant'].replace('Participant 10',10)


''' SVM '''
from sklearn import svm, metrics
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix 
from sklearn.model_selection import LeaveOneGroupOut

X = dframe.iloc[:,0:7].values
y = dframe['Activity'].values
groups = dframe['Participant'].values
logo=LeaveOneGroupOut()
logo.get_n_splits(X, y, groups=groups)

'''Δοκιμές μοντέλων SVM  για διάφορες τιμές των υπερπαραμέτρων C και γ.'''
'''Μοντέλο με τιμές C=0.1 και γ=1.'''
modl1 = SVC(C=0.1, kernel='rbf', gamma=1)

conf_mtx1 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    modl1.fit(X_train, y_train)
    y_pred1 = modl1.predict(X_test)
    conf_mtx1.append(confusion_matrix(y_test,y_pred1)) 
'''Μέσω της παραπάνω for έχουμε κάνει 10 επαναλήψεις διαχωρισμού των δεδομένων σε train και 
    test σετ, όπου κάθε φορά, μέσω του attribute groups της LeaveOneGroupOut(), παίρνουμε τα
    δεδομένα ενός από τους 9 συμμετέχοντες ως test set και των υπολοίπων ως training set.'''
  
#Αθροίζω τους confusion matrix κάθε επανάληψης για να βγάλω τον τελικό
cm_final1 = np.zeros((7,7))
for item in conf_mtx1:
     cm_final1 += item   

'''Plot του Confusion Matrix'''
ax= plt.subplot()
sns.heatmap(cm_final1, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for C=0.1 and gamma=1'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

'''Δημιουργώ μια συνάρτηση για να υπολογίσω την ακρίβεια από τον τελικό πίνακα συνάφειας.'''
def accuracy(confusion_matrix):
    diag_sum=confusion_matrix.trace() #άθροισμα διαγώνιων στοιχείων του πίνακα
    sum_of_all=confusion_matrix.sum() #άθροισμα όλων των στοιχείων του πίνακα 
    return diag_sum/sum_of_all        #accuracy=(TP+TN)/(TP+TN+FP+FN)

'''Υπολογίζουμε και άλλες μετρικές αξιολόγησης, όπως η μέση ευστοχία (precision) 
    και μέση ανάκληση (recall). Για τον υπολογισμό αυτών των μετρικών, θα πρέπει πρώτα να υπολογίσουμε
    τα TP, TN, FP και FN για κάθε κλάση.'''    
def precision(confusion_matrix):
    diag = [confusion_matrix[j][j] for j in range(len(confusion_matrix))] #άθροισμα διαγώνιων στοιχείων του πίνακα
    sum_cols = np.sum(confusion_matrix, axis=0)         #λίστα με τα αθροίσματα των στηλών
    sum_rows = np.sum(confusion_matrix, axis=1)         #λίστα με τα αθροίσματα των γραμμών
    FP=[]
    for i in range(len(confusion_matrix)):
        fpi=sum_cols[i]-diag[i]  #υπολογίζω τα FP=άθροισμα στήλης(predicted)-διαγώνιο στοιχείο που
        FP.append(fpi)           #είναι σωστά ταξινομημένο και τα βάζω σε λίστα
    return np.mean(diag[i]/(diag[i]+FP[i]))  #precision=TP/(TP+FP) (AVERAGE PRECISION)
 
def recall(confusion_matrix):
    diag2 = [confusion_matrix[j][j] for j in range(len(confusion_matrix))]
    sum_cols = np.sum(confusion_matrix, axis=0) 
    sum_rows = np.sum(confusion_matrix, axis=1) 
    FN=[]
    for i in range(len(confusion_matrix)):
        fni=sum_rows[i]-diag2[i]      #υπολογίζω τα FN=άθροισμα γραμμής-διαγώνιο στοιχείο που
        FN.append(fni)                #είναι σωστά ταξινομημένο και τα βάζω σε λίστα
    return np.mean(diag2[i]/(diag2[i]+FN[i])) #recall=TP/(TP+FN)  (AVERAGE RECALL)

print('Accuracy: {:.2f}'.format(accuracy(cm_final1)))
print('Precision: {:.2f}'.format(precision(cm_final1)))
print('Recall: {:.2f}'.format(recall(cm_final1)))


'''SVM με τις τιμές C=10 και γ=0.05'''
modl2 = SVC(C=10, kernel='rbf', gamma=0.05)

conf_mtx2 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    modl2.fit(X_train, y_train)
    y_pred2 = modl2.predict(X_test)
    conf_mtx2.append(confusion_matrix(y_test,y_pred2))

cm_final2 = np.zeros((7,7))
for item in conf_mtx2:
     cm_final2 += item        

ax= plt.subplot()
sns.heatmap(cm_final2, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for C=10 and gamma=0.05'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print('Accuracy: {:.2f}'.format(accuracy(cm_final2)))
print('Precision: {:.2f}'.format(precision(cm_final2)))
print('Recall: {:.2f}'.format(recall(cm_final2)))


'''SVM με τις default τιμές C=1 και γ=1/n, (n το μήκος του διανύσματος χαρακτηριστικ΄ών).'''
modl3 = SVC(C=1, kernel='rbf', gamma='scale')

conf_mtx3 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    modl3.fit(X_train, y_train)
    y_pred3 = modl3.predict(X_test)
    conf_mtx3.append(confusion_matrix(y_test,y_pred3))
    
cm_final3 = np.zeros((7,7))
for item in conf_mtx3:
      cm_final3 += item    

ax= plt.subplot()
sns.heatmap(cm_final1, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for default C and γ'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print('Accuracy: {:.2f}'.format(accuracy(cm_final3)))
print('Precision: {:.2f}'.format(precision(cm_final3)))
print('Recall: {:.2f}'.format(recall(cm_final3)))

'''Με την GridSearchCV, πραγματοποιούμε εξαντλητική έρευνα για τις βέλτιστες 
   υπερπαραμέτρους του μοντέλου.'''      
param_grid = {'C': [0.1, 1, 10, 100, 1000],
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['rbf']}

grid_svm = GridSearchCV(SVC(), param_grid, cv=10, refit=True, verbose = 3, \
                        scoring='accuracy', return_train_score=False)

for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    grid_svm.fit(X_train, y_train)
    y_pred = grid_svm.predict(X_test)  

#Κάποιες ενδεικτικές τιμές παραμέτρων κατά την διερεύνηση
results=pd.DataFrame(grid_svm.cv_results_)
C_svm=pd.DataFrame(results.iloc[:,4].values)
gamma_svm=pd.DataFrame(results.iloc[:,5].values)
params = pd.concat((C_svm, gamma_svm), axis=1)


# Τυπώνουμε τις βέλτιστες παραμέτρους του μοντέλου.
print(grid_svm.best_params_)

'''Το βέλτιστο μοντέλο είναι αυτό με C=1 και γ=0.1 '''
modl_best = SVC(C=1, kernel='rbf', gamma=0.1)

conf_mtx = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    modl_best.fit(X_train, y_train)
    y_pred = modl_best.predict(X_test)
    conf_mtx.append(confusion_matrix(y_test,y_pred))

cm_final = np.zeros((7,7))
for item in conf_mtx:
     cm_final += item    

ax= plt.subplot()
sns.heatmap(cm_final, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for the best model (C=1, γ=0.1)'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print('Accuracy: {:.2f}'.format(accuracy(cm_final)))
print('Precision: {:.2f}'.format(precision(cm_final)))
print('Recall: {:.2f}'.format(recall(cm_final)))
############################################################################################

''' Δημιουργώ ένα νέο dataframe dframe_svm = dframe, στο οποίο θα συγχωνε΄ύσω τις 
    δραστηριότητες που συγχέονται.'''        
dframe_svm = dframe

'''Η δραστηριότητα walking downstairs(7) συγχέεται με τις δραστηριότητες walking(1) και 
    walking upstairs(6),οπότε θα την ομαδοποιήσουμε χάριν ευκολίας με την walking upstairs(6).'''
dframe_svm['Activity'] = dframe_svm['Activity'].replace(6,67)
dframe_svm['Activity'] = dframe_svm['Activity'].replace(7,67)

'''Η δραστηριότητα standing(2) συγχέεται με την δραστηριότητες sitting(4),
    οπότε θα τις ομαδοποιήσουμε.'''
    
dframe_svm['Activity'] = dframe_svm['Activity'].replace(2,24)
dframe_svm['Activity'] = dframe_svm['Activity'].replace(4,24)

'''Οπότε παίρνουμε τα νέα διανύσματα προτύπων και στόχων.'''
X_new = dframe_svm.iloc[:,0:7].values  
y_new = dframe_svm['Activity'].values 
groups = dframe_svm['Participant']
logo=LeaveOneGroupOut()
logo.get_n_splits(X_new, y_new, groups=groups)

modl_best_new = SVC(C=1, kernel='rbf', gamma=0.1)
conf_mtx_new = []
for train, test in logo.split(X_new, y_new, groups):
    print("TRAIN:", train, "TEST:", test)
    X_new_train, X_new_test = X_new[train], X_new[test]
    y_new_train, y_new_test = y_new[train], y_new[test]
    modl_best_new.fit(X_new_train, y_new_train)
    y_new_pred = modl_best_new.predict(X_new_test)
    conf_mtx_new.append(confusion_matrix(y_new_test,y_new_pred))

cm_final_new = np.zeros((5,5))
for item in conf_mtx_new:
     cm_final_new += item    

ax= plt.subplot()
sns.heatmap(cm_final_new, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for the best model-merged classes'); 
ax.xaxis.set_ticklabels(range(1,6)); ax.yaxis.set_ticklabels(range(1,6));

print('Accuracy: {:.2f}'.format(accuracy(cm_final_new)))
print('Precision: {:.2f}'.format(precision(cm_final_new)))
print('Recall: {:.2f}'.format(recall(cm_final_new)))


''' ΚΝΝ '''
from sklearn.neighbors import KNeighborsClassifier

#KNN για k=5
knn2= KNeighborsClassifier(n_neighbors=5) 

knn_conf_mtx2 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    knn2.fit(X_train, y_train)
    knn_y_pred2 = knn2.predict(X_test)
    knn_conf_mtx2.append(confusion_matrix(y_test,knn_y_pred2))
    
#Αθροίζω τους confusion matrix κάθε επανάληψης για να βγάλω τον τελικό
knn_cm_final2 = np.zeros((7,7))
for item in knn_conf_mtx2:
     knn_cm_final2 += item
     
#Plot του Confusion Matrix
ax= plt.subplot()
sns.heatmap(knn_cm_final2, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for k=5'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));
    
print('Accuracy: {:.2f}'.format(accuracy(knn_cm_final2)))
print('Precision: {:.2f}'.format(precision(knn_cm_final2)))
print('Recall: {:.2f}'.format(recall(knn_cm_final2)))


#KNN για k=15
knn3= KNeighborsClassifier(n_neighbors=15) 

knn_conf_mtx3 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    knn3.fit(X_train, y_train)
    knn_y_pred3 = knn3.predict(X_test)
    knn_conf_mtx3.append(confusion_matrix(y_test,knn_y_pred3))

knn_cm_final3 = np.zeros((7,7))
for item in knn_conf_mtx3:
     knn_cm_final3 += item
     
#Plot του Confusion Matrix
ax= plt.subplot()
sns.heatmap(knn_cm_final3, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for k=15'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print('Accuracy: {:.2f}'.format(accuracy(knn_cm_final3)))
print('Precision: {:.2f}'.format(precision(knn_cm_final3)))
print('Recall: {:.2f}'.format(recall(knn_cm_final3)))


#KNN για k=3
knn4= KNeighborsClassifier(n_neighbors=3) 

knn_conf_mtx4 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    knn4.fit(X_train, y_train)
    knn_y_pred4 = knn4.predict(X_test)
    knn_conf_mtx4.append(confusion_matrix(y_test,knn_y_pred4))

knn_cm_final4 = np.zeros((7,7))
for item in knn_conf_mtx4:
     knn_cm_final4 += item
     
#Plot του Confusion Matrix
ax= plt.subplot()
sns.heatmap(knn_cm_final4, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for k=3'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print('Accuracy: {:.2f}'.format(accuracy(knn_cm_final4)))
print('Precision: {:.2f}'.format(precision(knn_cm_final4)))
print('Recall: {:.2f}'.format(recall(knn_cm_final4)))

'''Διερεύνηση του βέλτιστου μοντέλου'''
#Αποθηκεύουμε σε έναν πίνακα τα λάθη που κάνει ο ταξινομητής για κάθε μια από τις τιμές του
#k στο εύρος που έχουμε ορίσει, ώστε να έχουμε μια εικόνα για την βέλτιστη τιμή του k.
error=[]
for i in range(1,40):
    knn=KNeighborsClassifier(n_neighbors=i)
    for train, test in logo.split(X, y, groups):
        print("TRAIN:", train, "TEST:", test)
        X_train, X_test = X[train], X[test]
        y_train, y_test = y[train], y[test]
        knn.fit(X_train, y_train)
    pred_i=knn.predict(X_test)
    error.append(np.mean(pred_i !=y_test))

#Δημιουργώ ένα γράφημα για τα σφάλματα προκειμένου να παρατηρήσουμε καλύτερα για ποιες τιμές 
#του k το σφάλμα μεγαλώνει
plt.figure(figsize=(12,6))
plt.plot(range(1,40),error,color='red',linestyle='dashed',marker='o',markerfacecolor='blue',\
         markersize=10)
plt.title('Error Rate k value')
plt.xlabel('k value')
plt.ylabel('Mean Error')
plt.show()
 
'''Βέλτιστο μοντέλο βρέθηκε για k=11.'''
try_best=KNeighborsClassifier(n_neighbors=11)
conf_matrix_best = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    try_best.fit(X_train, y_train)
    y_pred_best = try_best.predict(X_test)
    conf_matrix_best.append(confusion_matrix(y_test,y_pred_best))

cm_knn_best = np.zeros((7,7))
for item in conf_matrix_best:
     cm_knn_best += item 

ax= plt.subplot()
sns.heatmap(cm_knn_best, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for the best K'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print("Accuracy for our training dataset is: {:.2f}".format(accuracy(cm_knn_best)))
print('Precision for our training dataset is: {:.2f}'.format(precision(cm_knn_best)))
print('Recall for our training dataset is: {:.2f}'.format(recall(cm_knn_best)))

'''Συγχώνευση δραστηριοτήτων στο βέλτιστο μοντέλο ΚΝΝ.
   Δημιουργούμε ένα νέο dataframe dframe_knn = dframe, στο οποίο θα συγχωνεύσω τις 
   δραστηριότητες που συγχέονται.'''        
dframe_knn = dframe
'''Η δραστηριότητα walking downstairs(7) συγχέεται με τις δραστηριότητες walking(1) και 
walking upstairs(6),οπότε θα την ομαδοποιήσουμε με την walking upstairs(6).'''
dframe_knn['Activity'] = dframe_knn['Activity'].replace(6,67)
dframe_knn['Activity'] = dframe_knn['Activity'].replace(7,67)
'''Η δραστηριότητα standing(2) συγχέεται με την δραστηριότητα sitting(4),
οπότε θα τις ομαδοποιήσουμε.'''   
dframe_knn['Activity'] = dframe_knn['Activity'].replace(2,24)
dframe_knn['Activity'] = dframe_knn['Activity'].replace(4,24)

#Οπότε παίρνουμε τα νέα διανύσματα
X_new_knn = dframe_knn.iloc[:,0:7].values  
y_new_knn = dframe_knn['Activity'].values 
groups = dframe_knn['Participant']
logo=LeaveOneGroupOut()
logo.get_n_splits(X_new_knn, y_new_knn, groups=groups)

#Υπολογίζουμε το νεο confusion matrix,accuracy και recall του μοντέλου μας για την βέλτιστη υπερπαράμετρο δηλαδή για k=11,
#μετά την συγχώνευση των δραστηριοτήτων που κάναμε.
knn_new= KNeighborsClassifier(n_neighbors=11) 
knn_conf_mtx_new = []
for train, test in logo.split(X_new_knn, y_new_knn, groups):
    print("TRAIN:", train, "TEST:", test)
    X_new_knn_train, X_new_knn_test = X_new_knn[train], X_new_knn[test]
    y_new_knn_train, y_new_knn_test = y_new_knn[train], y_new_knn[test]
    knn_new.fit(X_new_knn_train, y_new_knn_train)
    y_new_knn_pred = knn_new.predict(X_new_knn_test)
    knn_conf_mtx_new.append(confusion_matrix(y_new_knn_test,y_new_knn_pred))

knn_cm_final_new = np.zeros((5,5))
for item in knn_conf_mtx_new:
     knn_cm_final_new += item    

ax= plt.subplot()
sns.heatmap(knn_cm_final_new, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for the best KNN model-merged classes'); 
ax.xaxis.set_ticklabels(range(1,6)); ax.yaxis.set_ticklabels(range(1,6));

print('Accuracy: {:.2f}'.format(accuracy(knn_cm_final_new)))
print('Precision: {:.2f}'.format(precision(knn_cm_final_new)))
print('Recall: {:.2f}'.format(recall(knn_cm_final_new)))



'''Neural Networks - MLP'''
mlp_0 = MLPClassifier(hidden_layer_sizes=(5,),max_iter = 1500, solver = 'sgd')

conf_mtx_mlp0 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    mlp_0.fit(X_train, y_train)
    y_pred_mlp0 = mlp_0.predict(X_test)
    conf_mtx_mlp0.append(confusion_matrix(y_test,y_pred_mlp0))

cm_mlp0 = np.zeros((7,7))
for item in conf_mtx_mlp0:
     cm_mlp0 += item 

ax= plt.subplot()
sns.heatmap(cm_mlp0, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for MLP 0 - 1000 iter'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print("Accuracy for our training dataset is: {:.2f}".format(accuracy(cm_mlp0)))
print('Precision for our training dataset is: {:.2f}'.format(precision(cm_mlp0)))
print('Recall for our training dataset is: {:.2f}'.format(recall(cm_mlp0)))

##########################################################################################
mlp_1 = MLPClassifier(hidden_layer_sizes=(100,), max_iter = 2000, solver = 'sgd', \
                    activation='relu', batch_size='auto', learning_rate='constant', \
                    learning_rate_init=0.001, momentum=0.9)

conf_mtx_mlp1 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    mlp_1.fit(X_train, y_train)
    y_pred_mlp1 = mlp_1.predict(X_test)
    conf_mtx_mlp1.append(confusion_matrix(y_test,y_pred_mlp1))

cm_mlp1 = np.zeros((7,7))
for item in conf_mtx_mlp1:
     cm_mlp1 += item 

ax= plt.subplot()
sns.heatmap(cm_mlp1, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for MLP 1 - 2000 iter'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print("Accuracy for our training dataset is: {:.2f}".format(accuracy(cm_mlp1)))
print('Precision for our training dataset is: {:.2f}'.format(precision(cm_mlp1)))
print('Recall for our training dataset is: {:.2f}'.format(recall(cm_mlp1)))

'''Καμπύλη Σφάλματος του Μοντέλου Συναρτήσει των Εποχών.'''
plt.plot(mlp_1.loss_curve_)
plt.title("Loss Curve", fontsize=14)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.show()

#########################################################################################
mlp_2 = MLPClassifier(hidden_layer_sizes=(100,50),max_iter = 1300,\
                            activation = 'relu', batch_size=60, learning_rate='adaptive',\
                            learning_rate_init=0.01, solver = 'sgd', momentum=0.99)

conf_mtx_mlp_2 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    mlp_2.fit(X_train,y_train)
    y_pred_mlp_2 = mlp_2.predict(X_test)
    conf_mtx_mlp_2.append(confusion_matrix(y_test,y_pred_mlp_2))

cm_final_mlp_2 = np.zeros((7,7))
for item in conf_mtx_mlp_2:
     cm_final_mlp_2 += item    

ax= plt.subplot()
sns.heatmap(cm_final_mlp_2, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for MLP 2'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print('Accuracy: {:.2f}'.format(accuracy(cm_final_mlp_2)))
print('Precision: {:.2f}'.format(precision(cm_final_mlp_2)))
print('Recall: {:.2f}'.format(recall(cm_final_mlp_2))) 

###########################################################################################
mlp_3 = MLPClassifier(hidden_layer_sizes=(100,50),max_iter = 1500,\
                            activation = 'relu', batch_size=100, learning_rate='constant',\
                            learning_rate_init=0.001, solver = 'sgd', momentum=0.99)

conf_mtx_mlp_3 = []
for train, test in logo.split(X, y, groups):
    print("TRAIN:", train, "TEST:", test)
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    mlp_3.fit(X_train,y_train)
    y_pred_mlp_3 = mlp_3.predict(X_test)
    conf_mtx_mlp_3.append(confusion_matrix(y_test,y_pred_mlp_3))

cm_final_mlp_3 = np.zeros((7,7))
for item in conf_mtx_mlp_3:
     cm_final_mlp_3 += item    

ax= plt.subplot()
sns.heatmap(cm_final_mlp_3, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for the MLP 3'); 
ax.xaxis.set_ticklabels(range(1,8)); ax.yaxis.set_ticklabels(range(1,8));

print('Accuracy: {:.2f}'.format(accuracy(cm_final_mlp_3)))
print('Precision: {:.2f}'.format(precision(cm_final_mlp_3)))
print('Recall: {:.2f}'.format(recall(cm_final_mlp_3)))   

#####################################################################################
'''Συγχώνευση δραστηριοτήτων για το βέλτιστο μοντέλο MLP'''
dframe_mlp = dframe
'''Η δραστηριότητα walking downstairs(7) συγχέεται με τις δραστηριότητες walking(1) και 
    walking upstairs(6),οπότε θα την ομαδοποιήσουμε χάριν ευκολίας με την walking upstairs(6).'''
dframe_mlp['Activity'] = dframe_mlp['Activity'].replace(6,67)
dframe_mlp['Activity'] = dframe_mlp['Activity'].replace(7,67)
'''Η δραστηριότητα standing(2) συγχέεται με την δραστηριότητα sitting(4),
    οπότε θα τις ομαδοποιήσουμε.'''   
dframe_mlp['Activity'] = dframe_mlp['Activity'].replace(2,24)
dframe_mlp['Activity'] = dframe_mlp['Activity'].replace(4,24)

X_new_mlp = dframe_mlp.iloc[:,0:7].values  
y_new_mlp = dframe_mlp['Activity'].values 
groups = dframe_mlp['Participant']
logo=LeaveOneGroupOut()
logo.get_n_splits(X_new_mlp, y_new_mlp, groups=groups)

modl_best_new_mlp=MLPClassifier(hidden_layer_sizes=(100,), max_iter = 2000, solver = 'sgd',\
                    activation='relu', batch_size='auto', learning_rate='constant', \
                    learning_rate_init=0.001, momentum=0.9)

conf_mtx_new_mlp = []
for train, test in logo.split(X_new_mlp, y_new_mlp, groups):
    print("TRAIN:", train, "TEST:", test)
    X_new_mlp_train, X_new_mlp_test = X_new_mlp[train], X_new_mlp[test]
    y_new_mlp_train, y_new_mlp_test = y_new_mlp[train], y_new_mlp[test]
    modl_best_new_mlp.fit(X_new_mlp_train, y_new_mlp_train)
    y_new_mlp_pred = modl_best_new_mlp.predict(X_new_mlp_test)
    conf_mtx_new_mlp.append(confusion_matrix(y_new_mlp_test,y_new_mlp_pred))

cm_final_new_mlp = np.zeros((5,5))
for item in conf_mtx_new_mlp:
     cm_final_new_mlp += item    

ax= plt.subplot()
sns.heatmap(cm_final_new_mlp, annot=True, fmt='g', ax=ax);  
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix for the best MLP model-merged classes'); 
ax.xaxis.set_ticklabels(range(1,6)); ax.yaxis.set_ticklabels(range(1,6));

print('Accuracy: {:.2f}'.format(accuracy(cm_final_new_mlp)))
print('Precision: {:.2f}'.format(precision(cm_final_new_mlp)))
print('Recall: {:.2f}'.format(recall(cm_final_new_mlp)))
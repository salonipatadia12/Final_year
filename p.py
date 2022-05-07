b = "Benjamin_Netanyau"
j = "Jens_Stoltenberg"
ju = "Julia_Gillard"
m = "Magaret_Tarcher"
n = "Nelson_Mandela"

l = ["Benjamin_Netanyau", "Jens_Stoltenberg", "Julia_Gillard", "Magaret_Tarcher", "Nelson_Mandela"]
f = open('trainingDataPath.txt','a')


for i in range(1500):
    st = n+"/"+str(i)+".wav"
    print(st, file=f)


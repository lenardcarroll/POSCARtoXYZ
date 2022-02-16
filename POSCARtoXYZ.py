import numpy as np

parser = argparse.ArgumentParser()
#Cheat sheet of arguments to be used with the script
parser.add_argument("-inp", "--input", dest = "input", default = "POSCAR", help="Name of input file")
parser.add_argument("-out", "--output", dest = "output", default = "POSCAR.xyz", help="Name of output file")
args = parser.parse_args()

f = open(args.input,"r")
content = f.readlines()

Atoms = content[5].split()
ScaleFactor = float(content[1])
Vectors = []
for i in range(2,5):
    Vectors.append(content[i].split())
AtomTot = content[6].split()

sumAtoms = 0
for i in AtomTot:
    sumAtoms += int(i)

AtomCoords = []
for i in range(9,sumAtoms+9):
    AtomCoords.append([float(content[i].split()[0]),float(content[i].split()[1]),float(content[i].split()[2])])

VectorsAdj = []
for i in Vectors:
    VectorsAdj.append([float(i[0])*ScaleFactor,float(i[1])*ScaleFactor,float(i[2])*ScaleFactor])

Vectors = []
NewAtoms = []

f = open(args.output,"w")
print(sumAtoms,file=f)
print("POSCAR to XYZ",file=f)

sumAtoms = 0
for i in range(len(AtomTot)):
    if i==0:
        for j in range(int(AtomTot[i])):
            MatrixMult = np.matmul(AtomCoords[j],VectorsAdj)
            print(Atoms[i],MatrixMult[0],MatrixMult[1],MatrixMult[2],file=f)
        sumAtoms+=int(AtomTot[i])
    else:
        for j in range(int(AtomTot[i-1]),int(AtomTot[i])+sumAtoms):
            MatrixMult = np.matmul(AtomCoords[j],VectorsAdj)
            print(Atoms[i],MatrixMult[0],MatrixMult[1],MatrixMult[2],file=f)
            sumAtoms+=int(AtomTot[i])
f.close()

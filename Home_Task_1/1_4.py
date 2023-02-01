# *Задача 4. 
# Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# in 3 2 4 out yes
# in 3 2 1 out no
nSide = int (input("Input first quantity of slabs\n"));
mSide = int (input("Input second quantity of slabs\n"));
kSlabs = int (input ("Input quantity of slabs to braek\n"))
if (kSlabs < nSide * mSide and kSlabs % nSide == 0 or 
    kSlabs < nSide * mSide and kSlabs % mSide == 0):
    print ("YES");
else:
    print ("NO");
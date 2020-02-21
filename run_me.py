import os

N = 20

for i in range(0,N):
    try:
        os.mkdir("Wing{}".format(i+1))
    except:
	pass

    os.chdir("Wing{}".format(i+1))
    os.system("cp ../sbae.sh ../obj.py ../opti.py .")
    os.system("mv sbae.sh DV_{}.sh".format(i+1))
    cmd = "sbatch DV_{}.sh".format(i+1)
    os.system(cmd)
    os.chdir("..")



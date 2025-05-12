#!/usr/bin/env python3
import subprocess
import os

prng_seed = 154890100
num_iterations = 100
fuzzer = "fuzzer/fuzzer"
target  =  "targets/prog"
seed =  "seed/_seed_"
__curr_dir_ = os.getcwd()

def executescript(scrpath):
    result = subprocess.run(scrpath, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
    return result


if __name__ == '__main__':

    compareresults = []
    for i in range(1,11):
        if i == 9:
            continue
        print("Testing the fuzzer for level "+str(i))
        curr_result = "chklevel"+str(i)+".crash"
        targetpath =  str(target + str(i))
        args_file =  str("results/level-" + str(i)+"/level-"+str(i)+".txt")

        with open(args_file, 'r') as f:  
            prng_seed = f.readline().rstrip('\n')
            num_iterations = f.readline().rstrip('\n')
         
        exec_cmd = [fuzzer, prng_seed , num_iterations , targetpath,  seed , curr_result]
        status  = executescript(exec_cmd)
        print(status)

        if status.returncode == 0:
            print("Process executed for level"+str(i))
            submitted_output =  "results/level-"+str(i)+"/level-"+str(i)+".crash"

            exec_cmd = ["diff" ,  curr_result , submitted_output]
            compresult = executescript(exec_cmd)
            
            if compresult.returncode == 0:
                res = str("The fuzzer output and submitted output for Level "+str(i)+" is same.\n")
                print(res)
                compareresults.append(res)
            else:
                res = str("The fuzzer output and submitted output for Level "+str(i)+" is different.\n")
                print(res)
                compareresults.append(res)

    with open('compareresults.txt', 'w') as f:
        for item in compareresults:
            f.write(item)

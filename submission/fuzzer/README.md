# CSE-543 Fuzz Them All Project

## Requirements

* The project uses below runtime environment
  1. [Linux x86_64] - The fuzzer executable has been tested with Linux x86_64 OS. Please use the same.  
  2. Fuzzer built using golang v1.24.1.

## Submission Folder Structure

* Fuzzer - Contains Fuzzer
* Seed - seed file used.
* Results - Contains teh results from each pwn level.
* Targets - pwn.college prog from each level.
* runfuzzer.py - script to test the fuzzer



## Steps to execute


Manual:
=======

1. Extract the submission zip and navigate to that folder. 

2. Run the fuzzer by specifying the following 5 arguments in the same order from within the submissions directory. The fuzzer will do basic input verification for 5 arguments, if not will throw an error. It does not do any validation beyond that.
  * prng_seed -  154890100
  * num_iterations -  100
  * target program  -  "./prog"
  * seed file  -  "_seed_"
  * crash output file  -  level-1.crash 

3. The command to execute fuzzer will look like below assuming the fuzzer is executed from within the submissions folder and the target prog executable resides in the same submission folder.
  ``./fuzzer/fuzzer 154890100 100 <target program> <seed file> <crash output file>`
   ``./fuzzer/fuzzer 154890100 100 ./prog ./seed/_seed_ ./results/level1/level-1.crash``
4. Note: Due to a bug in the golang os.write() library (at least noticed in my testing), the target file won't be created if a folder does not exist in the given path. It will only create the crash output file if all the parent folders exist. Eg: If /home/user/submission/output/level-1.crash is your input argument. If the output folder is not created the fuzzer won't write the file.

Script
======

1. The runfuzzer.py script can be executed to run the fuzzer against pwn.college target programs. The prog from each level has been copied to the targets folder. If you are copying them please name the prog file corresponding to each level or modify the script to your needs.
2. The Script calls the fuzzer by reading the num_of_iterations and prng_seed from the "results/level-#.txt" file. And tests the fuzzer for each target program. The crash output is saved as submission/chklevel<#>.crash file.
3. It then runs a diff to compare the submitted results/level-#.crash file with the newly generated chklevel<#>.crash file. 
4. The crash output is saved to the submission folder as chklevel<#>.crash.
5. The comparison results are written to compareresults.txt.





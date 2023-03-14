import csv

def todo(task):
    
    
    file=open('cli-pal/tasks.csv',"a")
    file.write('\n'+task)
    file.close()
    file=open('cli-pal/tasks.csv',"r")
    while(True):
        line=file.readline()
        if not line:
            break
        print(line)
    file.close()
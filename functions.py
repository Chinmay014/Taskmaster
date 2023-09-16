def read_file(filename="tasks.txt"):
    tasks = []
    with open(filename,'r') as file:
        for line in file:
            tasks.append(line)
    return tasks

def write_to_file(tasks,filename="tasks.txt"):
    with open('tasks.txt','w') as file:
        for task in tasks:
            file.write(task)
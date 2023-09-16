with open('tasks.txt','r') as file:
        line_count = 0
        tasks = []
        for line in file:
            if line_count<2:
                line_count=line_count+1
                continue
            tasks.append(line[2:len(line)-1])
print("Welcome to your Taskmaster!")
print("add/a: add a task")
print("edit/e: edit an added task")
print("show/s: show all the tasks")
print("complete/c: mark an item as complete")
print("quit/q: exit Taskmaster")

while True:
    # read the file and store in a variable
    prompt =input("make your choice(a/e/s/c/q), type 'm' to see the menu again: ")
    prompt = prompt.strip()
    match prompt:
        case "show" | "s":
            for index,task in enumerate(tasks):
                row = f"{index+1}-{task}"
                print(row)
        case "add" | "a":
            while True:
                task=input("add a task(type 'f' to finish adding) ")
                match task:
                    case 'f':
                        print("all done! type 's' to see updated list")
                        break
                    case '':
                        "nothing has been entered. Perhaps a mistake"
                    case '_':
                        tasks.append(task)
        case "quit"|"q":
            # write the new contents to file
            with open('tasks.txt','w') as file:
                file.writelines("My ToDo List\n")
                file.writelines("==================\n")
                for index,task in enumerate(tasks):
                   row = f"{index+1}-{task}\n"
                   file.write(row) 
            break
        case "edit"|"e":
            print("This is how the task list look like, right now")
            for index,task in enumerate(tasks):
                # print(i+1,". ",tasks[i].capitalize())
                row=f"{index+1}-{task}"
                print(row)
            while True:
                task_num = input("Enter which task number you wanna change: ")
                if task_num>len(tasks):
                    print("invalid entry")
                else:
                    break
            new_task = input("Enter new task to replace the old task with: ")
            tasks[int(task_num)-1]=new_task
            print("done! type 's' to show the updated list")
        case "complete"|"c":
            print("This is how the task list look like, right now")
            for index,task in enumerate(tasks):
                # print(i+1,". ",tasks[i].capitalize())
                row=f"{index+1}-{task}"
                print(row)
            while True:
                task_num = input("Enter which task number you wanna mark as complete: ")
                if task_num>len(tasks):
                    print("invalid entry")
                else:
                    break
            tasks.remove(tasks[int(task_num)-1])
            print("done! type 's' to show the updated list")
        case "menu" | "m":
            print("add/a: add a task")
            print("edit/e: edit an added task")
            print("show/s: show all the tasks")
            print("complete/c: mark an item as complete")
            print("quit/q: exit Taskmaster")
        case _:
            print("hmm...this doesn't seem like a valid command. Try again?")



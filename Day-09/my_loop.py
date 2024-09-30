my_list = [0, 1, 2, 3, 4, 5]

for i in my_list:
    if i == 3:
        #break
        continue
    print(i) 

print("------------------")

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)    

print("------------------")

counter = 0
while  counter < 10:
    print(counter)
    counter += 1
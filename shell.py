import sys
import datetime

cmd_list = [
	"print","output","say",
	"input","get",
	"stop","quit",
	"help","version",
	"var",
	"view"
]

variable = [

]

month = [
	"JAN","FEB","MAR","APR","MAY","JUN","JUL","OUG","SEP","ACT","NOV","DEC"
]

cmd_check = 0
cmd_err = 0
version = "0.0.5"

last_input = ""
get_input = ""
inpu = ""

time = datetime.datetime.now()

print("doant shell {6} ({0} {1} {2}, {3}:{4}:{5})".format(time.year,month[time.month+1],time.day,time.hour,time.minute,time.second,version))
print("this shell is alpha mode!\n")
print("if need you help, using command 'help'")
print("if need you this shell's version, using command 'version'")

while True:
	last_input = inpu
	inpu=str(input(">>> "))
	for i in range(len(cmd_list)):
		if inpu.startswith(cmd_list[i]):
			if inpu.startswith("input") or inpu.startswith("get"):
				print(inpu.replace(cmd_list[i],"",1).replace(" ","",1))
				get_input = input("input : ")
				print("output : " + get_input)
			elif inpu.startswith("say") or inpu.startswith("output") or inpu.startswith("print"):
				print(inpu.replace(cmd_list[i], "",1).replace(" ", "",  1))
			elif inpu.startswith("stop") or inpu.startswith("quit"):
				print("exit code : 0")
				sys.exit()
			elif inpu.startswith("help"):
				print("input, get : save input, send input to output")
				print("print, output, say : string output")
				print("quit, stop : exit to 'shell' execute")
				print("version : watch this shell version")
			elif inpu.startswith("version"):
				print("doant shell's version is {0}".format(version))
			elif inpu.startswith("var"):
				if inpu.replace("var","",1).replace(" ","") == "":
					print("invaild command\ncommand 'var' has no char\nERROR message:\nVariableNameNoCharError: Variable name has no char")
				else:
					if inpu.replace("var","",1).replace(" ","").startswith("add"):
						variable.append(inpu.replace("var","",1).replace(" ","").replace("add","",1))
						print("successfully added variable.(variable name: {0})".format(inpu.replace("var","",1).replace(" ","" ).replace("add","",1)))
					else:
						print("invaild commad")
						print("The second input to the 'var' command is 'set' or 'add', but {0} is entered.".format(inpu.replace("var","",1).replace(" ","")))
						print("ERROR message: \nCommandSecondInputStringError: " + "The second input to the 'var' command is 'set' or 'add', but {0} is entered.".format(inpu.replace("var","",1).replace(" ","")))
			elif inpu.startswith("view"):
				print(inpu.replace("view","",1).replace(" ","",1))
			cmd_check = 1
	if cmd_check == 0:
		if last_input == inpu:
			if cmd_err == 8:
				print("invaild system\npython operating system wasn't found\nError message:\nDuplicateWordsError: The same word has been entered more then 10 times.")
				sys.exit()
			cmd_err += 1
		print("invaild command\n{0}".format(cmd_list))
	else: 
		cmd_check = 0

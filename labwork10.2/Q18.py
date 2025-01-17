import subprocess as sub 
input_command = ["ls","-l","/namya"]
terminal = sub.Popen(input_command,stdout=sub.PIPE,stderr=sub.PIPE)
answer,answer1 = terminal.communicate()
output_data = answer.decode("utf-8")
error_data = answer1.decode("utf-8")

print(f"Standard output {output_data}")
print(f"Standard error {error_data}")
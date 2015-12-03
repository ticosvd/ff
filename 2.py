import subprocess
print "ddddd"
proc=subprocess.Popen('ls')
print(proc.stdout.read())



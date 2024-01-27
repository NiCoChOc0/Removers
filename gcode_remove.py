import os

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".gcode"):
        with open(filename, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if not(line.startswith("M140 S0") or line.startswith("M104 S0")):
                    f.write(line) 
            f.truncate()
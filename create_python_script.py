import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'a') as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))
from pyscript import document

age = 15
height = 5.7
name = "Mark Anthony Herrington"
subjects = ["Physical Education", "Science", "English"]
student = True
colors = {"red", "orange", "blue"}
coordinates = (10, 20)


output = f"""
<P>Age = {age} {type(age).__name__}</p>
<P>Height = {height} {type(height).__name__}</p>
<P>Name = {name} {type(name).__name__}</p>
<P>Subjects = {subjects} {type(subjects).__name__}</p>
<P>Student = {student} {type(student).__name__}</p>
<P>Colors = {colors} {type(colors).__name__}</p>
<P>Coordinates = {coordinates} {type(coordinates).__name__}</p>
"""

document.querySelector("#output").innerHTML = output
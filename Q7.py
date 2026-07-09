                           # Student Performance Analyzer with Loop Control..
""" students = [
    {"name": "Alice", "scores": [85, 92, 78, 90]},
    {"name": "Bob", "scores": [72, 68, 75, 70]},
    {"name": "Charlie", "scores": [95, 98, 92, 96]},
    {"name": "Diana", "scores": [88, 85, 90, 87]},
    {"name": "Eve", "scores": [45, 52, 48, 50]},
    {"name": "Frank", "scores": [100, 100, 100, 100]}  # Special case
] """ 

#Student anaylsis with loop control.
#GIVEN DATA.

students = [
     {"name": "Alice", "scores": [86,78,99,84]},
     {"name": "Bob","scores": [76,78,96,67]},
     {"name": "Charlie","scores": [78,67,94,82]},
     {"name": "Diana", "scores": [78,88,99,67]},
     {"name": "Eve", "scores": [55,67,43,35]},
     {"name": "Frank", "scores": [100,100,100,100]} #special case
 ]

#Initialize overall statistics outside the loop
highest_avg = -1
highest_name = ""
lowest_avg = 101 # Assuming scores are 0-100
lowest_name = ""
passing_count = 0
failing_count = 0

#ITERATE THROUGH EACH STUDENT..
for student in students:
  name = student["name"]
  scores = student["scores"]

  #VALIDATE SCORES USING FOR LOOP..
  valid_scores = []
  for score in scores:
    if 0 <= score <= 100:
      valid_scores.append(score)
    else: "invalid scores are skipped"

  #handle case where no valid scores exist.
  if len(valid_scores) == 0:
    print(f"{name}: No valid scores found,Skipping..")
    continue

  #CALCULATE SUM USING WHILE LOOP FOR AT LEAST ONE STUDENT
  total = 0
  if name == "Alice":
    i= 0
    while i < len (valid_scores):
      total += valid_scores[i]
      i += 1

  #USE loop for others
  else:
    for s in valid_scores:
      total += s

  #Calculate Average.
  avg = total / len(valid_scores)

  #EARLY EXIT IF ANY STUDENT HAVE AVG OF 100
  if avg == 100:
    print(f"Perfect scorer found: {name}")
    break

  #GRADE CALCULATION USING CONDITIONALS..
  if avg >= 90:
    grade = "A"
  elif avg >= 80:
      grade = "B"
  elif avg >= 70:
      grade = "C"
  elif avg >= 60:
      grade = "D"
  else:
        grade = "F"

  #PRINT STUDENT RESULT:
  print(f"{name}: Average = {avg}, Grade = {grade}")


  #UPDATE STATISTICS..
  if avg > highest_avg:
          highest_avg = avg
          highest_name = name

  if avg < lowest_avg:
          lowest_avg = avg
          lowest_name = name

  if avg >= 60:
          passing_count += 1
  else:
          failing_count += 1


#PRINT CLASS STATISTICS..
print("\nClass Statistics")

if highest_name != "":
    print(f"Highest: {highest_name} = {highest_avg}")
    print(f"Lowest: {lowest_name} = {lowest_avg}")
    print(f"Number of passing students: {passing_count}")
    print(f"Number of failing students: {failing_count}")
else:
    print("No valid student data available.")


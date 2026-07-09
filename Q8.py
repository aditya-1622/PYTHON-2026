#PROBLEM STATEMENT.(Debug Mutable Default Argument in Python)

#FUNCTION DEFINITION { default list is created called tasks[] once so we can reused across all calls}

def add_task(task, tasks=[]):
  tasks.append(task)
  return tasks

#STEP BY STEP EXECUTION.
print("EXECUTION")

#CALL_1
result1 = add_task("Write report")
print("After Call 1:")
print("result1 =", result1)

#CALL_2
result2 = add_task("Review code")
print("\nAfter Call 2:")
print("result2 =", result2)

#CALL_3
result3 = add_task("Meeting", [])
print("\nAfter Call 3:")
print("result3 =", result3)

#CALL_4
result4 = add_task("Deploy")
print("\nAfter Call 4:")
print("result4 =", result4)

#FINAL OUTPUT..

print("\nFINAL OUTPUT:")
print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)

#BUG EXPLANATION..
"""The default argument tasks[] is created only
once when the function is defined. This same list is reused
across multiple function cells.
SO, result 1 and 2 both share the same result
result 4 also use that same list while result 3
use separate because of a new list explicity."""

#CORRECT EXPLANATION..

def add_task_fixed(task, tasks=None):
  #Create a new list each time if not provided.
  if tasks is None:
    tasks = []
  tasks.append(task)
  return tasks

#Test corrected function.

print("\nTesting Fixed Function")

fixed1 = add_task_fixed("Write report")
fixed2 = add_task_fixed("Review code")
fixed3 = add_task_fixed("Meeting", [])
fixed4 = add_task_fixed("Deploy")

print("fixed1:", fixed1)
print("fixed2:", fixed2)
print("fixed3:", fixed3)
print("fixed4:", fixed4)

#CONCLUSION..
#Always avoid using mutable default arguments like lists or dictionaries.

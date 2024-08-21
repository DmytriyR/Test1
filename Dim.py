''''
#ДЗ1
students=[("Alice",87),
          ("Bobik",87),
          ("Mar",65)]
result={}
for student, grade in students:
    if grade in result:
        result[grade].append(student)
    else:
        result[grade]=[student]
print(result)
''
#ДЗ2
dict={"Дима":100, 'Петя':57, "Вася":63, "Маша":49}
name1=dict["Дима"]
name2=dict["Петя"]
name3=dict["Вася"]
name4=dict["Маша"]
print(sum((name1,name2,name3,name4))/len(dict))
'''

#ДЗ3
kortej=(1,2,56,1,56,4,685)
print(sum(kortej)/len(kortej))

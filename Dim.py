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
''

#ДЗ3
kortej=(1,2,56,1,56,4,685)
print(sum(kortej)/len(kortej))
'


try:
 nam=input('Введіть назву файлу, який ви хочете відкрити:')
 with open(nam, "r")as file1:
  print(file1.read())
except FileNotFoundError:
    print(nam)
''

def filename():
    name = input("Enter file name\t")
    return name
def openfile(userInput):
    if os.path.exists(filename):
       with open(filename(), "a") as file1

    try:
        with open(userInput, "r") as file1:
            print(file1.read())
    except FileNotFoundError:
        print("not found")
openfile(filename())
'''
user = input('Ваше імʼя : \t')
user1 = input('Ваше прізвище : \t')
user2 = input('Ваш вік: \t')
user3 = input('Ваш навчальний заклад : \t')
with open("/Users/macbook/Desktop/kak.txt",'w') as file:
    file.write(f"імʼя:{user}\n")
    file.write(f"прізвище:{user1}\n")
    file.write(f"вік:{user2}\n")
    file.write(f"навчальний заклад:{user3}\n")
    file.close()
with open("/Users/macbook/Desktop/kak.txt",'r') as file:
    print(file.read())

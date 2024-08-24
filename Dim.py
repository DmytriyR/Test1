
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

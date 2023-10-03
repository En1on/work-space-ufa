import random
# после импортов 2 отступа и после функций
check = False # непонятные переменные
check_2 = False


def create_email():
  alphabet = ["a", "b", "c",
              "d", "e", "f",
              "g", "h", "i",
              "j", 'k', 'l',
              'm', 'n', 'o', 
              'p', 'q', 'r', 
              's', 't', 'u', 
              'v', 'w', 'x', 
              'y', 'z'
            ]
  
  mail= ["gmail","mail",'ya',
         'rambler', 'protonmail',
         'inbox', 'list'
        ]

# TODO: между переменными 0-1 отступ
  email = ''

  x = random.randint(0,5)# TODO: непонятная переменная

  for i in range(random.randint(6,19)): # TODO: прогуглить какие функции есть в рандоме
    email = email  + alphabet[random.randint(0,25)] # TODO: random.choice(alphabet)
    if i == x:
      email = email  + '_'
      x =1234567890
  
  for i in range(4):
    email = email.replace(alphabet[random.randint(0,random.randint(0,len(email)-1))],str(random.randint(0,9)))
    # TODO: ПЕРЕЧИТАТЬ ZEN Python и разобрать каждую строчку
  
  
  email = email + "@" + mail[random.randint(0,6)] + ".com"

  return email

# TODO: то же самое что и с созданием почты
def create_password():
  alphabet = ["a", "b", "c",
              "d", "e", "f",
              "g", "h", "i",
              "j", 'k', 'l',
              'm', 'n', 'o', 
              'p', 'q', 'r', 
              's', 't', 'u', 
              'v', 'w', 'x', 
              'y', 'z']
  
  password = ''
  
  x = random.randint(1,5)

  y = random.randint(0,5)

  locate_random_number = random.randint(0,5)

  if y == x and y != 0:
    y -=1
  else:
    y += 1
  
  for i in range(random.randint(8,25)):
    if i == x:
      password = password  + '_'
    elif i == y:
      password = password  + alphabet[random.randint(0,25)].upper()
    elif i == locate_random_number:
      password = password + str(random.randint(0,9))
    else:
      password = password  + alphabet[random.randint(0,25)]

  
  for i in range(4):
    # password = password.replace(alphabet[random.randint(0,random.randint(0,len(password)-1))],str(random.randint(0,9)))
    password = password.replace(alphabet[random.randint(0,len(password))],str(random.randint(0,9)))  
  return password

def check_mail():
  global created_mail
  brut_mail = input()
  if brut_mail == created_mail:
    return True

def check_password():
  global created_password
  brut_password = input()
  if brut_password == created_password:
    return True


created_mail = create_email()
created_password = create_password()
print(created_mail, created_password)



while True:
  if check == True:
    print("Введите пароль:")
    check_2 = check_password()# TODO: чек отдельно, ввод отдельно
    if check_2 == True:
      print("Добро пожаловать!")
      break
  else:
    print("Введите почту:") # TODO: тоже отдельно чек и ввод
    check = check_mail()

# brut_password = bruting(created_password) # TODO: при подборе пароля разрешается юзать длину пароля
# TODO: точно также подобрать почту
print(created_password == brut_password)



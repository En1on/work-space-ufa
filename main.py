import random


def random_place_number(string):
  random_place = random.randint(0,len(string)-1)
  random_number = str(random.randint(0,9))
  string = string.replace(string[random_place],random_number)
  return string


def create_email(lenght):
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

  email = ''

  random_place_underscore = random.randint(0,5)

  for i in range(lenght): # TODO: прогуглить какие функции есть в рандоме
    email = email  + random.choice(alphabet) 
    
    if i == random_place_underscore:
      email = email  + '_'
      random_place_underscore =1234567890
  
  for i in range(4):
    email = random_place_number(email)
  
  
  email = email + "@" + mail[random.randint(0,6)] + ".com"

  return email


def create_password(lenght):
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
  
  random_place_under = random.randint(1,5)

  random_upper = random.randint(0,5)

  locate_random_number = random.randint(0,5)

  if random_upper == random_place_under and random_upper != 0:
    random_upper -=1
  else:
    random_upper += 1
  
  for i in range(lenght):
    if i == random_place_under:
      password = password  + '_'
    elif i == random_upper:
      password = password  + alphabet[random.randint(0,25)].upper()
    else:
      password = password  + alphabet[random.randint(0,25)]

  
  for i in range(lenght//3):
    password =  random_place_number(password)
  
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

def bruting_password(correct_password):
  wrong_password = []

  
  while True:
    password = create_password(len(correct_password))
    if password not in wrong_password:
      if correct_password == password:
        print("True")
        break
      else:
        wrong_password.append(password)


def bruting_mail(correct_email):
  wrong_email = []

  
  while True:
    email = create_email(len(correct_email))
    if email not in wrong_email:
      if correct_email == email:
        print("True")
        break
      else:
        wrong_email.append(email)



created_mail = create_email(random.randint(6,10))
created_password = create_password(random.randint(5,8))
print(created_mail, created_password)

# bruting_password(created_password)
# bruting_email(created_mail)

bruting_password("a3b")
bruting_mail("g_hn8@mail.com")


while True:
  print("Введите почту:")
  if check_mail() == True:
    print("Введите пароль:")
    if check_password() == True:
      print("Добро пожаловать!")
      break # TODO: тоже отдельно чек и ввод



def bruting_password(correct_password):
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

  wrong_password = []

  
  while True:
    password = create_password(len(correct_password))
    if password not in wrong_password:
      if correct_password == password:
        print("True")
        break
      else:
        wrong_password.append(password)




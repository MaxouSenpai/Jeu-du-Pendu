
import turtle as t
import random as r

def iscorrect(l):
	return l.isalpha() and len(l) == 1
def posbegin(w):
	if len(w) % 2 == 0:
		res = ((-(len(w) / 2 - 1) * 50)-5,-150)
	else:
		res = (-(len(w)//2)*50,-150)
	return res

def shadow_word(w):
	if len(w) % 2 == 0:
		p_s.setpos(-5,-150)
		p_s.backward((len(w) / 2 - 1) * 50)
		for _ in range(len(w)):
			p_s.write("_",False,align = "center",font = ("Arial",30,"normal"))
			p_s.forward(50)
	else:
		p_s.setpos(0,-150)
		p_s.backward(len(w)//2*50)
		for _ in range(len(w)):
			p_s.write("_",False,align = "center",font = ("Arial",30,"normal"))
			p_s.forward(50)

def reveal(l,i):
	p_l.forward(i*50)
	p_l.write(letter,False,align = "center",font = ("Arial",30,"normal"))

def gallow():
	p_e.speed(0)
	p_e.forward(400)
	p_e.backward(800)
	p_e.forward(300)
	p_e.left(90)
	p_e.forward(250)
	p_e.right(90)
	p_e.forward(100)
	p_e.right(90)
	p_e.forward(25)

def head():
	p_e.right(90)
	p_e.circle(20,360)
	p_e.left(90)
	p_e.penup()
	p_e.forward(40)
	p_e.pendown()

def body():
	p_e.forward(100)
	p_e.backward(80)

def first_arm():
	p_e.left(30)
	p_e.forward(50)
	p_e.backward(50)
	p_e.right(30)

def second_arm():
	p_e.right(30)
	p_e.forward(50)
	p_e.backward(50)
	p_e.left(30)

def first_leg():
	p_e.forward(80)
	p_e.left(30)
	p_e.forward(50)
	p_e.backward(50)
	p_e.right(30)

def second_leg():
	p_e.right(30)
	p_e.forward(50)
	t.bgcolor("red")

t.title("Jeu du Pendu")

words = [x.strip().lower() for x in open("mots.txt")]

replay = 1

p_e = t.Pen() #Pen Error
p_s = t.Pen() #Pen Shadow Word
p_l = t.Pen() #Pen Letter
p_t_l = t.Pen() #Pen Tested Letter
	
while replay == 1:

	t.bgcolor("white")
	p_e.hideturtle()
	p_s.hideturtle()
	p_s.penup()
	p_s.speed(0)
	p_l.hideturtle()
	p_l.penup()
	p_l.speed(0)
	p_t_l.hideturtle()
	p_t_l.penup()
	p_t_l.speed(0)

	selected_word = words[r.randint(0,len(words)-1)]

	letters = set(selected_word)

	tested_letters = set()

	found = False

	num_error = 0

	shadow_word(selected_word)

	pos1 = posbegin(selected_word)

	p_t_l.setpos(-300,-250)

	a = ""

	while not found and num_error < 7:
		letter = t.textinput("Input",a + "Lettre :")
		a = ""
		if letter == None:
			num_error = 7
		elif iscorrect(letter) and letter.lower() not in tested_letters:
			letter = letter.lower()
			tested_letters.add(letter)
			if letter in letters:
				for indice in range(len(selected_word)):
					if letter == selected_word[indice]:
						p_l.setpos(pos1)
						reveal(letter,indice)
			else:
				p_t_l.write(letter,False,align = "center",font = ("Arial",15,"normal"))
				p_t_l.forward(30)
				num_error += 1
				if num_error == 1:gallow()
				elif num_error == 2:head()
				elif num_error == 3:body()
				elif num_error == 4:first_arm()
				elif num_error == 5:second_arm()
				elif num_error == 6:first_leg()
				elif num_error == 7:second_leg()
		elif letter in tested_letters:
			a = "Lettre déjà entroduite!\n"
		else:
			a = "Input incorrect!\n"


		found = (letters - tested_letters) == set()

	if found:
		t.bgcolor("green")
		b = "Vous avez gagné!\n"
	else:
		b = "Vous avez perdu!\nLe mot était : " + selected_word + "\n"

	replay = t.numinput("Rejouer",b + "Voulez-vous rejouer?\n1) Yes\n2) No")
	p_t_l.reset()
	p_e.reset()
	p_s.reset()
	p_l.reset()

t.bye()
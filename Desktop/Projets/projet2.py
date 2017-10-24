
import turtle as t
import random as r

def error(e):
	"""
	Fonction prenant en entrée le nombre d'erreurs et permettant de continuer le dessin du bonhomme pendu
	"""
	if e == 1:
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
	elif e == 2:
		p_e.right(90)
		p_e.circle(20,360)
		p_e.left(90)
		p_e.penup()
		p_e.forward(40)
		p_e.pendown()
	elif e == 3:
		p_e.forward(100)
		p_e.backward(80)
	elif e == 4:
		p_e.left(30)
		p_e.forward(50)
		p_e.backward(50)
		p_e.right(30)
	elif e == 5:
		p_e.right(30)
		p_e.forward(50)
		p_e.backward(50)
		p_e.left(30)
	elif e == 6:
		p_e.forward(80)
		p_e.left(30)
		p_e.forward(50)
		p_e.backward(50)
		p_e.right(30)
	elif e == 7:
		p_e.right(30)
		p_e.forward(50)
		t.bgcolor("red")

def shadow_word(w): #Toutes les opérations présentes dans cette fonction permettent de tout centrer
	"""
	Fonction prenant en entrée un mot et qui permet d'afficher les "_" pour chaque lettre du mot
	"""
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

def originpos(w):
	"""
	Fonction prenant en entrée un mot et qui renvoie la position sur Turtle où le mot doit débuter pour qu'il soit centré
	"""
	if len(w) % 2 == 0:
		pos = ((-(len(w) / 2 - 1) * 50)-5,-150)
	else:
		pos = (-(len(w)//2)*50,-150)
	return pos

def reveal(l,i):
	"""
	Fonction prenant en entrée une lettre et son indice et qui permet d'afficher la lettre à sa place
	"""
	p_l.forward(i*50)
	p_l.write(letter,False,align = "center",font = ("Arial",30,"normal"))

def iscorrect(l):
	"""
	Fonction renvoyant True seulement si l'entrée est une seule lettre
	"""
	return l.isalpha() and len(l) == 1

t.title("Jeu du Pendu")

words = [x.strip().lower() for x in open("mots.txt")]

replay = 1

p_e = t.Pen() #Stylo permettant de dessiner le bonhomme pendu
p_s = t.Pen() #Stylo permettant de mettre les "_" 
p_l = t.Pen() #Stylo permettant d'écrire les lettres au-dessus des "_"
p_t_l = t.Pen() #Stylo permettant d'écrire les lettres fausses déjà testées
	
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
	pos1 = originpos(selected_word)
	p_t_l.setpos(-90,-275)
	a = ""   # Variable permettant d'indiquer la nature de l'erreur de l'input
	while not found and num_error < 7:
		letter = t.textinput("Input",a + "Lettre :")
		a = ""
		if letter == None:
			num_error = 7	#Si le joueur appuye sur cancel on le fait directement perdre sa partie
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
				error(num_error)
		elif letter in tested_letters:
			a = "Lettre déjà introduite!\n"
		else:
			a = "Input incorrect!\n"
		#Si l'ensemble des lettres du mot se trouve dans l'ensemble des lettres testées le found passe à True
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
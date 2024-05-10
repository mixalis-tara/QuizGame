from Question.question import Question

quest = ("What year was the popular game 'Minecraft' first released?: ",

                "In the game 'The Legend of Zelda: Ocarina of Time,' what is the name of the main protagonist?: ",

                "Which gaming console is known for its exclusive titles like 'God of War' and 'Uncharted'?: ",

                "What is the name of the main character in the 'Assassin's Creed' series?: ",

                "In the game 'Overwatch, ' what is the name of the support hero who can resurrect fallen teammates?: ")

option = (("A) 2007", "B) 2009", "C) 2011", "D) 2013"),
           ("A) Link", "B) Zelda", "C) Ganondorf", "D) Epona"),
           ("A) Xbox Series X", "B) Nintendo Switch", "C) PlayStation 4", "D) PC (Personal Computer)"),
           ("A) Altair Ibn-La'Ahad", "B) Ezio Auditore", "C) Connor Kenway", "D) Desmond Miles"),
           ("A) Mercy", "B) Ana", "C) Zenyatta", "D) Lucio"))

answer = ("B", "A", "C", "D", "A")

questions_list = list()

def create_questions(questions_list):
    for q, o, a in zip(quest, option, answer):
        questions = Question(q, o, a)
        questions_list.append(questions)


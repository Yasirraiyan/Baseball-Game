import random

# Initialize variables
start = False
team = ["A", "B", "C", "D", "E"]
end = False
hit = False
strike = False
catch = False
win = False
rd = random.randint(1, 5)
skill = random.randint(1, 5)
innings = random.randint(1, 9)
score = 0
life = 50
chance = 5
out = False
allpassed = False

# Score increments for passing innings
score1 = score + 50
score2 = score + 100
score3 = score + 150
score4 = score + 200
score5 = score + 250
score6 = score + 300
score7 = score + 350
score8 = score + 400
score9 = score + 450
score10 = score + 500

# Game start logic
if rd == 1:
    start = True
    print(start)
if rd == 2:
    choose = random.choice(team)
if rd == 4:
    start = False
    end = True
    print(start)
    print(end)

# Team selection based on skill
if skill == 1:
    print(f"Choosable team is: {team[0]}")
if skill == 2:
    print(f"Choosable team is: {team[1]}")
if skill == 3:
    print(f"Choosable team is: {team[2]}")
if skill == 4:
    print(f"Choosable team is: {team[3]}")
if skill == 5:
    print(f"Choosable team is: {team[4]}")

# Batting function
def batting(hit):
    global score, life, chance
    while not hit:
        score += 5
        life /= 5
        chance -= 1
        print(f"The present score is: {score}")
        print(f"The present life is: {life}")
        print(f"The present chance is: {chance}")
        if life == 0 or chance == 0:
            print("Fail!")
            break

# Catching function
def catching(catch):
    global score, life, chance
    while not catch:
        score += 50
        life /= 50
        chance -= 1
        print(f"The present score is: {score}")
        print(f"The present life is: {life}")
        print(f"The present chance is: {chance}")
        if life == 0 or chance == 0:
            print("Fail!")
            break

# Strike function
def striking(strike):
    global score, life, chance
    while not strike:
        score += 25
        life /= 25
        chance -= 1
        print(f"The present score is: {score}")
        print(f"The present life is: {life}")
        print(f"The present chance is: {chance}")
        if life == 0 or chance == 0:
            print("Fail!")
            break

# Out function
def out_player(catch):
    global out
    if not catch:
        out = True
        print("Player is out!")

# Innings functions
def first_innings(innings, out):
    global score, life, chance
    if innings == 1 and not out:
        score += 10
        life /= 2
        chance -= 1
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("First innings passed successfully! Go to the second innings.")
    if out or chance == 0 or life == 0:
        print("Fail!")

def second_innings(innings, out):
    global score, life, chance
    if innings == 2 and not out:
        score += 15
        life /= 4
        chance -= 2
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("Second innings passed successfully! Go to the third innings.")
    if out or chance == 0 or life == 0:
        print("Fail!")

def third_innings(innings, out):
    global score, life, chance
    if innings == 3 and not out:
        score += 20
        life /= 8
        chance -= 3
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("Third innings passed successfully! Go to the fourth innings.")
    if out or chance == 0 or life == 0:
        print("Fail!")

def fourth_innings(innings, out):
    global score, life, chance
    if innings == 4 and not out:
        score += 25
        life /= 16
        chance -= 4
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("Fourth innings passed successfully! Go to the fifth innings.")
    if out or chance == 0 or life == 0:
        print("Fail!")

def fifth_innings(innings, out):
    global score, life, chance
    if innings == 5 and not out:
        score += 30
        life /= 32
        chance -= 5
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("Fifth innings passed successfully! Go to the sixth innings.")
    if out or chance == 0 or life == 0:
        print("Fail!")

def sixth_innings(innings, out):
    global score, life, chance
    if innings == 6 and not out:
        score += 35
        life /= 64
        chance -= 6
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("Sixth innings passed successfully! Go to the seventh innings.")
    if out or chance == 0 or life == 0:
        print("Fail!")

def seventh_innings(innings, out):
    global score, life, chance
    if innings == 7 and not out:
        score += 40
        life /= 128
        chance -= 7
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("Seventh innings passed successfully! Go to the eighth innings.")
    if out or chance == 0 or life == 0:
        print("Fail!")

def eighth_innings(innings, out):
    global score, life, chance
    if innings == 8 and not out:
        score += 45
        life /= 256
        chance -= 8
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("Eighth innings passed successfully! Go to the ninth innings.")
    if out or chance == 0 or life == 0:
        print("Fail!")

def ninth_innings(innings, out):
    global score, life, chance
    if innings == 9 and not out:
        score += 50
        life /= 512
        chance -= 9
        print(f"The present score is: {score}. The present life is: {life}. The present chance is: {chance}")
        print("Ninth innings passed successfully! Congratulations, you completed the game.")
    if out or chance == 0 or life == 0:
        print("Fail!")

# Final score calculation and win/lose determination
allpassed = True
print(allpassed)
final_score = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9
print(final_score)

def win(allpassed):
    global win
    if allpassed:
        win = True
        print("You win!")

def loser(allpassed):
    global win
    if not allpassed:
        win = False
        print("You lose!")

print(f"Your final score is: {final_score}")

# Example of calling functions
first_innings(innings, out)
second_innings(innings, out)
third_innings(innings, out)
fourth_innings(innings, out)
fifth_innings(innings, out)
sixth_innings(innings, out)
seventh_innings(innings, out)
eighth_innings(innings, out)
ninth_innings(innings, out)

if allpassed:
    win(allpassed)
else:
    loser(allpassed)

          
                
          

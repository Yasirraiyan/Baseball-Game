import random;
start=False;
team=["A","B","C","D","E"];
end=False
hit=False
strike=False
catch=False
win=False;
rd=random.randint(1,5)
skill=random.randint(1,5)
ennings=random.randint(1,9)
score=0;
life=50;
chance=5;
out=False;
win=False;
allpassed=False;
score1=score+50;
score2=score+100;
score3=score+150;
score4=score+200;
score5=score+250;
score6=score+300;
score7=score+350;
score8=score+400;
score9=score+450;
score10=score+500;
 if rd==1:
     start=True;
     print(start)
if rd==2:
    choose=random.choice(team)
if rd==4:
    start=False;
    end=True;
    print(start);
    print(end);

if skill==1:
    print(f"Choosable team is:{team[0]}");
if skill==2:
    print(f"Choosable team is:{team[1]}");
if skill==3:
    print(f"Choosable team is:{team[2]}");
if skill==4:
    print(f"Choosable team is:{team[3]}");
if skill==5:
    print(f"Choosable team is:{team[4]}");
def batting(hit):
    while:
        not hit:
        score+=5;
        life=life/5;
        chance-=1;
        print(f"The present score is:{score}")
        print(f"The present life is:{life}")
        print(f"The present chance is:{chance}")
        if life==0 or chance==0:
            print("Fail!")
 def catching(not catch):
    while:
        not catch:
        score+=50;
        life=life/50;
        chance-=1;
        print(f"The present score is:{score}")
        print(f"The present life is:{life}")
        print(f"The present chance is:{chance}")
        if life==0 or chance==0:
            print("Fail!")
def strike(not strike):
    while:
        not strike:
        score+=25;
        life=life/25;
        chance-=1;
        print(f"The present score is:{score}")
        print(f"The present life is:{life}")
        print(f"The present chance is:{chance}")
        if life==0 or chance==0:
            print("Fail!")
            
def out(catch):
    if not catch:
        out=True;
        print("Player is out!")
  def fistennings(ennings,out):
      if ennings==1 and not out:
          score+=10;
          life=life/2;
          chance--;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("First ennings passed successfully!Go second ennings.")
     if  not out or chance==0 or life==0:
         print("Fail!")
    def secondennings(ennings,out):
      if ennings==2 and not out:
          score+=15;
          life=life/4;
          chance-=2;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Second ennings  passed successfully!Go Third step.")
     if  not out or chance==0 or life==0:
         print("Fail!")
          print("Fail!")
    def thirdennings(ennings,out):
      if ennings==3 and not out:
          score+=20;
          life=life/8;
          chance-=3;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Third ennings  passed successfully!Go 4th step")
     if  not out or chance==0 or life==0:
         print("Fail!")
      def fourthennings(ennings,out):
      if ennings==4 and not out:
          score+=25;
          life=life/16;
          chance-=4;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Fourth ennings passed successfully.Go fifth step");
     if  not out or chance==0 or life==0:
         print("Fail!")
     def fifthenings(ennings,out):
      if ennings==5 and not out:
          score+=30;
          life=life/32;
          chance-=5
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Fifth ennings passed successfully.Go sixth step.");
     if  not out or chance==0 or life==0:
         print("Fail!")
     def sixthennings(ennings,out):
      if ennings==6 and not out:
          score+=35;
          life=life/64;
          chance-=6;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Sixth ennings passed successfully.Go seventh step.");
     if  not out or chance==0 or life==0:
         print("Fail!")
      def seventhennings(ennings,out):
      if ennings==7and not out:
          score+=40;
          life=life/128;
          chance-=7;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Seventh ennings passed successfully. go eighth step");
     if  not out or chance==0 or life==0:
         print("Fail!")
      def eigthennings(ennings,out):
      if ennings==8and not out:
          score+=45;
          life=life/264;
          chance-=8;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("8th passed successfully. go 9th step");
     if  not out or chance==0 or life==0:
         print("Fail!")
        def ninthennings(ennings,out):
      if ennings==9and not out:
         s9=score+50;
          life=life/512;
          chance-=9;
          print(f"The present score is:{s9}.The present life is:{life}.The present life is{chance}")
          print("9th ennings passed successfully.Go tenth step");
     if  not out or chance==0 or life==0:
         print("Fail!")
                                   
    allpassed=True;    
      print(allpassed);
      print();
 Finalscore=score1+score2+score3+score4+score5+score6+score7+score8+score9;
      print(Finalscore);
      Finalscore=score1+score2+score3+score4+score5+score6+score7+score8+score9;
  def win(allpassed):
      if not allpassed:
          win=True;
          print("You win!);
     def looser(all passed);
      if  allpassed:
          win=False;
          print("You looser!");
     print(f"Your final score is:{Finalscore}");
     first_innings(innings, out) 
     second_innings(innings, out)
     third_innings(innings, out) 
     fourth_innings(innings, out) 
     fifth_innings(innings, out) 
     sixth_innings(innings, out) 
     seventh_innings(innings, out) 
     eighth_innings(innings, out) 
     ninth_innings(innings, out)
             
          

 def fifthenings(ennings,out):
      if ennings==5 and not out:
          score+=30;
          life=life/32;
          chance-=5
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Fifth ennings passed successfully.Go sixth step.");
     if  not out or chance==0 or life==0:
         print("Fail!")

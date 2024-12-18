def sixthennings(ennings,out):
      if ennings==6 and not out:
          score+=35;
          life=life/64;
          chance-=6;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Sixth ennings passed successfully.Go seventh step.");
     if  not out or chance==0 or life==0:
         print("Fail!")

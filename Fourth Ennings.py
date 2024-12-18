def fourthennings(ennings,out):
      if ennings==4 and not out:
          score+=25;
          life=life/16;
          chance-=4;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Fourth ennings passed successfully.Go fifth step");
     if  not out or chance==0 or life==0:
         print("Fail!")

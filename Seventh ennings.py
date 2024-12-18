def seventhennings(ennings,out):
      if ennings==7and not out:
          score+=40;
          life=life/128;
          chance-=7;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Seventh ennings passed successfully. go eighth step");
     if  not out or chance==0 or life==0:
         print("Fail!")

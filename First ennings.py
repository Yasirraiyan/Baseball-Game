def fistennings(ennings,out):
      if ennings==1 and not out:
          score+=10;
          life=life/2;
          chance--;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("First ennings passed successfully!Go second ennings.")
     if  not out or chance==0 or life==0:
         print("Fail!")

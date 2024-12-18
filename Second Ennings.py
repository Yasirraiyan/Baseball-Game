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

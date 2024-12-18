def eigthennings(ennings,out):
      if ennings==8and not out:
          score+=45;
          life=life/264;
          chance-=8;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("8th passed successfully. go 9th step");
     if  not out or chance==0 or life==0:
         print("Fail!")

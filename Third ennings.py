def thirdennings(ennings,out):
      if ennings==3 and not out:
          score+=20;
          life=life/8;
          chance-=3;
          print(f"The present score is:{score}.The present life is:{life}.The present chance is:{chance}")
          print("Third ennings  passed successfully!Go 4th step")
     if  not out or chance==0 or life==0:
         print("Fail!")

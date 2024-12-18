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

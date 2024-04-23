email=input(" Enter your Email : ")#g@g.in, swapnilbilgoji@gmail.com
k,j,d=0,0,0
if len(email)>=6:#email should be greater than 6 character or equal to six character
    if email[0].isalpha():#first letter of email should be alphabet
        if ("@" in email) and (email.count("@")==1):#there should be @ in email and only one @ should be present
            if(email[-4]==".") ^ (email[-3]=="."):#. should be present in 21 indexin case of .com and 22 in case of .in
                for i in email:
                    if i==i.isspace():#check wheter space is present
                        k=1
                    elif i.isalpha():
                        if i==i.upper():#check wether alphabet is present
                            j=1
                    elif i.isdigit():#check wheter digit is present
                        continue
                    elif i=="_" or i=="." or i=="@": #check wheter _ or . or @ is present
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print( "Check wheter space is present or any uppercase" )
                else:
                    print(" YOUR__EMAIL__IS__CORRECT \n",email)    
                    print("\n THANK__YOU__FOR__ENTERING__YOUR__EMAIL")        
            else:
                print(".com and .in should be present in the end of the email ")
        else:
            print("There should be one @ in email")
    else:
        print("First letter of the email should be alphabet")
else:
    print(" email should be greater then six character")
    
                                        
                                    
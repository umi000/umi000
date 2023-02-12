# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.     c
print("Hello world")
subgenre = ["Horror", "Western"]
movieName01 = ["The Wicked Darling (1919)","Outside the Law (1920)",
"Vampires","The Unholy Three (1925)","The Blackbird (1926)",
"The Road to Mandalay (1926)","London After Midnight (1927)",
"The Unknown (1927)","West of Zanzibar (1928)","The Big City (1928)"]
movieName02 = [ "The Big Country (1958)","singing cowbo","Spaghetti Western","Pursued","Hud (1963)","Little Big Man","Dances With Wolves (1990)","Cat Ballou (1965)","Blazing Saddles (1974)","Mad Max 2"]
movieName02=[[movieName01], [movieName02]]
question00=[
    ["is this movie is silent movie or not ?","is film was considered as lost or not ","is it Europe where its copy is available in 1990s "],
    ["how many role chaney perfrom in Movie","Black Mike Sylva and Ah Wing is his main role or suporting role","The picture was the second film on which Browning worked with Lon Chaney"],
    ["Is vampire charcter is ubiquitous in history of cinema ?","when vampires began popular fiction ","how long first horor movie released"],
    ["in this movie what their activites lead Murder or support","for Murder they atempt to frame an inocent BookKeper ?","browing delight is the Outstanding example of The Unholy Three"],
    ["is Dan 'The Blackbird' and The Bishop the dual role of Chaney in that movie","This movie is directed by Tod Browining","in april 2012 it available in dvd"],
    ["the role of chaney in this movie is ?","is a 1926 American Movie ?","film was considered lost until an abridged version,"],
    ["London after Midnight is Marketed as The Hypnotist","is it silent Mystry movie","film was distribute by Metro-Goldwyn-mayer"],
    ["chaney is Armless Knife thrower, circus performer or not","Is chaney loved a carniwal girl ","this movie is produced by Irving G"],
    ["is hero cast as France megician ","his Name is Phroso ?","cripled and bald headed known as Dead legs ?"],
            ["is it A Lost Film ?","is this movie direted by tod Browing and lon Chaney  ?","is it France Movie ?"]
]
question01=[
    ["is it diretected by Wiliam Wyler,starring Gergory Peck, Burl Ives","The Picture is Based on Serialized magzine","Wiliam Wyler won the Academy award  ?"],
    ["singing cowboy is a northen Film","Real Worl Campfire side ballads is in American Frontier","is it continue singing with the modern genere"],
    ["spaghetti westorn is a board subgenere of westorn films?","it emerged int 1970 ","Majority of the sphagetti westorn genere were internationl"],
    ["diretced by Raul Walsh","set of this movie sets on Mexico","film earned almost 2536000 dollors"],
    ["The Film directed by chaney ","it was produced by Ritt and recenlty found company salem production","hud was filmed at texas ?"],
    ["is little big man is based on Novel 1964?","is film genere like comedy, drama or adventure ?","this is diretced by Arthur Penn "],
    ["the film budget is 1 million ","diretc and produced by one man ","is this mvie tell the story of Union Army Lieutenant Jhon "],
    ["cat Ballou is Serious Movie","is this movie won the Acedmy award  ?","the story is about to protect herslef ?"],
    ["is film received positive reviews ?","brook apperas in three supporting roles ?","is this film white western comedy movie ?"],
    ["is Mad Max 2 released as Road Warrior  ?","it is diretced by George Miller","it released on 24 December"]
    ]
question=[[question00],[question01]]

            
# print(question)

def isTrue(res):
    if res == 'yes' or res == 'YES' or res == 'Yes':
        return True
    elif res == 'no' or res == 'NO' or res == 'No':
        return False
    # An explicit return statement
x=0 
totalAnswer=0
    
    
for i in subgenre:
    print("is it the genre? ",subgenre[x],'----Yes or No  ')
    ans1 = input()
    Answersubgenre=isTrue(ans1)
    if(Answersubgenre == True):
        for i in range(len(question)) : 
            if(totalAnswer==2):
                break;
            for j in range(len(question[i])) : 
                print("is it the genre? ",question[i][j],'----Yes or No  ')
                ans2 = input()
                AnswerQuestion=isTrue(ans2)
                totalAnswer=1
                if(AnswerQuestion == True):
                    for q23 in range(1):
                        print("is it the genre? ",question[i][j],'----Yes or No  ')
                        ans3 = input()
                        AnswerQuestion23=isTrue(ans3)
                        if(AnswerQuestion23 == True):
                            totalAnswer+=1
                    if(totalAnswer==2):
                        break;
                        print("Finally MOVIE NAME IS: ",moviename[0][j])
                    row+=1
            # print(subgenre[x])
            break
        if(totalAnswer==2):
            break;
    elif (Answersubgenre == False):
        print("dcvadscvd bgbbgfbgf ")
                
            # print(question[i][j], end=" ")
        print() 
        
        
        row=0
    #     col=0
    #     for row in range(9):
    #         print("is it the genre? ",(question[row][col]),'----Yes or No  ')
    #         ans2 = input()
    #         AnswerQuestion=isTrue(ans2)
    #         totalAnswer=1
    #         if(AnswerQuestion == True):
    #             for q23 in range(1):
    #                 print("is it the genre? ",question[row][col],'----Yes or No  ')
    #                 ans3 = input()
    #                 AnswerQuestion23=isTrue(ans3)
    #                 if(AnswerQuestion23 == True):
    #                     totalAnswer+=1
    #             if(totalAnswer==2):
    #                 break;
    #                 print(moviename[row])
    #             row+=1
    #     print(subgenre[x])
    #     break
    # elif (Answersubgenre == False):
    #     print("dcvadscvd bgbbgfbgf ")
        
    

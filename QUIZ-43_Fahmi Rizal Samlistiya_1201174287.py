list_gpa :['2.1','2.5','4','3']
 
def gift (GPA):
    bonus = 500000
    gift = GPA * bonus
    return gift

for GPA in list_gpa:
    if GPA > 2.5:
        print("Congratulations! you get a bonus : Rp.", gift(GPA))
    else :
        print ("Sorry, better next time")
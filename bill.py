mtab=("\t\t\t\t\t")
mtab2=("\t\t\t\t")
billm=input("Enter Bill Month/DATE : ")
cn=input("Enter Consumer Name : ")
ca=input("Enter Consumer Address : ")
crd=input("Enter CURRENT READING DATE : ")
prd=input("ENTER PAST READING DATE : ")
cr=eval(input("ENTER CURRENT READING : "))
pr=eval(input("ENTER PAST READING : "))
tc=cr-pr
FS=69.12
UC=43.35
print("-------------------------------------------------------------------------------------------------------------------------------\n")
print(mtab,"Ajmer Vidyut Vitaran Nigam ltd.\n")
print(mtab2,"Rigestered Office Vidut Bhawan, Ajmer")
print(mtab2,"Pan.NO.:AAABCJ6373K, GSTIN.:-08AABCJ6373K127, HSN Code.:-2716")
print("CIN NO. U40109RJ2000SGC016486 *BILL OF SUPPLY*")
print("-------------------------------------------------------------------------------------------------------------------------------")
print("BILL MONTH / DATE             :  ",billm)
print("SUBDIVISION NAME              :  AEN_F-IV_PRATAP NAGAR")
print("ACCOUNT NUMBER                :  17380051")
print("CONSUMER NAME                 :  ",cn)
print("CONSUMER ADDRESS              :  ",ca)
print("BILL NO./MEATER CONDITION     :  10150/REGULAR")
print("TYPE/TEERIFIC CODE            :  DOMESTIC/1000T")
print("SANCTIONED LOAD               :  2.00/2.0 KW")
print("PRECIOUS/METER SAFETY AMOUNT  :  2316/0")
print("CURRENT READING DATE          :  ",crd)
print("PAST READING DATE             :  ",prd)
print("CURRENT READING(KWH)          :  ",cr)
print("PAST READING(KWH)             :  ",pr)
print("TOTAL CONSUMPTION(UNIT)       :  ",tc)
print("FUEL SURCHARGE                :  69.12")
print("URBAN CESS                    :  43.35")
print("--------------------------------------------------------------------------------------------------------------------------------\n")
if tc>=0 and tc<=50:
    TotalAmount=((tc*4.75)+FS+UC)
    print("TOTAL AMOUNT TILL DATE : ","RS.",TotalAmount,"\n","THANK YOU","\n","GOVT. OF INDIA")
elif tc>50and tc<=150:
    TotalAmount=(237.5+((tc-50)*6.50)+FS+UC)
    print("TOTAL AMOUNT TILL DATE : ","RS.",TotalAmount,"\n","THANK YOU","\n","GOVT. OF INDIA")
elif tc>150 and tc<=300:
    TotalAmount=(237.5+650+((tc-150)*7.35)+FS+UC)
    print("Total AMOUNT TILL DATE : ","RS.",TotalAmount,"\n","THANK YOU","\n","GOVT. OF INDIA")
elif tc>300 and tc<=500:
    TotalAmount=(237.5+650+1102.5+((tc-300)*7.65)+FS+UC)
    print("TOTAL AMOUNT TILL DATE : ","RS.",TotalAmount,"\n","THANK YOU","\n","GOVT. OF INDIA")
elif tc>500:
    TotalAmount=(237.5+650+1102.5+1530+((tc-500)*7.95)+FS+UC)
    print("TOTAL AMOUNT TILL DATE : ","RS.",TotalAmount,"\n","THANK YOU","\n","GOVT. OF INDIA")
else:
    print("METER IS NOT WORKING DUE TO :XYZ ","CONTACT TO ELECTRICITY BOARD ","TotalAmount - 00(penelty including to next bill)","\n","THANK YOU","\n","GOVT.OF INDIA")
    

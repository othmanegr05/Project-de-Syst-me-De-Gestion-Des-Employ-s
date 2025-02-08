import mysql.connector
import re # for regex
from tabulate import tabulate #for afficher les list de tuple de form un tableau
import os



conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your password",
    database="SGE"
)
mycursor=conn.cursor()

def menu():
    print("Les options possible ")
    print("1.Ajouter un employe")
    print("2.Modifier un employe")
    print("3.Supprimer un employe ")
    print("4.Rechercher un employe")
    print("5.Afficher la liste complète des employes")
    print("6.Exit")
    while 1:
        try:
            choix=int(input("Entez votre choix : "))
            if 1 <= choix <= 6 :
                return choix
            else:
                print("Incorrect choix , Entez un choix possible")
        except:
            print("Incorrect choix , Entez un choix possible")


def Ajouter():
    print("Le matricule est automatiquement incrémenté ")
    name=input("Entrez le nom complet de l'employe : ")
    while 1:
        try:
            age=int(input("Entrez l'age de l'employe : "))
            break
        except:
            print("l'age incorrect , Entrez un age correct")
    while 1:
        email=input("Entrez email de l'employe : ")
        check=re.search("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" , email)
        if check:
            break
        else:
            print("Entez une forme correct du l'email")

    fonction=input("Entrez la fonction de l'employe : ")

    sql="insert into employe  (nom,age,email,fonction) values (%s,%s,%s,%s)"
    values=(name,age,email,fonction)
    mycursor.execute(sql, values)
    conn.commit()
    print("L'utilisateur a ete ajouté avec succes")


    

def Rechercher():
    while 1:
        try:
            matricule=int(input("Enterz le matricule de l'employe : "))
            break
        except:
            print("le matricule incorrect , Entrez un matricule correct")
    sql="select * from employe where matricule=(%s)"
    value=(matricule,)
    mycursor.execute(sql,value)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(f"marticule : {x[0]}  \nnom : {x[1]} \nAge : {x[2]} \nEmail{x[3]} \nfonction : {x[4]}  ")



def Modifier():
    while 1:
        try:
            matricule=input("Enterz le matricule de l'employe : ")
            break
        except:
            print("le matricule incorrect , Entrez un matricule correct")

    print("Que veux-tu modifier ?")
    print("1.Nom")
    print("2.Age")
    print("3.Email")
    print("4.FONCTION")
    while 1:
            try:
                choix=int(input("Enter votre choix : "))
                if 1 <= choix <= 4 :
                    break
                else:
                    print("Incorrect choix , Entez un choix possible")
            except:
                print("Incorrect choix , Entez un choix possible")
    if choix==1:
        val=input("Entrez le nouveau nom complet : ")
        col='nom'
        update(matricule,col,val)
    elif choix==2 :
        while 1:
            try:
                age=int(input("Entrez l'age de l'employe : "))
                break
            except:
                print("l'age incorrect , Entrez un age correct")
        col='age'
        update(matricule,col,age)
    elif choix==3:
        while 1:
            email=input("Entrez email de l'employe : ")
            check=re.search("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" , email)
            if check:
                break
            else:
                print("Entez une forme correct du l'email")

        col='email'
        update(matricule,col,email)
    elif choix==4:
        fonction=input("Entrez la fonction de l'employe : ")
        col='fonction'
        update(matricule,col,fonction)

def update(matricule,col,val):
    sql=f"update employe set {col}=%s where matricule=(%s)"
    values=(val,matricule)
    mycursor.execute(sql,values)
    conn.commit()
    print("L'employe a ete modifie avec succes")



def affichage():
    sql="select * from employe"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    headers=["matricule","nom complet","age","email", "fonction"]
    print(tabulate(myresult, headers=headers,tablefmt="grid"))
def supprimer():
    while 1:
        try:
            matricule=tuple(input("Enterz le matricule de l'employe : "))
            break
        except:
            print("le matricule incorrect , Entrez un matricule correct")
    sql="delete from employe where matricule=%s"
    value=(matricule)
    mycursor.execute(sql,value)
    conn.commit()
    print("L'employe a ete supprime avec succes")


def main():
    while 1:
        choix=menu()
        if choix==1:
            Ajouter()
            input("Tapez pour continuer")
            os.system('cls')
        elif choix==2:
            affichage()
            Modifier()
            input("Tapez pour continuer")
            os.system('cls')
        elif choix==3:
            affichage()
            supprimer()
            input("Tapez pour continuer")
            os.system('cls')
        elif choix==4:
            affichage()
            Rechercher()
            input("\n\nTapez pour continuer")
            os.system('cls')
        elif choix==5:
            affichage()
            input("Tapez pour continuer")
            os.system('cls')
        elif choix==6:
            print("Exinting ...")
            input("Tapez pour continuer")
            os.system('cls')
            break
    
main()

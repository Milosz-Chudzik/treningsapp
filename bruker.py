import mysql.connector

mydb = mysql.connector.connect(
    host="10.2.2.119",
    user="[milosz]",
    password="[milosz2007]",
    database="kalender"
)

cursor = mydb.cursor(buffered=True)

#stats
def start():
    try:
        print("Velg fra menyen:")
        print("1. legge inn øvelser")
        print("2. oppdatere dine øvelser")
        print("3. se dine øvelser")
        print("4. Avslutt")
        valg = int(input("Skriv inn ditt valg: "))

        if valg == 1:
            legge_inn_ovelse()
        elif valg == 2:
            oppdater_ovelse()
        elif valg == 3:
            vis_ovelse()
        elif valg == 4:
            print("Avslutter...")
        else:
            print("Ugyldig valg, prøv igjen.")
            start()

    except ValueError:
        print("Ugyldig valg, prøv igjen.")
        start()

def legge_inn_ovelse():
    navn = input("navn på øvelsen: ")
    muskelgruppe = input("hvilken muskelgruppe trener øvelsen?: ")
    try:
        sql = f"SELECT * FROM ovelser WHERE ovelse = {navn}"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            sql = f"INSERT INTO ovelser (navn, muskelgruppe) VALUES ('{navn}', '{muskelgruppe}')"
            cursor.execute(sql)
            mydb.commit()
            print(f"øvelsen {navn} er lagret.")
            start()
    except:
        print("Noe gikk galt, prøv igjen.")
        legge_inn_ovelse()

def oppdater_ovelse():
    valg = int(input("hva er det du ønsker å endre? \ntrykk 1 for reps \ntrykk 2 for sets \ntrykk 3 for vekt \ntrykk 4 for å gå tilbake:"))
    if valg == 1:
        øvelse = input("hvilken øvelse skal du oppdatere: ")
        reps = input("nytt antall reps: ")
        sql = f"select ovelse_id from ovelser where ovelse = '{øvelse}';"
        cursor.execute(sql)
        ovelse_id = cursor.fetchone()[0]
        print(ovelse_id)
        sql = f"update bruker_ovelser set reps = 4 where ovelse_id = 4 and bruker_id = 1;"
        # sql = f"update bruker_ovelser set reps = {reps} where ovelse_id = {ovelse_id} and bruker_id = {innlogget_bruker};"
        cursor.execute(sql)
        print(sql)
        print(innlogget_bruker)

    elif valg == 2:
        print()

    elif valg == 3:
        print()

    elif valg == 4:
        start()
    
    else: 
        print("Ugyldig valg, prøv igjen.")
        oppdater_ovelse()  
        
        
def vis_ovelse():
    print()

innlogget_bruker = None

def register_user():
    brukernavn = input("Skriv inn brukernavnet du ønsker: ").strip()
    passord = input("Skriv inn et passord: ").strip()

    try:
        cursor.execute("INSERT INTO bruker (brukernavn, passord) VALUES (%s, %s)", (brukernavn, passord))
        mydb.commit()
        print("Brukeren din er registrert.")
    except mysql.connector.Error as err:
        print(f"Feil: {err}")
        print("Brukernavnet finnes kanskje allerede. Prøv et annet brukernavn.")

def login_user():
    global innlogget_bruker  
    brukernavn = input("Skriv inn brukernavnet ditt: ").strip()
    if brukernavn == "":
        brukernavn = "micha010"
    passord = input("Skriv inn passordet ditt: ").strip()
    if passord == "":
        passord = "passord"

    try:
        query = "SELECT passord FROM bruker WHERE brukernavn = '" + brukernavn +"';"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            stored_passord = result[0]
            if passord == stored_passord:
                print(f"Velkommen, {brukernavn}!")
                query = "SELECT bruker_id FROM bruker WHERE brukernavn = '" + brukernavn + "';"
                cursor.execute(query)
                brukerId = cursor.fetchone()
                innlogget_bruker = brukerId[0]
                print(f"{innlogget_bruker}")

                start()

            else:
                print("Feil passord. Prøv igjen.")
        else:
            print("Fant ikke bruker. Prøv igjen.")
    except mysql.connector.Error as err:
        print(f"Feil under innlogging: {err}")

def main():
    print("\n--- Brukeradministrasjon ---")
    print("1. Registrer")
    print("2. Logg inn")
    print("3. Avslutt")

    valg = input("Hva ønsker du å gjøre: ")

    if valg == "1":
        register_user()

    elif valg == "2":
        login_user()

    elif valg == "3":
        print("Avslutter programmet...")
        

    else:
        print("Ugyldig valg. Prøv igjen.")



main()

#cursor.close()
#mydb.close()



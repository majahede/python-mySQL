import csv
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
host='127.0.0.1', database='hedegard')
DB_NAME='hedegard'

# with open('./data/planets.csv') as csv_file:
#   csvfile = csv.reader(csv_file, delimiter=',')
#   all_value = []
#   for row in csvfile:
#     value = (row[0], row[1], row[2],  row[3],  row[4],  row[5],  row[6], row[7], row[8])
#     all_value.append(value)

# create = "CREATE TABLE planets (name varchar(50) not null, rotation_period int, orbital_period int, diameter int, climate nvarchar(200), gravity nvarchar(20), terrain nvarchar(200), surface_water int, population int, primary key(name))"
# insert = "insert into planets (`name`, rotation_period ,`orbital_period`,`diameter`,`climate`,`gravity`,`terrain`,`surface_water`,`population`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


# insert2 = "LOAD DATA LOCAL INFILE './data/planets.csv' INTO TABLE test.dummy FIELDS TERMINATED BY ',' "

mycursor = cnx.cursor()
#mycursor.execute(create_database)
# mycursor.executemany(insert, all_value)
# cnx.commmit()

def return_to_main():
  species = input ("Press any key to return to main menu: ")
  main_menu()

def list_planets():
  mycursor.execute("SELECT * from planets")
  for x in mycursor:
       print(x[0])
  return_to_main()

def planet_details():
  planet = input ("Enter name of a planet: ")
  mycursor.execute("SELECT * from planets WHERE name = '" + planet + "'")
  for x in mycursor:
       print("Name: " + x[0])
       print("Rotation period: " + str(x[1]))
       print("Orbital period: " + str(x[2]))
       print("Diameter: " + str(x[3]))
       print("Climate: " + x[4])
       print("Gravity: " + x[5])
       print("Terrain: " + x[6])
       print("Surface water: " + str(x[7]))
       print("Population: " + str(x[8]))
       return_to_main()

def species_height():
  planet = input ("Enter an average height: ")
  # display species that fulfills condition
  # press any key to return to main

def desired_climate():
  species = input ("Enter name of a species: ")
  # display species that fulfills condition
  # press any key to return to main

def average_lifespan():
  print("list of species") 
  # list name of species classification and their average lifespan
  # press any key to return to main

def main_menu():
  while True:
    print ("1. List all planets.") 
    print ("2. Search for planet details.")
    print ("3. Search for species with height higher than given number.")
    print ("4. What is the most likely desired climate of the given species?")
    print ("5. What is the average lifespan per species classification?")
    print ("Q. Quit")
    print ("---------")
    choice = input ("Please choose one option: ")

    if choice == "1":
          list_planets()
          break
    elif choice == "2":
          planet_details()
          break
    elif choice == "3":
          species_height()
          break
    elif choice == "4":
          desired_climate()
          break
    elif choice == "5":
          average_lifespan()
          break
    elif choice == "Q":
          quit()
    else:
          print("Please enter a valid input")
          print()
          continue

main_menu()
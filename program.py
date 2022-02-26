import csv
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
host='127.0.0.1', database='hedegard')
DB_NAME='hedegard'
cursor = cnx.cursor()

file = open('./data/planets.csv')
planets_data = csv.reader(file)
next(planets_data)
all_planets = []
for row in planets_data:
  value = [row[0], row[1], row[2],  row[3],  row[4],  row[5],  row[6], row[7], row[8]]
  for x in range(1, 9):
    if value[x] == "NA":
      value[x] = None
  all_planets.append(value)

file = open('./data/species.csv')
species_data = csv.reader(file)
next(species_data)
all_species = []
for row in species_data:
  value = [row[0], row[1], row[2],  row[3],  row[4],  row[5],  row[6], row[7], row[8], row[9]]
  for x in range(1, 10):
    if value[x] == "NA" or value[x] == "indefinite":
      value[x] = None
  all_species.append(value)

create_database = "CREATE DATABASE IF NOT EXISTS " + DB_NAME

drop_planets_table = "DROP TABLE IF EXISTS planets"
drop_species_table = "DROP TABLE IF EXISTS species"

create_planets_table = "CREATE TABLE planets (name varchar(50) not null, rotation_period int, orbital_period int, diameter int, climate nvarchar(200), gravity nvarchar(200), terrain nvarchar(200), surface_water int, population bigint, primary key(name))"

create_species_table = "CREATE TABLE species (name varchar(50) not null, classification nvarchar(200), destination nvarchar(200), average_height int, skin_colors nvarchar(200), hair_colors nvarchar(200), eye_colors nvarchar(200), average_lifespan int, language nvarchar(200), homeworld nvarchar(200), primary key(name))"
insert_planets = "insert into planets (`name`, `rotation_period` ,`orbital_period`,`diameter`,`climate`,`gravity`,`terrain`,`surface_water`,`population`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

insert_species = "insert into species (`name`, `classification` ,`destination`,`average_height`,`skin_colors`,`hair_colors`,`eye_colors`,`average_lifespan`,`language`, `homeworld`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

cursor.execute(create_database)
cursor.execute(drop_planets_table)
cursor.execute(drop_species_table)
cursor.execute(create_planets_table)
cursor.execute(create_species_table)
cursor.executemany(insert_planets, all_planets)
cursor.executemany(insert_species, all_species)
cnx.commit()

def return_to_main():
  input ("Press ENTER to return to main menu: ")
  main_menu()

def list_planets():
  cursor.execute("SELECT * from planets")
  for x in cursor:
       print(x[0])
  return_to_main()

def planet_details():
  planet = input ("Enter name of a planet: ")
  cursor.execute("SELECT * from planets WHERE name = '" + planet + "'")
  for x in cursor:
       print("Name: " + x[0])
       print("Rotation period: " + str(x[1]))
       print("Orbital period: " + str(x[2]))
       print("Diameter: " + str(x[3]))
       print("Climate: " + str(x[4]))
       print("Gravity: " + str(x[5]))
       print("Terrain: " + str(x[6]))
       print("Surface water: " + str(x[7]))
       print("Population: " + str(x[8]))
  return_to_main()

def species_height():
  height = input ("Enter an average height: ")
  cursor.execute("SELECT * from species WHERE average_height > " + height)
  for x in cursor:
       print(x[0])
  return_to_main()

def desired_climate():
  species = input ("Enter name of a species: ")
  cursor.execute("SELECT planets.climate, species.name from planets, species WHERE planets.name = species.homeworld and species.name = '" + species + "'")
  for x in cursor:
       print(x[0])
  return_to_main()

def average_lifespan():
  cursor.execute("SELECT classification, AVG(average_lifespan) from species GROUP BY classification")
  for x in cursor:
      print(x[0], x[1])
  return_to_main()

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
car_catalog = []; #marka, model, rocznik, silnik, moc, waga

def addCar(marka:str,model:str,rocznik:int,silnik:str,moc:int,waga:int):
	if not isinstance(marka, str):
		print("Marka musi być typem STRING")
		return
	if not isinstance(model, str):
		print("Model musi być typem STRING")
		return	
	if not isinstance(rocznik, int):
		print("Rocznik musi być typem INT")
		return
	if not isinstance(silnik, str):
		print("Silnik musi być typem STRING")
		return
	if not isinstance(moc, int):
		print("Moc musi być typem INT")
		return
	if not isinstance(waga, int):
		print("waga musi być typem INT")
		return
	car_catalog.append([marka.upper(),model,rocznik,silnik,moc,waga])
	print("Pomyślnie dodano ",marka," ",model," do bazy danych!")

def calcPowerToMassRatio(*args): 
	if(len(args)>0):
		found_list = {}
		for i in range(6): 
			found_list[i] = []
		for car_entry in range(len(car_catalog)):
			match_amount = 0;
			for argument in args:
				if argument in car_catalog[car_entry]:
					match_amount+=1
			if match_amount>0:
				found_list[match_amount].append(car_catalog[car_entry])
		biggest_matches = 0

		for matches in found_list: 
			if(len(found_list[matches])>biggest_matches):
				biggest_matches = matches
		#print("najwiecej dopasowan",biggest_matches,"argumentów, znaleziono:",len(found_list[biggest_matches]),"aut pasujących do wprowadzonych argumentów")
		for car in found_list[biggest_matches]:
			power_to_mass_ratio = round(car[4]/car[5],3)
			print(f"Pojazd:{car[0]} ||Model:{car[1]} ||Rocznik:{car[2]} ||Silnik:{car[3]} ||Stosunek mocy do wagi:{power_to_mass_ratio}")
		

		
			
addCar("BMW","E46",1999,"M52B28TU",193,1350)
addCar("BMW","E46",1999,"M52B28TU",193,1330)
addCar("BMW","E46",1999,"M52B28TU",193,1300)
addCar("BMW","E46",1999,"M52B28TU",194,1400)
calcPowerToMassRatio(194)
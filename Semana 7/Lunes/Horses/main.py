from Horse import Horse
from Valid import Valid
from Race import Race

def main():
    print("Welcome to Derby of Kentucky")
    valids = int(input("Please enter how many valids will we have: "))
    races = int(input("Please enter how many races will we have in each valid: "))
    horse1 = Horse("El rayo veloz",1)
    horse2 = Horse("Gustavo",2)
    horse3 = Horse("El caballo maravilla",3)
    horse4 = Horse("Superman",4)
    horse5 = Horse("Caballo Random",5)
    horse6 = Horse("El mas crack",6)
    for valid in range(valids):
        race_list = []
        horse_list = [horse1,horse2,horse3,horse4,horse5,horse6]
        for race in range(races):
            race_list.append(Race(race,horse_list))
        for race in race_list:
            race.start_race()
            race.choose_winner()
        


main()
import os
import random
import platform

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = {'gold': 0, 'food': 0, 'weapons': 0}


    def show_stats(self):
        self.clear_console()
        print(f"{self.name}'s Stats:")
        print(f"Health: {self.health}")
        print("Inventory:")
        for item, count in self.inventory.items():
            print(f"  {item}: {count}")
        print("If you want to restore your health (+7) print food, it will cost 10 food")    
        if input().lower() == 'food':
            self.heal() 
        
        input("\nPress Enter to continue...")

    def heal(self):  
        if self.inventory['food'] < 7:
            print("Not enough food")
        else:
            self.inventory['food'] -= 10
            self.health += 7
        
    def go_raid(self):
        self.clear_console()
        print(f"{self.name} is going on a raid...")
        raid_outcome = random.choice(['success', 'failure'])
        if raid_outcome == 'success':
            print("Raid successful! You found some resources.")
            self.gain_resources()
        else:
            print("Raid failed! You took some damage.")
            self.take_damage(20)
        input("\nPress Enter to continue...")

    def gain_resources(self):
        loot = {'gold': random.randint(10, 50),
                'food': random.randint(5, 20),
                'weapons': random.randint(1, 5)}

        print("You gained the following resources:")
        for item, count in loot.items():
            print(f"  {item}: {count}")
            self.inventory[item] += count
        input("\nPress Enter to continue...")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has died!")
            input("\nPress Enter to exit...")
            exit()

    def clear_console(self):
        system = platform.system().lower()
        if system == 'windows':
            os.system('cls')
        else:
            os.system('clear')

def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    while True:
        player.clear_console()
        print("\n1. Show Stats")
        print("2. Go on Raid")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            player.show_stats()
        elif choice == '2':
            player.go_raid()
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()

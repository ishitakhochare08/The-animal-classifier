animals=["dolphin","shark","tiger","lion","rabbit","cat","dog","wolf","goat"
         "cheetah","blue whale","elephant","pig","rat","anaconda","lizard"
         "snake","crocodile","tortoise","turtle","bear","frog","octopus","starfish"
         "salmander","toad"
         ]

land_mammals={"tiger","lion","rabbit","cat","dog","wolf","cheetah","elephant",
              "pig","rat","bear","goat"}
reptiles={"crocodile","snake","anaconda","tortoise","lizard"}
marine_animals={"blue whale","octopus","dolphin","turtle","starfish"}
amphibian={"frog","salmander","toad"}



input_an=input("Enter the animal for classification: ")


if input_an not in animals:
    print("sorry the animal is unavailable in our database!\nwe will update it very soon...")

elif input_an in land_mammals:
    print("Category: land mammal\ncan survive on land only,uses limbs for movement")

elif input_an in reptiles:
    print("Category: Reptile\n Cold blooded and walk with lateral body bending movement")

elif input_an in marine_animals:
    print("Category: Marine animal \n only found in the ocean,movement through fins or limbs(if not a fish)")

elif input_an in amphibian:
    print("Category: Amphibian\ncan survive on land as well as water")


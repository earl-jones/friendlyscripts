friends = ["Donovan", "Taylor", "Melvin", "Jon"]
friends.append("Bart")


name = input("Hello! What's your name?: ").strip().capitalize()

add_answer = input(f"Well, it's nice to meet you, {name}! My name is EJ. Would you like to be my friend? (y/n): ").strip().lower()

if add_answer == "y":
    friends.append(name)
    print("Look! I have added you to my friend list!")
    print(friends)
    remove_answer = input("Would you like to be remain on my friend list? (y/n): ").strip().lower()
    if remove_answer == "n":
        friends.remove(name)
        print("No problem! Please see my updated friend list below: ")
        print(friends)
    else :
        print(f"I'm glad to hear that! See you later, {name}!")

else :
    print("No worries! See my friend list below:")
    print(friends)

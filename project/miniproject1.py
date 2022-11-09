print("Welcome to the Yu-Gi-Oh quiz!")

questions = [
    "1. One of your bullies takes your things and throws them into the ocean. What do you do? \n A. Dive into the water to save it \n B. Beat them up \n C. Send them to the Shadow Realm",
    "2. Do you believe in the heart of the cards? \n A. Yes \n B. No \n C. I believe in world domination",
    "3. Your friends are in danger! What do you do? \n A. Challenge the kidnappers to a duel! \n B. Risk my life to save them! \n C. What friends? I only have minions",
    "4. What do you treasure the most? \n A. Friendship \n B. Family \n C. Power",
    "5. Which monster card do you like best? \n A. Dark Magician \n B. Red Eyes Black Dragon \n C. Any of the god cards",
    "6. How would you describe yourself? \n A. Brave \n B. Loyal \n C. Witty",
    "7. What would you do if you had a millenium item? \n A. Send wrong doers to the Shadow Realm \n B. Put it back where it belongs \n C. Take advantage of its powers!",
    "8. The fate of the world rests in your hands! How do you react? \n A. Save it through a duel card game \n B. Leave it to the protagonist \n C. Let it burn!!!",
    "9. How good are you at dueling? \n A. I'm the best \n B. I'm average \n C. I'll just send my opponents to the Shadow Realm if I lose",
    "10. How good are you working in teams? \n A. I like to do things solo \n B. I'm very much a team player \n C. I tend to take the lead"
]
user_input = ''
characters = {"Yami Yugi": 0, "Joey Wheeler": 0, "Yami Marik": 0}

def main():
    for question in questions:
        while True:
            print(question)
            user_input = input("Choose a character from the available choices: ").lower()
            match user_input:
                case "a":
                    characters["Yami Yugi"] += 1
                    break
                case "b":
                    characters["Joey Wheeler"] += 1
                    break
                case "c":
                    characters["Yami Marik"] += 1
                    break
                case _:
                    print("You must select a valid character.")

    character = max(characters, key=characters.get)
    print(f"Congratulations! Your Yu-Gi-Oh persona is {character}.")
    print("Thank you for playing. Have a good day!")

main()

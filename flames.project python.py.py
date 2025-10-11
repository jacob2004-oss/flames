def flames_game():
    print("🔥 Welcome to the FLAMES Game 🔥")
    print("--------------------------------")

    
    name1 = input("Enter your name: ").lower().replace(" ", "")
    name2 = input("Enter your crush's name: ").lower().replace(" ", "")

     
    name1_list = list(name1)
    name2_list = list(name2)

    for letter in name1[:]:
        if letter in name2_list:
            name1_list.remove(letter)
            name2_list.remove(letter)

    remaining_letters = len(name1_list) + len(name2_list)

    print(f"\n🧮 Total remaining letters: {remaining_letters}")

    
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

    while len(flames) > 1:
        split_index = (remaining_letters % len(flames)) - 1

        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    
    result = flames[0]
    print(f"\n💞 Relationship Status: {result} 💞")



if __name__ == "__main__":
    flames_game()

    

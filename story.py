def intro():
    print("You wake up in a dark forest. You can go left, center, or right.")
    choice = input("Which direction do you choose? (left/center/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "center":
        center_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def center_path():
    print("You walk straight ahead, following a faint trail of lanterns.")
    print("At a quiet clearing, a calm voice teaches you a secret that changes your fate.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()

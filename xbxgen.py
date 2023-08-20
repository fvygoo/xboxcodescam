import random
import time

xbox_usernames = [
    "SharpKnives", "TheZodiac", "OsamasGhost", "Angelofdeath", "DeathSquad",
    "Veteranofdeath", "T3rr0r1st", "Ebola", "LookURDead", "SharpKnives",
    "SepticMoma", "AssasinMeetUp", "TWitMeet", "AssasinFaceOff", "WickedImpulse",
    "B4UShout", "UrAssDontLie", "LazyKiller", "FireKiller", "Damnhunter", "Mahakaal"
]

pass_durations = [
    "1 Month Game Pass", "3 Month Game Pass",
    "6 Month Game Pass", "12 Month Game Pass"
]

def generate_random_username():
    return random.choice(xbox_usernames)

def generate_random_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(16))

def generate_random_balance():
    return random.randint(10, 100)

def generate_random_duration():
    return random.choice(pass_durations)

def create_gift_card():
    username = generate_random_username()
    code = generate_random_code()
    balance = generate_random_balance()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    gift_card = f"""
xʙᴏx ᴄᴀʀᴅ ɢᴇɴ
╔═════════════════╗
║  XBOX GIFT CARD ║
╠═════════════════╣
║ Username: {username}
║ Code: {code}
║ Balance: ${balance}
║ Last Updated: {timestamp}
╚═════════════════╝
"""

    return gift_card

def create_game_pass_code():
    code = generate_random_code()
    duration = generate_random_duration()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    game_pass_code = f"""
xʙᴏx ᴄᴀʀᴅ ɢᴇɴ
╔═══════════════════╗
║ = CREATE GAME PASS║
║       CODE =      ║
╠═══════════════════╣
║ Code: {code}
║ Duration: {duration}
║ Last Updated: {timestamp}
╚═══════════════════╝
"""

    return game_pass_code

def current_update():
    return """
xʙᴏx ᴄᴀʀᴅ ɢᴇɴ
┏━━━━━━━━━━━━━━━━━━━┓
┃= Check github for ┃
┃updates =          ┃
┃                   ┃
┗━━━━━━━━━━━━━━━━━━━┛
"""

def main():
    while True:
        print("\n" + "="*30)
        print("        DASHBOARD MENU        ")
        print("="*30)
        print("(1) Create Gift Card")
        print("(2) Create Game Pass Code")
        print("(3) Current Update")
        print("(4) Exit")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            while True:
                gift_card_output = create_gift_card()
                print(gift_card_output)
                print("\n(1) Regenerate Gift Card")
                print("(2) Back to Dashboard")
                back_choice = int(input("Enter your choice (1/2): "))
                if back_choice == 1:
                    continue
                elif back_choice == 2:
                    break
        elif choice == 2:
            while True:
                game_pass_code_output = create_game_pass_code()
                print(game_pass_code_output)
                print("\n(1) Regenerate Game Pass Code")
                print("(2) Back to Dashboard")
                back_choice = int(input("Enter your choice (1/2): "))
                if back_choice == 1:
                    continue
                elif back_choice == 2:
                    break
        elif choice == 3:
            while True:
                update_message = current_update()
                print(update_message)
                print("\n(1) Back to Dashboard")
                back_choice = int(input("Enter your choice (1): "))
                if back_choice == 1:
                    break
        elif choice == 4:
            print("Exiting the dashboard. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hickey's Arcade")
root.geometry("800x600")
root.configure(bg="purple")

# Load images
#logo_img = tk.PhotoImage(file="hickey_logo.png")
#shed_img = tk.PhotoImage(file="shed.jpg")

# Create logo and image widgets
#logo_label = tk.Label(root, image=logo_img)
#shed_label = tk.Label(root, image=shed_img)

# Position the widgets using grid layout
#logo_label.grid(row=0, column=0, columnspan=3)
#shed_label.grid(row=1, column=0, columnspan=3)


# Function placeholders for button actions
# Function to show player information
def show_players():
    # Clear the scoreboard
    scoreboard_tree.delete(*scoreboard_tree.get_children())

    # Populate the scoreboard with player data
    #for player_id, player_data in players.items():
    #    name = player_data["name"]
    #   money = player_data["money"]
    #    wins = player_data["wins"]
    #    games_played = player_data["games_played"]
    #    rank = calculate_player_rank(player_data)  # Function to calculate rank
#
     #   scoreboard_tree.insert("", "end", values=(name, rank, money, games_played))

#def calculate_player_rank(player_data):
    # Calculate player rank based on some criteria
    #rank = player_data["wins"] + player_data["money"] / 100
    #return rank


def show_scores():
    pass

def show_tournament():
    pass

def show_money():
    pass

# Create buttons
players_btn = tk.Button(root, text="Players", command=show_players)
scores_btn = tk.Button(root, text="Scores", command=show_scores)
tournament_btn = tk.Button(root, text="Tournament", command=show_tournament)
money_btn = tk.Button(root, text="Money", command=show_money)

# Position the buttons using grid layout
players_btn.grid(row=2, column=0)
scores_btn.grid(row=2, column=1)
tournament_btn.grid(row=2, column=2)
money_btn.grid(row=2, column=3)



import tkinter.ttk as ttk

# Create the Live Scoreboard
scoreboard_columns = ("Player", "Rank", "Money", "Games Won")
scoreboard_tree = ttk.Treeview(root, columns=scoreboard_columns, show="headings")

# Define the column headings
for col in scoreboard_columns:
    scoreboard_tree.heading(col, text=col)

# Position the Live Scoreboard using grid layout
scoreboard_tree.grid(row=3, column=0, columnspan=4)


# Function placeholder for top games and random games6
def show_top_games():
    pass

def show_random_games():
    pass

# Create labels for Top Games and Random Games
top_games_label = tk.Label(root, text="Top Games")
random_games_label = tk.Label(root, text="Random Games")

# Position the labels using grid layout
top_games_label.grid(row=4, column=0)
random_games_label.grid(row=4, column=1)

# Create a listbox for random games
#random_games_listbox = tk.Listbox(root, width=30, height=10)
#random_games_listbox.grid(row=5, column=1)

#import modules
import random
import time
from tkinter import *
from tkinter import messagebox, simpledialog, ttk
from tktooltip import ToolTip
import pyttsx3

#define the player class
class Player:

  def __init__(self, strategy, name, hand):
    self.name = name
    self.strategy = [strategy]
    self.hand = hand
    self.hand = self.organize_hand()
    if self.strategy == "computer":
      self.strategy = "computer" + str(random.randint(1, 3))

  def computer_mind(self, current_play_type, last_cards):
    plays = []
    if current_play_type == None:
      plays = []
      for i in [list(range(1, 6)).remove(3)]:
        plays.append(
            find_possible_plays(last_cards_played=last_cards,
                                play_type=i,
                                current_hand=self.hand))
        if plays[-1] == "Pass":
          plays.remove(-1)
        print(plays)
    else:
      plays = find_possible_plays(last_cards_played=last_cards,
                                  play_type=current_play_type,
                                  current_hand=self.hand)
      print(plays)
    if self.strategy == "computer1":
      return plays[1]
    elif self.strategy == "computer2":
      return random.choice(plays)
    elif self.strategy == "computer3":
      return plays[-1:]

  def __str__(self):
    str = f"Player of type {self.strategy}. Username: {self.name}. Current hand: {self.hand}"
    return str

  def play_card(self, current_play_type, last_card_player):
    if self.strategy == "player":
      plays = find_possible_plays(last_cards_played=last_card_player[0],
                                  play_type=current_play_type,
                                  current_hand=self.hand)
      my_play = input(
          f"here are the plays: {plays}\n What do you want to play: ")
      return [my_play, self.name]
    else:
      my_play = self.computer_mind(current_play_type, last_card_player[0])
      return [my_play, self.name]

  def organize_hand(self):
    sorted_hand = self.hand.sort()
    return sorted_hand

  def update(self, strategy, name, hand):
    self.name = name
    self.strategy = [strategy]
    self.hand = hand
    self.hand = self.organize_hand()


#define functions
def show_rules():
  #text-based
  # with open('rules.txt', 'r') as f:
  #   print(str(f.read()))
  #tkinter
  window = Tk()
  window.minsize(width=610, height=400)
  window.title("Rules")
  exit_button = Button(window, text="Done", command=exit, font=("Comic Sans MS", 18, "bold"))
  canvas = Canvas(window)
  canvas.pack(side="left", fill="both", expand=True)
  scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
  scrollbar.pack(side="right", fill="y")
  canvas.configure(yscrollcommand=scrollbar.set)
  canvas.bind("<Configure>",
              lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
  frame = Frame(canvas)
  title = Label(frame, text="Rules")
  title.configure(font=("Comic Sans MS", 25, "bold"))
  canvas.create_window((0, 0), window=frame, anchor="nw")
  with open('rules.txt', 'r') as f:
    label = Label(frame,
                  text=f.read(),
                  justify='left',
                  wraplength=600, 
                  font=("Comic Sans MS", 14, "bold"))
  title.pack()
  #exit_button.pack(side="right",anchor="ne")
  label.pack()
  window.mainloop()


def intro():
  # text-based
  # print("Welcome to Big Two, a Cantonese Card Game.")
  # if input("Have you played before?") == "yes"
  #   show_rules()
  # username = ""
  # while username == "":
  #   username = input("Enter a username")
  # input("Are you ready to play?")
  # return username
  # tkinter
  #engine = pyttsx3.init()
  #engine.say("Welcome to Big Two, a Cantonese Card Game. Let's Play!")
  #engine.runAndWait()
  messagebox.showinfo(title="Welcome",
                      message="Welcome to Big Two, a Cantonese Card Game.")
  print("Welcome to Big Two, a Cantonese Card Game.")
  if not messagebox.askyesno(
      title="Experience",
      message="Have you played before? If so, press yes. Otherwise, press no."
  ):
    show_rules()
  #time.sleep(1)
  username = ""
  while username == "":
    username = simpledialog.askstring("Username", "Enter a username:")
  messagebox.askokcancel("Game Time", f"Are you ready to play, {username}?")
  return username


def deal(deck, count_players):
  hand_dict = {}
  for number in range(0, count_players):
    hand_dict[number] = []
  while deck:
    for i in range(0, count_players):
      try:
        hand_dict[i].append(deck.pop(0))
      except IndexError:
        break
  return hand_dict


def check_end(players):
  type = None
  return type


def check_num_match(card1, card2):
  numbers = [
      "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "01",
      "02"
  ]
  return numbers.index(card1[:2]) == numbers.index(card2[:2])


def check_suit_match(card1, card2):
  suits = ["Diamond", "of Club", "f Heart", "f Spade"]
  return suits.index(card1[-7:]) == suits.index(card2[-7:])


def find_value(card):
  deck = [
      '03 of Diamond', '03 of Club', '03 of Heart', '03 of Spade',
      '04 of Diamond', '04 of Club', '04 of Heart', '04 of Spade',
      '05 of Diamond', '05 of Club', '05 of Heart', '05 of Spade',
      '06 of Diamond', '06 of Club', '06 of Heart', '06 of Spade',
      '07 of Diamond', '07 of Club', '07 of Heart', '07 of Spade',
      '08 of Diamond', '08 of Club', '08 of Heart', '08 of Spade',
      '09 of Diamond', '09 of Club', '09 of Heart', '09 of Spade',
      '10 of Diamond', '10 of Club', '10 of Heart', '10 of Spade',
      '11 of Diamond', '11 of Club', '11 of Heart', '11 of Spade',
      '12 of Diamond', '12 of Club', '12 of Heart', '12 of Spade',
      '13 of Diamond', '13 of Club', '13 of Heart', '13 of Spade',
      '01 of Diamond', '01 of Club', '01 of Heart', '01 of Spade',
      '02 of Diamond', '02 of Club', '02 of Heart', '02 of Spade'
  ]
  return deck.index(card)


def get_larger_value(card1, card2):
  suits = ["Diamond", "of Club", "f Heart", "f Spade"]
  numbers = [
      "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "01",
      "02"
  ]
  if numbers.index(card1[:2]) < numbers.index(card2[:2]):
    return card2
  elif numbers.index(card1[:2]) > numbers.index(card2[:2]):
    return card1
  elif numbers.index(card1[:2]) == numbers.index(card2[:2]):
    if suits.index(card1[-7:]) < suits.index(card2[-7:]):
      return card2
    elif suits.index(card1[-7:]) > suits.index(card2[-7:]):
      return card1


def find_possible_plays(last_cards_played, play_type, current_hand):
  possible_plays = []
  #print(current_hand)
  last_card = str(last_cards_played).strip("['").strip("']")
  if play_type == 1:
    play = []
    for card in current_hand:
      if get_larger_value(last_card, card) == card:
        play.append(card)
        possible_plays.append(play)
        play = []
    if possible_plays == []:
      possible_plays = "Pass"
    return possible_plays
  elif play_type == 2:
    #list with duplicates
    duplicates = {}
    #for each card
    for card in current_hand:
      print(card)
      #check if there are any matches
      #print(card)
      #print([x for x in current_hand if x != card])
      not_hand = [x for x in current_hand if x != card]
      print(not_hand)
      for other_card in not_hand:
        if check_num_match(card, other_card):
          duplicates[card] = [card, other_card]
          #print(duplicates[card])
    print(duplicates)
    for duplicate in duplicates:
      # print(f"duplicate of: {duplicate}")
      #print(duplicates[duplicate][0])
      #print(duplicates[duplicate][1])
      largest_value = get_larger_value(duplicates[duplicate][0],
                                       duplicates[duplicate][1])
      last_play_lv = get_larger_value(last_cards_played[0],
                                      last_cards_played[1])
      #if the largest card in the duplicate is larger
      #than the larger card in the duplicate played
      if get_larger_value(largest_value, last_play_lv) == largest_value:
        possible_plays.append(duplicates[duplicate])
    if possible_plays == []:
      possible_plays = "Pass"
    return possible_plays
  elif play_type == 3:
    #list with triplets
    triples = {}
    #duplicates = {}
    #for each card
    for card in current_hand:
      triples[card] = []
      #print(card)
      #check if there are any matches
      #print(card)
      #print([x for x in current_hand if x != card])
      not_hand = [x for x in current_hand if x != card]
      #print(not_hand)
      for other_card in not_hand:
        if check_num_match(card, other_card):
          not_not_hand = [x for x in not_hand if x != other_card]
          # print(card)
          # print(other_card)
          # print(not_not_hand)
          for yet_another in not_not_hand:
            if check_num_match(other_card, yet_another):
              triples[card].append([card, other_card, yet_another])
          #print(triples[card])
    print(triples)
    if last_cards_played == None:
      possible_plays = [triples[x] for x in triples]
      return possible_plays
    for triple in triples:
      print(triples[triple])
      if len(triples[triple]) > 0:
        for triplet in triples[triple]:
          print(triplet)
          #print(possible_plays)
          for i in possible_plays:
            if triplet.sort() == i.sort():
              continue
          largest_value1 = get_larger_value(triplet[0], triplet[1])
          largest_value = get_larger_value(largest_value1, triplet[2])
          last_play_lv1 = get_larger_value(last_cards_played[0],
                                           last_cards_played[1])
          last_play_lv = get_larger_value(last_play_lv1, triplet[2])
          if get_larger_value(largest_value, last_play_lv) == largest_value:
            possible_plays.append(triplet)
    if possible_plays == []:
      possible_plays = "Pass"
    return (possible_plays)
  elif play_type == 5:
    if len(current_hand) < 5:
      return "Pass"
    cardnumdict = {}
    five_card = {}
    five_card["Straight"] = []
    five_card["Flush"] = []
    five_card["Straight-Flush"] = []
    five_card["Four of a Kind"] = []
    five_card["Full House"] = []
    for num in [int(a.split()[0]) for a in current_hand]:
      for suit in [b.split()[-1] for b in current_hand]:
        cardnumdict[num] = ("0" if len(str(num)) == 1 else
                            "") + str(num) + " of " + suit
    print(cardnumdict)
    sortedkeys = sorted(cardnumdict.keys())
    print(sortedkeys)
    sorted_dict = {}
    for i in sortedkeys:
      sorted_dict[i] = cardnumdict[i]
    for card in current_hand:
      straight = []
      left_index = sortedkeys.index(int(
          card.split()[0]))  # get index based on the card
      if left_index == len(current_hand) - 1:
        break
      right_index = left_index + 1
      print(left_index, right_index, sep=", ", end="\n")
      try:
        print(sortedkeys[right_index],
              sortedkeys[left_index],
              sep=" - ",
              end="\n")
      except IndexError:
        break
      while len(straight) < 5:
        try:
          print(sortedkeys[right_index], sortedkeys[left_index])
        except IndexError:
          break
        if sortedkeys[right_index] == sortedkeys[left_index] + 1:
          straight.append(
              cardnumdict[sortedkeys[left_index]])  # add left card to straight
          left_index = right_index  # scoot left over
          right_index += 1
          print(left_index, right_index, sep=", ", end="\n")
          try:
            print(sortedkeys[right_index],
                  sortedkeys[left_index],
                  sep=" - ",
                  end="\n")
          except IndexError:
            break
          # scoot right over
        elif sortedkeys[right_index] == sortedkeys[
            left_index]:  # if there's a repeat card
          right_index += 1  # scoot right over
        else:  # next card is too big
          break
        if (len(straight) == 3) and (sortedkeys[right_index]
                                     == sortedkeys[left_index] + 1):
          straight.append(cardnumdict[sortedkeys[left_index]])
          straight.append(cardnumdict[sortedkeys[right_index]])
          five_card["Straight"].append(straight)
          straight = []
      # check flush
      # check straight-flush
      # check full house
    triples = find_possible_plays(
        ['03 of Diamond', '03 of Heart', '03 of Diamond'],
        play_type=3,
        current_hand=current_hand)
    doubles = find_possible_plays(['03 of Heart', '03 of Heart'],
                                  play_type=3,
                                  current_hand=current_hand)
    for i in triples:
      for j in doubles:
        if doubles in triples:
          break
        else:
          five_card["Full House"].append([i + j])
    # four-of-a-kind + 1 card
    possible_plays.append(five_card)
    if possible_plays == []:
      possible_plays = "Pass"
    return possible_plays


def display_winner(winner_name):
  print(f"{winner_name} wins!")


#shuffles and creates the deck
def create_shuffle_deck():
  deck = []
  suits = ["Diamond", "Club", "Heart", "Spade"]
  numbers = [
      "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "01",
      "02"
  ]
  for i in numbers:
    for j in suits:
      deck.append(i + " of " + j)
  #print(deck)
  random.shuffle(deck)
  #print(deck)
  return (deck)


#create run loop
class Game:

  def __init__(self, deck, players):
    self.deck = deck
    self.players = players
    self.next_player = random.randint(0, 3)
    self.last_card_player = []
    self.consecutive_passes = 0
    self.current_play = None
    self.root = Tk()
    self.root.title("Big Two: A Cantonese Card Game")
    self.root.geometry("700x700")
    self.root.minsize(700, 700)
    self.root.configure(bg="dark red")
    self.possible_plays = []
  def restart(self, deck, players):
    self.deck = deck
    self.players = players
    self.next_player = random.randint(0, 3)
    self.last_card_player = []
    self.consecutive_passes = 0
    self.current_play = None
  def create_widgets(self):
    self.select_play = Button(self.root,text="Play",command=None,font=("Comic Sans MS", 14, "bold"))
    self.lets_pass = Button(self.root,text="Pass",command=None,font=("Comic Sans MS", 14, "bold"))
    self.title_widget = Label(self.root,text="Big Two", font=("Comic Sans MS", 18, "bold"))
    self.canvas = Canvas(self.root,height=620, width=690,bg="#069FA0")
    self.card_back_image = PhotoImage(file="/Users/davidlam/Code/Big-Two/card_back.png")
    self.card_back_image = self.card_back_image.subsample(6,6)
    self.rules_button = Button(self.root, text="Rules", command=show_rules,font=("Comic Sans MS", 14, "bold"))
    self.username_label = ""
    for i in self.players:
      self.username_label += str(i.name) + ", "
    self.username_label = self.username_label[:-2]
    self.username_label = "Players: " + self.username_label
    self.username_label = Label(self.root, text=self.username_label, font=("Comic Sans MS", 14, "bold"),bg="#FFFFFF",fg="#000000")
    self.last_played_card = Label(self.root)
    self.choose_play = ttk.Combobox(self.root,values=self.possible_plays)
    self.exit = Button(self.root,text="Exit",command = exit, font=("Comic Sans MS", 14, "bold"))
    self.player_hand=None 
    # You had written ^^^pass but that's a keyword and cannot be asigned
  def game(self):
    self.create_widgets()
    self.rules_button.grid(column = 0,row=0)
    self.username_label.grid(column = 1,row=0)
    self.exit.grid(column = 2,row=0)
    self.canvas.grid(column = 0,row=1,columnspan=3)
    ToolTip(self.canvas, msg="Play Area",delay = 0.5,follow = True,
        parent_kwargs={"bg": "black", "padx": 3, "pady": 3},
        fg="#ffffff", bg="#1c1c1c", padx=2, pady=2)
    self.card_hands = {"Top_Player":[],"Left_Player":[],"Right_Player":[]}
    for i in range(0,13):
      self.card_hands["Top_Player"].append(self.canvas.create_image(200+20*i,10,anchor=N,image=self.card_back_image))
    for i in range(0,13):
      self.card_hands["Left_Player"].append(self.canvas.create_image(80,110+22*i,anchor=N,image=self.card_back_image))
    for i in range(0,13):
      self.card_hands["Right_Player"].append(self.canvas.create_image(610,110+22*i,anchor=N,image=self.card_back_image))
    print(self.card_hands)
    self.choose_play.grid(column = 1,row=2,columnspan=1,pady=5)
    self.select_play.grid(column=2,row=2,columnspan=1)
    self.lets_pass.grid(column=0,row=2,columnspan=1)
    self.root.mainloop()
    username_label = ""
    self.dealed_deck = deal(self.deck, 4)
    for i in self.players:
      i.hand = self.dealed_deck[self.players.index(i)]
      for card in i.hand:
        pass
    while True:
      self.root.update_idletasks()
      #get play
      self.new_play = self.players[self.next_player].play_card(
          self.current_play, self.last_card_player)
      #check if player passes
      if self.new_play == "Pass":
        #if true, add one to passes
        self.consecutive_passes += 1
      else:
        #otherwise, set the play to the last card played
        self.last_card_player = [self.new_play, self.next_player]
        #if three passes have been done,
        #set the current type of play to none
        #and the next player is the last player to play
      if self.consecutive_passes == 3:
        self.next_player = self.last_card_player[1]
        self.current_play = None
        self.consecutive_passes = 0
        continue
      #check if the player wins or exits
      if check_end(type) == "Win":
        display_winner(self.last_card_player[1])
        break
      elif check_end(type) == "Exit":
        print("Game Exited")
        break
      #finds the next player
      self.next_player = self.next_player + 1
      if self.next_player > 3:
        self.next_player -= 3
    self.root.destroy()

#messagebox.showerror(message="Wha?")
while True:
  player_info = {"Ming Fu": [1, []], "Jiang Kun": [2, []], "Fu Ai": [3, []]}
  print(player_info)
  players = []
  username = str(intro())
  player_info[username] = ["player", []]
  print("here")
  for i in player_info:
    players.append(
        Player(name=i, hand=player_info[i][1], strategy=player_info[i][0]))
  print(players)
  game = Game(create_shuffle_deck(), players=players)
  game.game()
  if not messagebox.askyesno("Replay", "Play again?"):
    break
  else:
    continue
  #intro()
#show_rules()
#
# show_rules()
#print(check_num_match("09 of Spade","09 of Diamond"))
# game = Game(1, 2)
# # if get_larger_value("09 of Spade","10 of Spade"):
# #   print("yay")
# # else:
# #   print("nay")
# parent = Tk()
# parent.title("Image in Tkinter")
# parent.minsize(700, 700)
# # Load the image
# image = PhotoImage(
#     file=
#     "/home/runner/Big-Two-A-Cantonese-Card-Game/Playing Card Images/2_of_spades.png"
# )
# image = image.subsample(3, 3)

# # Create a label to display the image
# image_label = Button(parent, image=image, command=show_rules)
# image_label.pack()

# # Start the Tkinter event loop
# parent.mainloop()

#--------------------------------------------------------------------------------#
#extra Code

# for card in current_hand:
#   five_cards = []
#   # check straights
#   not_hand = [x for x in current_hand if x != card]
#   maybe_play = []
#   for other_card in not_hand:
#     if int(other_card.split()[0]) == int(card.split()[0]) + 1:
#       not_hand = [x for x in not_hand if x != other_card]
#       maybe_play.append(other_card)
#       print(maybe_play)
#       for i in range(0,4):
#         if maybe_play == []:
#           break
#         for a in not_hand:
#           if int(a.split()[0]) == int(maybe_play[-1:].split()[0])+1:
#             not_hand = [x for x in not_hand if x != other_card]
#             maybe_play.append(a)
#             print(maybe_play)
#             break
#           else:
#             break
#   if len(maybe_play) == 5:
#     five_cards.append(maybe_play)
#   print(five_cards)
# More Code:
# counter = 0
# five_card = []
# cardnumdict = {}
# for num in [int(a.split()[0]) for a in current_hand]:
#   for suit in [b.split()[-1] for b in current_hand]:
#     cardnumdict[num] = suit
# print(cardnumdict)
# sortedkeys = sorted(cardnumdict.keys())
# #print(type(sortedkeys))
# print(sortedkeys)
# sorted_dict = {}
# for i in sortedkeys:
#   sorted_dict[i] = cardnumdict[i]
# for card in sorted_dict:
#   for other_card in sorted_dict:
#     if other_card == card + 1:
#       counter += 1
#       print(counter)
#     elif other_card == card:
#       continue
#     else:
#       break

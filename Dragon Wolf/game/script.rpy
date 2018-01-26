﻿# The script of the game goes in this file.

#Character Names
#Main Characters
define n = Character("Nathaniel")
define r = Character("Rockhopper")
define fm = Character("Fish Man")
#Supporting Characters
define p = Character("Pheonyx")
#Extra bitches
define k = Character("Fast Food Worker")
define whomst = Character("???")

# The game starts here.

label start:
    
#################################################################################################################
#Start of Chapter 1
#################################################################################################################

    scene bg black
    
    "Light peeks through the windows as birds chirp outside moving the branches brushing against the window. Nathaniel’s phone alarm rings."
    
    play music "birds chirping.mp3"
    play sound "alarm clock.mp3" fadein .5
    
    n "{i}yawns{/i}"
    
    "Stretching his arms in bed, he reaches for his phone and silences it."
    
    stop sound fadeout 1.0
    
    scene bg bedroom
    with fade
        
    n "What a beautiful morning!~"
    
    n "{i}yawns{/i} I should get ready... or..."

    stop music fadeout 1.0

    scene bg black
    with fade
    
    "The phone lights up and vibrates, “Pheonyx is calling” is displayed on his phone as he stumbles out of bed."
    
    play sound "phone vibrate.mp3"
    
    scene bg bedroom
    with hpunch
    
    n "Shit!... Did I...?"
    
    n "Oh shit! I’m late!"
    
    stop sound
    
    show nate flustered at center
    with easeinright
    
    n "I gotta run to the guild hall! I hope they didn't run out of hunts.."
    
    show nate flustered:
        ease 0.2 offscreenleft
        
    play sound "door shut.mp3"

    "He runs out the house slamming the door behind him rushing his way to the guild hall"
    
#################################################################################################################    
#Guild Hall Scene where Nathaniel picks up hunt slip, introduces Pheonyx    
#################################################################################################################
    
    scene bg guild hall
    with fade
    
    show nate flustered at left
    with easeinleft
    
    n "{i}Breathing Heavily{/i} I-I'm not late... Right..?"
    
    whomst "Someone's Late! Better pick up the last hunt."
    
    show Pheonyx dicks at right
    with easeinright
    
    p "Next time don't be so late buddy~ See you out on the field!"
    
    "She hands Nathaniel, hunched over trying to regain his breath, the last hunt slip."
    
    "He blushes grabbing the slip"
    
    n "Thanks Pheonyx I knew I could count on you."
    
    "She giggles. Winking at him, she runs out the guild hall"
    
    show Pheonyx dicks:
        ease 1.0 offscreenright
        
    n "'Get rid of the great crabs at Blackrock Beach' Well… at least the venue isn’t terrible."
    
    n "This is what I get for sleeping in I guess, off to Blackrock Beach I go..."
    
    show nate flustered at left:
        ease 1.0 offscreenleft

#################################################################################################################
#Blackrock Beach Scene where Nathaniel finds Rockhoppers hot but unconcious body on the floor and brings him home        
#################################################################################################################
        
    scene BlackrockBeachBG
    with fade
    
    show nate normal at left
    with easeinleft
    
    show darksoulscrab at right
    
    "Nathaniel pulls back on the bow launching his arrow slicing through the air and striking down a crab."

    n "Why do these crabs have to be so big?"
    
    "He runs around killing all of the crabs in sight, making them drop to the floor."
    
    scene hop1
    with dissolve
   
    "Amidst the giant crab corpses that litter the shower, a slight glimmer on the shore catches Nathaniel’s eye."

    scene hop2
    with dissolve
    
    n "Is… that a body?"
    
    scene hop3
    with dissolve
    
    "Nathaniel runs over to the the man and shakes the body."
    
    n "Hey! Are you alright?"

    "The fish man opens his eyes and takes a glance at Nathaniel and faints."
    
    n "That’s not good… At least he’s alive so that’s something. I’ll take him home but I can’t do it in this body I hate switching…"

    "owo sound effect"
    
    "Nathaniel transforms into a wolf and howls. He grabs the towering fish dragon thing in his mouth and runs home."
    
#################################################################################################################
# Nate brings Hops home and puts him in his tub to dry him also theres no food so he goes out to [fastfoodname]
#################################################################################################################

    scene bathroom
    with fade
    
    show nate embarassedblush
    
    "Nathaniel lays down the shinning wet body that barely fits in the tub."
    
    n " I hope he doesn’t mind waking up in a bathtub…"
    
    "He is a fish.. I think? Maybe I should fill up the tub just in case."
    
    "He leans over and turns the faucets. Steaming water fills up the tub, unsurprisingly, since the man takes up most of the tub, not a lot of water is needed to completely fill up the tub."
    
    n " I hope he’s okay and okay with waking up wet. He’ll probably be hungry when he wakes up. Who knows how long he’s been knocked out."
    
    scene kitchen
    with dissolve
    
    show nate embarassedblush
   
    "Nathaniel rummages through the cupboards looking for food only finding a bag of chips and and cookie dough mix."
    
    n "There’s no food in this house. I guess I gotta go out and get him something."
    
    "He leaves the house and locks the door"
    
    show nate embarassedblush:
        ease 1.0 offscreenright
        
    n "I hope he'll be fine."
   
########################################################################################################################################################
#Nate goes to [foodplace] and orders food for 2, Pheonyx notices and asks him questions about relationships allowing time for hops to fuck up the house
########################################################################################################################################################  

    scene restaurant
    with fade

    show kuroudick at right
    with easeinright

    show nate normal
    with easeinleft
    
    k "Hi welcome to Bhili's"
    
    n "Can I get uhh..."
    
    whomst "Nate!"
    
    show pheonyx dicks at left
    with easeinleft
    
    p "Hey! How was your mission?~ Find anything interesting?!"
    
    n "{b}{i}Interesting would be an understatement...{/i}{/b}"
    
    n "Oh you know! Same ol' same ol'."
    
    k "Sir... Your order???"
    
    n "Oh! Yeah sorry, my bad. Two big boys please!"
    
    p "{i}Scoffs{/i} Two meals? Someones hungry~"
    
    n "Well actually."
    
    n "Oh! Can I get onion rings for one my big boys?"
    
    k "{i}sigh{/i} Yeah sure whatever. Your total is going to be $69.42"
    
    n "{b}{i}Jeez that’s a lot… but he must be starving.{/i}{/b}"
    
    whomst "Can you stop FUCKING overcharging people just say it's $16.92"
    
    k "Okay fine it's $16.92."
    
    n "{b}{i}Still a lot... Oh well{/i}{/b}."
    
    show kuroudick:
        ease 0.5 offscreenright
        
    show nate normal:
        ease 0.5 right
    
    p "Pheonyx: Soo~ What’s with the two meals..?"

    n "Oh you know... It's for a friend."
    
    p "You're seeing someone?"
    
    show expression "nate embarassedblush" as nate
    
    n "{i}Blush{/i} Nonononoonono!! It's just a friend I swear!"
    
    p "{i}Giggle{/i} I'm just joking buddy. I know you're a single pringle but you should consider looking for someone. You deserve it."
    
    p "Are you at least looking?"
    
    show expression "nate normal" as nate
    
    n "Not at the moment, no. You know me though, I let things come to me"
    
    p "Well you're not gonna get a catch like that! Oh well, you'll find someone I'm sure. I gotta get going I have another hunt slip to finish! I'll see you later!"


    show pheonyx dicks:
        ease 1.0 offscreenleft
        
    n "I guess I should head home now before before the food gets cold. Hopefully he's awake"
 
###################################################################################################################################################################
#Nate hears shit outside the house and it gets fucked so he goes in and notices the house is fucked then meets Rockhopper known only as fish man for the time being
###################################################################################################################################################################

    scene BG House OutsideN
    
    "As Nathaniel approaches the house, loud banging and crashing noises come from the house."
    with hpunch
    
    n "Did someone break in?!"
    
    n "Shit what if he’s hurt!"
    
    "Hastily, he opens up the door and crashes in."
    
    scene HouseFucked
    
    fm "Hello~?"
    
    "The house is a mess, the floor is covered in slime and water. Cracks and holes over the wall, one door frame has a hole in the shape of the fish man’s head. Some of the furniture is displaced, sideways, and upside down."
    
    n "What"
    
    fm "He...llo? Ah- something smells good..."
    
    n "My house…"
    
    fm "You’re that cat from the beach, right?"
    
    "The fish dragon man slides over to Nathaniel to pet him on the head and gives him a hug, nearly suffocating Nathaniel."
    
    n "Please let go. Can’t. Breathe."
    
    show rock confused at left
    with easeinleft
    
    fm "...No good?"
    
    show nate flustered at right
    with easeinleft
    
    n "{i}Cough{/i} You can, but not that hard..."
    
    show expression "rock normal" as rock
    
    fm "Ah- That's right... Where is this?"
    
    show expression "nate confused" as nate
    
    n "Do… you not know where you are?"
    
    show expression "rock sad" as rock
    
    fm "Sorry... It's all fuzzy..."
    
    n "Do you at least know who you are?"
    
    "The fish man begins to look away nervously, tears well up in his eyes"
    
    fm "I-I… can’t remember…"
    
    n "{b}{i}He lost his memories...{/i}{/b}"
    
    "Trying not to slip, Nathaniel goes up to the man and tries to comfort him."
    
    show expression "nate normal" as nate
    
    n "Hey there… Don’t cry. My name’s Nathaniel."
    
    fm "Na-than-ie-a...l?"
    
    n "Yeah don’t worry about the mess we can fix it up."
    
    "Nate grabs his hand and walks him over to the kitchen table."
    
    scene bg kitchen
    
    show nate normal at right
    
    show rock normal at left
    
    n "Here, I got this for you."
    
    "He hands out the big boy meal out of the bag and hands it tot he fish man"

    fm "What is this?"
    
    n "It's a hamburger and french fries."
    
    "Nate pulls out his burger and onion ring and notices the fish man eyeing the onion rings."
    
    show expression "rock happy" as rock
    
    fm "Oh I've got it!"
    
    "He grabs an onion ring and attempts to put it on his wrist breaking it."
    
    fm "Ah-... I was mistaken?"
    
    show expression "nate happy" as nate
    
    n "{i}Chuckle{/i} No~ These are called onion rings, they’re like onions that are fried. You’re thinking of bracelets."
    
    show expression "nate normal" as nate
    
    fm "Then why are they called rings?"
    
    n "Cause they’re shaped like rings"
    
    fm "Ahh~ That makes sense."
    
    scene bg kithen
    with fade
    
    show rock happy at left
    show nate normal at right
    
    fm "That was so good!~"
    
    n "Well that's good to hear. Do you know how long you were knocked out for?"
    
    show expression "rock normal" as rock
    
    fm "I’m not sure… I can remember… the trees being orange? Yes- that's right, they must have just started to turn on the mainland."
    
    show expression "nate concerned" as nate
    
    "Nathaniel, drinking on his cup of soda, spits a bit out and starts to cough."
    
    fm "Is there something wrong?"
    
    n "No, it’s nothing just my drink went down the wrong pipe."
    
    n "{b}{i}If he got knocked out when the trees were changing colors then he got knocked out during Fall, it’s fucking Spring now.{/b}{/i}"
    
    n "Also what do you mean about the mainland?"
    
    fm "Ah well-... The largest island...? It was dry I did not like it… I remember spending most of my time in the ocean."
    
    n "{b}{i}So he is a fish… thing… person…{/b}{/i}"
    
    n "Well I don’t want you getting hurt so you can stay with me until you start remembering stuff again. First things first we need to fix up the house, then we can give you a good bath."
    
    show expression "rock happy" as rock
    
    fm "Thats sounds fun! Can we do it together?"
    
    show expression "nate embarassedblush" as nate
    
    "Nathaniel’s eyes opened wide as his cheeks lit up like lights on a Christmas tree. He turned away covering his face and coughing."
    
    n "{b}{i}Fuck{/b}{/i}"
    
    n "N-Nonono! I mean like you can take a bath yourself, and stuff."
    
    n "Anyways what happened when I was gone this place looks like it was wrecked."
    
    scene hop1
    with slideup
    
    fm "Well.. I woke up confused, so I figured I would check out my surrounds… but the ground wasn't like sand or the rock so it took me some time to get my footing..."
    
    scene hop2
    with slideleft
    
    fm "There was some creature… It was so small, I wanted to ask it a question but it got away from me"
    
    scene hop3
    with slideleft
    
    fm "Ah-! I found some books with pictures in them I thought they would help me figure out where I’d ended up..."
    
    n "{b}{i}They better have not been…{/b}{/i}"
    
    fm "...It’s nice to see people in love but I’m still confused what they were doing and what all that mi-"
    with vpunch
    
    n"OOOKAY. Don’t worry about those books let’s get to cleaning."
    
    scene bg house
    with fade
    
    n "{i}yawn{/i} That took a bit. Now that bath I promised you!"
    
    scene cg bath1
    
    n "Use this knob to turn on the hot water and use this one to turn on the cold water. Make sure you don't just put in hot water because it’ll burn you. Then use the soap over there to wash yourself"
    
    scene cg bath2
    with vpunch

    "Nate leans over the tub attempting to grab the soap, slipping into the tub. The fish man catches him and giggles and Nate’s face turns as red as a tomato."
    
    n "S-Sorry about t-that."
    
    fm "It’s okay Na-than-e-ale cat."
    
    n "I’m not a cat, I’m a werewolf."
    
    fm "Na-than-ieal pup?"
    
    n "{i}yawn{/i} The water is so warm. It’s nice."
    
    fm "Your a good dog, you’ve earned your rest haven’t you?"
    
    n "{i}yawn{/i} I did didn’t I? I gotta get… to bed…"
    
    "Nate’s eyes began to close as he yawned from exhaustion. He leaned over in the water as if he was going to get out but fell asleep. The fish man noticing this, picked up the werewolf and placed him on his stomach and pet Nate’s head as he also fell asleep."
    
 
    return
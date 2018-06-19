# The script of the game goes in this file.

#Character Names
#Main Characters
define n = Character("Nathaniel", color = "#1AA9E3")
define r = Character("Rockhopper", color = "#2EDFD7")
define fm = Character("Fish Man", color = "#2EDFD7")
#Supporting Characters
define t = Character ("Tita", color = "#CB2D2D")
define p = Character("Pheonyx", color = "#9DD633")
define k = Character("Kurou", color = "E1783B")
define a = Character("Apollo")
#Extra bitches
define fastfood = Character("Fast Food Worker", color = "E1783B")
define whomst = Character("???", color = "#CACACA")

#Choice Variable, determinds your standing with the big boy
define pathNum = 0


# The game starts here.

label start:
    
###########################################################################################################################################################################
###########################################################################################################################################################################
#Start of Chapter 1
#################################################################################################################

    scene cg chapter1
    
    pause 3.0
    
    scene bg black
    with fade
    
    "Light peeks through the windows as birds chirp outside moving the branches brushing against the window. Nathaniel's phone alarm rings."
    
    play music "birds chirping.mp3"
    play sound "alarm clock.mp3" fadein .5
    
    n "{i}yawns{/i}"
    
    "Stretching his arms in bed, Nate reaches for his phone and silences it."
    
    stop sound fadeout 1.0
    
    scene bg bedroom
    with fade
        
    n "What a beautiful morning!~"
    
    n "{i}yawns{/i} I should get ready... or..."

    stop music fadeout 1.0

    scene bg black
    with fade
    
    "The phone lights up and vibrates, 'Pheonyx is calling', he stumbles out of bed."
    
    play sound "phone vibrate.mp3"
    
    scene bg bedroom
    with hpunch
    
    n "Shit!... Did I...?"
    
    n "Oh shit! I'm late!"
    
    stop sound
    
    show nate flustered at center
    with easeinright
    
    n "I gotta run to the guild hall! I hope they didn't run out of hunts.."
    
    show nate flustered:
        ease 0.2 offscreenleft
        
    play sound "door shut.mp3"

    "He runs out the house slamming the door behind him rushing his way to the guild hall."
    
#################################################################################################################    
#Guild Hall Scene where Nathaniel picks up hunt slip, introduces Pheonyx    
#################################################################################################################
    
    scene bg guildhall
    with fade
    
    show nate flustered at left
    with easeinleft
    
    n "{i}Breathing heavily{/i} I-I'm not late... Right..?"
    
    whomst "Someone's Late! Better pick up the last hunt."
    
    show Pheonyx dicks at right
    with easeinright
    
    p "Next time don't be so late puppy!~"
    
    "She hands Nate, hunched over trying to regain his breath, the last hunt slip."
    
    "Nate blushes grabbing the slip"
    
    n "Thanks Pheonyx, I knew I could count on you."
    
    "She giggles. Pheonyx winks and walks out the door."
    
    show Pheonyx dicks:
        ease 1.0 offscreenright
        
    n "'Hunt the great crabs at Blackrock Beach!' Well, at least the venue isn't terrible."
    
    n "That's what I get for sleeping in... off to the beach I go..."
    
    show nate flustered at left:
        ease 1.0 offscreenleft

#################################################################################################################
#Blackrock Beach Scene where Nathaniel finds Rockhoppers hot but unconcious body on the floor and brings him home        
#################################################################################################################
        
    scene bg beach
    with fade
    
    show nate normal at left
    with easeinleft
    
    show crab at right
    
    "Nate pulls back on the bow launching his arrow striking down a crab."

    n "Why do these crabs have to be so big?"
    
    "He runs around killing all of the crabs in sight."
    
    scene cg hopStory1
    with dissolve
   
    "Amidst the giant crab corpses, a slight glimmer on the shore catches Nate's eye."

    scene cg hopStory2
    with dissolve
    
    n "Is... that a body?!"
    
    scene cg hopStory3
    with dissolve
    
    "Nathaniel runs over to the the man and shakes the body."
    
    n "Hey! Are you alright?"

    "The fish man opens his eyes and takes a glance at Nathaniel and faints."
    
    n "That's not good. At least he's alive so that's something."

    "Nate tugs at the body but can't seem to move him."
    
    n "Fuck he's heavy... I don't think I'd be able to carry him."
    
    n "I don't want to turn... but it's an emergency."
    
    "owo sound effect"
    
    "Nate transforms into a wolf and howls. He places the fish thing on his back and runs off."
    
#################################################################################################################
# Nate brings Hops home and puts him in his tub to dry him also theres no food so he goes out to [fastfoodname]
#################################################################################################################

    scene bg bathroom
    with fade
    
    show nate embarassedblush
    
    "Nate lays down the wet body that barely fits in the tub."
    
    n "I hope he doesn't mind waking up in a bathtub..."
    
    "He's a fish I think. Maybe I should fill up the tub just in case."
    
    "Nate leans over and turns the faucets. Steaming water fills up the tub within a couple of minutes."
    
    n "I hope he's okay and okay with waking up wet. He'll probably be hungry when he wakes up. Who knows how long he's been knocked out."
    
    scene bg kitchen
    with dissolve
    
    show nate embarassedblush
   
    "Nate rummages through the cupboards looking for food only finding a chips and and cookie dough mix."
    
    n "This fucking idiot forgot to buy food again."
    
    n "I guess I gotta go out and get him something."
    
    "He goes out the house and locks the door."
    
    show nate embarassedblush:
        ease 1.0 offscreenright
        
    n "I hope he'll be fine."
   
########################################################################################################################################################
#Nate goes to [foodplace] and orders food for 2, Pheonyx notices and asks him questions about relationships allowing time for hops to fuck up the house
########################################################################################################################################################  

    scene bhilis inside
    with fade

    show kurou normal at right
    with easeinright

    show nate normal
    with easeinleft
    
    fastfood "Hi welcome to Bhili's"
    
    n "Can I get uhh..."
    
    whomst "Nate!"
    
    show pheonyx dicks at left
    with easeinleft
    
    p "Hey! How was your hunt?~ Find anything interesting?!"
    
    n "{b}{i}Interesting would be an understatement...{/i}{/b}"
    
    n "Oh you know! Same ol' same ol'."
    
    fastfood "Sir... your order???"
    
    n "Oh! Yeah sorry, my bad. Two big boy meals please!"
    
    p "{i}Scoffs{/i} Two meals? Someones hungry!~"
    
    n "Well actually-"
    
    n "Oh! Can I get onion rings for one my big boys?"
    
    fastfood "{i}sigh{/i} Yeah sure whatever. Your total is going to be $69.42"
    
    n "{b}{i}Jeez that's a lot... but he must be starving.{/i}{/b}"
    
    whomst "Can you stop FUCKING lying to people, it's $16.92"
    
    fastfood "Okay fine it's $16.92."
    
    n "{b}{i}Is this what it feels like to pay for two people?{/i}{/b}."
    
    show kurou normal:
        ease 0.5 offscreenright
        
    show nate normal:
        ease 0.5 right
    
    p "Pheonyx: Soo~ What's with the two meals..?"

    n "Oh you know... It's for a friend."
    
    p "You're seeing someone, aren't you~"
    
    show expression "nate embarassedblush" as nate
    
    n "{i}Blushes{/i} Nonononoonono!! It's just a friend I swear!"
    
    p "{i}Giggles{/i} I'm just joking buddy. I know you're a single pringle but you should consider looking for someone. You deserve it!~"
    
    n "T-Thanks."
    
    p "Are you at least looking?"
    
    show expression "nate normal" as nate
    
    n "Not really. You know me though, I let things come to me."
    
    p "Well you're not gonna get a catch like that! Oh well, you'll find someone I'm sure. I gotta get going I have another hunt slip to finish! I'll see you later!"

    show pheonyx dicks:
        ease 1.0 offscreenleft
        
    n "I guess I should head home now before before the food gets cold. Hopefully he's awake"
 
###################################################################################################################################################################
#Nate hears shit outside the house and it gets fucked so he goes in and notices the house is fucked then meets Rockhopper known only as fish man for the time being
###################################################################################################################################################################

    scene bg houseOutN
    
    "Loud noises and crashing come from the house as he approaches it."
    
    with hpunch
    
    n "Did someone break in?!"
    
    n "Shit what if he's hurt!"
    
    "Hastily, he opens up the door and crashes in."
    
    scene bg houseFucked
    
    fm "Hello~?"
    
    "The house is a mess, the floor is covered in slime and water. Cracks and holes over the wall, one door frame has a hole in the shape of the fish man's head. Some of the furniture is upside down."
    
    n "Wh-"
    
    fm "He...llo? Ah~ something smells good..."
    
    n "My house..."
    
    fm "You're that cat from the beach, right?"
    
    "The fish dragon man slides over to Nathaniel to pet him on the head and gives him a hug, nearly suffocating Nate."
    
    n "Please. Let. Go. Can't. Breathe."
    
    show rock confused at left
    with easeinleft
    
    fm "...No good?"
    
    show nate flustered at right
    with easeinleft
    
    n "{i}Coughs{/i} You can, but not that hard..."
    
    show expression "rock normal" as rock
    
    fm "Ah- That's right... Where is this?"
    
    show expression "nate confused" as nate
    
    n "Do... you not know where you are?"
    
    show expression "rock sad" as rock
    
    fm "Sorry... It's all fuzzy..."
    
    n "Do you at least know who you are?"
    
    "The fish man begins to look away nervously, tears well up in his eyes"
    
    fm "I-I... can't remember..."
    
    n "{b}{i}He lost his memories didn't he...{/i}{/b}"
    
    "Nate goes up to the man and tries to comfort him."
    
    show expression "nate normal" as nate
    
    n "Hey there... Don't cry. My name's Nathaniel, most people call me Nate."
    
    fm "Na-than-ie-a...l?"
    
    n "Yeah don't worry about the mess we can fix it up."
    
    "Nate grabs his hand and walks him over to the kitchen table."
    
    scene bg kitchen
    
    show nate normal at right
    
    show rock normal at left
    
    n "Here, I got this for you."
    
    "He hands out the big boy meal out of the bag and hands it to the fish man"

    fm "What is this?"
    
    n "It's a hamburger and french fries."
    
    "Nate pulls out his burger and onion ring and notices the fish man eyeing the onion rings."
    
    show expression "rock happy" as rock
    
    fm "Oh I've got it!"
    
    "He grabs an onion ring and attempts to put it on his wrist breaking it."
    
    fm "Ah-... I was mistaken?"
    
    show expression "nate happy" as nate
    
    n "{i}Chuckle{/i} No~ These are called onion rings, they're like onions that are fried. You're thinking of bracelets."
    
    show expression "nate normal" as nate
    
    fm "Then why are they called rings?"
    
    n "Cause they're shaped like rings"
    
    fm "Ahh~ That makes sense."
    
    scene bg kitchen
    with fade
    
    show rock happy at left
    show nate normal at right
    
    fm "That was so good!~"
    
    n "Well that's good to hear. Do you know how long you were knocked out for?"
    
    show expression "rock normal" as rock
    
    fm "I'm not sure... I can remember... the trees being orange? Yes~ that's right, they must have just started to turn on the mainland."
    
    show expression "nate concerned" as nate
    
    "Nate spits a bit of soda out and starts to cough."
    
    fm "Is there something wrong?"
    
    n "No, it's nothing just my drink went down the wrong pipe."
    
    n "{b}{i}If he got knocked out when the trees were changing colors then he got knocked out during Fall, it's fucking Spring now.{/b}{/i}"
    
    n "Also what do you mean about the mainland?"
    
    fm "Ah well-... The largest island...? It was dry I did not like it... I remember spending most of my time in the ocean."
    
    n "{b}{i}So he is a fish... thing, person?{/b}{/i}"
    
    n "Well I don't want you getting hurt so you can stay with me until you start remembering stuff again. First things first we need to fix up the house, then we can give you a good bath."
    
    show expression "rock happy" as rock
    
    fm "Thats sounds fun! Can we do it together?"
    
    show expression "nate embarassedblush" as nate
    
    "Nathaniel's eyes opened wide as his cheeks lit up like lights on a Christmas tree. He turned away covering his face and coughing."
    
    n "{b}{i}Fuck{/b}{/i}"
    
    n "N-Nonono! I mean like you can take a bath yourself, and stuff."
    
    n "Anyways what happened when I was gone this place looks like it was wrecked."
    
    scene cg hopHousefb1
    with slideup
    
    fm "Well.. I woke up confused, so I figured I would check out my surrounds... but the ground wasn't like sand or the rock so it took me some time to get my footing..."
    
    scene cg hopHousefb2
    with slideleft
    
    fm "There was some creature... It was so small, I wanted to ask it a question but it got away from me"
    
    scene cg hopHousefb3
    with slideleft
    
    fm "Ah-! I found some books with pictures in them I thought they would help me figure out where I'd ended up..."
    
    n "{b}{i}They better have not been...{/b}{/i}"
    
    fm "...It's nice to see people in love but I'm still confused what they were doing and what all that mi-"
    with vpunch
    
    n"OOOKAY! Don't worry about those books let's get to cleaning."
    
    scene bg house
    with fade
    
    n "{i}Yawns{/i} That took a bit. Now that bath I promised you!"
    
    scene cg bath1
    
    n "Use this knob to turn on the hot water and use this one to turn on the cold water. Make sure you don't just put in hot water because it'll burn you. Then use the soap over there to wash yourself"
    
    scene cg bath2
    with vpunch

    "Nate leans over the tub attempting to grab the soap, slipping into the tub. The fish man catches him and giggles and Nate's face turns as red as a tomato."
    
    n "S-Sorry about t-that."
    
    fm "It's okay Na-than-e-ale cat."
    
    n "I'm not a cat, I'm a werewolf."
    
    fm "Na-than-ieal pup?"
    
    n "{i}Yawns{/i} The water is so warm. It's nice."
    
    fm "Your a good dog, you've earned your rest haven't you?"
    
    n "{i}Yawns{/i} I did didn't I? I gotta get... to bed..."
    
    "Nate's eyes began to close as he yawned from exhaustion. He leaned over in the water as if he was going to get out but fell asleep. The fish man noticing this, picked up the werewolf and placed him on his stomach and pet Nate's head as he also fell asleep."
    
    jump chapter2
    
###########################################################################################################################################################################
###########################################################################################################################################################################
######################################################################
# Chapter 2 Start / Nate Wakes up from a sleep
######################################################################
label chapter2:
    
    scene cg chapter2:
    with Fade(3.0, 1.0, 0.5)
    pause 3.0
    
    scene bg bathroom
    with hpunch

    show nate tired at left
    
    show rock happy at right

    #play sound water splash

    "Nate wakes up on the fish man's stomach, with it gently patting his head."

    fm "Good puppy!~"

    n "Fuck... How long was I?"

    fm "The sun is up now... So..."

    n "Great I slept on him..."

    "Their stomach rumbles."

    n "We should go get some food."

    n "Shit that's right we don't have any food in the house..."

    n "Hey fish- I mean buddy, I'm gonna go out to do some grocery shopping and get us some food."

    fm "Can I come?!"

    n "Sure, just don't do anything weird."

    fm "Like... What?"

    n "Try not to break things for starters."
    
    fm "Got it!"

    "They both get ready to leave the house. Nate gets his bags and shuts the for behind them."

######################################################################
# Grocery Store Scene Dick Jokes haha
######################################################################

    scene bg grocery outside

    show nate normal at left

    show rock normal at right

    n "So this is a grocery store."

    show expression "rock confused" as rock

    fm "Gros...sssy store?"

    n "{b}{i}Close enough...{/i}{/b}"

    n "Yeah you buy food and stuff from here"

    fm "Like.... Oh nyan rings?"

    n "Kinda, you buy stuff to make onion rings."

    show expression "rock happy" as rock

    fm "Ooh!~"

    n "Maybe we'll be able to find something you might like in here or something may jog your memory."

    scene bg grocery vegetables
    with slideright

    show rock normal at right

    "The fish grabs a bundle of broccoli from the stands."

    fm "Note o'neil! Look at this tiny tree!"

    show nate normal at left
    with easeinleft

    n "That's not a tree buddy, that's called broccoli. They're really good, do you want me to cook some for you?"

    fm "Oooh! Yes please!"

    "The fish grabs a eggplant from the stand and compares it with Nate"

    fm "Natmeal, I remember seeing this in your books the man shoved in the girl's-."

    show expression "nate blush" as nate

    "He looks at the man comparing him with the eggplant as he blushes and grabs it from him."

    n "O-oh, uh these are eggplants! I can cook them with the broccoli if you want."

    fm "So it's not something you put in a g-"

    n "Nononono! It's really good I'll show you when we get home!"

    n "I think that's enough vegetables. Let's go to the fruit section to get some snacks!~"

    scene bg grocery fruits
    with slideright

    show rock happy at right

    fm "DICK!"

    show nate embarrassed at left
    with easeinleft

    "The fish points at the fruit basket with a banana and strawberries at it's base."

    fm "Natanael look! It's like your boo-"

    "Nate runs over with his face bright red attempting to cover the fish's mouth and leans in to whisper to him."

    n "Don't say dick in public! It's bad!"

    "He muffles through his hand as Nate moves his hand away."

    fm "But it looks like a dick! Want to check mine?"

    "An image of a hamster eating a banana pops into Nate's head"

    n "Nonononono! It's okay I know how they look like."

    fm "Why do you always do that?"

    n "Do what...?"

    fm "Your face is always turns red."

    n "I'm not... sure either... haha..."

    fm "Haha!~"

    n "Do... you want that though, the thing shaped like the..."

    fm "What are they?"

    n "The long yellow thingy is called a banana and the small red things are called strawberries."

    n "You can use them to make things called smoothies."

    fm "Smoothly?"

    n "Yeah they're really good!"

    fm "If it's good!~"

    n "Okay that should be good for fruits. We should probably get some meat."

    scene bg grocery meats
    with slideright
    
    show rock normal at right

    show nate normal at left

    "They walk into the meat aisle, bustling with butchers cutting and moving the lumps of meat around."

    fm "Nathoniel listen! It's like what the noise from your books!"

    n "{b}{i}Why does he keep talking about the god damn....{/i}{/b}"

    fm "Is this what they mean by, 'Beating your meat'?"

    n "N-nono... That's uh... something else."

    fm "Then what does bea-"

    n "I'll tell you when we get home!"

    show expression "rock confused" as rock

    "Nate eyes a pack of steaks and grabs while the fish tilts his head in confusion."

    fm "Are... you going to beat it or are we going to beat it together?"

    show expression "nate flustered" as nate

    "Nates tomato red face looks at him as he tilts his head like a confused puppy."

    n "Don't worry about it for now! I'll show you what it means later!"

    fm "I can't wait to see you beat meat!"

    n "I-I mean tell you!"

    fm "No show?"

    n "N-no..."

    n "A-anyways I think we have all the food we need, I'll go grab some stuff for the bathtub."

    "Nate runs out of the meat section and grabs the remaining items of his list then they both head to the checkout."

    scene bg grocery checkout
    with Dissolve (1.0)

    show tita normal at left
    with easeinleft

    show nate normal at center
    with easeinright

    show rock normal at right

    with easeinright

    t "Oh~ Nate how are you today?~"

    n "Good Tita! How about you?"

    "Tita leans in and points at the fish and whispers to Nate."

    t "Hay naku(Oh dear)! Nate he your boyfriend diba(right)?"

    n "N-no its a long story Tita..."

    t "Bakit ganon(Why is that)? He is very handsome!"

    "She leans back and looks at the fish man."

    t "Sir are you Nate's boyfriend?"

    fm "Well Natangle is a boy and he calls me buddy a lot so... Yeah! I am Nate's boyfriend!"

    "Tita laughs." 

    t "I see! My name is Tita what is your name sir?"

    fm "Uh... I don't know..."

    "Nate leans in and whispers to Tita."

    n "Tita I think my friend lost his memories so I'm taking care of him until he remembers them."

    t "Anyare(What happened)?"

    n "I'm not sure really I found him washed up on the beach."

    "He grabs the fish man's hands."

    n "Hey don't worry about your name buddy in sure you'll remember it soon."

    t "Anak it will be $53.70!"

    #play sound card reader beep

    "Nate pays with his card causing the card reader to beep, startling the fish man."

    fm "Nat!"

    "He grabs Nate close shaking slightly."

    n "Oh it's a card reader it's how I pay for my stuff. Can you grab our bags for me?"

    "The fish nods and walks over to the full bags and picks them up effortlessly."

    t "Good bye boys!~"

    n "Bye Tita!~"

    fm "Bye ma'am!"

    show nate normal:
            ease 1.0 offscreenleft

    show rock normal:
            ease 1.0 offscreenleft

    "As they leave Tita waves goodbye and looks at the whispers to herself."

    "They are so cute together!~ Sayang (What a waste) they make a good couple."
######################################################################
# Apollo Encounter / Bhili's Encounter / Kurou Encounter / Rockhopper gets his name
######################################################################
   
    scene bg bhilis outside
    with Dissolve (1.0)

    show nate normal at left
    show rock normal at right

    "Their stomach growls on the way home."

    r "My tummy hurty..."    

    n "You know, I'm not gonna lie buddy I'm kinda hungry and I'm too lazy to cook..."
    
    r "What then?"

    n "Do you want burgers? We're in front of the Bhili's."

    r "Oh!~ Nyan rings?"

    n "We can get those too. Come on lets go get food."
    
    scene bg bhilis inside
    with dissolve

    show nate normal at center
    show rock normal at left

    fastfood "Hi Welcome to Bhili's!"

    show kurou normal at right
    with easeinright

    fastfood "Hey I remember you from yesterday!"
    
    n "O-Oh you did?"

    fastfood "Yeah you ordered two meals right? For your boyfriend I assume?"

    "He raiply raises and lowers his eyebrows really fast looking at the fish man."

    show expression "nate flustered" as nate

    "Nate looks away embarrassed and begins to stumble on his words."    
    
    n "W-Wait no."

    fastfood "Isn't it?"
    
    "The fast food worker leans in and places his hand at the bottom his chin and turns his head towards him."

    fastfood "Or... Do you have someone else in mind?"
    
    n "hhhhhhhhh-"

    "Nate's face lights up red as he stares into the eyes of the fast food worker."

    fastfood "Nah I'm just kiddin! What can I get ya?"

    n "Can I-I g-get uhhh...."
    
    fm "On you rings!"
    
    fastfood "On me whats?"

    show expression "nate normal" as nate

    n "Onion rings, he means onion rings."

    fm "Yeah that!"

    fastfood "Oookay..."

    n "Can you get us 2 big boy meals? Please?"

    fastfood "Of course! That'll be $42.30!"

    n "Wha-"

    fastfood "Nah I'm just joking!~ Your order will be with you shortly!"

    n "Thanks uhh..."

    k "Kurou, name's Kurou."

    n "Nice to meet you! Name's Nate."
    
    k "Nice name Nate, see you around!"
    
    show kurou normal:
        ease 1.0 offscreenright

    "They take a seat table waiting for their order."
     
    "Nate notices someone staring at them."

    show expression "nate concerned" as nate
    
    n "Hey buddy."
    
    fm "Yes Noot?"

    n "I think... Someone's staring at you."

    fm "Do I look that nice?"

    "The man gets up from his table and walks towards them."

    n "Uh... Can I he-"

    show apollo normal at right
    with easeinright

    whomst "I see you're one of THOSE dragons yes?"

    "He leans over and props his head up on the table with his arm and points at the fish man."

    whomst "THE dragons from the Great Barrier Reef yes?"
    
    show expression "rock confused" as rock

    fm "Me?"

    whomst "Yes!"

    fm "The great bingo reed?"

    whomst "I assume you HAVE been there before correct?"

    fm "Can't say I remember!"

    n "Excuse me sir ca-"

    whomst "Look BUCKO I know a rock hopper dragon when I see one."

    n "Wait you know what he is?"

    whomst "Of course I know what he is why?"

    fm "Rock... Hopper..?"

    "The fish looked at the man."

    show expression "rock happy" as rock

    r "That's who I am! I'm Rockhopper!"

    whomst "Wait no-"

    r "Nat! That's who I am Rockhopper!"
    
    n "If you want to be called that buddy then sure! Rockhopper it is!"
    
    whomst "Wai-"

    r "Do you hear that sir?! My name is Rockhopper!"

    a "Actually, my name is Apollo."

    k "Hey Nate your food's ready!"

    n "Hey Rockhopper, would you mind picking up the food for us?"

    r "Anything for you Nate!"

    show rock normal:
        ease 1.0 offscreenright

    n "Apollo right? What do you know about Rockhopper?"

    a "Anything really."

    n "So what exactly is he?"

    a "From the looks of it he's a Rockhopper dragon, most of them live in the Great Barrier Reef."

    n "Like, the one in Australia?"

    a "No the one in Canada, of course the one in Australia you imbecile."

    n "{b}{i} So those months he was missing... {/i}{/b}"

    n "Sorry about my friend, he lost his memory so he doesn't remember much."

    a "Really? Interesting... Not even his own name I suppose?"

    n "Yeah..."

    r "Nate!"

    a "Look I'd love to talk to you more cutie but I have to leave soon, boo is waiting for me. Give me your phone I'll add myself as a contact."

    "Nate hands Apollo his phone as he adds himself as a contact."

    a "See you around hot stuff!"

    show apollo normal:
        ease 1.0 offscreenleft

    n "Wh.."

    show rock happy:
        ease 1.0 left

    r "Our food!"

    "He plops the food down at the table and begin to eat."

######################################################################
# Scene Where nate gets fucking beat up
######################################################################
    #Hey make sure to look this over I'm not really sure if this is in character at all but he just fucking goes crazy and almost kills these people so let me know if it's any good.

    scene bg bhilis back
    with dissolve

    n "I think this is a good short cut home..."

    show nate worried at center
    with easeinleft

    n "Rockhopper?"

    n "{i}{b} Shit I lost him {/i}{/b}"

    whomst "What ya doin alone here kiddo?"

    "A sketchy man comes out from behind a dumpster"

    show criminal1 at right
    with easeinright    

    n "W-Walking home...?"

    whomst "All alone?"

    show criminal2 at left
    with easeinleft

    n "N-No..."

    whomst "Doesn't look like it."

    "One of them pulls out a knife."

    n "L-Leave me alone."

    whomst "Give us your money kid and we'll leave you alone."

    n "Fuck off!"

    whomst "What the fuck did you just say?"

    "He swings and makes a long cut on Nate's chest. Nate staggers back and falls on the ground."

    show expression "nate tears" as nate

    whomst "What the FUCK did you just say?"

    "They begin to kick Nate on the floor and Nate's eyes begin to well in tears"

    "A figure appears at the end of the street, unnoticed by the criminals, it comes closer."

    whomst "Well are you going to give us your FUCKIGN money or do you want another scar?"

    r "Leave Nate alone."

    "He grabs the heads of one of the criminals and throws him against the wall"
    
    show criminal2:
        ease 0.4 offscreenleft

    n "Rockhopper..."

    "The other one attempts to swing the knife at Rockhopper but is stopped as he grabs his arm."

    whomst "What the-"

    "Rockhopper breaks his arm and walks to Nate with the other criminal running away screaming."

    show criminal1:
        ease 0.4 offscreenright

    show rock angry at left
    with easeinleft

    r "Hurt?"

    n "A-A bit..."
    
    "He picks up Nate and puts him on his shoulders."
    
    show kurou normal at right
    with easeinright

    "The door of the back of the Bhili's opens."

    show expression "kurou surprised" as kurou

    k "Woah holy shit I was gonna take a break."

    n "H-Hey."
    
    k "Nate! Are you alright?"

    n "Y-Yeah... Rockhopper saved my ass."

    k "So Rockhopper is the name is it?"

    r "Yeah."

    k "You want me to call 911? But I'm on break and I'm not really forced to be nice to you anymore. {i} Chuckles {/i}"

    k "I'm just jokin'! Get home safe cuties."

    r "Of course Kangaroo!"

######################################################################
# Nate and Hops go home romance time
######################################################################

    scene bg black

    "Nate passed out on Rockhopper on the way home."

    scene bg house outside

    "Nate wakes up slowly."

    n "Argh...."

    "He looks down as his shirt covered in blood."

    r "Okay...?"

    n "N-Not really... L-Lets go inside..."

    scene bg house inside
    with fade

    show nate w normal at right

    show rock normal at left

    "Nate takes off his clothes and bandages himself up."
    
    n "Hey... Rockhopper..."

    menu:

        "Kiss him":
            jump chapter2lust
    
        "I just wanted... to say thanks.":
            jump chapter2true

        "You didn't have to break his arm.":
            jump chapter2bad

#####################################################################
# CHOICE?
######################################################################

label chapter2lust:
    
    $ pathNum += 1

    show expression "nate w blush" as nate

    n "H-Hey... C-Can you get down a bit?"

    "Nate walks over to Rockhopper blushing."

    "He closes his eyes and leans in for a kiss on the lips with Rockhopper."

    show expression "rock blush" as rock

    "Luckily, remembering something from those books, Rockhopper picks him up and places him on the table returning the kiss."

    "Nate stops pulling back with a trail of slime connecting their loops together"

    n "It's so slimey."

    r "O-Oh?"

    n "It tastes weird."

    "Nate laughs and soon after Rockhopper joins him."

    n "L-Let's go get some sleep okay?"

    jump chapter2end

label chapter2bad:
    
    $ pathNum -= 1

    show expression "nate w angry" as nate

    n "You didn't have to break his arm you know..."

    r "But... he hurt Nate..."

    n "Yeah he cut me, he didn't kill me. I didn't even need your help."

    show expression "rock sad" as rock

    "Rockhopper looks down in disappointment."

    n "Look... I don't mean to be too harsh or anything just try not to go overboard okay..."

    "He walks to Rockhopper to give him a hug."

    n "Look lets go to sleep okay?"

    jump chapter2end

label chapter2true:

    n "I just wanted to say thanks..."

    r "Thank... for... what?"

    n "For helping me out... from those people."

    r "Why don't you hurt them?"

    n "I don't like hurting other people... Even if they wanted to hurt me..."

    r "That thinking can kill."

    n "I know... but thanks again."

    r "Anything for Nate!~"

    "Rockhopper walks over to hug Nathaniel, squeezing against the bandages."

    n "Too... hard... Ow fuck it stings."

    r "Oops! Sorry Nate~"

    "Nate giggles"

    n "Its late, we should get some sleep."

    jump chapter2end

label chapter2end:

    r "Okay~"

    "He walks towards the bathroom."

    n "You don't have to sleep theres Hops, here follow me."

    scene bg bedroom
    with moveinright
        
    r "Oooh!"

    "He jumps on the bed, practically taking up the queen sized matress by just himself."

    show rock happy at right
    with easeinleft

    pause 1.0

    show natenormal at left
    with easeinleft

    n "Someone's a big boy."

    r "Aaahh~ So comfy!~"

    r "So..."

    "He falls asleep in an instant."

    n "I guess that's how I'd feel if I drifted in the ocean for months..."

    n "{i}Yawns{/i} Time to sleep with him... in my bed... heh..."

    "He crawls into bed with the little space he has and pulls over the blanket onto both of them."

    n "Night Hops..."

    "Nate wraps one arm around Rockhopper and then, unconsciously, Rockhopper hugs Nate in return."

    scene bg black
    with Fade(3.0, 3.0, 0.5)

###########################################################################################################################################################################
###########################################################################################################################################################################
#Chapter 3 Start / Nate wakes up on Rockhopper owo
######################################################################

label chapter3:

    scene cg chapter3:
    with Fade(3.0, 1.0, 0.5)
    pause 3.0
    
    scene bg bedroom
    with hpunch

    show nate concerned at left
    n "ROCKHOPPER!"

    show rock confused at right

    r "Y-Yes?"
    
    "Nate wakes up sweaty on top of Rockhopper as if he picked up Nate and placed him on top of him when he was asleep."

    show expression "rock happy" as rock

    r "{i}Giggles{/i} Nate so strange."

    n "S-Sorry..."

    r "Hmm...."

    n "Y-Yeah...?"

    r "Wet.... Like.... Bathtub.... How?"

    n "I... had a bad dream..."

    r "Made noises when sleepy."

    n "Yeah..."

    r "You say my name when sleepy?"

    n "D-Did I?"

    r "Yeah! It was cute!~"

    n "{b}{i} Shit did I really... {/b}{/i}"

    n "W-We should get out of bed... I'll make you breakfast!"

    r "Break...?"

    n "NONONO! Don't break anything, it's called breakfast, it's what you eat in the morning."

    r "Oooh!"

    scene bg kitchen
    with dissolve

    show nate happy at right
    show rock happy at left

    "Nate busts out a pan and begins to cook french toast for both of them."

    r "Ooooh!~ It smells nice!~"

    n "Yeeahh I'm making french toast."

    r "French... roast?"

    n "Nonono, french toast! It's like, bread, with stuffff."

    n "Oh! That reminds me I owe you a smoothie."

    "He starts cutting the bananas and strawberries and puts it in a blender."

    r "Wha is th-"

    "The blender turns on scaring Rockhopper."

    show expressioned "rock scared" as rock

    r "AAAHHHHH!!"

    "Nate turns it off and runs to Rockhopper to comfort him."

    n "S-Sorry."

    "Rockhopper grabs Nate and squeezes him tight hiding behind him."

    r "I-It's scary...."

    n "I-It's a blender."

    r "O-Oh...?"

    n "Yeah don't worry, it makes our smoothies."

    r "Smutty?"

    "Nate blushes."

    show expression "nate blush" as nate

    n "N-No, smoothies. H-Here."

    "He pours the smoothie in a glass and hands it to Rockhopper."

    "Rockhopper takes the glass and drinks it all in one go with his eyes wide open in amazement."

    r "Aaah!~"

    n "And... About your name, it's a bit long."

    r "Rockhopper!~"

    n "Howww about.... Hops?"

    show expression "rock happy" as rock

    "He starts hopping around the room at an incredible speed and Nate starts freaking out."
    with vpunch

    show expression "nate shook" as nate

    n "{i}{b} Holy fuck {/i}{/b}"
    with vpunch

    r "Like this?"
    with vpunch

    n "Y-Yea..Yeah... H-How are..."
    with vpunch

    r "Ahaha!~ Look!"
    with vpunch

    n "Wh"
    with vpunch

    n "Hops c-can you stop jumping?"
    with vpunch

    "He lands right in front of Nate."
    with vpunch

    r "Yes!~"

    n "Ca...Can I ask you something?"

    r "Of course Nate!"

    "He pats Nate's head."

    r "What is it?"
    
    show expression "nate blush" as nate

    n "D-Do... You want to go on a date with me?"

    r "Today's a Saturday!"

    n "I mean... Like... If you like a person a lot you go on a date to get to know them better."

    show expression "rock confused" as nate

    r "Ooh! Nate... Likes me?"

    n "Y-Yeah."

    r "I like me too! And I like you! Especially when your face is red!"

    n "Heh..."

    r "Where go?"

    menu:

        "The Arcade?":
            jump chapter3arcade

        "The Cafe?":
            jump chapter3cafe

        "A restaurant?":
            jump chapter3restaurant

label chapter3cafe:
    return
    
label chapter3restaurant:
    return


######################################################################
#Arcade Date
######################################################################

label chapter3arcade:

    n "Hooww about.... the... arcade?"

    r "Arrg!? Like pirates?"

    n "It's like uhh, a place full of games."

    r "Oooh!~ Okay!~"

    r "Alright then! Let's get ready and go."

    "They get ready to leave and leave the house."

    scene bg mall
    with fade
    
    show rock normal at left

    show nate normal at right

    r "Ooh!~ So big~"

    "The arcade with bright words '' light up."

    n "There it is!"

    "Loud music and noises come out of the arcade as they get closer."

    "Hops begins to hold Nate tight"

    n "It's fine Hops~ Those are just the games!."

    r "G-Gays?"

    n "N-No, Games! You've played games before right?"

    r "Like... Pin fin on shark?"

    n "Yeah kinda! Except there's more stuff to these games."

    r "Ooh!~"

    "He rushes in the arcade."
    
    n "Wait!"
    

    
    
         

    return
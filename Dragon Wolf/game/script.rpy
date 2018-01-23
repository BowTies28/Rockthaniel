# The script of the game goes in this file.

#Character Names
#Main Characters
define n = Character("Nathaniel")
define r = Character("Rockhopper")
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
    
    "Nathaniel shakes the body."
    
    n "Hey! Are you alright?"

    "The fish? Dragon? Looking man opens his eyes and takes a glance at Nathaniel and faints."
    
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
    
    "He locks the leaves the house and locks the door"
    
    show nate embarassedblush:
        ease 1.0 offscreenright
        
    n "I hope he'll be fine."
   
########################################################################################################################################################
#Nate goes to [foodplace] and orders food for 2, Pheonyx notices and asks him questions about relationships allowing time for hops to fuck up the house
########################################################################################################################################################  

    scene restaurant
    with fade

    show nate normal
    
    n "Can I get uhh..."
    
    whomst "Nate!"
    
    show pheonyx dicks at left
    with easeinleft
    
    p "Hey! How was your mission?~ Find anything interesting?!"
    
    n "{b}{i}Interesting would be an understatement...{/i}{/b}"
    
    n "Oh you know! Same ol' same ol'."
    
    show kurouFastFood at right
    with easeinright
    
    k "Sir... Your order???"
    
    n "Oh! Yeah sorry, my bad. Two big boys please!"
    
    p "{i}Scoffs{/i} Two meals? Someones hungry~"
    
    n "Well actually."
    
    n "Oh! Can I get onion rings for one my big boys?"
    
    k "{i}sighs{/i} Yeah sure whatever. Your total is going to be $16.98"
    
    n "{b}{i}Jeez that’s a lot… but he must be starving.{/i}{/b}"
    
    show kurouFastFood:
        ease 0.5 offscreenright
        
    show nathe normal:
        ease 0.5 right
    
    p "Pheonyx: Soo~ What’s with the two meals..?"

    n "Oh you know... It's for a friend."
    
    p "You're seeing someone?"
    
    n "{i}Blushes{/i} Nonononoonono!! It's just a friend I swear!"
    
    p "{i}Giggles{/i} I'm just joking buddy. I know you're a single pringle but you should consider looking for someone. You deserve it."
    
    p "Are you at least looking?"
    
    n "Not at the moment, no. You know me though, I let things come to me"
    
    p "Well you're not gonna get a catch like that! Oh well, you'll find someone I'm sure. I gotta get going I have another hunt slip to finish! I'll see you later!"

    return

# The script of the game goes in this file.

#Character Names
define n = Character("Nathaniel")
define r = Character("Rockhopper")
define p = Character("Pheonyx")
define whomst = Character("???")



# The game starts here.

label start:

    scene bg black
    
    "Light peeks through the windows as birds chirp outside moving the branches brushing against the window. Nathaniel’s phone alarm rings."
    
    n "*yawns*"
    
    "Stretching his arms in bed, he reaches for his phone and silences it."
    
    scene bg bedroom
    with fade
    
    n "What a beautiful morning!~"
    
    n "*yawns* I should get ready... or..."

    scene bg black
    with fade
    
    "The phone lights up and vibrates, “Pheonyx is calling” is displayed on his phone as he stumbles out of bed."
    
    scene bg bedroom
    with hpunch
    
    n "Shit!... Did I...?"
    
    n "Oh shit! I’m late!"
    
    show nate flustered at center
    with easeinright
    
    n "I gotta run to the guild hall! I hope they didn't run out of hunts.."
    
    show nate flustered:
        ease 1.0 offscreenleft

    "He runs out the house slamming the door behind him rushing his way to the guild hall"
    
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
    
    "She giggles and winks at him and runs out the guild hall"
    
    show Pheonyx dicks:
        ease 1.0 offscreenright
        
    "FUCK FUCK FUCK FUCK"
    
    

    return

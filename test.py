
#import modules, visual for windows and stimuli, event for mouse and keyboard, core for timing
from psychopy import visual, event, core
from psychopy.hardware import keyboard

#import random to randomize trial sequence
import random

#variable list
window = None #testing window
kb = None #keyboard
mouse = None #mouse
task1_prompt = None #prompt for task 1
ratingScale = None #rating scale for task 1
task1_list = [] #list of testing sentences for task 1
log_file1 = None #log file for task 1 data
task2_prompt = None #prompt for task 2
task2_story = None #scinario description for task 2
image_animal = [] #animal images for task 2
image_award = [] #award images for task 2
image_prompt = None #image prompt for task 2
judgement_sentence = [] #judgement sentences for task 2
judgement_prompt = None #judgement prompt for task 2
log_file2 = None #log file for task 2 data

# create major variables for task 1 and 2, input none
def Initialize():
    #declare global variables
    global window
    global mouse
    global kb
    global ratingScale
    global task1_list
    global log_file1
    global image_animal
    global image_award
    global image_prompt
    global judgement_sentence
    global judgement_prompt
    global log_file2
   
    
    #create visual window
    window = visual.Window([1280, 720], monitor = "testMonitor", units = "deg", screen = 0, color = "white")
    
    #initialize mouse
    mouse = event.Mouse()
    
    #initialize keyboard
    kb = keyboard.Keyboard()
    
    #initialize rating scale for task 1
    #ranging from 1 to 5, "1" and "5" labeled, only mouse click accepted, no extra conforming click, black scale line
    ratingScale = visual.RatingScale(window, low = 1, high = 5, scale = "1-unacceptable, 5-perfect", 
    mouseOnly=True, singleClick = True, lineColor="black")
    
    #creating task 1 sentence stimuli
    #("testing sentence", "sentence type/experimental condition")
    #5 sentence types, each having 5 sentences, 25 in total
    task1_list = [("John doesn't like espresso or biscotti.", "SD"), ("Pat didn't enter the room or see her.", "SD"), 
    ("The road wasn't very wide or easy to find.", "SD"), ("Andrew doesn't speak English or German.", "SD"),
    ("We did not close the door or the window.", "SD"), ("John doesn't like espresso and biscotti.", "SC"), 
    ("Pat didn't enter the room and see her.", "SC"), ("The road wasn't very wide and easy to find.", "SC"), 
    ("Andrew doesn't speak English and German.", "SC"), ("We didn't close the door and the window.", "SC"), 
    ("It is not true that John likes espresso or biscotti.", "HD"), ("It is not true that Pat entered the room or saw her.", "HD"),
    ("It is not true that the road was very wide or easy to find.", "HD"), ("It is not true that Andrew speaks English or German.", "HD"),
    ("It is not true that we closed the door or the window.", "HD"), ("It is not true that John likes espresso and biscotti.", "HC"),
    ("It is not true that Pat entered the room and saw her.", "HC"), ("It is not true that the road was very wide and easy to find.", "HC"),
    ("It is not true that Andrew speaks English and German.", "HC"), ("It is not true that we closed the door and the window.", "HC"), 
    ("John likes both espresso and biscotti.", "filler"), ("Pat didn't enter the room nor see her", "filler"),
    ("The road wasn't easy to find because it was not very wide.", "filler"), ("Andrew speaks German and English.", "filler"),
    ("We closed the door as well as the window.", "filler")]
    
    #creating log file for task 1
    log_file1 = open("task1.csv", "a")
    
    #creating images for task 2, animal + award
    # 5 animal images, presented 5 units to the left of the center in the window
    image_animal = [visual.ImageStim(window, image="elephant.gif", pos = (-5, 0)), 
    visual.ImageStim(window, image="lion.gif", pos = (-5, 0)), visual.ImageStim(window, image="monkey.gif", pos = (-5, 0)),
    visual.ImageStim(window, image="panda.gif", pos = (-5, 0)), visual.ImageStim(window, image="zebra.gif", pos = (-5, 0))]
    # 3 award images, presented 5 units to the right of the center in the window
    image_award = [visual.ImageStim(window, image="x.gif", pos = (5, 0)), 
    visual.ImageStim(window, image="trophy.gif", pos = (5, 0)), visual.ImageStim(window, image="star.gif", pos = (5, 0))]
    
    #creating prompt during the image visualization in task 2--what does each award mean--on top of the images
    image_prompt = visual.TextStim(window, text = "Cross: nothing.  Star: one vegetable.  Trophy: both vegetables",
    height = 0.7, wrapWidth = 30, color = "black", pos = (0, 10))
    
    #creating 4 judgement sentences for task 2
    judgement_sentence = [visual.TextStim(window, text = "The animal ate the cake, but he didn't eat the carrot or the pepper.",
    height = 1, wrapWidth = 30, color = "black"), visual.TextStim(window, text = "The animal ate the cake, but he didn't eat the carrot and the pepper.", 
    height = 1, wrapWidth = 30, color = "black"), visual.TextStim(window, text = "The animal ate the cake. He also ate both the carrot and the pepper.",
    height = 1, wrapWidth = 30, color = "black"), visual.TextStim(window, text = "The animal ate the cake and one of the vegetables.",
    height = 1, wrapWidth = 30, color = "black")]
    
    #creating prompt for the judgement task under the testing sentence
    judgement_prompt = visual.TextStim(window, text = "True or False? \n \n \n Press 'y' if true, 'n' if false, press SPACE if not sure about the answer.",
    height = 0.8, wrapWidth = 25, color = "black", pos = (0, -5))
    
    # creating log file for task 2
    log_file2 = open("task2.csv", "a")
    
    
    
    
#Task one --grammatical judgement 

#function purpose: create the insturction window for task 1
#input：none； output：instruction window to be called
def ShowInstruction1():
    #declare global variables
    global window
    global kb
    global task1_prompt
    
    #assigning task 1 prompt as text stimulus 
    #presented in window, font height of 1, text width of 25, black text, in the center of the window
    task1_prompt = visual.TextStim(window, height = 1, wrapWidth = 25, color = "black", pos = (0, 0))
    #assigning value to the text argument
    task1_prompt.text = "For the first task, in each trial, please read the prompt sentence presented in the box, \
and rate the level of its acceptibility based on your intuition of grammaticality by clicking the scale, from 0 (not acceptbale at all), \
to 5 (perfectly acceptable). \n \n \n Please press any key to start."
    
    #present the instruction until any keys are pressed 
    while not event.getKeys():
        task1_prompt.draw()
        window.flip()

#function purpose: create the first task to be called
#input: none; output: 25 rating scales in random order, rating score for each, data logged in log file 1
def FirstTask():
    global window
    global mouse
    global ratingScale
    global task1_list
    global log_file1
    
    #randomize sentence order
    #creating a list containing 0 to 24 (25 items in task1_list)
    sen_idx = list(range(len(task1_list)))
    #randomizing the list
    sen_seq = random.sample(sen_idx, len(sen_idx))
    
    # for each item (i) in the randomized list of 0 to 24
    for i in sen_seq:
        #creating a text stimulus of the i+1 sentence in the task1_list
        #task1_list = [("sentence1", "type1"), ("sentence2", "type1"),...("sentence25", "type5")]
        #task1_list[i][0] = "sentence i+1"
        item = visual.TextStim(window, text = task1_list[i][0], height = 1, wrapWidth = 30, color = "black", pos = (0, 4))
        
        #presenting the rating sclae and the text stimulus until clicking on the scale
        while ratingScale.noResponse:
            item.draw()
            ratingScale.draw()
            window.flip()
        
        #getting rating score for item i
        rating = ratingScale.getRating()
        #data entry for each item: "sentence i+1", "sentence i+1 type", "rating score"
        task1_entry = str(task1_list[i][0]) + "," + "condition:," + str(task1_list[i][1]) +"," + "rating:," + str(rating)
        #reset rating scale for the next item
        ratingScale.reset()  
        #writing data entry of item i into log file 1
        log_file1.write(task1_entry + "\n")
            
        #pause 0.35s between trials
        window.flip()
        core.wait(0.35)


# Task two -- factual judgement

#function purpose: create the instruction window for task 2
#input: none; output: instruction window to be called
def ShowInstruction2():
    global window
    global kb
    global task2_prompt
    global task2_story
    
    #assigning task 2 prompt as text stimulus 
    #presented in window, font height of 1, text width of 25, black text, in the center of the window
    task2_prompt = visual.TextStim(window, height = 1, wrapWidth = 25, color = "black", pos = (0, 0))
    #assigning value to the text argument
    task2_prompt.text = "For the second task, you will first read a story describing the scenario. Based on \
the scenario, you'll be asked to make a factual judgement in each trial. The detailed instruction will be \
given after the story. \n \n \n Please press any key to start." 
    
    #presenting the instruction until any keys are pressed
    while not event.getKeys():
        task2_prompt.draw()
        window.flip()
    
    #assigning task 2 story as text stimulus
    #presented in window, font height of 0.8, text width of 25, black, in the center
    task2_story = visual.TextStim(window, height = 0.8, wrapWidth = 25, color = "black", pos = (0, 0))
    #assigning value to the text argument
    task2_story.text = "Five types of animals will take part in an eating contest. All these animals love cake, so \
they will all eat the cake. But no all these animals like vegetables, so they will get a special reward for \
eating vegetables. \n \n \n Those anmials who can eat BOTH the carrot and the pepper will receive a trophy. \
Those animals who eat ONLY ONE vegetables--the carrot OR the pepper--will receive a star. But those animals \
who eat NO vegetables at all will get nothing. \n \n \n Unfortunately, we can't see the eating contest, but \
we can see which award the animals received. Based on the information presented in the picture, you'll need \
to judge whether the following statement is right or wrong, by typing in 'true' or 'false' after the promt. \
\n \n \n Please press any key to start."
    
    #presenting the story description until any keys are pressed
    while not event.getKeys():
        task2_story.draw()
        window.flip()

#function purpose: create one trial in the second task
#input: animal = trial_seq[i][0], award = trial_seq[i][1], sentence = trial_seq[i][2]
#trial_seq = randomized ([animal1, award1, sentence1], [animal1, anward1, sentence2],...[animal5, award3, sentence4])
#output: visual stimulus of a trial, get a resposne of a trial, logging trial data to log file 2
def RunTrial(animal, award, sentence):
    global window
    global kb
    global image_animal
    global image_award
    global image_prompt
    global judgement_sentence
    global judgement_prompt
    global log_file2
    
    #draw stimuli for one trial: animal + award + prompt
    image_animal[animal].draw()
    image_award[award].draw()
    image_prompt.draw()
    #creating data entry for image: "animal type", "award type"
    image_entry = "animal:," + str(animal) + "," + "award:," + str(award)
    #flipping window to present the simuli 
    window.flip()
    
    #presenting the stimuli for 2s
    core.wait(2)
    
    #presenting judgement sentence and prompt until getting a response, only 'y', 'n', and space are allowed
    while not event.getKeys(keyList = ['y', 'n', 'space']):
        judgement_sentence[sentence].draw()
        judgement_prompt.draw()
        window.flip()
    #creating data entry for sentence: "sentence"
    sentence_entry = "sentence:," + str(sentence)
    
    # checking keys
    judgement_response = kb.getKeys()
    
    #creating data entry for response
    response_entry = "response:,"
    #if get "y" key, append 1 to response entry
    if judgement_response[0].name == 'y':
        response_entry += "1,"
    #if get "n" key, append -1 to response entry
    elif judgement_response[0].name == 'n':
        response_entry += "-1,"
    #else append 0 to response entry
    else:
        response_entry += "0,"
    
    #writing data entry of the trial to log file 2: image entry, sentence entry, response entry in one row
    log_file2.write(image_entry + "," + sentence_entry + "," + response_entry + "\n")

#function purpose: create second task with randomized trial sequence
#input: none; output: 60 trials 
def SecondTask():
    
    #function purpose: generate trial sequence
    #input: none
    #output: variable trials as a list of lists
    #trials = ([animal1, award1, sentence1], [animal1, award2, sentence1], [...])
    def GenerateTrialSequence():
        #declare global variables
        global image_animal
        global image_award
        global judgement_sentence
        
        #creating variable trials as an empty list
        trials = []
        
        #creating lists containing positions of elements in the three stimulus lists in task 2
        #animal_idx = [0:4]
        #award_idx = [0:2]
        #sentence_idx = [0:3]
        animal_idx = list(range(len(image_animal)))
        award_idx = list(range(len(image_award)))
        sentence_idx = list(range(len(judgement_sentence)))
        
        #looping through all combinations
        for animal in animal_idx:
            for award in award_idx:
                for sentence in sentence_idx:
                    #(animal = 0, award = 0, sentence = 0), (animal = 0, award = 0, sentence = 1),...
                    t = [animal, award, sentence]
                    #add to trials
                    trials.append(t)
        return trials
        #trials = ([animal1, award1, sentence1], [animal1, award2, sentence1], [...])
    
    #call funtion GenerateTrialSequence, get trials value
    trials = GenerateTrialSequence()
    #randomizing the elements in trials, assigning them to a new variable trial_seq
    trial_seq = random.sample(trials, len(trials))
    
    #for each element (i) in the trial_seq, input (trial_seq[i][0], trial_seq[i][1], trial_seq[i][2]) as argument of RunTrial function
    for i in range(len(trial_seq)):
        RunTrial(trial_seq[i][0], trial_seq[i][1], trial_seq[i][2])
            

#function purpose: terminate the experiment
#input: none; output: window closed, log file 1 and 2 closed, module core quitted 
def TerminateTask():
    global window
    global log_file1
    global log_file2
    
    window.close()
    log_file1.close
    log_file2.close
    core.quit()    
    
    
#call functions
#initialize major variables, show task 1 instruction, run task 1, show task 2 instruction, run task 2, end experiment
Initialize()
ShowInstruction1()
FirstTask()
ShowInstruction2()
SecondTask()
TerminateTask()       
    
    
    
    
        
        
        
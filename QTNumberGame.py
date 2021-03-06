#!/usr/bin/env python
# encoding=utf8

#import modules
import random
import rospy
import os
import sys
import time
import string
from std_msgs.msg import String
from qt_robot_interface.srv import *
from qt_gesture_controller.srv import *
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState
from thumb.msg import Res
#include IMU, button, orthosis
import rosbag
from heapq import nlargest
#gesture choose
def choose_behaviors(number):
    global right_pub, left_pub, head_pub, emotionShow_pub, gesturePlay_pub, speechSay_pub, audioPlay_pub
    #talking:1~6
    if(number == 1):
    #show_both_hands:9s
        emotionShow_pub.publish("QT/talking")
        gesturePlay_pub.publish("numbergame/talking1")
        rospy.sleep(9)
    elif(number == 2):
    #stretch_talk:8s
        gesturePlay_pub.publish("numbergame/talking2")
        emotionShow_pub.publish("QT/talking")
        rospy.sleep(8)
    elif(number == 3):
    #challenge:5s
        gesturePlay_pub.publish("QT/challenge")
        emotionShow_pub.publish("QT/talking")
        time.sleep(5)
    elif(number == 4):
    #show left and right:10s
        emotionShow_pub.publish("QT/talking")
        gesturePlay_pub.publish("numbergame/talking3")
        rospy.sleep(10)
    elif(number == 5):
    #teaching,10s
        emotionShow_pub.publish("QT/talking")
        gesturePlay_pub.publish("numbergame/talking4")
        rospy.sleep(10)   
    elif(number == 6):
    #teaching:10s
        emotionShow_pub.publish("QT/talking")
        gesturePlay_pub.publish("numbergame/talking5")
        rospy.sleep(10)
    elif(number == 7):
    #show:9s
        emotionShow_pub.publish("QT/talking")
        gesturePlay_pub.publish("numbergame/talking6")
        rospy.sleep(9)

    #listening:8~9
    elif(number == 8):
    #nod:4s
        head = Float64MultiArray()
        emotionShow_pub.publish("QT/showing_smile")
        head.data = [0,-10]
        head_pub.publish(head)
        time.sleep(1)
        head.data = [0,10]
        head_pub.publish(head)
        time.sleep(1)
        head.data = [0,0]
        head_pub.publish(head)
        time.sleep(2)
    elif(number == 9):
    #arm back smile:7s
        emotionShow_pub.publish("QT/calming_down")
        time.sleep(1)
        gesturePlay_pub.publish("QT/bored")
        time.sleep(6)    


    #guessing:10~12
    elif(number == 10):
    #confused:11s
        emotionShow_pub.publish("QT/confused")
        gesturePlay_pub.publish("numbergame/thinking1")
        rospy.sleep(11)
    elif(number == 11):
    #touch head:11s
        emotionShow_pub.publish("QT/confused")
        gesturePlay_pub.publish("numbergame/thinking2")
        rospy.sleep(11)
    elif(number == 12):
    #thinking:11s
        emotionShow_pub.publish("QT/confused")
        gesturePlay_pub.publish("numbergame/thinking3")
        rospy.sleep(11)


    #feedback and encouragement:13~16
    elif(number == 13):
    #surprise:5.5s
        gesturePlay_pub.publish("QT/surprise")
        emotionShow_pub.publish("QT/surprise")
        time.sleep(5.5)
    elif(number == 14):
    #happy:5s
        gesturePlay_pub.publish("QT/happy")
        emotionShow_pub.publish("QT/happy")
        time.sleep(5)
    elif(number == 15):
    #hug:6s
        left_arm = Float64MultiArray()
        right_arm = Float64MultiArray()
        emotionShow_pub.publish("QT/happy")
        left_arm.data = [-20, -10, -15]
        left_pub.publish(left_arm)
        right_arm.data = [20, -10, -15]
        right_pub.publish(right_arm)
        time.sleep(3)
        left_arm.data = [90, -60, -30]
        left_pub.publish(left_arm)
        right_arm.data = [-90, -60, -30]
        right_pub.publish(right_arm)
        time.sleep(3)
    elif(number == 16):
    #hand clap:8.8s
        left_arm = Float64MultiArray()
        right_arm = Float64MultiArray()
        emotionShow_pub.publish("QT/happy")
        left_arm.data = [10, -90, -30]
        left_pub.publish(left_arm)
        right_arm.data = [-10, -90, -30]
        right_pub.publish(right_arm)
        time.sleep(1.8)
        left_arm.data = [10, -90, -90]
        left_pub.publish(left_arm)
        right_arm.data = [-10, -90, -90]
        right_pub.publish(right_arm)
        time.sleep(1)
        left_arm.data = [10, -90, -30]
        left_pub.publish(left_arm)
        right_arm.data = [-10, -90, -30]
        right_pub.publish(right_arm)
        time.sleep(1)
        left_arm.data = [10, -90, -90]
        left_pub.publish(left_arm)
        right_arm.data = [-10, -90, -90]
        right_pub.publish(right_arm)
        time.sleep(1)
        left_arm.data = [10, -90, -30]
        left_pub.publish(left_arm)
        right_arm.data = [-10, -90, -30]
        right_pub.publish(right_arm)
        time.sleep(1)
        left_arm.data = [90, -60, -30]
        left_pub.publish(left_arm)
        right_arm.data = [-90, -60, -30]
        right_pub.publish(right_arm)
        time.sleep(3)


    #special_function:17~19
    elif(number == 17):
    #hi/bye:7s
        gesturePlay_pub.publish("QT/hi")
        emotionShow_pub.publish("QT/happy")
        time.sleep(7)
    elif(number == 18):
    #fly kiss:7.5s
        gesturePlay_pub.publish("QT/kiss")
        time.sleep(1)
        emotionShow_pub.publish("QT/kiss")
        time.sleep(6.5)
    elif(number == 19):
    #yawn:6.8s
        gesturePlay_pub.publish("QT/yawn")
        time.sleep(0.8)
        emotionShow_pub.publish("QT/yawn") 
        time.sleep(6)
    
    #rest
    elif(number == 20):
    #
        abc =1
        
    
    else:
        print("Please use a correct number!")


def gesture_talk(num):
    i = 1
    while i <= num:
        choose_behaviors(random.randint(1, 7))
        i = i + 1
    
    
def gesture_listen(num):
    i = 1
    while i <= num:
        choose_behaviors(random.randint(8, 9))
        i = i + 1
    

def gesture_guess(num):
    i = 1
    while i <= num:
        choose_behaviors(random.randint(10, 12))
        i = i + 1


def gesture_encourage():
    choose_behaviors(random.randint(13, 16))


#encourage decision function
def encourage_score():
    score = 1
    return score


def dictionary_set():
    #setting up phrase dictionaries
    #to guess
    guess_dict = {1: 'Is your number {}?', #2.5 sec
                    2: 'I guess {}. Did I guess your number?', #5.5 sec
                    3: 'Ok I think I know your number. Is it {}?', #5.5 sec
                    4: 'Is {} right?'} #2.5 sec
    #higher or lower
    second_dict = {1: 'Hey {} ,is your number higher than mine? Show me yes or no.', #7 sec 
                    2: 'Oh no I didn’t get it. Is your number higher than my guess {}?', #7 sec
                    3: 'Hmm is your guess bigger than mine {}?'} #4 sec  
    #to encourage play during game 
    encourage_dict = {1:'Good job {}!', #2.5 sec
                    2:'That was your best one so far! Keep up the good work {}!', #7 sec
                    3:'I can tell you are trying really hard {}, nice job!', #5 sec
                    4:'You are getting better at this {}, wow!', #4 sec
                    5:'I know this is hard {}, keep trying!'} #4.5 sec
    clarify_dict = {1: 'I didn’t see that {}, could you repeat that answer for me?', #6 sec
                    2: 'I think that was a {}. If I’m right could you make a thumbs up/down for me?', #6.5 sec
                    3: 'Could you show me that answer again {}?'} #4 sec 
    reward_dict = {1: 'Let’s dance.', #2 sec
                    2: 'I have a joke {}, why did a crocodile marry a chicken? Because crock-o-doodle-doodle is a good last name!', #9.5 sec
                    3: 'What is your favorite color {}? Mine is blue.', #5.5 sec
                    4: 'I like playing games with you {}, you’re very fun. Do you like playing with me?'} #8 sec
    return guess_dict,second_dict,encourage_dict,clarify_dict,reward_dict


def feedback_function(thumb_angle, time,name):
    global speechSay_pub, encourage_dict, reward_dict
    #give each item weights and combine weights to make a %
    #want reward to be 80-50% and encourage >80% always
    #camera angle, GAS (fatigue), history of gestures, # of prompts
    
    #camera angles should be matched to buckets on the GAS - need to see lit if standard #s for this (10% is 1, 20% is 2)
        #these should be the most important factors to weight
    
    #increase the encouragement when GAS, camera angle is worse and increase more if history shows a pattern of worsening
    
    #if high number of rewards maybe dont need to increase encouragement as much
    
    #if a lot of clarification is needed, and bad history of gestures, more encouragement and more reward for lower GAS
    
    #if history of gestures is bad but shows one good case give a reward

    #50 degrees is the threshold, determined by GAS
    if abs(thumb_angle) < 50:
        encourage_prob = 0.85 -abs(thumb_angle/100.0) + time/300.0 #smaller angle, worse performance/ longer time, more tired, more enc
        if encourage_prob<0:
            print("encourage_prob is 0!")
            encourage_prob = 0
        if encourage_prob>1:
            print("encourage_prob is 1!")
            encourage_prob = 1
        enc_flag = random.randrange(1,100)
        if enc_flag<encourage_prob*100:
            random_encourage = random.randrange(1,len(encourage_dict))
            speechSay_pub.publish(encourage_dict[random_encourage].format(name))
            rospy.sleep(7)


    else:
        reward_prob = 0.5 + abs(thumb_angle/100.0) + time/300.0 #larger angle, better performance/ longer the time playing, more reward
        if reward_prob<0:
            print("reward_prob is 0!")
            reward_prob = 0
        if reward_prob>1:
            print("reward_prob is 1!")
            reward_prob = 1
        rew_flag = random.randrange(1,100)
        if rew_flag<reward_prob*100:
            random_rew = random.randrange(1,len(reward_dict))
            speechSay_pub.publish(reward_dict[random_rew].format(name))
            rospy.sleep(9)



def get_thumb_input():
    # print("enter")
    #wait for 5s to get the best thumb input during 5s, get 50 results totally
    i = 1
    reses = []
    angles = []
    while(i<40):
        print i
        msg = rospy.wait_for_message("/thumb_result",String)
        msg = str(msg.data)
        msg_list = msg.split('+')
        res_msg = int(msg_list[0])
        angle_msg = float(msg_list[1])
        reses.append(res_msg)
        angles.append(angle_msg)
        i = i+1
        time.sleep(0.1)
    print("down")
    return reses,angles


def isThumbUp_Down():
    #return up or down and the angle
    reses, angles = get_thumb_input()
    if reses.count(1) > 15:
        angles = nlargest(10, angles)
        res = sum(angles)/len(angles)
        return 1, res
    elif reses.count(-1) > 15:
        angles = [ -x for x in angles]
        angles = nlargest(10, angles)
        res = -sum(angles)/len(angles)
        return -1,res
    else 
        return 0,sum(angles)/len(angles)


def record_data():
    #use rosbag to record data
    #astra camera data/QT camera data/angle result data/button data/game playing data:sentence said by QT and children response
    #astra camera data should be recorded on the local computer, use compressed
    #QT camera just rosbag /image_raw
    #motion and sentences just rosbag moter topic and speech topic
    #button data just rosbag button data
    pass




if __name__=="__main__":
    guess_dict,second_dict,encourage_dict,clarify_dict,reward_dict = dictionary_set()
    rospy.init_node('qt_numbergame')
    #initialize publishers
    right_pub = rospy.Publisher('/qt_robot/right_arm_position/command', Float64MultiArray, queue_size=1)
    left_pub = rospy.Publisher('/qt_robot/left_arm_position/command', Float64MultiArray, queue_size=1)
    head_pub = rospy.Publisher('/qt_robot/head_position/command', Float64MultiArray, queue_size=1)
    emotionShow_pub = rospy.Publisher('/qt_robot/emotion/show', String, queue_size=10)
    gesturePlay_pub = rospy.Publisher('/qt_robot/gesture/play', String, queue_size=10)
    speechSay_pub = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)
    audioPlay_pub = rospy.Publisher('/qt_robot/audio/play', String, queue_size=10)

    #wait for publisher connections
    wtime_begin = rospy.get_time()
    while (audioPlay_pub.get_num_connections() == 0 or
        speechSay_pub.get_num_connections() == 0 or
        gesturePlay_pub.get_num_connections() == 0 or
        emotionShow_pub.get_num_connections() == 0 or
        right_pub.get_num_connections() == 0 or
        left_pub.get_num_connections() == 0 or
        head_pub.get_num_connections() == 0 ) :
        rospy.loginfo("waiting for subscriber connections")
        if rospy.get_time() - wtime_begin > 5.0:
            rospy.logerr("Timeout while waiting for subscribers connection!")
            sys.exit()
        rospy.sleep(1)
    # get_thumb_input()

    game_flag = 0 #set to 0 to play intro
    start_time = time.time()
    while 1:
        #game always running, until shutdown by children
        # exit_msg = rospy.wait_for_message()
        # if exit_msg.flag == False:
        # once_again = raw_input('Play again? ') #type 'yes' or 'no'
        print("Play again?")
        print("please do thumb up/down!")
        res, the_angle = isThumbUp_Down()
        if res == -1:
        # if once_again == 'no':
            #game over
            speechSay_pub.publish("I had a great time with you today. Bye-bye!")
            choose_behaviors(16)
            break
        # elif once_again == 'yes':
        elif res == 1:
            if game_flag == 0:#the first time to play
                #introduction
                speechSay_pub.publish("Hello, my name is Q T Robot. What is your name? ") #6.5 sec
                choose_behaviors(16)
                name = raw_input('What is your name? ')
                speechSay_pub.publish("Hi   "+name+""",      I would like to play a guessing game with you. 
                In the game I get to ask you questions, and you get to answer yes or no
                only by using a thumbs up or a thumbs down gesture with your right arm.
                Let's practice. Can you show me a thumbs up to say yes?""") #22-25 sec
                gesture_talk(3)
                #configuration
                # correctup = raw_input('Was it a good thumbs up? ')
                print("please do a thumb up!")
                # if correctup == 'yes':
                res, the_angle = isThumbUp_Down()
                if res == 1:
                # maybe need to sleep some time to wait for input
                # msg = rospy.wait_for_message("/thumb_result", Res)
                # msg.up_down
                # ^ these two lines would be replaced by camera or IMU input, worst case experimenter prompts
                #we need a time limit they can answer in - 5 sec?
                    speechSay_pub.publish("Awesome! Now can you show me a thumbs down to say no?") #6 sec
                    gesture_talk(1)
                # correctdown = raw_input('Was it a good thumbs down? ')
                print("please do a thumb down!")
                # if correctdown == 'yes':
                res, the_angle = isThumbUp_Down()
                if res == -1:
                # ^ these two lines would be replaced by camera or IMU input, worst case experimenter prompts
                    speechSay_pub.publish("""Cool!! During the game, please keep your hand in the 
                        middle until I ask you a question. That means your thumb is pointing sideways, 
                        not up or down! Remember to try as hard as you can to show me thumbs up 
                        or thumbs down, so I can understand if you mean yes or no! If your thumb 
                        is going the wrong way, just push the red button to move it back to the 
                        middle. Remember to keep your hands in the middle when you are not answering 
                        a question.  And just do your best. Can you show me yes if that’s ok?""") #40.5 sec
                    gesture_talk(5)
                rospy.sleep(5)
            #initialize variables
            nocounter = 0
            yescounter = 0
            wrongcounter = 0
            high = 101
            low = -1
            # correctok = raw_input('Was it OK? ')
            print("please do a thumb up to say OK")
            # if correctok == 'yes':
            res, the_angle = isThumbUp_Down()
            if res == 1:
                #play game now
                speechSay_pub.publish("Let's play now! Please think of a number between 1 and 100.") #6.5 sec
                gesture_talk(1)
                start = input('What is your number? ') #type a number - no rospy.sleep because waiting for input
                # ^ this line would be replaced by camera or IMU input, worst case experimenter prompts
                # we should in general have a way to incorporate this in game to track wrong answers
                speechSay_pub.publish("I'm thinking of your number.") #3 sec
                gesture_guess(1)
                while start < 101:
                #this line should be changed to a while loop without a prompt input
                    half_range = int((high-low)/2)
                    current = half_range+low
                    random_add = random.randrange(-half_range,half_range) #never add on outside of the guessing range
                    random_guess = random.randrange(1,len(guess_dict))
                    QT = current+random_add
                    speechSay_pub.publish(guess_dict[random_guess].format(QT))    
                    choose_behaviors(2)
                    #encourage the child - should be timed via feedback function
                    speechSay_pub.publish("Show me through your thumbs up or down"+str(name))
                    
                    # random_encourage = random.randrange(1,len(encourage_dict))
                    # speechSay_pub.publish(encourage_dict[random_encourage].format(name))
                    # gesture_talk(1)
                    # val = raw_input('Is my guess correct? ')
                    print("is my guess correct?")

                    # # ^ this line would be replaced by camera or IMU input, worst case experimenter prompts
                    #     # use # number = sys.stdin.readline() if prompt
                    #     # number.split()[0]
                    
                    # if val == 'no':
                    res, the_angle = isThumbUp_Down()
                    rospy.sleep(3)
                    feedback_function(the_angle,time.time()-start_time,name)
                    
                    if res == -1:
                        if QT == start: #prompt if they make a wrong answer about the correctness of QTs guess
                            speechSay_pub.publish("Are you sure about that?")
                            gesture_talk(1)
                            wrongcounter += 1
                        else:
                            speechSay_pub.publish(second_dict[random_guess].format(name))
                            gesture_talk(1)
                            speechSay_pub.publish("My guess is "+str(QT))
                            choose_behaviors(2)
                            nocounter += 1
                            while True:
                                # val2 = input('yes(1) or no(0)? ')
                                print("please do a thumb up/down to say higer or lower")
                                feedback_function(the_angle,time.time()-start_time,name)
                                # random_encourage = random.randrange(1,len(encourage_dict))
                                # speechSay_pub.publish(encourage_dict[random_encourage].format(name))
                                # ^ this line would be replaced by camera or IMU input, worst case experimenter prompts
                                    # use # number = sys.stdin.readline() if prompt
                                # if val2 == 1:
                                res, the_angle = isThumbUp_Down()
                                if res == 1:
                                    if QT > start:
                                        speechSay_pub.publish("Are you sure about that?")
                                        choose_behaviors(2)
                                        wrongcounter += 1
                                    else:
                                        low = QT
                                        yescounter += 1
                                        break
                                # if val2 == 0:
                                if res == -1:
                                    if QT < start:
                                        speechSay_pub.publish("Are you sure about that?")
                                        choose_behaviors(2)
                                        wrongcounter += 1
                                    else:
                                        high = QT
                                        nocounter += 1
                                        break
                                else:
                                    print("Wrong input! Please input again.")
                            

                    # elif val == 'yes':
                    elif res == 1:
                        speechSay_pub.publish('Hooray! I got it! Thanks for playing with me. Do you want to play again with me?') #9 sec
                        #should they play a minimum of 3 games mandatory, the rest optional?
                        choose_behaviors(13)
                        yescounter += 1
                        print("Number of yes: "+str(yescounter)+". Number of no: "+str(nocounter)+". Number wrong: "+str(wrongcounter))
                        print('I got it!')
                        game_flag = game_flag + 1
                        break


                    else:#child can input something except 'yes' and 'no' to break out the game
                        #game over
                        print("Number of yes: "+str(yescounter)+". Number of no: "+str(nocounter)+". Number wrong: "+str(wrongcounter))
                        speechSay_pub.publish("OK! I had a great time with you today. Bye-bye!")
                        choose_behaviors(16)
                        sys.exit()
        else:
            print("Wrong input! Please input again.")


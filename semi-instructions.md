# Text File Versions of Location and Time

(for reference)


**LOCATION**
``` html 
<div id="Consent">
    <br><br>
    <h3>READ INSTRUCTIONS CAREFULLY BEFORE ACCEPTING TO PARTICIPATE:</h3>

    <p>This study is part of a research project titled "How large is your visual memory capacity?". The principal investigator 
    in charge of this study is Jeremy Wolfe (jwolfe@bwh.harvard.edu), Visual Attention Lab, Brigham and Women's Hospital. However, other research staff may be involved and can act on behalf of 
    the person in charge.</p>

    <h4>Requirements:</h4>
    <p> You need color vision for this task. </p>
    <p> You need at least 20/25 visual acuity (with or without correction). </p>
    <p> You have not participated in a similar study before. </p>
    <p> Please complete this study on a desktop or laptop. </p>

    <h4>Instructions:</h4>
    <p><b>NOTE: </b>The experiment works in Safari and Chrome. If the experiment does not show in your browser, please notify the experimenter.</p> 
    When you start a trial:
    <p>(1) You will see one object image on the screen at a time, each will be appear for 3 seconds.  </p> 
    <p>(2) Your job is to REMEMBER what objects you saw as well as where you saw them.  </p> 
    <p>(3) Some items will appear twice. If you saw the item before, click the location where you thought you saw them (guess if you need to) during the testing section.  </p>
    <p>(4) Please respond as quickly and accurately as possible. We will record your responses and reaction time. </p> 

    <p>The experiment consists of around ~350 trials. You should be able to complete them in 30 minutes. You are alloted 60 min in total. 
        You will receive $6 for your participation. <b>You will be compensated only if you complete all the trials and correctly identify whether an item is old/new at least 70% of the time.</b> </p>

    <p>By participating in this study, you will be part of the scientific effort to understand the 
    functioning of the human visual system and the decision making process. </b></p> <br>

    <p> PLEASE READ THROUGH OUR CONSENT INFORMATION SHEET BEFORE CONSENTING TO PARTICIPATING IN OUR STUDY. <br>
        <a href="https://search.bwh.harvard.edu/OnlineExperiment/Consent_InformationSheet_Online_Nov2021.pdf" target="_blank"> >> CONSENT INFORMATION SHEET  </a>
    </p>
    
    <label><input type = "radio" class = "checkbox"> BY CHECKING THIS BOX, YOU ACKNOWLEDGE THAT YOU READ THE INSTRUCTIONS AND THE CONSENT INFORMATION SHEET, UNDERSTAND THE 
        TASK AND YOU CONSENT TO PARTICIPATE IN THIS STUDY.<br>
        <br>
        </label> 
    <br><br>

    <div id = "Start_Experiment" >
    <a href = "javascript:consented()" id= 'consentHIT' class = 'PressButton'> Click Here to Start the Experiment</a> </div>
  <!--<a href = "javascript:startTesting()" id= 'consentHIT' class = 'PressButton'> Click Here to Start the Experiment</a> </div>
--> 
    
    <br><br> <br><br>

    
</div>

<div id = "demographic">
    <br><br><br>

    <h3>Demographic Survey:</h3>

    <p> This study is funded by the NIH (National Institutes of Health) and requires the report of the participants' demographic information. 
        The questions in this form are voluntary. We collect this information to accurately report
        the characteristics of our samples, and ensure that they are representative of the population. </p>

    <form>     
        <label for="age">What is your age:</label><br>
            <input type="number" id="age" name="age"><br><br>

        <label for="gender">Gender:</label><br>
            <input type="radio" id="male" name="gender" value="male">
            <label for="male">Male</label><br>
            <input type="radio" id="female" name="gender" value="female">
            <label for="female">Female</label><br>
            <input type="radio" id="other" name="gender" value="other">
            <label for="other">Other</label><br>
            <input type="radio" id="genderNoResponse" name="gender" value="genderNoResponse">
            <label for="genderNoResponse">Prefer Not to Respond</label><br><br>

        <label for="citizenship">Are you a U.S. citizen:</label><br>
            <input type="radio" id="isCitizen" name="citizenship" value="isCitizen">
            <label for="isCitizen">Yes</label><br>
            <input type="radio" id="notCitizen" name="citizenship" value="notCitizen">
            <label for="notCitizen">No</label><br><br>

        <label for="ethnicity">Ethnic category:</label><br>
            <input type="radio" id="HL" name="ethnicity" value="HL">
            <label for="HL">Hispanic or Latino</label><br>
            <input type="radio" id="notHL" name="ethnicity" value="notHL">
            <label for="notHL">Not Hispanic or Latino</label><br><br>

        <label for="Race">Racial Categories (if more than one race, check all that apply):</label><br>
            <input type="checkbox" id="AIAN" name="Race" value = "AIAN">
            <label for="AIAN">American Indian/Alaska Native</label><br>
            <input type="checkbox" id="asian" name="Race" value = "asian">
            <label for="asian">Asian</label><br>
            <input type="checkbox" id="NH" name="Race" value = "NH">
            <label for="NH">Native Hawaiian or Other Pacific Islander</label><br>
            <input type="checkbox" id="black" name="Race" value = "black">
            <label for="black">Black or African American</label><br>
            <input type="checkbox" id="white" name="Race" value = "white">
            <label for="white">White</label><br>
            <input type="checkbox" id="unsure" name="Race" value = "unsure">
            <label for="unsure">Unsure/prefer not to respond</label><br>
            <input type="checkbox" id="raceOther" name="Race" value = "raceOther">
            <label for="raceOther">Other</label><br><br>

        <label for="AddComments">Additional comments:</label><br>
            <input type="text" id="AddComments" name="AddComments"><br><br>

        <label for="mTurkId">If you are on mTurk, please enter your mTurk ID here:</label><br>
            <input type="text" id="mTurkId" name="mTurkId"><br>
        
    </form> 

    <br>

    Thank you for your responses. Please click the submit button.<br><br><br>
    <a href="javascript:SaveData()" class = 'PressButton'>Submit</a>

    <br><br><br><br>
</div> 

<div class = "TestScreen" id = "TestScreen">
    <body>
        <div class = "ResponseButton" id = "ResponseButton"> 
            <div id = "ResponseButton_instr"></div>
        </div>
        <div class = "StimWindow" id = "StimWindow" >    
            <div class = "Instruction">
                <p> 
                    <!-- <br><br> -->
                    <p style = "color:red"> In this experiment, <br><br>Your job is to REMEMBER what <b>objects</b> you saw 
                    and the <b>locations</b> where you saw them.<br></p>
                    <br>
                    Items will appear on the screen for 3 seconds each at different locations. Some items will show up twice. <br>
                    <b>If you saw the item before,</b> click the location on the screen where you thought you saw it (Guess if you need to). Then, respond on the time bar when in the training portion you saw it (in terms of start to end order).
                    <br><br>
                    <b>If you have not seen it before,</b> click in the purple box to the right. 
                    <br><br>
                    You will receive feedback on whether you are right or wrong about the old/new decision. <br>
                    You will NOT receive feedback on your spatial decision.
                    <br><br><br>

                    <i>If the image size is too small, please enter the browser into full screen, and refresh the webpage to restart. </i>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:startAudioCheck()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">NEXT</a>
                    
                </div>
            </div>

            <div class = "audioCheck" id = "audioCheck"> 
                <br><br><br><br><br><br><br>
                In the experiment, we will provide you with audio feedback. <br>
                Before starting the experiment, please adjust your volume and make sure that you can clearly hear the sound effect when clicking on the buttons below. <br>
                <br><br>

                <button onclick="playSound_pos()" id="ACButton" style = "color:green; border-color: green" > CORRECT </button>
                <button onclick="playSound_neg()" id="ACButton" style = "color:maroon; border-color: maroon " > WRONG </button>

                <br><br><br>
                <div class = 'StartButton'> 
                    <a href="javascript:startExp()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Click to Start the Experiment</a>       
                </div>
            </div>

            <div class = "Instruction2" id = "Instruction2">
                <p> 
                    <br><br><br>
                    You have finished part 1. 
                    <br><br>

                    Now we will ask you again about the displays you saw earlier. Do your best. 
                    <br><br>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:NextTrial_retest()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Click here to start Part 2 </a>
    
                </div>
            </div>

            <div class = "TestingEnds" id = "TestingEnds">
                <p> 
                    <br><br><br><br><br><br>
                    You have completed the experiment. Your accuracy for the old/new response is <span id="Practice_Accuracy"></span>%. <br><br>


                    <br><br> <br><br>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:ExpEnd()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Continue </a>
    
                </div>
            </div>

            <div class = "PracticeEnd" id = "PracticeEnd">
                <p> 
                    <br><br><br>
                    Great! You have completed the practice. <br><br>

                    Now you will start the main experiment. Please answer as quickly and accurately as you can. <br><br>

                    The main experiment takes about 45 min 
                    <br><br>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:startTesting()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Click here to begin </a>
    
                </div>
            </div>

            <div class = "viewingEnd" id = "viewingEnd">
                <p> 
                    <br><br><br>
                    You have viewed all the images. <br><br>

                    Now we will show you one image at a time. If you have seen the image before, click on the location where you have seen it. <br><br>

                    If you have not seen the image before, click on the purple button on the right.
                   
                    <br><br>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:TestingBlock_setup()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Click here to begin </a>
    
                </div>
            </div>

            <div class = "EndPage" id = "EndPage">
                <p> 
                    <br><br><br> <br><br><br>
                    Done! You have finished the experiment. You can close the window now. 

                    <br><br>

                    Thanks.
                    <br><br>
                </p>
    
            </div>

            <header class="headboard" id = "headboard" style= "background-color:transparent;">   </header>
            <div class = "myProgress" id = "myProgress" >
                 <div class = "myBar" id = "myBar">
                     <div id = "myBar_start">Start</div>
                    <div id = 'myBar_now'>End</div>
                    </div>
            </div>
            <canvas id="StimCanvas" style = "cursor:pointer" > </canvas>
        </div>

        <div class = "DisplayWindow" id = "DisplayWindow">    
            <div id = "DisplayWindow_img"></div>
            <div id = "DisplayWindow_instr"> Click Old Location <br> or Click in New Box</div>
        </div>
    </body>
</div>

<!--Break screen -->
<div class = "Break" id = "Break">
    <p> 
        <br><br><br>
        Click NEXT to start trial <span id="trleft">1</span>/<span id="tr-total">20</span>
    </p>

    <div class = 'StartButton'> 
        <a href="javascript:DisplaySetup()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Next</a>

    </div>
</div>

<div class = "Break_retest" id = "Break_retest">
    <p> 
        <br><br><br>
        Click NEXT to start retest trial <span id="trleft2">1</span>/<span id="tr-total2">20</span>
    </p>

    <div class = 'StartButton'> 
        <a href="javascript:NextTrial_retest()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Next</a>

    </div>
</div>
```

^^ this changes the basic instructions in all the screens + includes the demographics file. 


**TIME**
```html 
<div id="Consent">
    <br><br>
    <h3>READ INSTRUCTIONS CAREFULLY BEFORE ACCEPTING TO PARTICIPATE:</h3>

    <p>This study is part of a research project titled "How large is your visual memory capacity?". The principal investigator 
    in charge of this study is Jeremy Wolfe (jwolfe@bwh.harvard.edu), Visual Attention Lab, Brigham and Women's Hospital. However, other research staff may be involved and can act on behalf of 
    the person in charge.</p>

    <h4>Requirements:</h4>
    <p> You need color vision for this task. </p>
    <p> You need at least 20/25 visual acuity (with or without correction). </p>
    <p> You have not participated in a similar study before. </p>
    <p> Please complete this study on a desktop or laptop. </p>

    <h4>Instructions:</h4>
    <p><b>NOTE: </b>The experiment works in Safari and Chrome. If the experiment does not show in your browser, please notify the experimenter.</p> 
    When you start a trial:
    <p>(1) You will see one object image on the screen at a time, each will be appear for 3 seconds.  </p> 
    <p>(2) Your job is to REMEMBER what objects you saw as well as when you saw them.  </p> 
    <p>(3) Some items will appear twice. If you saw the item before, indicate on a time bar the time when you saw them during the testing portion.  </p>
    <p>(4) Please respond as quickly and accurately as possible. We will record your responses and reaction time. </p> 

    <p>The experiment consists of around ~350 trials. You should be able to complete them in 30 minutes. You are alloted 60 min in total. 
        You will receive $6 for your participation. <b>You will be compensated only if you complete all the trials and correctly identify whether an item is old/new at least 70% of the time.</b> </p>

    <p>By participating in this study, you will be part of the scientific effort to understand the 
    functioning of the human visual system and the decision making process. </b></p> <br>

    <p> PLEASE READ THROUGH OUR CONSENT INFORMATION SHEET BEFORE CONSENTING TO PARTICIPATING IN OUR STUDY. <br>
        <a href="https://search.bwh.harvard.edu/OnlineExperiment/Consent_InformationSheet_Online_Nov2021.pdf" target="_blank"> >> CONSENT INFORMATION SHEET  </a>
    </p>
    
    <label><input type = "radio" class = "checkbox"> BY CHECKING THIS BOX, YOU ACKNOWLEDGE THAT YOU READ THE INSTRUCTIONS AND THE CONSENT INFORMATION SHEET, UNDERSTAND THE 
        TASK AND YOU CONSENT TO PARTICIPATE IN THIS STUDY.<br>
        <br>
        </label> 
    <br><br>

    <div id = "Start_Experiment" >
    <a href = "javascript:consented()" id= 'consentHIT' class = 'PressButton'> Click Here to Start the Experiment</a> </div>
  <!--<a href = "javascript:startTesting()" id= 'consentHIT' class = 'PressButton'> Click Here to Start the Experiment</a> </div>
--> 
    
    <br><br> <br><br>

    
</div>

<div id = "demographic">
    <br><br><br>

    <h3>Demographic Survey:</h3>

    <p> This study is funded by the NIH (National Institutes of Health) and requires the report of the participants' demographic information. 
        The questions in this form are voluntary. We collect this information to accurately report
        the characteristics of our samples, and ensure that they are representative of the population. </p>

    <form>     
        <label for="age">What is your age:</label><br>
            <input type="number" id="age" name="age"><br><br>

        <label for="gender">Gender:</label><br>
            <input type="radio" id="male" name="gender" value="male">
            <label for="male">Male</label><br>
            <input type="radio" id="female" name="gender" value="female">
            <label for="female">Female</label><br>
            <input type="radio" id="other" name="gender" value="other">
            <label for="other">Other</label><br>
            <input type="radio" id="genderNoResponse" name="gender" value="genderNoResponse">
            <label for="genderNoResponse">Prefer Not to Respond</label><br><br>

        <label for="citizenship">Are you a U.S. citizen:</label><br>
            <input type="radio" id="isCitizen" name="citizenship" value="isCitizen">
            <label for="isCitizen">Yes</label><br>
            <input type="radio" id="notCitizen" name="citizenship" value="notCitizen">
            <label for="notCitizen">No</label><br><br>

        <label for="ethnicity">Ethnic category:</label><br>
            <input type="radio" id="HL" name="ethnicity" value="HL">
            <label for="HL">Hispanic or Latino</label><br>
            <input type="radio" id="notHL" name="ethnicity" value="notHL">
            <label for="notHL">Not Hispanic or Latino</label><br><br>

        <label for="Race">Racial Categories (if more than one race, check all that apply):</label><br>
            <input type="checkbox" id="AIAN" name="Race" value = "AIAN">
            <label for="AIAN">American Indian/Alaska Native</label><br>
            <input type="checkbox" id="asian" name="Race" value = "asian">
            <label for="asian">Asian</label><br>
            <input type="checkbox" id="NH" name="Race" value = "NH">
            <label for="NH">Native Hawaiian or Other Pacific Islander</label><br>
            <input type="checkbox" id="black" name="Race" value = "black">
            <label for="black">Black or African American</label><br>
            <input type="checkbox" id="white" name="Race" value = "white">
            <label for="white">White</label><br>
            <input type="checkbox" id="unsure" name="Race" value = "unsure">
            <label for="unsure">Unsure/prefer not to respond</label><br>
            <input type="checkbox" id="raceOther" name="Race" value = "raceOther">
            <label for="raceOther">Other</label><br><br>

        <label for="AddComments">Additional comments:</label><br>
            <input type="text" id="AddComments" name="AddComments"><br><br>

        <label for="mTurkId">If you are on mTurk, please enter your mTurk ID here:</label><br>
            <input type="text" id="mTurkId" name="mTurkId"><br>
        
    </form> 

    <br>

    Thank you for your responses. Please click the submit button.<br><br><br>
    <a href="javascript:SaveData()" class = 'PressButton'>Submit</a>

    <br><br><br><br>
</div> 

<div class = "TestScreen" id = "TestScreen">
    <body>
        <div class = "ResponseButton" id = "ResponseButton"> 
            <div id = "ResponseButton_instr"></div>
        </div>
        <div class = "StimWindow" id = "StimWindow" >    
            <div class = "Instruction">
                <p> 
                    <!-- <br><br> -->
                    <p style = "color:red"> In this experiment, <br><br>Your job is to REMEMBER what <b>objects</b> you saw 
                    and the <b>time</b> when you saw them <br></p>
                    <br>
                    Items will appear on the screen for 3 seconds each at different locations. Some items will show up twice. <br>
                    <b>If you saw the item before,</b> respond on the time bar when in the training portion you saw it (in terms of start to end order).
                    <br><br>
                    <b>If you have not seen it before,</b> click in the purple box to the right. 
                    <br><br>
                    You will receive feedback on whether you are right or wrong about the old/new decision. <br>
                    You will NOT receive feedback on your temporal decision.
                    <br><br><br>

                    <i>If the image size is too small, please enter the browser into full screen, and refresh the webpage to restart. </i>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:startAudioCheck()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">NEXT</a>
                    
                </div>
            </div>

            <div class = "audioCheck" id = "audioCheck"> 
                <br><br><br><br><br><br><br>
                In the experiment, we will provide you with audio feedback. <br>
                Before starting the experiment, please adjust your volume and make sure that you can clearly hear the sound effect when clicking on the buttons below. <br>
                <br><br>

                <button onclick="playSound_pos()" id="ACButton" style = "color:green; border-color: green" > CORRECT </button>
                <button onclick="playSound_neg()" id="ACButton" style = "color:maroon; border-color: maroon " > WRONG </button>

                <br><br><br>
                <div class = 'StartButton'> 
                    <a href="javascript:startExp()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Click to Start the Experiment</a>       
                </div>
            </div>

            <div class = "Instruction2" id = "Instruction2">
                <p> 
                    <br><br><br>
                    You have finished part 1. 
                    <br><br>

                    Now we will ask you again about the displays you saw earlier. Do your best. 
                    <br><br>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:NextTrial_retest()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Click here to start Part 2 </a>
    
                </div>
            </div>

            <div class = "TestingEnds" id = "TestingEnds">
                <p> 
                    <br><br><br><br><br><br>
                    You have completed the experiment. Your accuracy for the old/new response is <span id="Practice_Accuracy"></span>%. <br><br>


                    <br><br> <br><br>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:ExpEnd()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Continue </a>
    
                </div>
            </div>

            <div class = "PracticeEnd" id = "PracticeEnd">
                <p> 
                    <br><br><br>
                    Great! You have completed the practice. <br><br>

                    Now you will start the main experiment. Please answer as quickly and accurately as you can. <br><br>

                    The main experiment takes about 45 min 
                    <br><br>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:startTesting()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Click here to begin </a>
    
                </div>
            </div>

            <div class = "viewingEnd" id = "viewingEnd">
                <p> 
                    <br><br><br>
                    You have viewed all the images. <br><br>

                    Now we will show you one image at a time. If you have seen the image before, please estimate when that item appeared during the viewing block and respond using the time bar. <br><br>

                    If you have not seen the image before, click on the purple button on the right.
                   
                    <br><br>
                </p>
    
                <div class = 'StartButton'> 
                    <a href="javascript:TestingBlock_setup()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Click here to begin </a>
    
                </div>
            </div>

            <div class = "EndPage" id = "EndPage">
                <p> 
                    <br><br><br> <br><br><br>
                    Done! You have finished the experiment. You can close the window now. 

                    <br><br>

                    Thanks.
                    <br><br>
                </p>
    
            </div>

            <header class="headboard" id = "headboard" style= "background-color:transparent;">   </header>
            <div class = "myProgress" id = "myProgress" >
                 <div class = "myBar" id = "myBar">
                     <div id = "myBar_start">Start</div>
                    <div id = 'myBar_now'>End</div>
                    </div>
            </div>
            <canvas id="StimCanvas" style = "cursor:pointer" > </canvas>
        </div>

        <div class = "DisplayWindow" id = "DisplayWindow">    
            <div id = "DisplayWindow_img"></div>
            <div id = "DisplayWindow_instr"> Click Old Location <br> or Click in New Box</div>
        </div>
    </body>
</div>

<!--Break screen -->
<div class = "Break" id = "Break">
    <p> 
        <br><br><br>
        Click NEXT to start trial <span id="trleft">1</span>/<span id="tr-total">20</span>
    </p>

    <div class = 'StartButton'> 
        <a href="javascript:DisplaySetup()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Next</a>

    </div>
</div>

<div class = "Break_retest" id = "Break_retest">
    <p> 
        <br><br><br>
        Click NEXT to start retest trial <span id="trleft2">1</span>/<span id="tr-total2">20</span>
    </p>

    <div class = 'StartButton'> 
        <a href="javascript:NextTrial_retest()" class="nextButton" id="nextTrialButton" style="text-decoration: none;">Next</a>

    </div>
</div>


```
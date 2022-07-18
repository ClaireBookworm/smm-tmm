    <!-- ROUND TWO with full instructions! -->


    <div class="TestScreen" id="TestScreenP2">

        <body>
            <div class="ResponseButton" id="ResponseButton">
                <div id="ResponseButton_instr"></div>
            </div>
            <div class="StimWindow" id="StimWindow">
                <div class="Instruction">
                    <p>
                    <p style="color:red"> In this second round, <br><br>your job is to REMEMBER what <b>objects</b> you
                        saw and the <b>locations</b> where you saw them, and the <b>time</b> when you saw them, as
                        you've
                        been tested previously. <br></p>
                    <br>
                    Life before, items will appear on the screen for 3 seconds each at different locations. Some items
                    will show up twice. <br>
                    <b>If you saw the item before,</b> click the location on the screen where you thought you saw it
                    (Guess if you need to). Then, respond on the time bar when in the training portion you saw it (in
                    terms of start to end order).
                    <br><br>
                    <b>If you have not seen it before,</b> click in the purple box to the right.
                    <br><br>
                    You will receive feedback on whether you are right or wrong about the old/new decision. <br>
                    You will still NOT receive feedback on your spatial and temporal decision.
                    <br><br><br>
                    </p>

                    <div class='StartButton'>
                        <a href="javascript:startAudioCheck()" class="nextButton" id="nextTrialButton"
                            style="text-decoration: none;">NEXT</a>

                    </div>
                </div>

                <div class="audioCheck" id="audioCheck">
                    <br><br><br><br><br><br><br>
                    Please check your audio feedback again, or, if not needed, press next to continue. <br>
                    Before starting the experiment, please adjust your volume and make sure that you can clearly hear
                    the sound effect when clicking on the buttons below. <br>
                    <br><br>

                    <button onclick="playSound_pos()" id="ACButton" style="color:green; border-color: green"> CORRECT
                    </button>
                    <button onclick="playSound_neg()" id="ACButton" style="color:maroon; border-color: maroon "> WRONG
                    </button>

                    <br><br><br>
                    <div class='StartButton'>
                        <a href="javascript:startExp()" class="nextButton" id="nextTrialButton"
                            style="text-decoration: none;">Click to Start the Experiment</a>
                    </div>
                </div>

                <div class="Instruction2" id="Instruction2">
                    <p>
                        <br><br><br>
                        You have finished part 1 of round 2.
                        <br><br>

                        Now we will ask you again about the displays you saw earlier. Do your best.
                        <br><br>
                    </p>

                    <div class='StartButton'>
                        <a href="javascript:NextTrial_retest()" class="nextButton" id="nextTrialButton"
                            style="text-decoration: none;">Click here to start Part 2 </a>

                    </div>
                </div>

                <div class="TestingEnds" id="TestingEnds">
                    <p>
                        <br><br><br><br><br><br>
                        You have completed the experiment. Your accuracy for the old/new response is <span
                            id="Practice_Accuracy"></span>%. <br><br>


                        <br><br> <br><br>
                    </p>

                    <div class='StartButton'>
                        <a href="javascript:ExpEnd()" class="nextButton" id="nextTrialButton"
                            style="text-decoration: none;">Continue </a>

                    </div>
                </div>

                <div class="PracticeEnd" id="PracticeEnd">
                    <p>
                        <br><br><br>
                        Great! You have completed the practice. <br><br>

                        Now you will start the main experiment. Please answer as quickly and accurately as you can.
                        <br><br>

                        The main experiment takes about 45 min
                        <br><br>
                    </p>

                    <div class='StartButton'>
                        <a href="javascript:startTesting()" class="nextButton" id="nextTrialButton"
                            style="text-decoration: none;">Click here to begin </a>

                    </div>
                </div>

                <div class="viewingEnd" id="viewingEnd">
                    <p>
                        <br><br><br>
                        You have viewed all the images. <br><br>

                        Now we will show you one image at a time. If you have seen the image before, click on the
                        location where you have seen it. <br><br>

                        Additionally, please estimate when that item appeared during the viewing block and respond using
                        the time bar. <br><br>

                        If you have not seen the image before, click on the purple button on the right.

                        <br><br>
                    </p>

                    <div class='StartButton'>
                        <a href="javascript:TestingBlock_setup()" class="nextButton" id="nextTrialButton"
                            style="text-decoration: none;">Click here to begin </a>

                    </div>
                </div>

                <div class="EndPage" id="EndPage">
                    <p>
                        <br><br><br> <br><br><br>
                        Done! You have finished the experiment. You can close the window now.

                        <br><br>

                        Thanks.
                        <br><br>
                    </p>

                </div>

                <header class="headboard" id="headboard" style="background-color:transparent;"> </header>
                <div class="myProgress" id="myProgress">
                    <div class="myBar" id="myBar">
                        <div id="myBar_start">Start</div>
                        <div id='myBar_now'>End</div>
                    </div>
                </div>
                <canvas id="StimCanvas" style="cursor:pointer"> </canvas>
            </div>

            <div class="DisplayWindow" id="DisplayWindow">
                <div id="DisplayWindow_img"></div>
                <div id="DisplayWindow_instr"> Click Old Location <br> or Click in New Box</div>
            </div>
        </body>
    </div>

// ****** NOTE ******
// This code was modified several times, some of the variables and params listed below may come from
// an earlier version and no longer used in the current experiment

// PARAMETERS
var MemSetSize = 3; //150;//25;//15;
var PresentationTime = 3000; //000//00//00;//2000; // Presentation time of each item, in millisec
var holdtime = 100; //
var trialtotal = 12;
var Num_boxes = 49;
var IncludeBackGroundBoxes = 1; // 1 = box visible, 0 = box unvisible
var imageSizeParam = 0.9; // default = 0.9;
var practiceOn = 0; // 1= include practice, 0 = go straight into experiment.
var viewingBlock_instr =
  "Try to remember the identity and location of each item";

// STIMULUS VARIABLES
var ImgList_all = [];
var AllTestImage = [];
var Tar_list;
var Dis_list;
var totalImgNum = 2400;
var save_jitterX = [];
var save_jitterY = [];
var trial_img_loc; // save image location in pix [x,y]
var trial_img_row_column;
var trial_jitter_x; // save jitter of box location for redrawing
var trial_jitter_y; // save jitter of box location for redrawing
var toggle1;
var viewImgCounter = -1;
var testingCounter = -1;
var testingCounter_dis = -1;
var testingCounter_tar = -1;

var trCount = document.querySelector("#trleft");
var trTotal = document.querySelector("#tr-total");
var trCount2 = document.querySelector("#trleft2");
var trTotal2 = document.querySelector("#tr-total2");
trTotal.textContent = trialtotal;
trTotal2.textContent = trialtotal;
var thisAccuracy;
var FinalAccuracy = document.querySelector("#Practice_Accuracy");

//n-Back new Variables
var count_Allimages = 0;
var OldList = [];
var isOld_item;
var imgClick;
var ImageOnTime;
var GetThisImageLoc;
var save_clickLoc;
var thisImageLoc;
var thisImage;
var ClickRegistered = 0;
var timer1;
var OldOrNewList;
var TimeBarLoc_1st = -1;
var timeBarLoc_resp = -1;
var test_accuracy = [];

// SAVE VARIABLES
var curID_save;
var trialResult_save;
var save_blockNum;
var save_blockName;
var save_response;
var save_isCorrect;
var itemLoc_appear;
var save_itemRowColumn;
var get_clickLoc;
var save_RT;
var thisImageID;
var save_allResult = [];
var test_timeStamp;
var view_timeStamp;
var thisImage_viewInd;

//SET UP CANVAS CCC
// set canvas width and height equal to stimwindow.
var $StimCanvas = $("#StimCanvas"),
  $StimWin = $(".StimWindow");
$StimCanvas.attr({ width: $StimWin.width(), height: $StimWin.height() });
var CanvasHeight = document.getElementById("StimCanvas").clientHeight;
var CanvasWidth = document.getElementById("StimCanvas").clientWidth;
var BoxSize = CanvasHeight / 9; //CanvasHeight/9;
var MarginLeft = -CanvasHeight / 14;
var MarginUp = -CanvasHeight / 10; // CanvasHeight/20;
var GapSize = CanvasHeight / 75;
const canvas = document.querySelector("#StimCanvas");
const respbutton = document.querySelector("#ResponseButton");
const myProgressBar = document.querySelector("#myProgress");

// PREPARE IMAGE LIST
function CreateImageList() {
  for (var ImgInd = 1; ImgInd <= 2400; ImgInd++) {
    var GetImg =
      "https://search.bwh.harvard.edu/OnlineExperiment/SpatialMassiveMemory/Images/Object" +
      ImgInd +
      ".jpg";
    var curItem = {
      GetImg,
      id: ImgInd,
    };
    ImgList_all.push(curItem);
  }
  ImgList_all = shuffle(ImgList_all);
  Tar_list = ImgList_all.slice(0, MemSetSize);
  Dis_list = ImgList_all.slice(MemSetSize, MemSetSize * 2);
  AllTestImage = AllTestImage.concat(Tar_list, Dis_list);
  AllTestImage = shuffle(AllTestImage);
  //Tar_list_prac = ImgList_all.slice(MemSetSize*2, MemSetSize*2+MemSetSize_prac)
  //Dis_list_prac = ImgList_all.slice(MemSetSize*2+MemSetSize_prac, MemSetSize*2+MemSetSize_prac*2)
}

CreateImageList();

// SET UP CANVAS
var c = document.getElementById("StimCanvas");
var ctx = c.getContext("2d");

/*-----------------------------------------------------------------------------------------------------------------------------------------------------*/
/*-----------------------------------------------------------------------------------------------------------------------------------------------------*/
/*-----------------------------------------------------------------------------------------------------------------------------------------------------*/
$("#TestScreen").hide();
$(".checkbox").click(AcceptHIT);

function AcceptHIT() {
  $("#Start_Experiment").show();
  //openFullscreen()
}

//START TESTING
function consented() {
  $("#Consent").hide();
  $("#TestScreen").show();
}

function startAudioCheck() {
  $(".Instruction").hide();
  $("#audioCheck").show();
}

function startExp() {
  experimentStartTime = new Date().getTime();
  console.log("Experiment start at " + experimentStartTime);
  curID_save = experimentStartTime;

  $("#audioCheck").hide();
  $(".Instruction").hide();
  $("#DisplayWindow").show();
  $("#DisplayWindow_instr").show();
  $("#StimCanvas").show();
  $("#headboard").show();
  $("#myProgress").hide();
  document.getElementById("DisplayWindow").style = "background-color: white;";

  if (practiceOn == 1) {
    startPractice();
  } else {
    startTesting();
  }
}

/*function startPractice (){
        $("#PracticeEnd_notpass").hide();
        $("#DisplayWindow").hide();
        $("#DisplayWindow_instr").show();
        $("#StimCanvas").show();
        $("#headboard").show();
        $('#myProgress').show();

        save_blockNum = 1;
        save_blockName = 'Practice';

        OldOrNewList_prac=[];
        OldList = [];
        OldOrNewList = OldOrNewList_prac;
        DisplaySetup();
        test_accuracy = [];
    }*/

function startTesting() {
  $("#PracticeEnd").hide();
  $("#DisplayWindow").show();
  $("#DisplayWindow_instr").show();
  $("#StimCanvas").show();
  $("#headboard").show();
  $("#myProgress").hide();

  save_blockNum = 1;
  save_blockName = "Test";
  OldList = [];
  DisplaySetup();
}

// A. START A TRIAL
function DisplaySetup() {
  $("#TestScreen").show();
  $("#Break").hide();

  //clear and set up display
  $("#DisplayWindow").hide();
  document.getElementById("ResponseButton_instr").innerHTML = " ";
  document.getElementById("ResponseButton").style = "background-color: white;";
  //change headboard instruction
  document.getElementById("headboard").innerHTML = viewingBlock_instr; // ccc
  document.getElementById("headboard").style.fontSize = "100%";

  //clean and set up canvas
  ctx.clearRect(0, 0, CanvasHeight, CanvasWidth);
  //DRAW BOXES AND SAVE LOCATIONS
  var BoxCount = 0;
  trial_img_loc = [];
  trial_jitter_x = [];
  trial_jitter_y = [];
  trial_img_row_column = [];
  for (var nbox = 1; nbox <= 7; nbox++) {
    //for each column
    for (var nRow = 1; nRow <= 7; nRow++) {
      // for each row
      // draw box to current loc
      var jitterX = randomIntFromInterval(
        -CanvasHeight / 55,
        CanvasHeight / 55
      );
      var jitterY = randomIntFromInterval(
        -CanvasHeight / 55,
        CanvasHeight / 55
      );
      var xx = MarginLeft + BoxSize * nbox + GapSize * nbox + jitterX;
      var yy = MarginUp + BoxSize * nRow + GapSize * nRow + jitterY;

      if (IncludeBackGroundBoxes == 1) {
        ctx.beginPath();
        ctx.rect(xx, yy, BoxSize, BoxSize);
        ctx.closePath();
        ctx.lineWidth = 1;
        ctx.stroke();
      }

      //save jtter for redrawing boxes
      trial_jitter_x.push(jitterX);
      trial_jitter_y.push(jitterY);
      // save xy coor
      trial_img_loc.push([xx, yy]);
      trial_img_row_column.push([nRow, nbox]);
    }
  }

  ViewingBlock();
}

// show n images one by one, n = MemSetSize
function ViewingBlock() {
  // loop func:Viewing Block until all target images are shown
  if (viewImgCounter + 1 < MemSetSize) {
    viewImgCounter++;
    // which image
    thisImage = Tar_list[viewImgCounter];
    thisImageID = thisImage.id; // find id of this image
    thisImage = thisImage.GetImg;
    // what location
    itemLocInd_1st = randomIntFromInterval(0, Num_boxes - 1); // get a random location
    // what time
    TimeBarLoc_1st = ((viewImgCounter + 1) / Tar_list.length) * 100;

    // LOAD IMAGE
    GetThisImageLoc = trial_img_loc[itemLocInd_1st];
    loadImage(thisImage, GetThisImageLoc);
    // Remove Image after presentationtime
    timer1 = setTimeout(function () {
      // after 3000ms
      //clear present image
      clearThisImage(GetThisImageLoc);
      ViewingBlock();
    }, PresentationTime);

    // save to list
    OldList.push([
      thisImage,
      thisImageID,
      itemLocInd_1st,
      viewImgCounter,
      TimeBarLoc_1st,
      ImageOnTime,
    ]);
  } else {
    // if all targets have been shown, present testingBlock instruction
    $("#DisplayWindow").hide();
    $("#DisplayWindow_instr").hide();
    $("#StimCanvas").hide();
    $("#headboard").hide();
    $("#myProgress").hide();
    $("#viewingEnd").show();
  }
}

function TestingBlock_setup() {
  OldOrNewList_test = []; // 1 = new, 2 = old
  var aaa = Array(MemSetSize).fill(1);
  var bbb = Array(MemSetSize).fill(0);
  OldOrNewList_test = OldOrNewList_test.concat(aaa, bbb);
  OldOrNewList_test = shuffle(OldOrNewList_test);

  $("#viewingEnd").hide();
  $("#DisplayWindow").show();
  $("#DisplayWindow_instr").show();
  $("#StimCanvas").show();
  $("#headboard").show();
  $("#myProgress").show();
  document.getElementById("ResponseButton_instr").innerHTML =
    "Click here if this is a new item";
  document.getElementById("ResponseButton").style =
    " background-color:rgba(196, 182, 233, 0.932);";
  TestingBlock();

  var elem = document.getElementById("myBar");
  var width = 100; // this is the width of the bar
  elem.style.width = width + "%";
}

var view_timeStamp;
function TestingBlock() {
  save_clickLoc = [-1, -1];
  imgClick = 0; //reset click variable; 0 = no click has been registered

  if (testingCounter + 1 < MemSetSize * 2) {
    testingCounter++;
    //Reset previous location in case values are saved incorrectly
    isOld_item = -1;
    TimeBarLoc_1st = -1;

    //  0 = new distractor
    if (OldOrNewList_test[testingCounter] == 0) {
      testingCounter_dis++;
      //get distractor image
      thisImage = Dis_list[testingCounter_dis];
      thisImageID = thisImage.id; // find id of this image
      thisImage = thisImage.GetImg;
      isOld_item = 0;
      thisImage_viewInd = -1;
      view_timeStamp = -1;
    } else {
      //if 1 = old target
      isOld_item = 1;
      testingCounter_tar++;
      // pick one old item randomly
      var Rand_oldItem = randomIntFromInterval(0, OldList.length - 1);
      var thisOldItem = OldList[Rand_oldItem]; // reture 2x2 array [thisImageID,itemLocInd_1st]
      thisImage = thisOldItem[0];
      thisImageID = thisOldItem[1];
      itemLocInd_1st = thisOldItem[2];
      thisImage_viewInd = thisOldItem[3];
      TimeBarLoc_1st = thisOldItem[4];
      view_timeStamp = thisOldItem[5];
      // remove this image from old list
      OldList.splice(Rand_oldItem, 1); //remove array with the current index, 1 stands for remove one array starting from 'Rand_oldItem' position
    }

    // LOAD IMAGES on the left of the screen and enable click
    document.getElementById("DisplayWindow_img").innerHTML =
      "<img src = '" +
      thisImage +
      "' ImgId = '" +
      thisImageID +
      "' style =  height:15%; width:15%" +
      ">";
    test_timeStamp = new Date().getTime();
    console.log("image test at ", test_timeStamp);
    canvas.addEventListener("click", Click_canvas);
    respbutton.addEventListener("click", Click_newLoc);
  } else {
    // get accuracy
    var sum = test_accuracy.reduce(function (a, b) {
      return a + b;
    }, 0);
    thisAccuracy = (sum / test_accuracy.length) * 100;
    var roundedAccuracy = Math.round(thisAccuracy * 10) / 10;
    FinalAccuracy.textContent = roundedAccuracy;

    $("#TestingEnds").show();
    $("#DisplayWindow").hide();
    $("#DisplayWindow_instr").hide();
    $("#StimCanvas").hide();
    $("#headboard").hide();
    $("#myProgress").hide();

    document.getElementById("ResponseButton_instr").innerHTML = " ";
    document.getElementById("ResponseButton").style =
      "background-color: white;";
  }
}

function ExpEnd() {
  $("#StimCanvas").hide();
  $("#headboard").hide();
  $("#TestScreen").hide();
  $("#demographic").show();
  document.getElementById("DisplayWindow").style =
    "background-color:rgba(196, 182, 233, 0.932);";
}

// -------------------------------------------------------------------------------------------------------------------------------------//
// -------------------------------------------------------- Helper functions -----------------------------------------------------------//
// -------------------------------------------------------------------------------------------------------------------------------------//

function moveBar() {
  var elem = document.getElementById("myBar");
  var width = ((count_Allimages + 1) / OldOrNewList.length) * 100; // this is the width of the bar

  elem.style.width = width + "%";
  //elem.innerHTML = width + "%";
}

function clearThisImage(GetThisImageLoc) {
  ctx.clearRect(
    GetThisImageLoc[0] + BoxSize * 0.05,
    GetThisImageLoc[1] + BoxSize * 0.05,
    BoxSize * imageSizeParam,
    BoxSize * imageSizeParam
  );
}

function loadImage(thisImage, GetThisImageLoc) {
  //Loading of the home test image
  var showImage = new Image();
  //drawing of the test image
  showImage.onload = function () {
    //draw background image
    ctx.drawImage(
      showImage,
      GetThisImageLoc[0] + BoxSize * 0.05,
      GetThisImageLoc[1] + BoxSize * 0.05,
      BoxSize * imageSizeParam,
      BoxSize * imageSizeParam
    );
  };
  showImage.src = thisImage; //.GetImg;
  ImageOnTime = new Date().getTime();
  console.log("image viewed at", ImageOnTime);
}

function GetTime() {
  myProgressBar.addEventListener("click", Click_bar);

  //clean boxes
  ctx.clearRect(0, 0, CanvasHeight, CanvasWidth);
  ctx.font = "1rem Arial";
  ctx.fillText(
    "Don't forget to mark when you saw this item on the timeline at the top! ",
    CanvasHeight / 18,
    CanvasWidth / 3
  );
  ctx.fillText("", CanvasHeight / 18, CanvasWidth / 2.5);
}

function redrawBoxes() {
  //clean boxes
  ctx.clearRect(0, 0, CanvasHeight, CanvasWidth);
  for (var nbox = 0; nbox < 49; nbox++) {
    var thisLoc1 = trial_img_loc[nbox];
    ctx.beginPath();
    ctx.rect(thisLoc1[0], thisLoc1[1], BoxSize, BoxSize);
    ctx.closePath();
    ctx.lineWidth = 1;
    ctx.stroke();
  }
}

var Click_bar = function (e) {
  if (isOld_item == 1) {
    //clicked when the item was old --> old/new correct

    playSound_pos();

    document.getElementById("headboard").innerHTML =
      "Correct! This is an old item";
    document.getElementById("headboard").style.color = "green";
    document.getElementById("headboard").style.fontSize = "150%";
    save_isCorrect = 1;
    test_accuracy = test_accuracy.concat(1);
    toggle1 = setTimeout(function () {
      document.getElementById("headboard").innerHTML = " ";
      document.getElementById("headboard").style.color = "black";
      document.getElementById("headboard").style.fontSize = "150%";
    }, 1000);
  } else {
    playSound_neg();
    test_accuracy = test_accuracy.concat(0);

    document.getElementById("headboard").innerHTML =
      "Wrong! This is a new item";
    document.getElementById("headboard").style.color = "maroon";
    document.getElementById("headboard").style.fontSize = "150%";

    save_isCorrect = 0;
    toggle1 = setTimeout(function () {
      document.getElementById("headboard").innerHTML = " ";
      document.getElementById("headboard").style.color = "black";
      document.getElementById("headboard").style.fontSize = "150%";
    }, 1000);
  }

  //playSound_neu2();
  myProgressBar.removeEventListener("click", Click_bar);
  var max = $(this).width(); //Get width element
  var pos = e.pageX - $(this).offset().left; //Position cursor

  console.log(max, pos);
  timeBarLoc_resp = (pos / max) * 100;
  ClickSummary();

  setTimeout(function () {
    ctx.clearRect(0, 0, CanvasHeight, CanvasWidth);
    redrawBoxes();
  }, 500);

  setTimeout(function () {
    TestingBlock();
  }, 1000);
};

var Click_canvas = function (e) {
  //clearThisImage(GetThisImageLoc)
  //clearTimeout(timer1);
  save_response = "SaidOld";
  imgClick = 1;

  getCursorPosition(canvas, e);
  canvas.removeEventListener("click", Click_canvas); // disable click on screen
  respbutton.removeEventListener("click", Click_newLoc); // disable click on screen
  save_RT = new Date().getTime() - ImageOnTime; //XXXX

  playSound_neu2();
  /*
        if (isOld_item == 1){ //clicked when the item was old --> old/new correct 

            playSound_pos();
            
            document.getElementById("headboard").innerHTML = "Correct! This is an old item"
            document.getElementById("headboard").style.color = "green"
            document.getElementById("headboard").style.fontSize = '150%'

            save_isCorrect = 1;
            toggle1= setTimeout(function() {
                document.getElementById("headboard").innerHTML = " "
                document.getElementById("headboard").style.color = "black"
                document.getElementById("headboard").style.fontSize = '150%'
            },1000)

        }else {
            playSound_neg();
        
            document.getElementById("headboard").innerHTML = "Wrong! This is a new item"
            document.getElementById("headboard").style.color = "maroon"
            document.getElementById("headboard").style.fontSize = '150%'

            save_isCorrect = 0;
            toggle1= setTimeout(function() {
                document.getElementById("headboard").innerHTML = " "
                document.getElementById("headboard").style.color = "black"
                document.getElementById("headboard").style.fontSize = '150%'

            },1000)

        }
        */
  GetTime();
};

var Click_newLoc = function (e) {
  clearThisImage(GetThisImageLoc);
  clearTimeout(timer1);
  imgClick = 0;

  save_response = "SaidNew";
  respbutton.removeEventListener("click", Click_newLoc); // disable click on screen
  canvas.removeEventListener("click", Click_canvas); // disable click on screen
  save_RT = new Date().getTime() - ImageOnTime; //XXXX
  timeBarLoc_resp = -1;

  if (isOld_item == 0) {
    //clicked when the item was old --> old/new correct

    playSound_pos();

    document.getElementById("headboard").innerHTML =
      "Correct! This is a new item";
    document.getElementById("headboard").style.color = "green";
    document.getElementById("headboard").style.fontSize = "150%";

    save_isCorrect = 1;
    test_accuracy = test_accuracy.concat(1);
    toggle1 = setTimeout(function () {
      document.getElementById("headboard").innerHTML = " ";
      document.getElementById("headboard").style.color = "black";
      document.getElementById("headboard").style.fontSize = "150%";
    }, 1000);
  } else {
    playSound_neg();
    test_accuracy = test_accuracy.concat(0);

    document.getElementById("headboard").innerHTML =
      "Wrong! This is an old item";
    document.getElementById("headboard").style.color = "maroon";
    document.getElementById("headboard").style.fontSize = "150%";

    save_isCorrect = 0;
    toggle1 = setTimeout(function () {
      document.getElementById("headboard").innerHTML = " ";
      document.getElementById("headboard").style.color = "black";
      document.getElementById("headboard").style.fontSize = "150%";
    }, 1000);
  }
  ClickSummary();

  setTimeout(function () {
    TestingBlock();
  }, 500);
};

function ClickSummary() {
  //var xy_thisImage =[GetThisImageLoc[0]+BoxSize*0.05+BoxSize*0.90/2, GetThisImageLoc[1]+BoxSize*0.05+BoxSize*0.90/2 ]
  var xy_1st_raw = trial_img_loc[itemLocInd_1st];
  var xy_1st = [
    xy_1st_raw[0] + BoxSize * 0.05 + (BoxSize * 0.9) / 2,
    xy_1st_raw[1] + BoxSize * 0.05 + (BoxSize * 0.9) / 2,
  ];

  var rc_1st = trial_img_row_column[itemLocInd_1st];

  var euclidianDistance;
  var clickLoc_row;
  var clickLoc_column;
  var timeBarError;

  if (imgClick == 1) {
    //save_response = 'SaidOld';
    euclidianDistance = Math.sqrt(
      (xy_1st[0] - save_clickLoc[0]) ** 2 + (xy_1st[1] - save_clickLoc[1]) ** 2
    );
    clickLoc_row = Math.round(
      (save_clickLoc[1] - MarginUp - BoxSize * 0.5) / (BoxSize + GapSize)
    );
    clickLoc_column = Math.round(
      (save_clickLoc[0] - MarginLeft - BoxSize * 0.5) / (BoxSize + GapSize)
    );
    TimeError_RespMinus1stAppear = timeBarLoc_resp - TimeBarLoc_1st;
  } else {
    //save_response = 'SaidNew';
    euclidianDistance = -1;
    clickLoc_row = -1;
    clickLoc_column = -1;
    TimeError_RespMinus1stAppear = -1;
  }

  console.log(euclidianDistance);
  trialResult_save = {
    blockName: save_blockName,
    Setsize: MemSetSize, //
    cueLength: PresentationTime, //
    test_ind: testingCounter + 1,
    test_timeStamp: test_timeStamp,
    view_ind: thisImage_viewInd + 1,
    view_timeStamp: view_timeStamp,
    "1=OldItem": isOld_item, //
    Response: save_response, //
    "1=correct": save_isCorrect, //r
    viewLoc_index: itemLocInd_1st, //
    viewLoc_x: xy_1st[0],
    viewLoc_y: xy_1st[1],
    viewLoc_row: rc_1st[0], //
    viewLoc_col: rc_1st[1], //
    clickLoc_x: save_clickLoc[0], //
    clickLoc_y: save_clickLoc[1], //
    clickLoc_row: clickLoc_row, //
    clickLoc_column: clickLoc_column, //
    Euclidian_distance: euclidianDistance, //
    TimeBarLoc_1st: TimeBarLoc_1st,
    TimeBarLoc_resp: timeBarLoc_resp,
    TimeError_RespMinus1stAppear: TimeError_RespMinus1stAppear,
    RT: save_RT,
    LapseTimeSinceExpStart: new Date().getTime() - experimentStartTime,
    imageID: thisImageID,
    CanvasHeight: CanvasHeight,
    CanvasWidth: CanvasWidth,
  };

  save_allResult.push(trialResult_save); //aaa
  console.log(trialResult_save);
  saveData_toServer(trialResult_save);
}

function getCursorPosition(canvas, event) {
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  console.log("x: " + x + " y: " + y);
  save_clickLoc = [x, y];
}

//Play sounds
function playSound_pos() {
  var audio = new Audio(
    "https://search.bwh.harvard.edu/OnlineExperiment/SpatialMassiveMemory/Sounds/Pos1.wav"
  );
  audio.play();
}
function playSound_neu() {
  //var sound = document.getElementById("audio_neu");
  var audio = new Audio(
    "https://search.bwh.harvard.edu/OnlineExperiment/SpatialMassiveMemory/Sounds/Neutralclick.wav"
  );
  audio.play();
}
function playSound_neg() {
  var audio = new Audio(
    "https://search.bwh.harvard.edu/OnlineExperiment/SpatialMassiveMemory/Sounds/Neg3.wav"
  );
  audio.play();
}

function playSound_neu2() {
  var audio = new Audio(
    "https://search.bwh.harvard.edu/OnlineExperiment/SpatialMassiveMemory/Sounds/Pos_jump.wav"
  );
  audio.play();
}

function randomIntFromInterval(min, max) {
  // min and max included
  return Math.floor(Math.random() * (max - min + 1) + min);
}

function shuffle(a) {
  var j, x, i;
  for (i = a.length - 1; i > 0; i--) {
    j = Math.floor(Math.random() * (i + 1));
    x = a[i];
    a[i] = a[j];
    a[j] = x;
  }
  return a;
}

function SaveData() {
  // save demographic info
  //age
  var d_age = "empty";
  d_age = document.getElementById("age").value;
  //gender
  var check_F = document.getElementById("female").checked;
  var check_M = document.getElementById("male").checked;
  var check_O = document.getElementById("other").checked;
  var check_NA = document.getElementById("genderNoResponse").checked;
  var d_gender = "empty";
  if (check_F == 1) {
    d_gender = "female";
  } else if (check_M == 1) {
    d_gender = "male";
  } else if (check_O == 1) {
    d_gender = "other";
  } else if (check_NA == 1) {
    d_gender = "noResponse";
  }
  //citizen
  var d_citizen = "empty";
  var check_Cyes = document.getElementById("isCitizen").checked;
  var check_Cno = document.getElementById("notCitizen").checked;
  if (check_Cyes == 1) {
    d_citizen = "Yes";
  } else if (check_Cno == 1) {
    d_citizen = "No";
  }
  //ethnicity
  var d_ethnicity = "empty";
  var check_HL = document.getElementById("HL").checked;
  var check_notHL = document.getElementById("notHL").checked;
  if (check_HL == 1) {
    d_ethnicity = "Hispanic or Latino";
  } else if (check_notHL == 1) {
    d_ethnicity = "Not Hispanic or Latino";
  }
  //race
  var d_race = [];
  var check_AIAN = document.getElementById("AIAN").checked;
  var check_asian = document.getElementById("asian").checked;
  var check_NH = document.getElementById("NH").checked;
  var check_black = document.getElementById("black").checked;
  var check_white = document.getElementById("white").checked;
  var check_unsure = document.getElementById("unsure").checked;
  var check_raceOther = document.getElementById("raceOther").checked;
  if (check_AIAN == 1) {
    d_race = d_race + "American Indian/Alaska Native;";
  }
  if (check_asian == 1) {
    d_race = d_race + "Asian;";
  }
  if (check_NH == 1) {
    d_race = d_race + "Native Hawaiian or Other Pacific Islander;";
  }
  if (check_black == 1) {
    d_race = d_race + "Black or African American;";
  }
  if (check_white == 1) {
    d_race = d_race + "White;";
  }
  if (check_unsure == 1) {
    d_race = d_race + "Unsure/prefer not to respond;";
  }
  if (check_raceOther == 1) {
    d_race = d_race + "Other;";
  }

  var OsComments = "empty";
  OsComments = $("#AddComments").val();

  var OsmTurkId = "empty";
  OsmTurkId = $("#mTurkId").val();

  var newDate = new Date();
  d = {
    curID: curID_save,
    curTime: newDate.today() + " @ " + newDate.timeNow(),
    userAgent: navigator.userAgent,
    windowWidth: $(window).width(),
    windowHeight: $(window).height(),
    screenWidth: screen.width,
    screenHeight: screen.height,
    duration_ms: new Date().getTime() - experimentStartTime,
    d_age: d_age,
    d_gender: d_gender,
    d_citizen: d_citizen,
    d_ethnicity: d_ethnicity,
    d_race: d_race,
    d_comments: OsComments,
    d_mTurkID: OsmTurkId,
  };

  saveData_toServer(d);

  for (var i = 0; i < save_allResult.length; i++) {
    saveData_toServer2(save_allResult[i]);
  }
  saveData_toServer2(d);

  alert("Your data are saved. Thank you for participating!");
}

function saveData_toServer(thisData) {
  $("#demographic").hide();

  filename = curID_save + "_TMM.txt"; //"2.txt"
  filedata = JSON.stringify(thisData); //"data, (this can be a csv string or JSON or whatever data representation"
  console.log(filename, filedata, "saveData_toServer");
  $.ajax({
    //this requires jQuery
    type: "post",
    cache: false,
    url: "./save_data.php", // this is the path to the PHP script
    data: {
      filename: filename,
      filedata: filedata,
    },
    success: function (msg) {
      console.log("This is the successful callback");
    },
  });
}

function saveData_toServer2(thisData) {
  filename = curID_save + "_TMM_backup.txt"; //"2.txt"
  filedata = JSON.stringify(thisData); //"data, (this can be a csv string or JSON or whatever data representation"
  console.log(filename, filedata);
  $.ajax({
    //this requires jQuery
    type: "post",
    cache: false,
    url: "./save_data.php", // this is the path to the PHP script
    data: {
      filename: filename,
      filedata: filedata,
    },
    success: function (msg) {
      console.log("This is the successful callback");
    },
  });
}

/* Get the documentElement (<html>) to display the page in fullscreen */
var elem = document.documentElement;

/* View in fullscreen */
function openFullscreen() {
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.mozRequestFullScreen) {
    /* Firefox */
    elem.mozRequestFullScreen();
  } else if (elem.webkitRequestFullscreen) {
    /* Chrome, Safari and Opera */
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) {
    /* IE/Edge */
    elem.msRequestFullscreen();
  }
}

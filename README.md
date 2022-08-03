# smm-tmm


The various categories:
- old/new
- old/new + location
- old/new + time
- old/new + both


Every file will link to Round 2; use the mTurk ID ti differentiate between who is who. Instructions are different for all, and Full_Double is deprecated.

## details

SMMTMM_[trialtype] consists of the html, js, and css required. In addition, there is a `save_data.php` file that is required for data to be generated. In order to actually run the experiment you need to start a http-server (npm install http-server) or else HTML will not be able to collect any data (during testing).

Generated data / rename.py / analysis.py are various helper tools that may not make sense. F1 = full instruction; T1 = temporal instruction; I1 = identity instruction; S1 = spatial instruction; and F2 is the second round with full instructions.

Images are hosted on ERIS web + numbered in a specific way to sort for natural and artificial. 


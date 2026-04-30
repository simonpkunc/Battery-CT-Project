/==================================================================================\
|
|  TEKSCAN I-Scan 6.03 README.TXT FILE // December 2009
|  ***********************************
|
|  This file contains important information about I-Scan Version 6.03
|  It contains a description of all changes that were made to the software
|  in the current version.
|
\==================================================================================/

1. EVOLUTION HARDWARE ONLY: WINDOWS 7 & VISTA SUPPORT (32-bit & 64-bit)
-----------------------------------------------------------------------
Evolution hardware ONLY:
The software can now be installed and run on Microsoft Windows 7 in both 32-bit and 64-bit modes.
The software can now be installed and run on Microsoft Windows Vista in both 32-bit and 64-bit modes.

Note for USB, PCI & Versatek hardware:
The software can now be installed and run on 32-bit Microsoft Windows 7. (64-bit is not currently supported)
The software can now be installed and run on 32-bit Microsoft Windows Vista. (64-bit is not currently supported)


2. SAVE AVI
-----------
A new feature that allows FSX files to be exported as AVIs is now available.


3. BUG FIX (#680): View Max Area frame doesn't work with I-Scan 6.02
--------------------------------------------------------------------
When you select View>>Max Area Frame, the software does not move to the frame with the maximum area loaded. 
It just goes to frame 1. This is a 6.02-specific bug (feature worked on prior versions).


4. TOOLBAR BUTTON CUSTOMIZATION REMEMBERED ACROSS SESSIONS
----------------------------------------------------------
Customizing the toolbars (adding/removing buttons) is now remembered across software sessions.


5. LANGUAGE SUPPORT: DUTCH, POLISH 
----------------------------------
The product has been localized into Dutch and Polish (in addition to the already supported Chinese, French, German, Italian, Japanese, Korean, Spanish, Russian and Greek languages).



\============================ End of Version Section =============================/

/==================================================================================\
|
|  TEKSCAN I-Scan 6.02 README.TXT FILE // August 2009
|  ***********************************
|
|  This file contains important information about I-Scan Version 6.02
|  It contains a description of all changes that were made to the software
|  in the current version.
|
\==================================================================================/

1. BUG FIX (#652): API2 - RequestCalRealTimeData() STOPS AFTER ~3-4 MINUTES
---------------------------------------------------------------------------
RequestCalRealTimeData() would stop after 3-4 minutes. This is now fixed.


2. BUG FIX (#653): API2 - ERRONEOUS LINE DATA IN THE MIDDLE OF THE CONFORMAT DUAL SENSOR SEEN IN FSXUSER
-------------------------------------------------------------------------------------------------------
Masked sensor areas would transmit positive data values via API2. Values like that, while not corresponding to any valid physical area of the sensor, could be misinterpreted as legitimate data, leading to erroneous/confusing results.
To address this problem, the following logic has been implemented:
 - Masked sensor areas will emit a "+1" in pfData if the data is raw, and "-1" if the data is calibrated. These values should be discarded! 
The sample application demonstrates this: a "-1" value is always emitted. (if raw data, +1 is converted to -1)


3. BUG FIX (#654): VIDEO NOT SYNCHRONIZED WHEN PRE-TRIGGERING IS USED
---------------------------------------------------------------------
Video synch does not work properly when pre-triggering is set. If a video is synchronized to an fsx movie frame other that the first, rewinding to the first frame is results in both the video and the fsx movie propagating to their respective first frames. Playback would then resume from the first frame for both the video and the fsx movie, 
effectively resulting on an invalid synchronization. This is now fixed. Synchronized playback resumes for both movie and video at the original synchronization point.


4. BUG FIX (#655): RIGHT-CLICK ON BLANK PORTION OF NEW UI TOOLBAR STRIP CAUSES CRASH
------------------------------------------------------------------------------------
Right-clicking on the unused portion of the new UI toolbar strip would cause the application to crash. This is now fixed.


5. BUG FIX (#661): ASCII - COMMA IS NOT PRESENT BETWEEN ABSOLUTE TIME AND FORCE/PRESSURE DATA IN ASCII GRAPH FILE
-----------------------------------------------------------------------------------------------------------------
A comma (',') is now added between the "Absolute time" and "Force" values when saving data in ASCII form.


6. SAVE-ASCII FILE EXTENSION CHANGE
-----------------------------------
The file extension for ASCII-based exported movie data has been changed from '*.asf' to '*.asm'.
To open older '*.asf' files, rename the file extension to '*.asm'


7. ADC CLOCK DIVISOR ADJUSTMENT (VERSATEK CUFF ELECTRONICS ONLY)
----------------------------------------------------------------
The ADC clock divisor in the VersaTek Cuff electronics was adjusted from 4MHz to 2MHz to improve noise and bleeding issues.


8. WIRING TABLE CHANGE FOR THE PCI-TO-VERSA CUFF (VERSATEK CUFF ELECTRONICS ONLY)
---------------------------------------------------------------------------------
Corrected "Driver 0" mapping on the wiring translation table between PCI and VersaTek Cuff electronics.
This was an issue on some sensors that were available for both the PCI and Versatek Cufff electronics (edge connector).
This problem manifested itself as a missing sensel when the sensor was connected to the VersaTek Cuff electronics. 


9. MULTI-HANDLE TRACE RESISTANCE SUPPORT
----------------------------------------
The software now supports trace resistance values for multi-handle maps.


10. BUG FIX (#667): TARE DOES NOT WORK CORRECTLY WITH THE FLIP ROWS AND COLUMNS FEATURE
---------------------------------------------------------------------------------------
When you apply Tare to a section of the sensor and use the Flip Rows or Flip Columns feature, the Tared values remain in the same section of the window. The Tared sensels should move to a new section of the window so that they cover the same sensels on the sensor when the rows or columns are flipped.
This is now fixed.


\============================ End of Version Section =============================/

/==================================================================================\
|
|  TEKSCAN I-Scan 6.01 README.TXT FILE // April 2009
|  ***********************************
|
|  This file contains important information about I-Scan Version 6.01
|  It contains a description of all changes that were made to the software
|  in the current version.
|
\==================================================================================/

1. HEIGHT VS. DISTANCE GRAPH CHANGES (OPTIONAL FEATURE)
-------------------------------------------------------
The following have been implemented with regards to the Height vs. Distance graph:
 
 - 'H' (Height) is now the last item in the Graph’s right pane 
 - 'Average' is displayed instead of 'Mean' in the Graph’s right pane
 - Nip Height is now always averaged or "filtered". 'Height' is now always 'Filtered'. 
   Graph's right mouse click menu toggle has been eliminated.
 - After a recording is completed the last frame gets automatically displayed.
 - After a recording is completed both the movie and the graph will be visible on the 
   desktop (movie on top portion, graph on lower portion).
 

\============================ End of Version Section =============================/


/==================================================================================\
|
|  TEKSCAN I-Scan 6.00 README.TXT FILE // January 2009
|  ***********************************
|
|  This file contains important information about I-Scan Version 6.00
|  It contains a description of all changes that were made to the software
|  in the current version.
|
|  Tip
|  ~~~
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window
|  from the WordPad View/Options menu to wrap the text within the document window.
|
|
\==================================================================================/

1. NEW HARDWARE SUPPORT: VERSATEK HANDLES
-----------------------------------------
This is the first version of the software with support for the new USB-based VersaTek hub and handles.


2. SAVE AS MATLAB FILE (OPTIONAL FEATURE)
-----------------------------------------
FSX data can be exported and saved in a Matlab-compatible *.mat binary file format that can be directly loaded and processed by Matlab.
The feature is accessible via the "File|Save MATLAB *.mat file..." menu and it operates on the currently active fsx movie.
Data is exported 'as is', i.e. calibrated, equilibrated, raw...


3. UPDATED USER INTERFACE
-------------------------
The look & feel of the UI has been updated: 
  - new customizable toolbars, 
  - updated color scheme
  - tab-based ribon indicator oF open/active window(s)


4. SAVE-ASCII FEATURE IMPROVEMENTS
----------------------------------
- An additional column with absolute timestamps is now also generated when saving data in ASCII form
- The precision of the ASCII-exported timestamps has been increased 


5. BUG FIX (#590): EDIT-AVERAGE IS APPLIED AFTER EQUILIBRATION
--------------------------------------------------------------
Edit-Average is now applied after equilibration, regardless of the sequence of the equilibration operation or the placement of the Edit-Average object: Edit-Average will not incorrectly modify the equilibrated data.
Edit-delete-internal/external is applied before equilibration (identical behavior to prior versions). 




\============================ End of Version Section =============================/

/==================================================================================\
|
|  TEKSCAN I-Scan 5.93 README.TXT FILE // April 2008
|  ***********************************
|
|  This file contains important information about I-Scan Version 5.93
|  It contains a description of all changes that were made to the software
|  in the current version.
|
|  Tip
|  ~~~
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window
|  from the WordPad View/Options menu to wrap the text within the document window.
|
|
\==================================================================================/


1. HEIGHT VS. DISTANCE GRAPH (OPTIONAL FEATURE)
-----------------------------------------------
An optional feature has been developed that provides I-Scan software with a default view, whereby the graph is automatically opened full-screen, and displays the Nip Height vs. Distance graph. The X-axis displays the Distance across Columns, while the Y-axis displays the Nip Height.
Nip Height can be averaged or filtered. This averages the Nip Height according to neighboring data within the recording. To do this, right-click anywhere on the graph display and select Filter Height Data.

\============================ End of Version Section =============================/


/==================================================================================\
|
|  TEKSCAN I-Scan 5.92 README.TXT FILE // January 2008
|  ***********************************
|
|  This file contains important information about I-Scan Version 5.92
|  It contains a description of all changes that were made to the software
|  in the current version.
|
|  Tip
|  ~~~
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window
|  from the WordPad View/Options menu to wrap the text within the document window.
|
|
\==================================================================================/


1. CUSTOM TEXT IN MOVIE WINDOWS (OPTIONAL FEATURE)
--------------------------------------------------
The user can enter custom text (35 characters max) that becomes visible on the upper left corner of the movie window in 2-d, 3-d, and print views.
The feature is available by right-clicking on the movie window and selecting "Custom Text..." from the popup menu.


2. SAVE AS MATLAB FILE (OPTIONAL FEATURE)
-----------------------------------------
FSX data can be exported and saved in a Matlab-compatible *.mat binary file format that can be directly loaded and processed by Matlab.
The feature is accessible via the "File|Save MATLAB *.mat file..." menu and it operates on the currently active fsx movie.
Data is exported 'as is', i.e. calibrated, equilibrated, raw...



\============================ End of Version Section =============================/


/==================================================================================\
|
|  TEKSCAN I-Scan 5.90 README.TXT FILE // September 2007
|  ***********************************
|
|  This file contains important information about I-Scan Version 5.90
|  It contains a description of all changes that were made to the software
|  in the current version.
|
|  Tip
|  ~~~
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window
|  from the WordPad View/Options menu to wrap the text within the document window.
|
|
\==================================================================================/


1. RUSSIAN LANGUAGE SUPPORT
---------------------------
The product has been localized into Russian (in addition to the already supported Chinese, French, German, Italian, Japanese, Korean and Spanish languages). 
The user can select which version to install during the initial setup of the product.
The default installation language is English.


2. VISTA SUPPORT
----------------
The product is now compatible with the Windows Vista operating system.


3. UPDATED KERNEL DRIVER TLW32DRV.SYS
----------------------------------------------------
A new version of the kernel driver tlw32drv.sys (version 5.33) is now included with the system.


4. BUG FIX (#368): INCORRECT SECONDS DISPLAY RECORDING LENGTH EXCEEDS 16K SECONDS
---------------------------------------------------------------------------------
An overflow occurred when a movie window is set to display elapsed seconds and the number of seconds exceeds 16k seconds.
This is now fixed.


5. BUG FIX (#360): UPDATED USB DEVICE DRIVER
--------------------------------------------
A new version of the USB device driver (version 2.6) is now included with the system. This driver fixes certain crashes (BSOD-crashes) experienced by some users. 


6. BUG FIX (#373): EVOLUTION HANDLES RECORDING @98% OF REQUESTED FREQ.
--------------------------------------------------------------------
A truncation  error in computing the number of frames to record was resulting in the Evolution handles recording @ 98% of the requested frequency.
This is now fixed.


7. BUG FIX (#375): EQUILIBRATED VALUES ROLLOVER WHEN RAW VAL > 255
-----------------------------------------------------------------
When the equilibrated raw value exceeds 255 raw, instead of stabilizing at 255 raw, the value becomes 0 raw and then continues increasing from 0 as the pressure on the sensel increases. 
In some cases the sensel may also briefly report a value of B, and be displayed as a masked sensel. 
This is now fixed.
Once the equilibrated raw output reaches 255, the value now remains saturated at 255.


8. IMPROVED WIRELESS HANDLE CONNECTIVITY (OPTIONAL FEATURE)
-----------------------------------------------------------
Code improvements to the wireless handle component (an optional feature), allows for a more robust wireless connection, and an overall better quality in establishing and maintaining the WiFi link between the desktop application and the wireless handle. 


9. REWORKED USER PREFERENCES DIALOG
-----------------------------------
A new multi-tab dialog is now handling the user preferences, with each tab dedicated to a specific product area.


10. NEW KEYBOARD SHORTCUTS FOR MOVIE PLAYBACK
---------------------------------------------
Movie playback can now be controlled by the keyboard arrow keys and spacebar: 
LEFT/RIGHT arrow = Move Back/Forward a single frame.
UP/DOWN arrow = Jump to the  Beginning/End of the movie
SPACEBAR = Play / Pause
SHIFT+SPACEBAR = Play movie continuously in a loop fashion


11. STATUS BAR TEXT IN 2-D & 3-D
--------------------------------
- The "Sensor OK" text on the left-most status bar box becomes RED when this box is clicked and the realtime or movie goes into a PAUSE state. (clicking the status box again reverts to normal state)


12. DRIVER VERSION INFO ON THE ABOUT DIALOG BOX
-----------------------------------------------
The USB driver version is now displayed on the About dialog box. The previous "Hardware Version" info is now renamed to "Common Driver Version"


13. BUG FIX (#519): OPEN WINDOWS LIST NOT REFLECTING ACTUAL OPEN WINDOWS
------------------------------------------------------------------------
Under the Window menu, the dynamic list of all currently open windows is supposed to be displayed.
This list was not always updated properly.


14. BUG FIX (#528): COF IS OFF BY HALF A CELL
---------------------------------------------
COF computation was off by half a cell. This was more problematic and evident when mirroring was used. It is now fixed.


15. BUG FIX (#524): ASCII GRAPH FROM MOVIES OF DIFFERENT LENGTH HAS INCORRECT TIME COLUMN AFTER THE END OF THE FIRST DATA SERIES
--------------------------------------------------------------------------------------------------------------------------------
If you Save an ASCII graph that contains multiple movies of different lengths, then at some point the time column will be lost.
This happens after the last from of whatever graph is labeled as #1. Instead of continuing with the time values for the remaining movies, the ASCII graph values (force, pressure, etc...) for the remaining movies get shifted to the time column.
This is now fixed.


16. PRODUCT NO LONGER SUPPORTS WINDOWS 95,98,ME
-----------------------------------------------
This product in no longer compatible with Windows 95, 98, ME.



\============================ End of Version Section =============================/


/==================================================================================\
|                                                                                  |
|  TEKSCAN I-Scan 5.83 README.TXT FILE // June 2006                                |
|  ***********************************                                             |
|                                                                                  |
|  This file contains important information about I-Scan Version 5.83              |
|  It contains a description of all changes that were made to the software         |
|  in the current version.                                                         |
|                                                                                  |
|  Tip                                                                             |
|  ~~~                                                                             |
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window     |
|  from the WordPad View/Options menu to wrap the text within the document window. |
|                                                                                  |
|                                                                                  |
\==================================================================================/


1. MINOR LOCALIZATION CHANGES
-----------------------------
String modifications for some parts of the install routine, as well as some minor string tranlations for the main application.





\============================ End of Version Section =============================/

/==================================================================================\
|                                                                                  |
|  TEKSCAN I-Scan 5.82.2 README.TXT FILE // April 2006                             |
|  *************************************                                           |
|                                                                                  |
|  This file contains important information about I-Scan Version 5.82.2.           |
|  It contains a description of all changes that were made to the software         |
|  in the current version.                                                         |
|                                                                                  |
|  Tip                                                                             |
|  ~~~                                                                             |
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window     |
|  from the WordPad View/Options menu to wrap the text within the document window. |
|                                                                                  |
|                                                                                  |
\==================================================================================/


1. MULTI LANGUAGE SUPPORT
-------------------------
The product has been localized into Chinese, French, German, Italian, Japanese, Korean and Spanish. The user can select which version to install during the initial setup of the product.
The default installation language is English.


2. INSTALLSHIELD 11.5 INSTALLATION
--------------------------------------------------------------
This is the first version of I-Scan to use the Installshield 11.5 installation engine. This also includes a new CD browser for the installation CD.



\============================ End of Version Section =============================/

/==================================================================================\
|                                                                                  |
|  TEKSCAN I-Scan 5.82 README.TXT FILE // March 2006                               |
|  ***********************************                                             |
|                                                                                  |
|  This file contains important information about I-Scan Version 5.82.             |
|  It contains a description of all changes that were made to the software         |
|  in the current version.                                                         |
|                                                                                  |
|  Tip                                                                             |
|  ~~~                                                                             |
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window     |
|  from the WordPad View/Options menu to wrap the text within the document window. |
|                                                                                  |
|                                                                                  |
\==================================================================================/


1. SUPPORT FOR THE NEW EVOLUTION TEKSCAN HANDLE
--------------------------------------------------------------
This is the first version of I-Scan to support for the new USB-based EVOLUTION handle.


2. NEW PHOTO INTEGRATION FEATURE
--------------------------------
The Photo Integration feature is introduced, allowing users to associate static images with Tekscan movies, on a per frame basis.


3. MOUSE-BASED FREEHAND ROTATION OF THE 3D VIEWS
-------------------------------------------------
The user can now use the mouse directly (click and drag) to freely rotate the 3D views.


4. VISIBILITY OF THE COF MARKER IS INI CONTROLLABLE
---------------------------------------------------
By manually editing the DrawCofTarget entry under the [Settings] section of the program ini file, the user can show or hide the COF marker (diamond) when the COF Trajectory is displayed on the movie windows.
Setting this: "DrawCofTarget=0" will hide the COF marker.
Setting this: "DrawCofTarget=1" will show the COF marker.


5. BUG FIX: APPLICATION CRASH WHEN LARGE AMOUNTS OF MOVIE DATA WERE COPIED TO THE CLIPBOARD
-------------------------------------------------------------------------------------------
When movie data was copied to the clipboard, (especially from multihandle virtual map recordings) the application would crash. This is now fixed.



\============================ End of Version Section =============================/




/==================================================================================\
|                                                                                  |
|  TEKSCAN I-Scan 5.76 README.TXT FILE // July 2005                                |
|  ***********************************                                             |
|                                                                                  |
|  This file contains important information about I-Scan Version 5.76.             |
|  It contains a description of all changes that were made to the software         |
|  in the current version.                                                         |
|                                                                                  |
|  Tip                                                                             |
|  ~~~                                                                             |
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window     |
|  from the WordPad View/Options menu to wrap the text within the document window. |
|                                                                                  |
|                                                                                  |
\==================================================================================/


1. FRENCH & GERMAN LANGUAGE SUPPORT
-----------------------------------
The product has been fully localized into German and French. The user can select which version to install during the initial setup of the product.


2. WIRELESS HANDLE SUPPORT (OPTIONAL)
-------------------------------------
The software now supports the new wireless USB handle. A PocketPC based WiFi-enabled PDA is required, and can be provided by Tekscan.
The USB handle is attached to the PDA, and the PDA/USB-handle pair act as the wireless transmitting handle back to the receiving desktop system.


3. BUG FIX: HELP FILE IS NOT GETTING INVOKED
--------------------------------------------
On some systems, the Help file is not getting invoked by either F1 or the explicit menu item. (Help | Contents)


4. SILENT INSTALL OF THE USB DEVICE DRIVERS
-------------------------------------------
The USB Device Drivers installation portion of the main install is now silent. (No wizard pages are displayed).


5. NEW EDIT MODE DIALOG
-----------------------
The UI of the Edit dialog has been modified. Underlying functionality has also been modified to allow edit objects (cells & boxes) to operate independently (i.e. one placed cell can perform a deletion of its enclosed internal data, while a placed box can perform an average of its internal area). All edit operations do not affect originally recorded data, but act as a filter on top of it. (i.e. original data can be fully restored by removing all edit objects, or by un-selecting the "View Modified Data" checkbox on the main Edit dialog)




\============================ End of Version Section =============================/

/==================================================================================\
|                                                                                  |
|  TEKSCAN I-Scan 5.72 README.TXT FILE // March 2005                               |
|  ***********************************                                             |
|                                                                                  |
|  This file contains important information about I-Scan Version 5.72.             |
|  It contains a description of all changes that were made to the software         |
|  in the current version.                                                         |
|                                                                                  |
|  Tip                                                                             |
|  ~~~                                                                             |
|  If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window     |
|  from the WordPad View/Options menu to wrap the text within the document window. |
|                                                                                  |
|                                                                                  |
\==================================================================================/


1. UPDATED USB DRIVER
---------------------
Updated USB driver from version 2.0 to 2.1. This USB driver supports more than 8 USB handles.



\============================ End of Version Section =============================/




***************************************
TEKSCAN I-Scan 5.70 README.TXT FILE   // December 2004
***************************************

This file contains important information about I-Scan Version 5.70.  It contains
a description of all changes that were made to the software in the current
version.

Tip: If necessary, choose Word Wrap from the Notepad Edit menu or Wrap To Window
from the WordPad View/Options menu to wrap the text within the document window.
--------------------------------
--------------------------------

1. UPDATED USB DRIVER
---------------------
Updated USB driver from version 1.72 to 2.0. Updated USB driver solves system stability and synchronization issues with multiple USB handles.


2. BUG FIX: GRAPH DISPLAY IS NOT IN-SYNC WITH WINDOWS XP DISPLAY STYLE
----------------------------------------------------------------------
When using the force vs. time graph with the Windows XP display style, the graph image was not correct. The graph would appear transparent around the edges and the graph cursor would not align with the correct time displayed in the status bar of the movie window. This could be corrected by changing the display style to Windows Classic style.
This has now been fixed. The graph is properly rendered irrespectively of the XP display style the user has chosen.


3. BUG FIX: GRAPH CRASHES WITH VERY LONG MOVIES
-----------------------------------------------
The I-Scan software crashes when graphs are open and manipulated on movies that are over 80,000 frames long. This has now been fixed.


4. SENSITIVITY CAN BE SET ON A PER USB HANDLE BASIS
---------------------------------------------------
When multiple USB handles are connected and available to the I-Scan software, the sensitivity of each handle can be set independently. Note: Virtual maps will not allow this. A single sensitivity setting is applied across all handles connected to a virtual map.


5. MODIFIED SENSITIVITY DIALOG
------------------------------
Applies to multiple USB handles: The sensitivity dialog has been modified to allow for the sensitivity to be set for either just the active real-time window the dialog was invoked against, or all real-time windows currently open. The title bar of the Real-Time & Movie windows has also been modified to display the sensitivity setting.(rightmost text after map info, separated by ":")




***************************************
TEKSCAN I-Scan 5.62 README.TXT FILE   // August 2004
***************************************

1. SUPPORT FOR THE NEW USB TEKSCAN HANDLE
--------------------------------------------------------------
This is the first version of I-Scan to support for the new USB-based Tekscan handle.



***************************************
TEKSCAN I-Scan 5.24 README.TXT FILE   // November 2003
***************************************

1. NEW HELP FORMAT
-------------------------------------------------
The Help file format has been changed from *.hlp format to *.chm format. This new help file format contains more detailed information on the use of the I-Scan software, including much of the information that was previously only available in the printed manual. It also includes a calibration guide for calibrating I-Scan sensors in different situations


2. NEW GRIP FEATURES
-------------------------------------------------
This version includes the ability to use the new 4255CRN.mp software map for calibrating and equilibrating separate regions of the Grip sensor. The software includes the ability to use the Tile Calibration and Tile Equilibration features with this ambidextrous map. The map also recognizes the orientation of the grip sensor when it is inserted and displays a left or right window depending on the orientation of the sensor.


3. BUG FIX: FLICKER WITH VIRTUAL MAPS IN EQUILIBRATION
-------------------------------------------------
When virtual maps were used (maps using multiple handles) the pressure data would flicker when equilibration was used.  This flicker has been fixed.


4. NEW MAP FEATURE
-------------------------------------------------
Maps now can have an acquisition speed limit to reduce residual charge or "blue noise" in some sensors.



***************************************
TEKSCAN I-Scan 5.23 README.TXT FILE   // August 2003
***************************************

1. NEW MOVIE OFFSET FOR VIDEO SYNCHRONIZATION
-------------------------------------------------
When using the video capture feature of the software, an offset can be applied to either the pressure movie or the video to achieve synchronization. In the previous version, the frame offset could only be applied to the video.


2. BUG FIX: REAL-TIME DELAY WITH VIRTUAL MAPS
-------------------------------------------------
In version 5.20, when virtual maps were used that contained multiple handles from different PCI boards, there was a delay in the response time in real-time windows. Pressure applied to the sensor would not be displayed in the real-time window for 5-10 seconds, but during recording the software worked fine. This real-time delay has now been fixed.


3. BUG FIX: CANCEL OPEN STAND-ALONE VIDEO DIALOG
-------------------------------------------------
If you pushed Cancel in the Open Stand-alone video dialog window, then the software would crash. This has now been fixed.


4. BUG FIX: LOSE VIDEO SYNCH WHEN CUTTING VIDEO
-------------------------------------------------
In version 5.20, if you cut part of the video, the video would need to be re-synchronized with the Tekscan movie. This now happens automatically


5. BUG FIX: VIDEO RECORDS UNTIL TEKSCAN MOVIE IS PROCESSED
----------------------------------------------------------
When using the Video capture feature at the same time as recording a long pressure recording, the video would continue to record after the Tekscan movie stopped capturing pressure data. The video stopped recorded when the Tekscan movie finished processing. The video now stops whenever the Tekscan movie stops recording.


6. BUG FIX: LOSE VIDEO SYNCH WHEN CLOSING AND REOPENING MOVIE
--------------------------------------------------------------
In some rare circumstances, when a synchronized video was played for the first time with the play button on the main Tekscan toolbar, when the movie and video were closed and re-opened, they were no longer synchronized. This has been fixed.


7. BUG FIX: ONE SECOND DELAY IN VIDEO SYNCH
--------------------------------------------------------------
Sometimes when saving a linked video, when it was reopened, the video synchronization would be offset by 1 second. This has been fixed.


8. VIDEO SYNCHRONIZED WITH MULTIPLE TEKSCAN MOVIES
--------------------------------------------------------------
If a video is linked to one Tekscan movie, pushing the play button in the video window will play back the linked Tekscan movie and any other Tekscan movies that begin at the same time stamp. This allows for effective synchronization of one video with multiple pressure movies.


9. BUG FIX: EDIT APPLIED TO 3D
---------------------------------------------------
When Edit-mode was used to edit sensels, if it was done with a 2D real-time window, the changes would not affect the 3D real-time view. This is fixed.


10. EQUILIBRATION MAY NOT BE ACCURATE WARNING MESSAGE
---------------------------------------------------
A warning message was added if the user tries to change the sensitivity of parallel electronics while an equilibration is active.


11. INSTALLSHIELD 7.0 INSTALLATION
--------------------------------------------------------------
This is the first version of I-Scan to use the Installshield 7.0 installation method. This also includes a new CD browser for the installation CD.



***************************************
TEKSCAN I-SCAN 5.20 README.TXT FILE   // February 2003
***************************************

1. NEW VIDEO ITEMS (OPTIONAL) FEATURE
---------------------------------------------------
A new feature has been added for user of the Optional video synchronization package. This new feature allows users to use a digital video camera connected to the computer via firewire to capture video directly to the I-Scan software while simultaneously recording pressure movies. In addition to real-time capture, this feature can be used to capture previously recorded videos while the digital camera is playing back video stored on tape.


2. CALIBRATED/EQUILIBRATED DATA EXPORT WITH (OPTIONAL) API2 FEATURE
--------------------------------------------------------------------
The optional API2 feature has been enhanced to allow the user to export calibrated and equilibrated data from the Tekscan software to their own client software. In previous versions, this API2 would only export raw data. The sample client files included with the software have been updated to use this new feature.


3. VIEW STATUSBAR CONTROL FEATURE ADDED
------------------------------------
An icon has been added to the Movie Status Bar, that allows the user to open or close multiple windows in one step.  With only a Movie window open, clicking the icon will open the other view (2D/3D) window, as well as a Graph window.  If all three windows are already open, clicking the icon will close either the 2D or 3D view.


4. NOISE FIX (OPTIONAL FEATURES) ADDED
------------------------------------
There are two new optional noise reduction features. Noise Spot Filter, allows the user to filter out sensels with low raw output that appear outside the main contact area. The user can select the raw filter level and the software will apply this filter only to single sensels that are surrounded by unloaded sensels and groups of two connected sensels that together are surrounded by unloaded sensels.

The optional Running Average feature averages each frame with the frame(s) before it. This reduces noise because each frame displayed is the average of several frames collected. The user can select the number of frames that are averaged together. This setting can be set from 1 frame (effectively no averaging) to 5 frames (averages each frame with the previous 4 frames).

If these two features are not enabled, they are by default set to no filtering and no averaging.


5. RENAMES
---------------------------------------------------
"Tiles" has been renamed "Panes". The "Show Tiles" graphing feature has been renamed to "Show Panes".
"Solid" has been renamed "Contours". The "3-D Solid" view type has been renamed to "3-D Contours".
In the view and graph Properties Dialog windows the "Relative" <Y-mode>  label has been renamed "Percentage". The feature has not changed and still reports Y values as a relative percentage of the total value calculated for the entire view window.


6. ABILITY TO OPEN HISPEED MOVIES
----------------------------------------------------
Movies that were recorded with software using the optional HISPEED feature can now be opened in both HISPEED software and regular speed software, where before they could only be opened in HISPEED software. The HISPEED option now only controls the maximum frequency at which the software can record.


7. LOCK ICON IN TOOLBAR
----------------------------------------
A new icon has been added in the toolbar that locks the relative position of all graphing objects(boxes, polygons, etc.) within the view window. When a window contains multiple graph objects, and the Lock Objects button is depressed, moving one object will also move all other objects in the window so that they retain the same relative position to the object that was moved.


8. BUG FIX: EDIT FEATURE TIMESTAMPS FIXED
----------------------------------------
In versions 4.xx and 5.xx when you edited a movie (e.g.edit box) and then you applied it to only some frames within the movie and not for the entire movie then this produced problems with the timestamps of the edited frames. This is a 'general' bug for all products (where edit enabled) and versions until and including version 5.10.


9. BUG FIX: HANDLING COLOR AND BW PRINTERS
----------------------------------------
With some Windows operating systems, the software will not recognize whether the printer connected is B/W or Color. A new entry can now be added in the *.ini file to force the software to print in either color or B/W. This entry should be made in the "Settings" section of the *.ini file. Setting "PrintPalette=1" forces the program to print in Color, setting 'PrintPalette=-1" forces B/W, and Setting "PrintPalette=0" lets the program decide.


***************************************
TEKSCAN I-SCAN 5.10 README.TXT FILE   // October 2002
***************************************


1. MULTI-HANDLE MULTI-MAP FEATURE
--------------------------------
Iscan can now be used with multiple handles and sensors without requiring a custom multi-sensor software map. In order to organize the sensor type and calibration data for each handle, past multiple handled systems required the use of a single software map, which combined all of the sensors in use into one real-time window. Multi-sensor maps can still be used, but now the software can also open multiple real-time windows for as many handles as are connected. Each real-time and movie window is labeled with the handle letter and sensor map. Separate equilibration and calibration information will be maintained throughout the recording session for each separate handle.


2. NEW FUNCTION KEYS
--------------------------------
New keyboard function keys have been added to activate software commands with a single keystroke. The available keyboard functions are now: F1 or Ctrl+F1 (Help), F2 (record), F3 (snapshot), F4 (stop), F5 (play), F9 (print), Ctrl+F9 (print preview), F10 (peak)


3. MASK IS SHOWN FOR 2D-CONTOUR
--------------------------------
In previous releases the sensor mask was only available in regular 2D display. It is now also available in 2D-Contour display. In real-time and movie windows, the sensor mask displays gray shading in the area outside the sensor boundary. This is especially useful with irregularly shaped sensors in a rectangular window.


4. 3D-SOLID GRAPHICS CHANGED
--------------------------------
The 3D solid display has been changed to remove the black/white outline around each cell. Previous releases created a black or white 3D mesh and displayed the pressure color inside the mesh. Now only the pressure colors are displayed without the mesh outine.


5. BLANK FRAME REMOVAL DISABLED BY DEFAULT
--------------------------------
In previous versions of I-Scan, by default, blank frames were removed from the beginning and end of each recording. It was possible to enable/disable this option in Options>>Set User Preferences. To allow the software to perform better with multiple windows, the default setting for this option has been changed so that it no longer deletes frames from the beginning and end of a movie. This setting may still be changed in Options>>Set User Preferences.


6. 2D DISPLAY INTERPOLATION (OPTIONAL) FEATURE
--------------------------------
Three display options are now available for 2D sensel display. 3x3 interpolation splits the display of each sensel into 9 sub-sensels with the center sub-sensel displaying the original cell value and surrounding 8 sub-sensles using an interpolation algorithm to calculate the pressure gradient between sensels. 5x5 interpolation uses the same method to divide each sensel into 25 sub-sensels. The original single sensel display is also still available.


7. BUG FIX: EQUILIBRATION AND CALIBRATION
--------------------------------
After equilibrating, the software still used the original unequilibrated raw sum during calibration. This accounted for some small error because the equilibrated raw sum is usually slightly different than the un-equilibrated raw sum. This bug is fixed in 5.10.


8. BUG FIX: 2D-CONTOUR (SATURATION) COLORING
----------------------------------------
2D-Contour view has been changed to treat saturated sensels in the same way that regular 2D mode currently deals with them. Now in both views, any sensels that are saturated will always be displayed as red regardless of what values are set in the upper limit of the color legend.



***************************************
TEKSCAN I-SCAN 5.01 README.TXT FILE   // August 2001
***************************************

1. MOVE TO A FRAME NUMBER
--------------------------------
Right clicking on the Frame Number in the view's status bar brings up a dialog box.  Entering a frame number in this dialog box moves the view to that frame.


2. LOCK OBJECTS
--------------------------------
All items in a view can be "locked" to each other, such that when one object is moved, all other objects (except edit objects) move at the same time, maintaining their relationship to each other.  When in this mode, a "lock" icon is displayed.


3. LAST EQUILIBRATION/CALIBRATION FILE REMEMBERED
-----------------------------
When in the Load Equilibration or Load Calibration dialog boxes, the last loaded file is shown.  Because equilibration and calibration can now be extracted from *.fsx movies, the file shown may be *.cal, *.equ, or *.fsx.

If an equilibration/calibration was done in a Real-time window, and you attempt to exit the program without saving it, an error message will be displayed.


4. VIEW PROPERTIES DIALOG BOX SET ALL FEATURE
--------------------------------
In the Analysis>>Properties Dialog box, a new button has been added. This dialog box changes the properties of the values displayed in the corner of objects in the view window. You may choose <Set> to make changes apply to only the active window, or <Set All> to make changes apply to all open windows.  This eliminates the need change every window to read the same box data.


5. TRACKING BLOBS (OPTIONAL) FEATURE ADDED
--------------------------------
This new feature allows you to add a blob to the Movie or Realtime window that will "track", or follow, the loaded sensels in the window. Once you add a blob to the window, you can make it a tracking blob by clicking the right-mouse button on an edge of the blob, and selecting "Tracking Blob". You can also do this by placing a check mark in the "Tracking Blob" checkbox in the 'Box Placement' dialog box. Once the tracking blob is in place, it will move so that it covers the nearest loaded sensels in the window.


6. PERMANENT EQUILIBRATION METHOD (OPTIONAL)
-------------------------------
This is an optional alternate method for saving equilibration data.  The standard equilibration method described in Switchable Equilibration saves information about the equilibration procedure along with the movie file so that the movie data is equilibrated and the equilibration procedure can be viewed, added, or removed from a previously recorded movie file.

With this optional method, when the user creates an equilibration file, it can only be implemented in real-time before recording and once recorded the sensor data is permanently modified using the scale factors created by the equilibration. This means that movie data will be equilibrated data, but information about the specific equilibration procedure performed will not be available after the movie is recorded.

This is useful for users who have created their own software to read and analyze Tekscan fsx files. It is very difficult to write programs to read and process this equilibration separately from the movie data. This method is optional and only shipped to those who request it. It replaces the Switchable equilibration method described.


7. BUG FIX: VIDEO HANDLING
-----------------------------
Previously in I-Scan 5.0, when a video was opened and "Save As" was selected before the movie was edited, the video would not save in the entered location.  The media player logo would be displayed but the video would no longer play.  Selecting "Save" would create a separate video file under the same name, but beginning with a ~ (i.e. exam1.avi would "Save" as ~exam1.avi).

"Save As" now places the video file in the correct location, and the video plays correctly in media player.  "Save" now overwrites the existing file.


8. BUG FIX: KEYBOARD SHORTCUTS FIXED
-----------------------------
In I-Scan 5.00, when starting a recording with the <F2> shortcut key, the recording would stop after only one frame. Releases previous to 5.00 were not affected by this problem. With 5.01, the <F2> key records for the full duration.


9. BUG FIX: ACQUISITION DIALOG FIXED
-----------------------------
Occasionaly with I-Scan 5.00, when the acquisition parameters were set for the very highest or very lowest sampling rate in the available range, there was an error message that said the sampling rate was not within the accepted range. This error has been corrected so that all sampling rates selected within the available range will be accepted.


10. BUG FIX: EDIT MODE EFFECTS 3D DISPLAY
--------------------------------
In previous versions, if you edited a 2-D movie and then switched to 3-D mode, the effects of an edit were not immediately visible.  The movie had to be saved and re-opened before the edit changes were visible.  In version 5.01, you can edit in 2-D mode, switch to 3-D and immediately see any edit effects.


11. BUG FIX: BLOB PRINTOUT
--------------------------------
In I-Scan 5.00, when a blob was placed on a movie and the movie window was rotated before printing, the position of the blob did not rotate in the printout.


12. BUG FIX: TARE HANDLING
--------------------------------
Several problems with the tare fuction have been fixed. Frame tare has been deactivated for realtime windows and will only be active fore movies. When loading a tare file into the calibration dialog box, the software now recognizes the difference between single tile and multi-tile calibrations. New message boxes have been added to describe the error when a user tries to apply tare to a movie or real-time window before calibrating.


13. BUG FIX: ODBC LIBRARIES
--------------------------------
I-Scan 5.01 does not require ODBC dynamic link library files to be installed.



***************************************
TEKSCAN I-SCAN 5.00 README.TXT FILE   // March 2001
***************************************

1. SWITCHABLE EQUILIBRATION
------------------------------
In previous versions, the equilibration procedure permanently modified the raw real-time and movie data to conform to the equilibration that had been performed and loaded into the real-time window.  Therefore once a movie was recorded; the equilibration file matrix could not be removed from or added to the fsx movie file after the recording. With this new equilibration data structure the unmodified raw sensor data contained in the fsx and the equilibration data matrix are stored separately.  Therefore equilibration can now be done and loaded before a movie is taken or done after a movie is made and added to the fsx after the movie is recorded.

The equilibration interface has also changed.  You can save and load equilibration data while in a real-time window and from within a movie that has an equilibration file. You can also turn the loaded equilibration file on or off.  This gives the user the ability to see the effect equilibration has on a movie by choosing to display the fsx data in an unequilibrated or equilibrated mode. One can also load equilibration files into previously recorded movies and save equilibration data as a separate file that can be loaded into real time windows at any time.


2. CALIBRATION DIALOG NEW OPTIONS
---------------------
Two new buttons have been added to the calibration dialog window. Buttons for saving and loading calibration files are now at the bottom of this window. These two features were previously only available in the tools menu. They now exist in both locations.


3. PARTIAL CALIBRATION IN CALIBRATION FILES
----------------------------
The tile calibration method has been made more convenient and improved so that "partial" calibration files can be saved.  A partial calibration file is a calibration where not all tiles in the complete sensor map have been calibrated.  Therefore, for sensor maps involving multiple tiles, the calibration may be saved before all of the tiles have been calibrated. The partial calibration file can then be opened at a later time in order to complete the calibration on the remaining tiles.  All tiles must still be calibrated before the calibration file can be applied to the real-time window.  This change is useful for virtual maps where multiple sensors are included as one map and each tile represents a separate sensor.  Since partial equilibration is also available this enhancement allows the user to equilibrate, calibrate and check each tile/sensor before proceeding to the next tile/sensor.


4. CALIBRATION DIALOG TITLE ADDITIONS
---------------------
In the title bar of the calibration dialog window, the calibration status in labeled in parentheses to show whether the current realtime window is (uncalibrated) or (calibrated).


5. TOOLBAR CHANGES
---------------------
(a) The Comments icon has been changed to a pencil and pad image.
(b) The Print Preview and Calibration icons have been added to the Main Toolbar.


6. ADD POLYGON (OPTIONAL) FEATURE ADDED
----------------------------------------
This new feature allows you to add a custom-shaped box to a Realtime or Movie window.  To add a polygon, select Analysis>>Add Polygons, and click in the active window.  When you click in a second location in the window, a node will be placed at that point, and a line will be drawn between the two nodes.  You may add as many lines (sides) of the polygon as you wish, and the polygon will automatically be completed when two lines of the polygon cross.


7. TRACKING BOX (OPTIONAL) FEATURE ADDED
------------------------------------------
This new feature allows you to add a box to the Movie or Realtime window that will "track", or follow, the loaded sensels in the window.  Once you add a box to the window, you can make it a tracking box by clicking the right-mouse button on an edge of the box, and selecting "Tracking Box".  You can also do this by placing a check mark in the "Tracking Box" checkbox in the 'Box Placement' dialog box.  Once the tracking box is in place, it will move so that it covers the nearest loaded sensels in the window.


8. GROSS CONTACT BOX (OPTIONAL) FEATURE ADDED
------------------------------------------
This feature draws a line around the perimeter of contact area within a box. To use this feature one must "add a box" to the movie window, highlight the box and right mouse click on the edge of the box.  Then select the "Outline Box" option from the Menu list. You can also enable this feature by placing a check mark in the "Outline Box" checkbox in the 'Box Placement' dialog box. Once the outline option is on, the box will be drawn by a dotted line and a solid line will be automatically drawn that outlines the contact perimeter. The forces and pressures data and graphs displayed for this box will reflect only the cells surrounded by this perimeter line.  Selecting Object Area from the Properties menu will accurately reflect the area enclosed by the outlining perimeter.


9. ADD BLOB (OPTIONAL) FEATURE ADDED
---------------------------------------
This new feature enables you to study a group of loaded sensels separately from the rest of the window.  To add a blob, select Analysis>>Add Blob, and click in the active window.  A box with dashed borders will be added to the window.  Inside this box will be a single node, which is the active point (crossing point of the two solid lines).  Click on this node, and while holding your left mouse button down, drag it over the group of loaded sensels of interest.

The program will draw a line around all loaded cells that are adjacent to the active point, and include them in the blob. If there are no loaded cells in the area of the active point, no blob will be drawn.


10. READ-ASCII (OPTIONAL) FEATURE ADDED
----------------------------------------
In I-Scan 5.00, the ability to open and view an ASCII (*.asf) file as a movie has been added.  To open an ASCII file, select File>>Open Movie, and set the "Files of Type" field at the bottom of the dialog box to "ASCII (*.asf)".  Note that you may not open *.asc or *.asg files using this feature.


11. SENSOR MIRRORING FEATURE ADDED
---------------------------------------------
This feature allows you to "mirror" the sensor in the X or Y direction.  With a Movie or Realtime window open and active, select Analysis>>Properties.  Under Options, select "Row Mirroring" or "Column Mirroring", and the entire window will be mirrored across the rows or columns, respectively.


12. DYNAMIC CALIBRATION FEATURE ADDED
---------------------------------------------
I-Scan enables you to perform a dynamic calibration, which is a calibration performed while recording realtime data.  To use this feature, select Dynamic Calibration from the Tools pull-down menu.  This will open the Dynamic Calibration dialog box.

You may enter one or two force values, depending on whether you would like to perform a 1- or 2-point dynamic calibration.  You will then click the Record button in the dialog box to begin recording data.  As the system is recording, you must load the sensor, and then click the "Force 1" button at the appropriate time.  A calibration point will be added using the current frame data.  If you wish to add a second calibration point, repeat these steps and click the "Force 2" button.  Once the dynamic calibration is complete, a message will be displayed to tell you which frame(s) were used for the calibration.


13. TARE FEATURE ADDED
---------------------------------------------
This feature modifies the calibrated data to correct for residual pressure on the sensor at zero load. The Tare feature is located in the Calibration dialog. The raw data is not affected by the tare function but an extra calculation has been added when converting the raw data to calibrated data. Any cells reading raw pressure during the tare are set at zero raw before the calibration scale factor is applied. There is also a method to perform the tare function on one frame of a previously recorded movie that is assumed to be the point of zero load. Tare is recommended only for single point calibration and may increase error when using a multipoint calibration.


14. VIDEO PLAY AND SYNCHRONIZATION CAPABILITY (OPTIONAL)
-------------------------------------
Three optional new buttons have been added to the toolbar for opening video files with the I-Scan software. If, at the time of recording, the video capture was synchronized with the recording of the Tekscan movie, the pressure data for each frame can be correlated to the video image that occured at the same time.


15. API 2 INTERFACE (OPTIONAL)
--------------------------------
This optional feature allows the I-Scan software to export real-time pressure data using standard Microsoft COM technology. Users who write their own client software can then receive and handle the Tekscan pressure data in their applications as they wish.


16. OBJECT LABEL
--------------------------------
Boxes and lines (but not tiles) can be assigned labels in the placement dialog box. The object label is (optionally) displayed next to the data in the corner or the object in the movie view. It is also always displayed in the graph as well as in exported ASCII graph files. When a box or line is saved or loaded as an object file, the label is stored as well.


17. OPEN MULTIPLE FILES
--------------------------------
In the open file dialog window, if the user selects multiple movies or videos using CTRL or SHIFT, all selected movies will be opened at the same time.


18. ADDED "CLOSE ALL" MENU ITEM
--------------------------------
The Close All menu item was added to the File pull-down menu.  When this item is selected, all open windows (Movie, Realtime, and Graph) will be closed (you will be prompted to save them if they have been changed).


19. LAST DIRECTORIES REMEMBERED
--------------------------------
The default directory when saving or loading any of the following file types is the folder for the current patient selected: fsx (Movie), fbx (Object), fed (Edit Boxes), cal (Calibration), equ (Equilibration), asf (ASCII Frame), asc (ASCII COF), asg (ASCII Graph) and Video.


20. 2D VIEW OUTLINES (ISOBARS) FEATURE ADDED
---------------------------------------------
This feature allows you to display any 2D pressure images, in a Movie or Realtime window, as colored outlines of the pressure areas (also called "isobars").  To enable this feature, select Analysis>> Properties, and de-select the "Fill Contour" checkbox under "Options".  By default, "Fill Contour" is selected, and the colored areas will be filled in.


21. X/Y/Z COORDINATES FEATURE ADDED
------------------------------------
When View>>Coordinates is selected, the X and Y coordinates are shown in any open Movie or Realtime windows.  If the window is in a 3D view mode, the sensor origin (0,0) point is marked by a vertical black or white line, and the X and Y axes are not displayed.


22. SELECTABLE LEGEND SCROLLING INCREMENT
------------------------------------------
In the 'Measurement Units' dialog box (Options>>Measurement Units), you can now select the increment by which the upper and lower limits of the legend will be increased/decreased.  The allowable increments are 1, 10, 100, 1000, and 10000.


23. 'PRINT BOX' FEATURE ADDED
----------------------------
If you select the 'Print Box Enabled' checkbox, in the 'Print Setup' dialog box (File>>Print), and select a box in the movie window, only that box will be printed.  If no box is active/selected, the entire window/sensor will be printed, regardless of the 'Print Box Enabled' checkbox.


24. X, Y COORDINATES IN ENGINEERING UNITS
------------------------------------------
When the cursor is over a Movie or Realtime window, the Main Status Bar (at the bottom of the window) displays the sensor row and column numbers (Row, Col) that the cursor is currently above.  In I-Scan 5.00, this status bar also displays these coordinates in engineering units, such as inches or centimeters.  Note that this feature is disabled if "cells" is selected as the Unit of Length in the 'Units of Measure' dialog box.


25. ADDED MOVIE PAUSE FOR GRAPHS
---------------------------------
When a movie is "paused", the movie's timeline in any graphs is also paused.  Previously, the time line could be moved in the graph, and the associated movie would jump to the same point, even if it was paused.


26. COF (TRAJECTORY) CALCULATION MODIFICATIONS
------------------------------------------------
The method that the software uses to calculate the COF (Trajectory) has been changed slightly to assure more accurate results.  The new calculation method takes the calibrated pressure range (if the window has been calibrated) and the tile calibration information into account.  This new method is also more flexible and useful if you are viewing the window pressures when the legend limits are not at the default settings.


27. FIXED Y-AXIS SCALE OPTION ADDED FOR GRAPHS
-------------------------------------------------
The user now has the ability to set a fixed scale for the Y-axis of graphs.  In the Graph Properties dialog box, click on "Fixed Scale", and then enter values in the Maximum and Minimum fields.  These numbers will be used as the maximum and minimum values for the Y-axis of the graph.  By default, "Auto Scale" will be selected, and the software will automatically scale the Y-axis.


28. RELATIVE PROPERTY DISPLAY ENABLED
----------------------------------------
In the 'Properties' dialog box for the View and Graph windows, the "Relative" option is now available when any of the Peak, Contact or Object options are selected.  Previously, it was unavailable when some options were selected.


29. GRAPH Y-AXIS NAME CHANGED
-------------------------------
The title of the graph's Y-axis, when "Relative" is selected in the 'Properties' dialog box, has been changed to read "% of Total..." or "% of Average...".  Previously, it read "% of Maximum", which might have been misleading.


30. BUG FIX: RELATIVE FORCE DISPLAY IN RAW UNITS
--------------------------------------------------
For calibrated movies, when the measurement units were changed to "raw sum", the relative percentages displayed in any tiles or boxes would sometimes be inaccurate.  This problem has been corrected in Version 5.00.


31. BUG FIX: GRAPH'S HISTOGRAM DISPLAY
---------------------------------------------
In previous releases the "non-bar" or "smoothed" graph display was sometimes incorrect when the x-axis on the graph was set to measure distance across rows or distance across columns instead of time. The data displayed at the origin of and at the end of the graph was incorrect or missing. This problem has been corrected.


32. BUG FIX: LOAD CALIBRATION PROBLEMS FIXED
---------------------------------------------
Modifying a loaded calibration file was difficult in previous releases. After any modification to the second point of a two-point calibration, the software would create a stepwise linear curve between the points instead creating an exponential formula to connect the points. This would happen if one added a second point to a previously loaded one-point calibration and if you modified the second point in an existing previously loaded calibration. The software now restricts modifications to the calibration points and requires that both points be deleted and reentered if one wants to modify either point.


33. BUG FIX: CONTOUR DISPLAY HOLES
-------------------------------------
In previous releases, there was a bug with color legend when using 2D contour mode. If an area of low pressure was surrounded on all sides by higher pressure values, when this area was viewed with 2D contour mode the color of the low pressure area would correspond to a range in the color legend that was higher than what the actual pressure data was. Regular 2D mode would produce the colder colors in the low pressure area that corresponded with correct range of pressures in the color legend. This has been fixed so that 2D contour mode displays the correct colors in these situations.


34. DEMO VERSION (OPTIONAL)
-------------------------------------
A demonstration version is now available for shipping.  This software will stop functioning after 30 days.



***************************************
TEKSCAN I-ISCAN 4.23 README.TXT FILE  // April 2000
***************************************

1. BUG FIX: DISTANCE GRAPH FOR LINES
-------------------------------------
When the 'Distance across rows' or the 'Distance across columns' graphing option was selected for line objects, occasionally the graph would show nothing.  This problem has been corrected.



***************************************
TEKSCAN I-SCAN 4.22 README.TXT FILE  // February 2000
***************************************

This file contains important information about I-Scan Version 4.22.  It contains
a description of all changes that were made to the software in the current
version.
--------------------------------
--------------------------------

1. FEATURE CHANGE: CUTTING FRAMES
-------------------------------------
Cutting frames from the beginning of the movie used to leave dead space at the beginning of the graph.
Now, timestamps of the remaining frames are shifted to start at 0 again, removing the dead space from the graph.


2. BUG FIX: LEGEND LIMITS HANDLING
-------------------------------------
A bug that caused the upper and lower limits of the legend to default to zero, in some operating systems, has been corrected.


3. BUG FIX: CUTTING FRAMES
-------------------------------------
A bug that caused invalid timestamps to be generated when cutting frames from a movie without timestamps has been corrected.


4. BUG FIX: DUAL HANDLE RECORDING
-------------------------------------
A bug in the driver that sometimes caused dual handles to record double frames has been corrected.


5. BUG FIX: SERIAL/PARALLEL COMMUNICATION
-------------------------------------
The buffer used in communicating with the serial or parallel handle has been enlarged to stop data being missed.



************************************
TEKSCAN I-SCAN 4.21 README.TXT FILE  // December 1999
************************************

1. NEW FEATURE: ABSOLUTE TIME STAMPS
----------------------------------
This feature display the exact date and time a frame was recorded.  The time stamp stays the same as the movie is edited (e.g. comments change or frames cut).  This is only available on movies recorded with version 4.21 or higher.  Movies recorded in previous versions will not display the date time stamp.  The time stamp will be displayed in the graph and optionally in the movie status bar.  To change the display of the status bar, go to Options -> Set User Preferences.  There you can select from three displays in the status bar (frame count, relative time and absolute time).


2. NEW FEATURE (OPTIONAL): AUTOMATIC SEQUENTIAL RECORDING
---------------------------------------
This feature allows the computer to automatically start a new recording when the current one is complete.  The software will save the recordings in a user specified directory and prefix (e.g. C:\movies\Data_0001.fsx, C:\movies\Data_0002.fsx, etc.).  The software checks the given directory for space and sets limits for number of movies according to the available drive space.  If triggering is used, each movie is separately triggered.


**************************************
TEKSCAN I-SCAN 4.20 README.TXT FILE  // October 1999
**************************************

1. NEW FEATURE: DELAY RECORDING
----------------------------------
This feature allows you specify a time delay (in seconds) before recording begins.  This value is entered in the "Delay Recording" field in the Data Acquisition Parameters dialog box.  By default, this value will be zero, and recording will begin as soon as 'Record' is selected.  This delay and the triggering options are mutually exclusive, i.e. one is not available when the other is selected.


2. NEW FEATURE: COMB-CUT MOVIE FRAMES
---------------------------------------
This feature allows you to remove frames from a movie at specified intervals.  The comb-cut feature can be used to reduce the number of frames in a movie while retaining the overall pattern.

To comb-cut frames, make sure a Movie window is active, and open the Cut Frames dialog box (select Cut Frames from the Edit menu). Select 'Cut Frames' as the Cut Method, place a checkmark in the 'Comb' checkbox, then enter a number in the "Cut Every __ Frames" field. Each n-th frame will be removed from the movie. For example, if you entered a "3", every 3rd frame (i.e. the 3rd, 6th, 9th, and so on) would be removed.


3. NEW FEATURE - AVERAGE MOVIE INTO MULTIPLE FRAMES
-----------------------------------------------------
This feature, which has been added to the Movie Averaging and Movie Contact Averaging options (View menu), allows you to average a movie into multiple frames.  Previously, you could create only a single averaged frame.

To use this feature, open the Averaging Range dialog box (by selecting Movie Averaging or Movie Contact Averaging from the View pull-down menu).  Place a checkmark in the "Average the movie into multiple frames" checkbox, then enter a value in the "Number of averaged frames" field.

The movie will be broken into groups of frames, each of which will contain the number of frames you entered.  Each of these groups of frames will then be averaged into a single frame.  For example, if your movie has 50 frames, and you enter 10 in this field, your averaged movie will have 5 frames.  The first frame would have been created by averaging the first 10 frames, the second frames from averaging the second 10 frames, and so on.


4. NEW FEATURE: EXTENDED COMPRESSION
-------------------------------------
Extended compression was implemented for handling movies that were created with large sensors (greater than 64,000 sensels). Extended compression is a new way of indexing the data that was necessitated by the large amount of data gathered when a large sensor is used to record a movie.


5. NEW FEATURE: BOX CENTER OF FORCE (COF)
------------------------------------------------------
This feature allows you to view the COF (center of force) for each separate box and tile in a Movie or Realtime window, in addition to the COF for the entire window.  When COF (and COF Trajectory for Movie windows) is selected, a color-coded COF marker is placed into each box or tile in the window.  The COF marker will be the same color as its corresponding box or tile, and the COF marker for the entire window will be gray.

You can disable one or both of these COF features by selecting or de-selecting "Main" or "Boxes", under "COF" in the Properties dialog box (Analysis pull-down menu).


6. NEW FEATURE: MULTI-POINT EQUILIBRATION
------------------------------------------------------
I-Scan now enables you to create multiple equilibration points for a sensor.  In the Equilibration dialog box (Tools>>Equilibration), you can add your first equilibration point by clicking the "Equilibrate-1" button.

Once you complete the first equilibration point, the "Equilibration-2" radio button will become available on the right side of the dialog box.  To add a second point, click on this radio button; the button at the bottom of the dialog box will change to "Equilibrate-2".  Click the "Equilibrate-2" button to add the second equilibration point.

Once you have created one or more equilibration points, you can display the data for a specific point by selecting it's radio button to the right.  The selected point's raw value will be displayed (e.g. "Raw-1: 56") and its equilibration data will be displayed in the window to the left.


7. NEW FEATURE: GRAPH ZOOM
----------------------------
This new feature allows you to zoom in on a specific area of a graph.  To zoom in or out, place the cursor on an appropriate area of the graph, click the right mouse button, and select "Zoom In" or "Zoom Out".  The scale of the X- and Y-axis will change to reflect the smaller or larger view area.


8. NEW FEATURE: RUNNING MULTIPLE TEKSCAN PROGRAMS SIMULTANEOUSLY
--------------------------------------------------------------------
This feature enables you to open more than one Tekscan application at the same time.  Previously, you could only open one Tekscan program at a time.


9. NEW FEATURE: DUAL PARALLEL SYSTEMS NOW SUPPORTED
-----------------------------------------------------
I-Scan 4.20 has the ability to support two parallel systems simultaneously.  Previously, only one parallel system could be connected to the system at a time.


10. NEW FEATURE: CALIBRATION TRIGGERING
-----------------------------------------
This feature enables you to trigger the start of a calibration.  You must enter a force (in Raw Sum) AND an area (in number of cells) at which you want the calibration process to begin.  Triggering will not occur until both limits are reached; however, you can enter a zero in either one to disable it.  If a trigger event is specified, the calibration timer will not start counting down until after this event occurs.


11. NEW FEATURE: MULTI-REGION MAPS
------------------------------------
This feature allows you to treat different areas of a single sensor as separate tiles.  This option can only be used with certain sensors, which have map files designed for this purpose. Using this feature, you can calibrate and equilibrate each section of the sensor as a separate tile.


12. NEW FEATURE: SELECTABLE MOVIE PLAYBACK SPEED
--------------------------------------------------
This new feature allows you to adjust the speed at which your recording will be played back.  To adjust the movie playback speed, click the Play Speed icon in the Main Toolbar. You will be given the following options: Slowest, Medium, Slow, Normal (default), Medium Fast, Fastest.  You may change the speed either before or during movie playback.


13. NEW FEATURE: MAXIMUM NUMBER OF TILES CHANGED
--------------------------------------------------
The maximum number of tiles that may be used for calibration/equilibration purposes has been raised to 16 for compatibility reasons.  Previously, the maximum number of tiles was 8.


14. BUG FIX: PROPORTIONAL DRAWING
-----------------------------------
When using a sensor, any lines, boxes, and numeric values will be scaled to the size of that sensor. Previously, when using especially small or large sensors, the boxes or values would sometimes be too large or small.


15. BUG FIX: ASCII COF SAVE
-----------------------------
In earlier versions, when a COF ASCII data was saved, certain frames of data were missing from the resulting ASCII file.  This problem has been corrected.



**************************************
TEKSCAN I-SCAN 4.13 README.TXT FILE  // June 1999
**************************************

1. MULTI-TILE CALIBRATION AND EQUILIBRATION OPTIONS
-----------------------------------------------------
These new features allow you to calibrate or equilibrate a "virtual" sensor, either as a single window or as separate 'tiles'.  The new 'Calibration' and 'Equilibration' dialog boxes both have been modified to make this possible, with color-coded graphic representations enabling the user to see the tiles' size and positions in the overall virtual sensor.


2. ADDED 'SAVE OBJECT FILE' WARNING MESSAGE
---------------------------------------------
When an object (tiles, box or line) has been placed in a Movie or Realtime window (and has not yet been saved as an "object file"), an error message will be displayed when you attempt to close the window, saying that the object(s) has been modified, and asking whether or not you would like to save it.


3. BUG FIX: MULTI-TILE TRIGGERING
-----------------------------------
Updated the way the software handles triggering when multiple sensors ("tiles") are used.  Previously, when a 2-point calibration was performed, or two Realtime windows were open during calibration, the system would sometimes trigger incorrectly.


4. BUG FIX: RUNNING SYSTEM ON WINDOWS NT
-------------------------------------------
To install I-Scan versions 4.12 and 4.13 onto a Windows NT system, you must log on as an administrator, and then you may log on as a client and run the program later.  However, in version 4.12, a client would sometimes have trouble running the program after it had been installed.  This problem has been corrected.


5. BUG FIX: HIGH SPEED EQUILIBRATION FILES
--------------------------------------------
In previous versions (high speed versions only), equilibration files could not be loaded into a window.  This has been fixed in Version 4.13.



***************************************
TEKSCAN I-SCAN 4.12 README.TXT FILE  // April 1999
***************************************

1. WINDOWS(TM) NT COMPATIBILITY OPTION
-----------------------------------------
I-Scan software version 4.12 can now be installed on computers running the Windows NT operating system.  Previously, it could only be installed on Windows 95/98 systems.  Note that each customer will be sent either Windows 95/98 or NT installation disks, and they are not interchangeable.


2. ADDED ABILITY TO SELECT HANDLE WHEN APPENDING A MOVIE
----------------------------------------------------------
This option allows you to select which handle you would like to use to record the appended data.  When a Movie window is open, and Append is selected from the Movie pull-down menu, the 'Select Sensor' dialog will be displayed.  Under "Available Handles", you may select which handle to use for the "Append to.." Realtime window.  The "Available Maps" will be grayed out, because the appended data must use the same map as the initial movie.


3. ADDED "AUTO-NAMING" OF EDIT AND OBJECT FILES
-------------------------------------------------
When saving an object file (*.fbx) or an edit file (*.fed) from a Movie window, the file will automatically be named with the same name as the movie file (e.g. "Movie1").  This option is not available for Realtime windows.


4. ADDED OPTIONAL FEATURE:  "FINE-TUNING" OF SENSITIVITY (GAIN) SETTING
----------------------------------------------------------------------------
In the 'Adjust Sensitivity' dialog box, the <Fine Tune> button has been added. Clicking this button displays the 'Adjust Gain' dialog box, which allows you to manually enter a gain (sensitivity) setting.  Here you may type in the test voltage (Vtest) and reference voltage (Vref), which will be used to calculate the new gain.  This feature is used to "fine tune" the sensitivity setting, which could previously only be selected from 11 broad ranges.


5. GRAPH LEGEND IMPROVED
---------------------------
In the Legend to the right of the graph, the X-axis value (Time, Frames, or Distance Across Columns/Rows) is displayed, followed by its title ("Time", "Frames", or "Distance").  In previous versions, the title was displayed first, and the user would often have to scroll to the right to read the corresponding value.


6.  BUG FIX: <DEFAULT> BUTTON IN 'DATA ACQUISITION PARAMETERS' DIALOG NOW WORKS CORRECTLY
-------------------------------------------------------------------------------------------
In earlier versions, when the <Default> button (in the 'Data Acquisition Parameters' dialog box) was selected, the software sometimes placed incorrect default values in the Frequency, Period, and/or Frames to Record fields.  Clicking this <Default> button will now place the correct default value in each of these fields.


7.  BUG FIX: PEAK AND COF CRASH ELIMINATED
---------------------------------------------
Previously, the system would crash when PEAK and COF (Center of Force) were both selected.  This problem has been corrected.



***************************************
TEKSCAN I-SCAN 4.11 README.TXT FILE  // February 1999
***************************************

1. 'ADD BOX/LINE' SHORTCUT ADDED
------------------------------------
This new feature allows you to add a box or line to a Movie or Realtime window using the <CTRL> and <SHIFT> keys on your computer keyboard.  Press the <CTRL> key and click the mouse cursor in an open window to add a box at that point, or press the <SHIFT> key and click in an open window to add a line.


2. ADDED 'SAVE VIEW AS MOVIE' ITEM TO FILE MENU
-------------------------------------------------
This menu item allows you to save the current movie frame, or 'view', as a movie file (with extension *.fsx).  This new movie file will consist of one frame, and will be saved exactly as it appeared when saved.  Any 'View' menu items that are in effect when 'Save View as Movie' is selected will be retained in the saved file.


3. ADDED 'MOVIE AVERAGING' & 'MOVIE CONTACT AVERAGING ITEMS TO VIEW MENU
--------------------------------------------------------------------------
These menu items display the averaged pressure value of each cell for the entire recording, or for a selected range of frames, in one composite frame. The difference between the two types of movie averaging is that cells with zero load are disregarded in 'Movie Contact Averaging', whereas they are factored into the formula with a zero value in the 'Movie Averaging' option.

When 'Movie Averaging' or 'Movie Contact Averaging' is selected, the Movie Status Bar will read 'Averaged Frame', followed by the range of frames that were averaged.


4. ADDED 'SETTINGS' ITEM TO OPTIONS MENU
-------------------------------------------
This menu item displays the 'Settings' dialog box for the currently 'active' Movie or Realtime window. This dialog box allows you to view the window's general information, comments, calibration data, and sensitivity, all in one place.  These four pages are viewed by clicking on their 'tab' in the dialog box.  You can change comments, perform a number of calibration functions, and adjust the sensitivity from the separate pages of this dialog box.

You may also select 'Settings' by clicking the right mouse button with your cursor over a window, and clicking on 'Settings'.


5. ADDED 'APPEND' ITEM TO MOVIE MENU
---------------------------------------
This menu item allows you to record additional frames of data at the end of an existing movie. When you select Append, a Realtime window is opened (the title bar will say "Append to ...").  The frames of data you record in this Realtime window will automatically be added to the end of the previous movie.


6. 'OBJECTS' DIALOG BOX CHANGED TO ALLOW MULTIPLE SELECTION
--------------------------------------------------------------
This feature gives you the ability to select multiple objects in the 'Objects' dialog box.  To select more than one object, hold down the <CTRL> key and click on any objects you wish to select.  To select a range of objects, hold down the <SHIFT> key and click on the first and last objects in the range.


7. 'SHOW TILES' OPTION CHANGES
-----------------------------------------------
When 'Show Tiles' is selected from the ANALYSIS pull-down menu, one box (by default) will be placed into all open windows.  If you press the <SHIFT> key and select this option, four (4) tiles will be added.  If you press <CTRL> and select this option, the tile(s) will be added to only the 'active' window.


8.  'SAVE ASCII' PROPERTIES SELECTABLE
----------------------------------------
When you click on the 'Save ASCII' button in the 'Objects' dialog box, the Graph 'Properties' dialog box is displayed.  Here you select the X- and Y-axis values you want to be saved with the ASCII file, without changing the properties of any open graphs.


9.  MOVIE CALIBRATION (POST-CALIBRATION) FEATURE ADDED
--------------------------------------------------------
This feature enables you to calibrate an existing movie window.  The 'Movie Calibration Point' dialog box is accessed by clicking the 'Frame' button in the 'Calibration' dialog box.  In this dialog box, you must enter a frame number and the total force applied to the sensor in that frame.  The system will use this point to perform a linear calibration for the entire movie.  If you add a second point, a 2-point calibration will be performed.


10.  TOOLBAR CHANGES - ADDED 2 NEW ICONS
------------------------------------------
Icons were added to the upper level of the Main Tool Bar, for the 'Comments' item (Edit menu) and the new 'Settings' item (Options menu).


11. TOOLBAR CHANGED TO TWO-LEVEL
----------------------------------
The Tool Bar is now two separate tiers, instead of one, to make it easier to view entirely, and easier to move it around inside the window.  The two levels can now be moved and resized independently of each other.


12.  MAIN MENU CHANGES - SHORTCUTS CHANGED
------------------------------------------
In the Main Menu, the shortcuts for many of the menu items have been changed.  All shortcuts were previously accessed by pressing <ALT> plus another key; they now are accessed by pressing <CTRL> plus another key.


13.  RECORDING - KEYBOARD SHORTCUTS ADDED
------------------------------------------
These new shortcuts enable you to start and stop recording using only the computer keyboard. Pressing the <F2> key begins recording, <F3> takes a snapshot, and <F4> stops recording.


14.  EXTERNAL TRIGGERING CAPABILITY
-------------------------------------
The I-Scan system is now able to trigger a recording based on an external electrical signal received over a COM port.  The external triggering event occurs when an electrical signal is sensed at the selected COM port.

To set up the system for External Triggering, the triggering 'start method' or 'stop method' must be set to 'External', and a COM port must be selected in the 'External triggering port' field, in the 'Triggering' dialog box.


15.  EXTERNAL DEVICE SYNCHRONIZATION CAPABILITY
------------------------------------------------
I-Scan can now be set up to generate a signal synchronized to the recording of logical frames.  This signal may be used to synchronize external devices to the recording of movies.

To synchronize an external device to the I-Scan system, click in the 'Generate external synch signal' box, and select a COM port in the 'External synch/triggering port' field, in the 'Data Acquisition Parameters' dialog box.


16.  TRIGGERING - START METHOD NOW SELECTABLE
-----------------------------------------------
The method of triggering the start of recording is now selectable.  The options are FIRST CONTACT, EXTERNAL, and NONE.  'First Contact' causes the system to trigger based on the contact force and area, 'External' sets up the system for external triggering, and 'None' disables start triggering.


17. TRIGGERING STOP METHOD CHANGED
-------------------------------------
When the 'Stop Method' is set to NONE or LAST CONTACT, the 'Stop Frame Count' field is disabled (grayed out).  When the 'Stop Method' is set to NONE, the 'Enable Group Recordings' checkbox is also disabled.  Previously, these two fields would remain available, regardless of the 'Stop Method', even though they performed no function.


18. TRIGGERING - START AND STOP DEFAULTS CHANGED
---------------------------------------------------
The start triggering default contact 'Force' and 'Area' have been changed to 500 (raw sum) and 0, respectively.  The stop triggering default contact 'Force' and 'Area' have been changed to 200 (raw sum) and 0, respectively.  The stop triggering default method has also been changed - from LAST CONTACT to NONE.


19. INTEGRAL VALUE DISPLAYED IN GRAPH
----------------------------------------
When the Movie window is in PEAK mode, and FORCE vs. TIME graph is selected, the "Integral" value ("Int:") is displayed to the right of the graph. This value is the area under the curve in the graph, in units of force*time (e.g. lb*sec).


20. LEGEND LOWER LIMIT ICON ADDED
------------------------------------
When the lower limit of a Legend is raised, a small red and white icon is displayed in the center of the status bar of any affected Movie or Realtime windows, to warn the user of the change.


21. GRAPH LEGEND CHANGED
---------------------------
In the Legend to the right of the graph, all X- and Y-axis data values are in black, with a colored line next to them, representing their graph trace.  Previously, the actual values were also the color of the graph trace, and they were sometimes difficult to read.


22. 3D VERTICAL ZOOM ADDED
---------------------------
When in any 3D mode, and VIEW>>ZOOM TO is selected, the user is given the option of adjusting the vertical height, as well as the zoom percentage.


23. FILE MENU ITEM NAMES CHANGED
---------------------------------
In the FILE pull-down menu, NEW was changed to NEW RECORDING, and OPEN was changed to OPEN MOVIE.


24. 'PROPERTIES' OPTION NAMES CHANGED
--------------------------------------
In the PROPERTIES dialog box options, for both graphs and Movie/Realtime windows, the word "ACTIVE" has been replaced with "CONTACT",to avoid any possible confusion.


25. ADDED <CTRL> KEY FUNCTION
-------------------------------
When selecting a VIEW menu item, or SHOW TILES, simultaneously pressing <CTRL> will apply the option to only the 'active' window.


26. ADDED <SHIFT> KEY FUNCTIONS
---------------------------------
 + If you press <SHIFT>, and select SHOW TILES (ANALYSIS Menu), four (4) tiles are placed into the window.  When <SHIFT> is not pressed, only one tile is placed.
 + To get CONTINUOUS PLAY, press <SHIFT> while selecting PLAY FORWARD or PLAY BACKWARD.  The recording will play in a loop in the desired direction until stopped using the STOP button.


27.  CALIBRATION FUNCTION CHANGES
-------------------------------------
 + The system now considers the sensor unloaded if less than 1% of the sensels are not loaded.  Previously, more than 3% of the sensels had to be loaded to perform a calibration.
+ When less than 1% of the sensels are loaded, and a calibration is attempted, the error message "Insufficient Area Loaded" will be displayed.  Formerly, this messaged read "No Load on Sensor", which was not as accurate.


28.  "SPLASH" PAGE UPDATED
----------------------------
The splash page was updated to include the new Tekscan corporate logo, as well as the ISO 9001 registration statement.


29. DIALOG BOX LAYOUTS (SIZE & SHAPE) CHANGES
-----------------------------------------------
The size and shape of a number of dialog boxes were changed to accomodate foreign language versions of the software.


30.  BUG FIX:  LAST ROW NOW AVERAGED CORRECTLY
------------------------------------------------
In Version 4.02, when Fixed Area Averaging was selected (View menu), the final row would not be averaged - it would simply take on the cell values of an adjacent row.  The final row values are now averaged correctly, with the cells outside of the sensor not used in the calculation.


31.  BUG FIX:  CONTACT (LOAD) TRIGGER NOW HANDLED CORRECTLY
-------------------------------------------------------------
In earlier versions, when Start Triggering was selected (Triggering dialog), the program may have started recording before the trigger limit was reached.  The system now ignores the discharge line and only checks cells that are used by the current map, to ensure the system is triggered accurately.


32.  BUG FIX:  'SAVE ASCII' FOR DISTANCE GRAPH NOW SAVED CORRECTLY
--------------------------------------------------------------------
In earlier versions, when a graph's X-axis property was set to 'Distance Across Columns' or 'Distance Across Rows', and that graph was saved as an ASCII (*.asg) file, the resulting file was saved with the X-axis property as 'Time'.  The ASCII file now lists the X-axis values correctly.


33. THE *.VXD FILE WAS UPDATED.
-------------------------------
This file was updated to correct some bugs and to implement some new features. The changes include the following:

 + Spurious data is now flushed from the parallel handle whenever the handle is reconnected, to ensure that no incorrect data is reported.



*************************************
TEKSCAN I-SCAN 4.02 README.TXT FILE
*************************************


1. A bug with using dual handles in a virtual map has been fixed.



*************************************
TEKSCAN I-SCAN 4.01 README.TXT FILE
*************************************

1. THE *.VXD FILE WAS UPDATED.
-------------------------------
This file was updated to correct some bugs and to implement some new features.
The changes include the following (the affected hardware types are in
parentheses before each):

 + (Parallel) Fixed parallel port driver to co-exist with Win95 ECP driver.
 + (All) External trigger and external synchronization added (not yet in User
Interface).
 + (All) Added handling of a sensor's Discharge line.  The discharge line is
ignored by the trigger.
 + (All) Added speed optimizations.
 + (Parallel) Fixed parallel timing bug, which occurred on fast computers.
 + (Super Receiver) Implemented button filtering (debounce)on Super Receiver.
 + (Super Receiver) Fixed occasional freezing of Super Receiver display.
 + (Super Receiver) Fixed button handling to report missed button clicks.
 + (Super Receiver) Changed SetTimeStamp to use microseconds in addition to
milliseconds.  This is for hi-speed recording, which could have frequencies >
1kHz.
 + (Super Receiver) Changed detection code to skip interrupts that are in use by
other devices.  Hooking the comm port interrupt would cause problems with serial
mice.
 + (All) Added ability of user application to get the version of the driver.

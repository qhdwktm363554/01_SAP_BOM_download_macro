# 01_SAP_BOM_download_macro

purpose: 
  1. macro program realization with ultiple monitors having different resolution 
  2. automatic work for BOM download from SAP(ERP system)

features: 
  1. ImageGrab: ImageGrab.grab = partial(ImageGrab.grab, all_screens = True) 
  (reference: https://qhdwktm363554.github.io/02_python/python_pyautogui/)
  without this, program will not run with captured images on a different resolution monitor
  2. pyautogui: for macro program
  3. pandas: it does not necessarily to be pandas. I am just more familiar with pandas
  4. Pause function: once mouse pointer goes very left up(screen coordinator is [zero, zero]), program execution will be stopped

Code execution is recommended with command line since IDE is possibly eliminated when it is active on a screen

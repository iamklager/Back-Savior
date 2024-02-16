#### Packages
import tkinter # For the popup window
import time # For waiting 30min

#### Function to create the popup
def f_CreatePopup(
        n_PopupWidth = 640,
        n_PopupHeight = 240,
        c_PopupMessage = "\n30min are over!\n\nStand up!\n\nStraighten your back!\n\nWalk a bit!\n\nAnd sit down in PROPER position!\n\nYou shrimp!",
        c_PopupTitle = "Back Savior",
        n_WaitingTime = 5 # Time to wait before another popup appears (in seconds)
    ):
    ### Dynamic variables
    c_PopupSize = str(n_PopupWidth) + "x" + str(n_PopupHeight) # Popup window size
    b_PopupOpen = False # Popup state (True = Open, False = Close)
    
    ### Main loop
    while 1:
        # Changing the popup state
        b_PopupOpen = False
        
        ## Creating a popup window if none is open
        if b_PopupOpen == False:
            # Popup object
            tk_Popup = tkinter.Tk()
            tk_Popup.geometry(c_PopupSize)
            tk_Popup.title(c_PopupTitle)
            # Annotating a label
            tk_MessageLabel = tkinter.Label(tk_Popup, text = c_PopupMessage)
            tk_MessageLabel.pack()
            # Saving the popup state as True
            b_PopupOpen = True

            # Main loop of the tkinter popup object
            tk_Popup.mainloop()
            
            #  Waiting the desired amount of time
            time.sleep(n_WaitingTime)


#### Main program
if __name__ == "__main__":
    f_CreatePopup(n_WaitingTime = 30*60)

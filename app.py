from tkinter import *
import threading
from stopwatchapp import StopWatch
from record_audio import AudioRecorder
import whisper


class App:
    def __init__(self,root):
        self.root = root
        self.root.title("Stopwatch")
        self.stopwatch = StopWatch()
        self.recorder = AudioRecorder()
        self.root.geometry()
        self.root.config(bg="Cadet Blue")

        self.model = whisper.load_model('base')

        rootFrame = Frame(root,bg="Cadet Blue",pady=2,padx=40,bd=20,relief=RIDGE)
        rootFrame.grid(column=0,row=0)

        lblTitle=Label(rootFrame,font=('arial',100,'bold'),text="Stopwatch",bg="Cadet Blue",fg="Cornsilk",justify=CENTER,borderwidth=2,
                       width=11)
        
        lblTitle.grid(row=0,column=0,padx=10)

        MainFrame = Frame(root,bg="Cadet Blue",width=900,height=400,bd=20,relief=RIDGE)
        MainFrame.grid(column=0,row=1,padx=30)

        MainFrameTop = Frame(MainFrame,bg="Cadet Blue",width=900,height=200,bd=20,relief=RIDGE)
        MainFrameTop.grid(column=0,row=0,padx=40)

        MainFrameBottom = Frame(MainFrame,bg="Cadet Blue",width=900,height=200,bd=20,relief=RIDGE)
        MainFrameBottom.grid(column=0,row=1,padx=30)        

        self.lblStopwatch = Label(MainFrameTop,font=('arial',100,'bold'),text="00:00:00",width=14,justify=CENTER)
        self.lblStopwatch.grid(row=0,column=0)

        self.startButton = Button(MainFrameBottom,text="Start",font=('arial',20,'bold'),width=10,command=self.start_timer)
        self.startButton.grid(row=0,column=0)
        self.stopButton = Button(MainFrameBottom,text="Stop",font=('arial',20,'bold'),width=10,command=self.stop_timer)
        self.stopButton.grid(row=0,column=1)
        self.resetButton = Button(MainFrameBottom,text="Reset",font=('arial',20,'bold'),width=10,command=self.reset_timer)
        self.resetButton.grid(row=0,column=2)

        self.transcriptionBox = Text(root, height=10, width=80, font=('arial', 14, 'bold'))
        self.transcriptionBox.grid(column=0, row=2, padx=20, pady=10)

    def start_recording(self):
        self.recording_thread = threading.Thread(target=self.recorder.start_recording)
        self.recording_thread.start()
    
    def transcribe(self):
        frames = self.recorder.get_frames()
        results = self.model.transcribe(frames)
        return results['text']

    def stop_recording(self):
        self.recorder.stop_recording()
        self.recorder.terminate()
        transcription = self.transcribe()
        self.transcriptionBox.delete('1.0', END)  # Clear previous text
        self.transcriptionBox.insert(END, transcription)  # Insert new transcription

    def reset_recording(self):
        self.recorder.reset_recording()


    def start_timer(self):
        self.stopwatch.start()
        self.start_recording()
        self.update_timer()
    def stop_timer(self):
        self.stopwatch.stop()
        self.stop_recording()
    def reset_timer(self):
        self.stopwatch.reset()
        self.reset_recording()
        self.update_timer()
    def update_timer(self):
        self.lblStopwatch.config(text=self.stopwatch.update())
        self.root.after(10,self.update_timer)


root = Tk()
app = App(root)
root.mainloop()
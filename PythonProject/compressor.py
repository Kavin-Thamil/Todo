import FreeSimpleGUI as gui

label1 = gui.Text("Select the files to compress: ")
input1 = gui.InputText()
button1 = gui.FileBrowse("CHOOSE")

label2 = gui.Text("Select Destination folder:  ")
input2 = gui.InputText()
button2 = gui.FolderBrowse("CHOOSE")

button3 = gui.FileBrowse("Compress")

window = gui.Window('Compressor de Zip',
                    layout = [[label1], [input1, button1],
                              [label2], [input2, button2],
                              [button3]])
window.read()
window.close()
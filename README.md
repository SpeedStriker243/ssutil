# SpeedStriker Utility

SpeedStriker Utility is a discontinued proof-of-concept command line application written in Python. 

Further development will be done in [Synax Console]("https://github.com/That1M8Head/SynaxConsole"). Please go there instead.

## Command list


`su` - Opens a Command Prompt (not SYC4WIN) window with your current user privileges

`netsu <servername>` - Possesses the same function as su, but for use if your computer is on a network.
  
`psu` - Opens a PowerShell window with your current user privileges

`netpsu <servername>` - Possesses the same function as psu, but for use if your computer is on a network.
  
`sudo <command>` - Runs any CMD command with your current user privileges

`pccheck` - Displays information about your PC.

`clear/cls` - Clears the screen.

`prompt <nothing|path|syc4win|all>` - Affects the visibility of elements of the prompt.

  > For example, `prompt path` would make the prompt display as `C:\Folder\`
  
`cd <dirname>` - Changes your current directory.
  
`path` - Gets and prints the current path.

`copypath` - Copies the current path to the clipboard.

`ls` - Lists directories.

`up` - Goes up a directory.

`open` - Opens the specified file.

`echo <message>` - Prints a message to the console.
  
`new <dirname>` - Creates a new directory.
  
`del <filename>` - Deletes the specified file.
  
`web <URL>` - Opens the specified URL in your default browser.
  
`wsearch <search term>` - Searches the web for the specified search term.
  
`exit` - Gracefully exits the console.
  
`crash` - Invokes a crash.

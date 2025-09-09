Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

strScriptPath = objFSO.GetParentFolderName(WScript.ScriptFullName)
strVsDevCmdPath = objShell.ExpandEnvironmentStrings("%ProgramFiles(x86)%") & "\Microsoft Visual Studio\2019\BuildTools\Common7\Tools\VsDevCmd.bat"
strCommand = "cmd.exe /c ""call """ & strVsDevCmdPath & """ && cd /d """ & strScriptPath & """ && code ."""

' Run the command silently (0 = hidden window, True = wait for completion)
objShell.Run strCommand, 0, True
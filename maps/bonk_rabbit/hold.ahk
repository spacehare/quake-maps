#Requires AutoHotkey v2.0

toggle := false
#HotIf WinActive('ahk_exe quakespasm.exe')
RButton:: {
	global toggle := !toggle
	SendInput toggle ? '{LButton down}' : '{LButton up}'
}

~LButton:: {
	global toggle := false
}
#HotIf
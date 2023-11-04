#MaxThreadsPerHotKey, 2

Time := 18000
Toggle_M := 0

F6::
Toggle := !Toggle
If (Toggle){
	ControlSend,, {k down}, Minecraft 1.8.9
	While (Toggle){
		Random, Delay,, 100, 250
		ControlSend,, {d down}, Minecraft 1.8.9
		Sleep, Time
		Sleep, Delay
		ControlSend,, {d up}, Minecraft 1.8.9
		ControlSend,, {s down}, Minecraft 1.8.9
		Sleep, Time
		Sleep, Delay
		ControlSend,, {s up}, Minecraft 1.8.9
		ControlSend,, {w down}, Minecraft 1.8.9
		Sleep, 50
		ControlSend,, {w up}, Minecraft 1.8.9
	}
}
ControlSend,, {k up}, Minecraft 1.8.9
ControlSend,, {d up}, Minecraft 1.8.9
ControlSend,, {s up}, Minecraft 1.8.9

F7::
Toggle := !Toggle
ControlSend,, {k down}, Minecraft 1.8.9
While (Toggle){
	ControlSend,, {w down}, Minecraft 1.8.9
}
ControlSend,, {k up}, Minecraft 1.8.9
ControlSend,, {w up}, Minecraft 1.8.9
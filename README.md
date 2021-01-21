# RemoteShell
Wrapper that uses telnetlib and paramiko to allow remote shell connection that will first try SSH, then if that fails it falls back to telnet. The purpose is to make a tool that allows the easy creation of Cisco network scripts that run in an enviroment where some equipment has SSH enabled, some does not, and some of the equipment has no user name for the telnet access. This will hide that complexity from the higher level script. 


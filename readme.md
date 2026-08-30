### how to setup flash mcp

# Method 1:
if you have "Adobe extension manager cs6" it is the easy way.
open extension manager(if it freezes dont worry. stop it with task manager and rerun as admistrator if doesnt works use compalibity mode with windows 7)
chose load.
select flash-mcp.zxp
agree

thats all.
for use:
open flash cs6 and open panel (windows -> Other Panels -> flash-mcp-server)
open claude/opencode etc.
select working directory as here.
prompt: connect to flash and learn the skill from skill md.

note: some tiny models cannot use mcp-server.py(includes over 150 tools) you can change .mcp.json as:
---------------------------------------------------------------

{
  "mcpServers": {
    "flash-mcp": {
      "command": "python",
      "args": [
        "${current_working_directory}/mcp/mcp_server.py"
      ]
    }
  }
}

----------------------------------------------------------------
(_small has only 16 tools)

# method 2:
if you dont have extensşon manager dont worry.
copy flash-mcp.swf
(flash mustn't be running)
and paste into these two folders(both of them)

1- %localappdata%\Adobe\Flash CS6\en_US\Configuration\WindowSWF\flash-mcp.swf

2- local disk c\Program Files (x86)\Adobe\Adobe Flash CS6\en_US\Configuration\WindowSWF\flash-mcp.swf

Note: if there is no WindowSWF folder create it manually.
other steps are similar with Method 1.
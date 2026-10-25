---
name: godot-mcp-setup
description: "Install and use Godot MCP (Coding-Solo/godot-mcp), an MCP server that lets Claude Code launch the Godot editor, run a project, read debug output, create scenes and add nodes. Use when the user works on a Godot project and wants Claude to run or inspect it, or asks how to connect Godot to Claude."
license: MIT (this guide); godot-mcp itself is MIT
---

# Godot MCP setup

Godot MCP is not a skill. It is an MCP server (Node.js) that gives Claude tools to drive a local Godot install. It works in Claude Code on the user's computer, not in claude.ai chat, because it needs Godot and Node on that machine.

Source: https://github.com/Coding-Solo/godot-mcp (MIT).

## Requirements

- Godot 4 installed (Godot 4.4+ for the UID tools).
- Node.js 18 or newer with npm.

## Install in Claude Code

```bash
claude mcp add godot -- npx @coding-solo/godot-mcp
```

If Godot is not on PATH, give its path:

```bash
claude mcp add godot -e GODOT_PATH=/path/to/godot -- npx @coding-solo/godot-mcp
```

Restart Claude Code, then check with `/mcp` that `godot` is connected.

For other MCP clients, use this config:

```json
{ "mcpServers": { "godot": { "command": "npx", "args": ["@coding-solo/godot-mcp"], "env": { "GODOT_PATH": "/path/to/godot" } } } }
```

## Tools it adds

`launch_editor`, `run_project`, `get_debug_output`, `stop_project`, `get_godot_version`, `list_projects`, `get_project_info`, `create_scene`, `add_node`, `load_sprite`, `export_mesh_library`, `save_scene`, `get_uid`, `update_project_uids`.

## How to work with it

1. `get_godot_version` first, to confirm the server sees Godot.
2. `get_project_info` on the project folder before editing scenes.
3. After code changes: `run_project`, then `get_debug_output` to read errors, fix, and run again. Call `stop_project` when done.
4. Pair with the gamedev plugin skills `godot-gdscript`, `godot-nodes-scenes`, `godot-gdscript-headless-testing`.

## Troubleshooting

- "Godot not found": set `GODOT_PATH` to the executable (on macOS: `/Applications/Godot.app/Contents/MacOS/Godot`).
- Set `DEBUG=true` in the env to see server logs.

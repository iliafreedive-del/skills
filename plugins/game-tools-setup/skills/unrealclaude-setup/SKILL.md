---
name: unrealclaude-setup
description: "Install and use UnrealClaude (Natfii/UnrealClaude), an Unreal Engine 5.7 editor plugin that docks a Claude Code chat in the editor and runs an MCP server with 20+ tools for actors, Blueprints, levels, materials and assets. Use when the user works in Unreal Engine and wants Claude inside the editor or controlling it."
license: MIT (this guide); UnrealClaude itself is MIT
---

# UnrealClaude setup

UnrealClaude is not a skill. It is a C++ editor plugin for Unreal Engine 5.7 plus an MCP bridge (Node.js). It runs on the user's computer next to Unreal and Claude Code; it does nothing in claude.ai chat.

Source: https://github.com/Natfii/UnrealClaude (MIT). Supports Win64, Linux and macOS (Apple Silicon).

## Requirements

- Unreal Engine 5.7 (with a C++ toolchain to build plugins).
- Node.js and Claude Code CLI, signed in (`claude auth login`). It uses the Claude Code subscription, no separate API key.

## Install

1. Clone with the submodule:
   ```bash
   git clone --recurse-submodules https://github.com/Natfii/UnrealClaude.git
   ```
2. Build for your platform (no prebuilt binaries):
   ```bash
   # Windows
   Engine\Build\BatchFiles\RunUAT.bat BuildPlugin -Plugin="PATH\UnrealClaude\UnrealClaude\UnrealClaude.uplugin" -Package="OUT" -TargetPlatforms=Win64
   # Linux / macOS: RunUAT.sh with -TargetPlatforms=Linux or Mac
   ```
3. Copy the build output to `YourProject/Plugins/UnrealClaude/` (or the engine's `Engine/Plugins/Marketplace/` for all projects).
4. Install the MCP bridge dependencies:
   ```bash
   cd YourProject/Plugins/UnrealClaude/Resources/mcp-bridge && npm install
   ```
5. Launch the editor and open **Tools > Claude Assistant**.
6. Optional: point Claude Code at the plugin's MCP bridge as the plugin's setup panel shows, then restart Claude Code.

See the repository's INSTALL_LINUX.md and INSTALL_MAC.md for platform details.

## How to work with it

- Ask in the editor panel, or from Claude Code once the MCP bridge is connected.
- Blueprint editing still has bugs upstream: save the project before large Blueprint changes and check the result.
- Script execution and Live Coding ask for permission; read the script before approving.
- Pair with the gamedev plugin skills `unreal-cpp-gameplay`, `unreal-blueprints`, `unreal-enhanced-input`, and the game-studios agents `unreal-specialist`, `ue-blueprint-specialist`.

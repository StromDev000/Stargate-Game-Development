# Stargate Game Development Architecture

A mono-repository for independent Godot, Unity and WebGL clients, shared versioned game data and asset catalogs.

- `game/`: independent engine-specific prototypes
- `assets/`: Blender sources, GLB/glTF, animations, textures, shaders and environments
- `database/`: validated JSON design data for characters, races, planets and weapons
- `systems/`: shared specifications for combat, AI, inventory, multiplayer
- `tools/`: asset validation and conversion helpers
- `research/`: upstream sources and license evidence
- `docs/`: architecture and roadmap

For mobile rendering, target LODs, texture compression, atlases and limited draw calls; validate with real Android/iOS devices. Use feature branches and PR review. Never commit tokens or unlicensed media.

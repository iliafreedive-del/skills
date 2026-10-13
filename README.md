# Скилы для Claude Code

Набор скилов (Agent Skills, формат `SKILL.md`) для наших проектов, прежде всего игры Dark Ascent ([game-rpg](https://github.com/iliafreedive-del/game-rpg)). Источник: папка «СКИЛЫ» на Яндекс Диске.

## Как поставить

```bash
git clone https://github.com/iliafreedive-del/skills
./skills/install.sh path/to/game-rpg            # все скилы в проект
./skills/install.sh path/to/game-rpg router threejs-scene-setup game-feel   # выборочно
./skills/install.sh -g ponytail graphify        # глобально, для всех проектов
```

Скил — это папка с `SKILL.md`. Claude Code сам подгружает его, когда задача подходит под описание, или по команде `/имя`.

## Что внутри

| Пак | Скилов | Что даёт | Лицензия |
| --- | ---: | --- | --- |
| [awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 72 + `router` | Геймдев: движки (three.js, Phaser, PixiJS, Godot, Unity, Unreal…), жанры (RPG, рогалик…), дисциплины (game feel, UI/UX, камера, сохранения, производительность, звук). `router` сам выбирает нужные | Apache-2.0 |
| [ponytail](https://github.com/DietrichGebert/ponytail) | 6 | Режим «ленивого сеньора»: самая маленькая правка, которая решает задачу; аудит, ревью, техдолг | MIT |
| [graphify](https://github.com/Graphify-Labs/graphify) | 1 | База знаний: строит граф проекта (код, документы, картинки) в `graphify-out/` и отвечает на вопросы по нему. Нужен Python-пакет `graphifyy` | Apache-2.0 |
| [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | 11 | Рабочий процесс разработки: `verification-loop` (проверка перед сдачей), `eval-harness` (проверки «готово» до кода), `tdd-workflow`, `coding-standards`, `frontend-patterns`, `security-checklist`, `continuous-learning`, `strategic-compact` и др. Агенты, команды, правила и хуки пака лежат в `extras/everything-claude-code/` | MIT (по README) |
| [img2threejs](https://github.com/img2threejs/img2threejs) | 1 | Картинка → 3D-модель в коде three.js: по референсу (персонаж, предмет, оружие, постройка) собирает процедурную модель проход за проходом, сверяя скриншоты с картинкой; умеет риг под анимацию и экспорт. Утилиты `forge/` на чистом Python 3.10, без pip | Apache-2.0 |
| [agentskills](https://github.com/agentskills/agentskills) | — | Спецификация формата и валидатор `tools/skills-ref` | Apache-2.0 |

Для веб-игры на three.js главные: `router`, `threejs-scene-setup`, `threejs-gltf-loading`, `threejs-materials-lighting`, `performance-optimization`, `game-feel`, `game-ui-ux`, `camera-systems`, `input-systems`, `save-systems`, `audio-design`, `rpg`, `roguelike`, `level-design`, `create-game-assets`, `graphify`, `ponytail`, `img2threejs` (модели по картинке).

Из папки не вошёл `OmniRoute-release-v3.8.52.zip`: это отдельное приложение-шлюз для ИИ-моделей (209 МБ), а не скил.

## Проверка формата

```bash
pip install ./tools/skills-ref
for d in skills/*/; do skills-ref validate "$d"; done
```

Все скилы проходят проверку; у `ponytail` есть поле `argument-hint`, его нет в базовой спецификации, но Claude Code его понимает.

Из everything-claude-code: скил `security-review` переименован в `security-checklist`, чтобы не перекрывать встроенную команду Claude Code `/security-review`; у `eval-harness`, `verification-loop` и `project-guidelines-example` не было заголовка `name`/`description`, он добавлен.

Лицензии и NOTICE исходных паков лежат в `licenses/`.

Из img2threejs не взята папка `.github` (CI и шаблоны исходного репозитория); её утилиты `forge/` ставятся вместе со скилом и запускаются из папки скила.

## Каталог

| Скил | Описание |
| --- | --- |
| `ai-behavior-trees-utility-ai` | Build a production behavior-tree runtime (Blackboard, action/condition leaves, sequence/selector/parallel composites, decorators) and a Utility AI sys… |
| `audio-design` | Implement game audio practice — bus/mixer architecture and gain in decibels, ducking (sidechain), adaptive/dynamic music via layering and re-sequencin… |
| `bevy-ecs` | Structure a Bevy app around its Entity Component System: build the App with plugins, define Component/Resource types, write systems with Query/Res/Com… |
| `camera-systems` | Build game cameras that feel good — 2D follow with a deadzone, look-ahead, smoothing, and level-bounds clamping; 3D third-person orbit with collision … |
| `card-game` | Build a card game: card data, deck/hand/discard zones, draw/shuffle/reshuffle, a turn structure, costs, and effect resolution. Use for a deckbuilder, … |
| `create-game-assets` | Plan, generate, source, normalize, and validate cohesive visual game assets. Use for art direction, style bibles, sprites, tilesets, backgrounds, UI a… |
| `dialogue-systems` | Build branching dialogue and narrative — a node/choice graph with conditions, variables, and localization hooks — and choose between authoring tools I… |
| `fps-shooter` | Build a first-person shooter: move+mouse-look controller, hitscan or projectile shooting, weapons, health, and enemy AI. Use for an FPS, or tuning aim… |
| `game-ai` | Design NPC and enemy decision-making with finite state machines, behavior trees, steering behaviors, and A* pathfinding — engine-neutral algorithms th… |
| `game-feel` | Add "juice" and game feel that makes actions satisfying — screen shake, hit-stop/freeze frames, tweened/eased motion, squash & stretch, knockback, and… |
| `game-jam` | Plan and ship a game under a jam deadline: lock scope to the clock, schedule the hours, cut features, and submit on time. Use for a game jam (Ludum Da… |
| `game-ui-ux` | Design and build game UI/UX — HUDs, menus, and overlays — that survive every screen: anchor- based responsive layout, resolution/aspect scaling and sa… |
| `godot-2d-movement` | Implement 2D kinematic character movement in Godot 4.7 with CharacterBody2D and move_and_slide(): platformer run/jump with gravity, top-down 8-directi… |
| `godot-3d-essentials` | Set up a Godot 4.7 3D scene: Node3D transforms, Camera3D, lighting (DirectionalLight3D/OmniLight3D), WorldEnvironment for sky/ambient/tonemap/post, Me… |
| `godot-animation` | Animate in Godot 4.7 three ways: AnimationPlayer for keyframed clips (incl. call and signal tracks), AnimationTree with state machines and blend space… |
| `godot-audio` | Play and mix audio in Godot 4.7: AudioStreamPlayer (2D/3D variants), audio buses with volume/mute and effects, music vs SFX routing, db/linear volume,… |
| `godot-csharp` | Use C#/.NET in Godot 4.7: partial classes extending nodes, the PascalCase lifecycle (_Ready/_Process/_PhysicsProcess), [Export] fields, [Signal] deleg… |
| `godot-export` | Export and build a Godot 4.7 project for distribution: install export templates, define export presets (Windows/macOS/Linux/Web/Android), run headless… |
| `godot-gdscript-headless-testing` | Run GDScript test suites from the command line with `godot --headless`, using a SceneTree/MainLoop runner script that exits non-zero on failure so CI … |
| `godot-gdscript` | Write idiomatic GDScript for Godot 4.7: static typing, the node lifecycle (_ready/_process/_physics_process), @export/@onready/@tool annotations, sign… |
| `godot-multiplayer` | Build networked games with Godot 4.7 high-level multiplayer: set up an ENetMultiplayerPeer server/client, define RPCs with the @rpc annotation (call v… |
| `godot-nodes-scenes` | Structure a Godot 4.7 project with the scene tree and node composition: build reusable scenes, instance PackedScenes at runtime, navigate the tree saf… |
| `godot-physics` | Use Godot 4.7 physics bodies and detection in 2D and 3D: RigidBody, StaticBody, Area, and CharacterBody; collision layers vs masks; contact/overlap si… |
| `godot-resources` | Design data-driven Godot 4.7 games with custom Resource classes: define typed data with class_name + @export, save/load .tres/.res files, instance and… |
| `godot-shaders` | Write Godot 4.7 shaders in the Godot Shading Language: canvas_item shaders for 2D and spatial shaders for 3D, with vertex/fragment functions, uniforms… |
| `godot-signals-groups` | Build event-driven, decoupled Godot 4.7 gameplay with signals and node groups: declare and emit custom signals, connect with Callables (incl. bind/one… |
| `godot-tilemap` | Build and edit tile-based 2D levels in Godot 4.7 with TileMapLayer and TileSet: paint layers, set up collision/navigation/custom-data on tiles, autoti… |
| `godot-ui-control` | Build Godot 4.7 user interfaces with Control nodes: anchors and offsets for responsive layout, Container nodes (VBox/HBox/Grid/Margin) for automatic a… |
| `graphify` | Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the ques… |
| `img2threejs` | Turn an object or character reference image into a quality-gated, animation-ready procedural Three.js model built in code. Use for image-to-3D reconstruction, detail-accurate object rebuilds… |
| `input-systems` | Architect game input — action mapping (abstracting keys into named actions), rebinding with conflict detection and persistence, multi-device support (… |
| `itch-publish` | Publish and update a game on itch.io: create the project page and upload builds with the butler CLI (butler push) to named channels. Use for itch.io p… |
| `level-design` | Design and build playable levels — the blockout/whitebox-to-playable workflow, player metrics and grid layout, pacing and flow (tension/rest curve), g… |
| `love2d-core` | Structure and debug a LÖVE (Love2D) game in Lua: the love.load/update/draw loop, delta-time movement, input, and screen states. Use when building a LÖ… |
| `performance-optimization` | Find and fix game performance problems methodically — measure with the engine profiler first, reason about the frame-time budget, locate the CPU-vs-GP… |
| `phaser-arcade-physics` | Use Phaser 4 Arcade Physics: enable the world, give sprites bodies, set velocity/acceleration/gravity, and resolve collisions with colliders, overlaps… |
| `phaser-core` | Set up and debug a Phaser 4 game: the Game config, the Scene lifecycle (init/preload/create/update), the asset loader, cameras, and cross-scene commun… |
| `physics-tuning` | Tune game physics for stable, good-feeling motion — fixed vs variable timestep, render interpolation, mass/gravity/drag, continuous collision detectio… |
| `pixijs-rendering` | Build a PixiJS v8 render layer: create the async Application, load textures with Assets, compose the scene graph with Container and Sprite, drive the … |
| `platformer` | Build a 2D platformer: run/jump control with coyote time, jump buffering, and variable jump height, plus tiled levels and hazards. Use for a platforme… |
| `ponytail-audit` | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or s… |
| `ponytail-debt` | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes nothing. Use for "ponytail debt", "what did pon… |
| `ponytail-gain` | Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display. Use for /ponytail-gain, "what does ponytail save", "ponytai… |
| `ponytail-help` | Quick reference for ponytail levels, skills and commands. One-shot display. Use for /ponytail-help, "ponytail help", "how do I use ponytail". |
| `ponytail-review` | Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line n… |
| `ponytail` | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writin… |
| `procedural-gen` | Generate game content procedurally — seeded deterministic RNG, value/Perlin/ Simplex noise for terrain and heightmaps, grid dungeon generation (rooms … |
| `prototype-fast` | Build a playable prototype in about an hour to answer one question — is it fun? — with greybox primitives, a hard timebox, and explicit keep/kill crit… |
| `puzzle` | Build a puzzle game: grid/board state, move input, rule-based resolution (match-3 cascades, sokoban pushes, tile logic), scoring, and undo. Use for a … |
| `pygame-core` | Structure a pygame (pygame-ce) game in Python: the init/event/update/draw loop, delta-time movement, Surface/Rect blitting, keyboard/mouse input, and … |
| `roblox-characters` | Build respawn-safe Roblox character systems around Players, CharacterAdded/CharacterRemoving, Humanoid, HumanoidRootPart, Animator, R6/R15 rigs, movem… |
| `roblox-datastores` | Persist player data in Roblox with DataStoreService: GetDataStore, GetAsync/ SetAsync/UpdateAsync/IncrementAsync wrapped in pcall, load-on-join and sa… |
| `roblox-luau` | Script a Roblox experience in Luau: get services, create and parent Instances, connect events, run server Scripts vs client LocalScripts, and communic… |
| `roblox-networking` | Design and harden Roblox client/server networking with RemoteEvent, RemoteFunction, and UnreliableRemoteEvent; server authority, argument and Instance… |
| `roblox-physics` | Implement Roblox physical simulation and queries with assemblies, anchoring, constraints, collision groups, CanCollide/CanTouch/CanQuery, raycasts and… |
| `roblox-studio-workflow` | Modify living Roblox Studio projects safely: inspect Explorer and execution locations, preserve existing structure, reuse modules/remotes, create mean… |
| `roblox-ui` | Build production Roblox interfaces with ScreenGui/PlayerGui lifecycle, responsive UDim2 layouts, safe insets, reusable editable Instances, cross-devic… |
| `roguelike` | Build a roguelike: turn-based grid movement, procedural dungeons, permadeath, field-of-view, and loot tables. Use for a roguelike/roguelite or turn-ba… |
| `router` | Routes any game-development request to the right specialized skill(s): it detects the engine (Godot, Unity, Unreal, Bevy, Phaser, PixiJS, three.js, LÖ… |
| `rpg` | Build an RPG: stats and leveling, inventory and equipment, quests, branching dialogue, save/load, and combat. Use for an RPG/JRPG, or designing stat, … |
| `save-systems` | Design save/load for game state — choosing what to serialize, file formats, save slots, atomic crash-safe writes, schema versioning and migration, and… |
| `shader-programming` | Write game shaders from cross-engine fundamentals — the vertex→fragment pipeline, coordinate spaces, UV math, and common 2D/3D effects (tint, UV scrol… |
| `steam-publish` | Publish or update a game on Steam with Steamworks and SteamPipe: configure depots and packages, upload builds with steamcmd, set a build live on a bra… |
| `survival-crafting` | Build a survival-crafting game: resource gathering, inventory, crafting and a tech tree, needs (hunger/thirst/temperature), and base building. Use for… |
| `threejs-gltf-loading` | Load glTF/GLB models in three.js with GLTFLoader and play their skinned animations with AnimationMixer, including DRACO/Meshopt-compressed meshes and … |
| `threejs-materials-lighting` | Light and shade a three.js scene: choose materials (MeshStandardMaterial PBR vs unlit MeshBasicMaterial), add ambient/hemisphere/directional/point/spo… |
| `threejs-scene-setup` | Stand up a three.js scene: import maps and the three/addons path, the Scene/PerspectiveCamera/WebGLRenderer trio, the setAnimationLoop render loop, re… |
| `tower-defense` | Build a tower defense: enemies pathing along lanes, wave spawning, towers that auto-target and fire, an economy, and lives. Use for a tower-defense/wa… |
| `unity-animation` | Drive Unity 6.3 LTS character animation with Animator Controllers: states, transitions, parameters, blend trees, animation layers, and humanoid Avatar… |
| `unity-build-pipeline` | Build and ship Unity 6.3 LTS players: build settings and scenes, player/quality settings, the IL2CPP vs Mono scripting backend, managed code stripping… |
| `unity-csharp-scripting` | Write Unity 6.3 LTS C# gameplay scripts: the MonoBehaviour lifecycle (Awake/OnEnable/Start/Update/FixedUpdate/LateUpdate), GameObject and component ac… |
| `unity-input-system` | Wire player input in Unity 6.3 LTS with the Input System package: Input Actions, action maps, the PlayerInput component, and reading values via callba… |
| `unity-navmesh` | Add AI navigation in Unity 6.3 LTS: bake a NavMesh with the AI Navigation package (NavMeshSurface), move agents with NavMeshAgent.SetDestination, and … |
| `unity-physics` | Set up 3D physics in Unity 6.3 LTS: Rigidbody movement and forces, colliders, triggers vs collisions, layer-based collision, raycasts, and joints. Use… |
| `unity-scriptableobjects` | Architect Unity 6.3 LTS data and decoupling with ScriptableObjects: config/data assets, shared runtime variables, event channels, and runtime sets/reg… |
| `unity-tilemap-2d` | Build and script 2D tilemaps in Unity 6.3 LTS: the Grid + Tilemap components, the Tile Palette, tilemap colliders, rule tiles, and runtime SetTile/Get… |
| `unreal-behavior-trees` | Build NPC AI in Unreal Engine 5 with Behavior Trees and Blackboards: composites (Selector/Sequence), tasks, decorators, services, and running the tree… |
| `unreal-blueprints` | Build Unreal Engine 5 gameplay with Blueprint visual scripting: Blueprint Classes, the Event Graph and Construction Script, variables/functions/macros… |
| `unreal-cpp-gameplay` | Write Unreal Engine 5 C++ gameplay code: the UCLASS/UPROPERTY/UFUNCTION reflection macros, the Gameplay Framework (GameMode, Pawn, Character, PlayerCo… |
| `unreal-enhanced-input` | Set up player input in Unreal Engine 5 with Enhanced Input: Input Actions, Input Mapping Contexts, modifiers and triggers, adding the mapping context,… |
| `unreal-niagara` | Create and control VFX in Unreal Engine 5 with Niagara: systems and emitters, modules and the spawn/update stages, exposed User parameters, and spawni… |
| `unreal-packaging` | Package and ship an Unreal Engine 5 project: the Platforms menu Package Project flow, build configurations (Development vs Shipping), cooking content,… |
| `visual-novel` | Build a visual novel: a branching script, character and background display, a text box with choices, save/load, backlog, and skip/auto. Use for a VN, … |
| `backend-patterns` | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| `clickhouse-io` | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. |
| `coding-standards` | Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development. |
| `continuous-learning` | Automatically extract reusable patterns from Claude Code sessions and save them as learned skills for future use. |
| `eval-harness` | Eval-driven development for Claude Code sessions: define capability and regression evals before coding, run them, and track pass@k. Use when adding a … |
| `frontend-patterns` | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| `project-guidelines-example` | Example template of a project-specific guidelines skill (architecture, file layout, code patterns, testing, deployment). Use as a starting point when … |
| `security-checklist` | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive featur… |
| `strategic-compact` | Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction. |
| `tdd-workflow` | Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with 80%+ coverage including unit, integr… |
| `verification-loop` | Run a full verification pass before calling work done or opening a PR: build, typecheck, lint, tests, security scan, diff review, and a final report. … |

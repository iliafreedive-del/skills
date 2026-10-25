# Скилы для Claude

Библиотека скилов (Agent Skills, формат `SKILL.md`) для всех проектов. Репозиторий оформлен как маркетплейс плагинов Claude: 227 скилов в 7 плагинах.

## Как поставить в claude.ai (все чаты, проекты, Cowork и Claude Code)

1. Открой [Customize → Plugins](https://claude.ai/customize/plugins) (в левом меню **Customize**, вкладка **Plugins**).
2. Нажми **Add** → **Add marketplace** → **Add from a repository**.
3. Введи `iliafreedive-del/skills`. Если Claude попросит, нажми **Connect GitHub** или **Install the Claude GitHub App** и дай доступ к этому репозиторию.
4. В списке появятся плагины ниже. У каждого нажми **Add** (или **Install**).
5. Включи **Sync automatically** у маркетплейса, тогда новые скилы из репозитория будут подтягиваться сами. Вручную: **Check for updates**.

Скилы срабатывают сами, когда задача подходит под описание. Выбрать вручную: `/` в поле сообщения, затем `плагин:скил`.

Плагины доступны на платных тарифах (Pro, Max, Team, Enterprise). Агенты (`agents/`) работают в Cowork и Claude Code, в обычном чате пропускаются.

## Claude Code из терминала

```bash
claude plugin marketplace add iliafreedive-del/skills
claude plugin install gamedev@iliafreedive-skills      # и так для каждого плагина
```

Или скопировать отдельные скилы в проект: `./install.sh путь/к/проекту router game-feel` (`-g` вместо пути ставит в `~/.claude/skills`).

## Плагины

| Плагин | Скилов | Агентов | Что даёт | Лицензия |
| --- | ---: | ---: | --- | --- |
| `gamedev` | 75 | — | Геймдев: движки (three.js, Phaser, PixiJS, Godot, Unity, Unreal, Roblox…), жанры и дисциплины. Скил router сам выбирает нужные. | [Apache-2.0](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) |
| `game-studios` | 74 | 49 | Claude Code Game Studios: 49 агентов-ролей студии (директора, программисты, дизайнеры, QA) и 74 скила процесса от идеи до релиза. Агенты работают в Cowork и Claude Code. | [MIT](https://github.com/Donchitos/Claude-Code-Game-Studios) |
| `game-tools-setup` | 3 | — | Инструкции по установке внешних инструментов: Godot MCP, UnrealClaude, NVIDIA Audio2Face-3D. | [MIT](https://github.com/iliafreedive-del/skills) |
| `acestep-music` | 6 | — | Музыка через ACE-Step 1.5: генерация и ремикс песен, тексты, обложки, клипы, расшифровка текста. Нужен запущенный сервер ACE-Step. | [MIT](https://github.com/ace-step/ACE-Step-1.5) |
| `img2threejs` | 1 | — | Картинка в процедурную 3D-модель three.js с проверкой по скриншотам. | [Apache-2.0](https://github.com/img2threejs/img2threejs) |
| `dev-workflow` | 18 | — | Рабочий процесс разработки: ponytail (минимальные правки, аудит), graphify (граф знаний проекта), everything-claude-code (проверка перед сдачей, TDD, стандарты, безопасность). | [MIT / Apache-2.0](https://github.com/iliafreedive-del/skills) |
| `marketing` | 50 | — | 50 маркетинговых скилов: SEO, реклама, копирайтинг, запуск, аналитика, цены, рассылки, соцсети. | [MIT](https://github.com/coreyhaines31/marketingskills) |

Для веб-игры на three.js главные: `router`, `threejs-scene-setup`, `threejs-gltf-loading`, `threejs-materials-lighting`, `performance-optimization`, `game-feel`, `game-ui-ux`, `camera-systems`, `save-systems`, `audio-design`, `rpg`, `level-design`, `create-game-assets`, `img2threejs`, `graphify`, `ponytail`.

### Заметки по плагинам

- **game-studios** взят из [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) (папка `.claude`: скилы, агенты, docs, rules, scripts). Хуки автоматизации из оригинала не подключены (`hooks/hooks.json` нет), лежат только их скрипты, которые вызывают скилы. Часть скилов ждёт структуру проекта из шаблона (`.claude/docs`, `design/`, `production/`); для полного процесса студии клонируй оригинальный репозиторий как шаблон игры.
- **acestep-music** из [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5): скилы обращаются к запущенному серверу ACE-Step (модель генерации музыки ставится отдельно, нужна видеокарта). Обложки через Gemini API, расшифровка через Whisper/ElevenLabs, нужны свои ключи.
- **game-tools-setup**: инструкции для того, что скилом не является: [Godot MCP](https://github.com/Coding-Solo/godot-mcp) (MCP-сервер, MIT), [UnrealClaude](https://github.com/Natfii/UnrealClaude) (плагин Unreal Engine 5.7, MIT), [NVIDIA Audio2Face-3D](https://github.com/NVIDIA/Audio2Face-3D) (ИИ-модели лицевой анимации; SDK и плагины MIT, модели под лицензией NVIDIA).
- **dev-workflow**: в everything-claude-code скил `security-review` переименован в `security-checklist`; агенты, команды, правила и хуки этого пака лежат в `extras/everything-claude-code/`, в плагин не входят.
- **marketing**: справочник инструментов пака в `extras/marketingskills/`.

## Проверка формата

```bash
claude plugin validate .                 # маркетплейс и все плагины
pip install ./tools/skills-ref
for d in plugins/*/skills/*/; do skills-ref validate "$d"; done
```

Лицензии и NOTICE исходных паков лежат в `licenses/`. Из папки на Яндекс Диске не вошёл `OmniRoute-release-v3.8.52.zip`: это приложение-шлюз для ИИ-моделей, а не скил.

## Каталог

### gamedev

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

### game-studios

| Скил | Описание |
| --- | --- |
| `adopt` | Brownfield audit — do existing artifacts actually work? Numbered migration plan. Unlike /project-stage-detect, checks compliance not existence. |
| `architecture-decision` | Create an ADR documenting a technical decision: context, alternatives considered, consequences. |
| `architecture-review` | Traceability matrix mapping GDD requirements to ADRs. Finds gaps, cross-ADR conflicts, engine compatibility. PASS/CONCERNS/NOT ASSESSED/FAIL. |
| `art-bible` | Author the Art Bible — visual identity gating asset production. Run before /map-systems. |
| `asset-audit` | Audit assets against naming conventions, file size budgets, format standards. Finds orphaned assets, missing references. |
| `asset-spec` | Per-asset visual specs plus AI generation prompts from GDDs and character profiles. After the art bible. |
| `balance-check` | Find balance outliers, broken progressions, degenerate strategies, economy imbalances in formulas and data. 'Check game balance'. |
| `brainstorm` | Guides the user through finding and choosing a game concept. Use when the user wants game ideas, a new concept, a game jam idea, or to explore other d… |
| `bug-report` | Structured bug report from a description, or analyze code for potential bugs. Reproduction steps, severity. |
| `bug-triage` | Re-evaluate open bugs — priority vs severity, assign to sprints, surface systemic trends. Run when the count grows. |
| `changelog` | Auto-generate a changelog from git commits and sprint data. Internal and player-facing versions. |
| `code-review` | Architectural code review — coding standards, SOLID, testability, performance concerns. |
| `consistency-check` | Scan GDDs against the entity registry for cross-document conflicts. Grep-first approach targets conflicting sections, different stats. |
| `content-audit` | Audit GDD content counts against what's implemented — planned vs built. |
| `create-architecture` | Author the architecture blueprint before code is written. Validates decisions against the pinned engine, flags knowledge gaps. |
| `create-control-manifest` | Builds a short list of must-do and never-do coding rules per system from accepted ADRs. Use when the user wants programmer rules or a cheat sheet from… |
| `create-epics` | Turns the GDDs and architecture into epics, one per architectural module. Use when the user wants to break the game into epics or plan the work before… |
| `create-stories` | Breaks one epic into implementable stories with acceptance criteria. Use when the user wants stories for an epic or the next batch of work to build. N… |
| `day-one-patch` | Day-one launch patch — focused fix for known issues found after gold master. Mini-sprint with QA gate and rollback. |
| `design-review` | Reviews one design document for completeness, internal consistency, implementability, and design standards. Before handing to programmers. |
| `design-system` | Section-by-section GDD authoring for one system — walks through each required section, cross-references dependencies. |
| `dev-story` | Implements one story in code with tests, following its ADRs. Use when the user says to build, implement or start working on a story. Not for checking … |
| `estimate` | Estimate task effort from complexity, dependencies, velocity, risk. Structured estimate with confidence levels. |
| `gate-check` | Ready to advance between development phases? PASS/CONCERNS/NOT ASSESSED/FAIL with blockers and required artifacts. 'Can we move to production?' |
| `help` | What should I do next? Use when stuck or you don't know what to do. |
| `hotfix` | Emergency fix bypassing normal sprint process — hotfix branch, approvals tracked, backport verified, full audit trail. |
| `launch-checklist` | Launch readiness across every department: code, content, store, marketing, community, infrastructure, legal, go/no-go sign-offs. |
| `localize` | Localization pipeline — find hardcoded strings, extract string tables, cultural review, VO, RTL, enforce string freeze. |
| `map-systems` | Decompose a concept into individual systems, map dependencies, prioritize design order, create the systems index. |
| `milestone-review` | Milestone progress review — completeness, quality metrics, risk, go/no-go recommendation. At checkpoints or before a deadline. |
| `onboard` | Onboarding doc for a new contributor or agent — project state, conventions, priorities relevant to the specified role. |
| `patch-notes` | Player-facing patch notes from git history and changelogs. Translates developer language into player communication. |
| `perf-profile` | Performance profiling — find bottlenecks, measure against budgets, produce ranked optimization recommendations. |
| `playtest-report` | Structured playtest report template, or turn existing playtest notes into structured feedback. |
| `project-stage-detect` | Analyze project state, detect stage, identify gaps, recommend next steps. 'Where are we in development?' |
| `propagate-design-change` | Finds architecture decisions (ADRs) made stale by a changed GDD and walks through resolving each. Use when the user changed a number or rule in a GDD … |
| `prototype` | Concept prototype before GDDs — throwaway HTML, Engine or Paper build, PROCEED/PIVOT/KILL/NOT ASSESSED. After /brainstorm and /setup-engine. |
| `qa-plan` | QA test plan for a sprint — classifies stories by Logic/Integration/Visual/UI, covers automated tests, manual cases, smoke scope. |
| `quick-design` | Lightweight spec for small changes — tuning adjustments, minor mechanics. Embeds directly into stories; skips full GDD. |
| `regression-suite` | Map test coverage to GDD critical paths, find fixed bugs lacking regression tests, flag drift from new features. |
| `release-checklist` | Pre-release checklist — build verification, certification requirements, store metadata, launch readiness. |
| `retrospective` | Sprint or milestone retrospective from completed work, velocity, blockers. Actionable insights for the next iteration. |
| `reverse-document` | Generate missing design or architecture docs from existing implementation — works backwards from code and prototypes. |
| `review-all-gdds` | Holistic cross-GDD review — contradictions between systems, dominant strategies, economic imbalance, cognitive overload, pillar drift. |
| `scope-check` | Scope creep check — current scope versus the original plan. Flags additions, quantifies bloat, recommends cuts. 'Any scope creep?' |
| `security-audit` | Security audit — save tampering, cheat vectors, network exploits, data exposure, input validation. Before public or multiplayer release. |
| `settings` | View or change project config — effective merged values, or set locally in project.local.yaml. |
| `setup-engine` | Configure engine and version. Pins it in CLAUDE.md; WebSearch fills reference docs when the version is beyond LLM training data. |
| `skill-improve` | Improve a skill via a test-fix-retest loop — static checks, targeted fixes, keep or revert on score change. |
| `skill-test` | Validate skill files for structural compliance and behavioral correctness. Four modes: static linter, spec, category rubric, audit. |
| `smoke-check` | Critical-path smoke gate before QA hand-off — runs the automated suite. A failed check means the build is not QA-ready. |
| `soak-test` | Soak test protocol for extended play — what to observe and log for slow leaks, fatigue, late-appearing edge cases. |
| `sprint-plan` | New or updated sprint plan from the current milestone, completed work, and available capacity. |
| `sprint-status` | Fast, concise sprint snapshot — burndown and emerging risks for situational awareness. 'How is the sprint going?' |
| `start` | Guides a first-time user through onboarding and picks the right workflow. Use when the user is new, just cloned or installed the studio, has no idea o… |
| `story-done` | Closes a finished story: verifies each acceptance criterion, checks for design or ADR deviations and updates its status. Use when the user says a stor… |
| `story-readiness` | Checks whether a story is ready to implement: clear acceptance criteria, no open questions, valid ADR and dependencies. Use when the user asks if a st… |
| `team-audio` | Orchestrate the audio team — audio-director, sound-designer, technical-artist, gameplay-programmer — direction through implementation. |
| `team-combat` | Orchestrate the combat team — game-designer, gameplay-programmer, ai-programmer, technical-artist, sound-designer, qa-tester — design through implemen… |
| `team-level` | Orchestrate the level team — level-designer, narrative-director, world-builder, art-director, systems-designer, qa-tester — for complete area creation… |
| `team-live-ops` | Orchestrate the live-ops team — live-ops-designer, economy-designer, analytics-engineer, community-manager, writer — for a season or live event. |
| `team-narrative` | Orchestrate the narrative team — narrative-director, writer, world-builder, level-designer — for story, world lore, narrative-driven levels. |
| `team-polish` | Orchestrate the polish team — performance-analyst, technical-artist, sound-designer, qa-tester — to optimize and harden a feature or area. |
| `team-qa` | Orchestrate the QA team through a full testing cycle — qa-lead strategy and test plan, qa-tester case writing, execution, sign-off. |
| `team-release` | Orchestrate the release team — release-manager, qa-lead, devops-engineer, producer — to execute a release from candidate to deployment. |
| `team-ui` | Orchestrate the UI team through the UX pipeline — authoring, visual design, implementation, review, polish. Uses /ux-design, /ux-review, studio templa… |
| `tech-debt` | Track, categorize and prioritize technical debt across the codebase — scans for debt indicators, maintains a register. |
| `test-evidence-review` | Quality review of test files and evidence — goes beyond existence, evaluates assertion coverage. ADEQUATE/INCOMPLETE/MISSING/NOT ASSESSED per story. |
| `test-flakiness` | Find flaky tests from CI logs — aggregates pass rates, spots intermittent failures, recommends quarantine. After multiple runs. |
| `test-helpers` | Generate engine-specific test helper libraries — assertion utilities, factory functions, mocks in the engine's test folder. Reduces boilerplate. |
| `test-setup` | Scaffold the test framework and CI — tests/ directory, engine test runner, GitHub Actions workflow. Once, before the first sprint. |
| `ux-design` | Section-by-section UX spec authoring for a screen, flow or HUD. Reads the player journey to provide context; also project-wide accessibility. |
| `ux-review` | Validate a UX spec, HUD design or pattern library — accessibility, GDD alignment, readiness. APPROVED / NOT ASSESSED / NEEDS REVISION / MAJOR REVISION… |
| `vertical-slice` | Pre-production validation — end-to-end build to confirm the full loop is achievable before committing to Production. After GDDs, architecture, UX spec… |

### game-tools-setup

| Скил | Описание |
| --- | --- |
| `audio2face-setup` | Choose and set up NVIDIA Audio2Face-3D, AI models and tools that turn speech audio into 3D facial animation (lip-sync, emotion) via SDK, Maya plugin, … |
| `godot-mcp-setup` | Install and use Godot MCP (Coding-Solo/godot-mcp), an MCP server that lets Claude Code launch the Godot editor, run a project, read debug output, crea… |
| `unrealclaude-setup` | Install and use UnrealClaude (Natfii/UnrealClaude), an Unreal Engine 5.7 editor plugin that docks a Claude Code chat in the editor and runs an MCP ser… |

### acestep-music

| Скил | Описание |
| --- | --- |
| `acestep-docs` | ACE-Step documentation and troubleshooting. Use when users ask about installing ACE-Step, GPU configuration, model download, Gradio UI usage, API inte… |
| `acestep-lyrics-transcription` | Transcribe audio to timestamped lyrics using OpenAI Whisper or ElevenLabs Scribe API. Outputs LRC, SRT, or JSON with word-level timestamps. Use when u… |
| `acestep-simplemv` | Render music videos from audio files and lyrics using Remotion. Accepts audio + LRC/JSON lyrics + title to produce MP4 videos with waveform visualizat… |
| `acestep-songwriting` | Music songwriting guide for ACE-Step. Provides professional knowledge on writing captions, lyrics, choosing BPM/key/duration, and structuring songs. U… |
| `acestep-thumbnail` | Generate song cover/thumbnail images using Gemini API. Creates artistic images suitable for music video backgrounds. Use when users want to generate a… |
| `acestep` | Use ACE-Step API to generate music, edit songs, and remix music. Supports text-to-music, lyrics generation, audio continuation, and audio repainting. … |

### img2threejs

| Скил | Описание |
| --- | --- |
| `img2threejs` | Turn an object or character reference image into a quality-gated, animation-ready procedural Three.js model built in code. Use for image-to-3D reconst… |

### dev-workflow

| Скил | Описание |
| --- | --- |
| `backend-patterns` | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| `clickhouse-io` | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. |
| `coding-standards` | Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development. |
| `continuous-learning` | Automatically extract reusable patterns from Claude Code sessions and save them as learned skills for future use. |
| `eval-harness` | Eval-driven development for Claude Code sessions: define capability and regression evals before coding, run them, and track pass@k. Use when adding a … |
| `frontend-patterns` | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| `graphify` | Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the ques… |
| `ponytail-audit` | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or s… |
| `ponytail-debt` | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes nothing. Use for "ponytail debt", "what did pon… |
| `ponytail-gain` | Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display. Use for /ponytail-gain, "what does ponytail save", "ponytai… |
| `ponytail-help` | Quick reference for ponytail levels, skills and commands. One-shot display. Use for /ponytail-help, "ponytail help", "how do I use ponytail". |
| `ponytail-review` | Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line n… |
| `ponytail` | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writin… |
| `project-guidelines-example` | Example template of a project-specific guidelines skill (architecture, file layout, code patterns, testing, deployment). Use as a starting point when … |
| `security-checklist` | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive featur… |
| `strategic-compact` | Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-compaction. |
| `tdd-workflow` | Use this skill when writing new features, fixing bugs, or refactoring code. Enforces test-driven development with 80%+ coverage including unit, integr… |
| `verification-loop` | Run a full verification pass before calling work done or opening a PR: build, typecheck, lint, tests, security scan, diff review, and a final report. … |

### marketing

| Скил | Описание |
| --- | --- |
| `ab-testing` | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. Also use when the user mention… |
| `ad-creative` | When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertisi… |
| `ads` | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms. Also us… |
| `ai-seo` | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions '… |
| `analytics` | When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking," "GA4," "Google… |
| `aso` | When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO audit,' 'app store optimization,' '… |
| `attribution` | When the user wants to figure out which marketing actually drives conversions and revenue, choose or interpret an attribution model, or reconcile conf… |
| `churn-prevention` | When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategies. Also us… |
| `co-marketing` | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. Use when the user says 'co-marketing… |
| `cold-email` | Write and run B2B cold outbound that gets replies, from cold emails and follow-ups to sending setup, LinkedIn, multichannel cadences, and reply handli… |
| `community-marketing` | Build and leverage online communities to drive product growth and brand loyalty. Use when the user wants to create a community strategy, grow a Discor… |
| `competitor-profiling` | When the user wants to research, profile, or analyze competitors from their URLs. Also use when the user mentions 'competitor profile,' 'competitor re… |
| `competitors` | When the user wants to create competitor comparison or alternative pages for SEO and buyer-facing use. Also use when the user mentions 'alternative pa… |
| `content-strategy` | When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. Also use when the user mentions "co… |
| `copy-editing` | When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. Also use when the user mentions 'edit this copy,… |
| `copywriting` | When the user wants to write, rewrite, or improve marketing copy for any page, including homepage, landing pages, pricing pages, feature pages, about … |
| `cro` | When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pricing pages, fe… |
| `customer-research` | When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer research," "ICP research," "talk to cus… |
| `directory-submissions` | When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks, domain rating, and discove… |
| `emails` | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user m… |
| `events` | When the user wants to plan, run, sponsor, speak at, or get pipeline from events — webinars, conferences, trade shows, meetups, dinners, workshops, vi… |
| `free-tools` | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. Also use when the… |
| `image` | When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product mockups, profile banners, list… |
| `influencer-marketing` | When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structuring deals,… |
| `launch` | When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product Hunt,' 'fe… |
| `lead-magnets` | When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. Also use when the user mentions "lead magnet," "g… |
| `marketing-council` | When the user wants multiple expert perspectives on a marketing question — a simulated board of advisors staffed by legendary marketers (Seth Godin, D… |
| `marketing-ideas` | When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. Also use when the user asks for 'marketing ideas,'… |
| `marketing-loops` | When the user wants to set up a recurring, self-running marketing workflow — a repeatable loop an AI agent runs on a cadence (weekly, daily, on a trig… |
| `marketing-plan` | When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. Also use when the user mentions "marketi… |
| `marketing-psychology` | When the user wants to apply psychological principles, mental models, or behavioral science to marketing. Also use when the user mentions 'psychology,… |
| `offers` | When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guarantee desi… |
| `onboarding` | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also use when the user mentions "onbo… |
| `paywalls` | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions "paywall,… |
| `popups` | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also use when the user mentions "ex… |
| `pricing` | When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions 'pricing,' 'pricing tiers,' 'fre… |
| `product-marketing` | When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing contex… |
| `programmatic-seo` | When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages,… |
| `prospecting` | When the user wants to find, qualify, and build a list of prospects to reach out to, across B2B SaaS, general B2B, or local small businesses. Also use… |
| `public-relations` | When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). Also use whe… |
| `referrals` | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. Also use when the user mentions … |
| `revops` | When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. Also use when the user mentions … |
| `sales-enablement` | When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also use when the user mentions 'sa… |
| `schema` | When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user mentions "schema markup," "struct… |
| `seo-audit` | When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I no… |
| `signup` | When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup conversions… |
| `site-architecture` | When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. Also use when the use… |
| `sms` | When the user wants to plan, build, or optimize SMS, MMS, or WhatsApp marketing — including welcome flows, abandoned cart texts, post-purchase, win-ba… |
| `social` | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, or Facebook, or wants to… |
| `video` | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. Also use when the user mentions 'video pr… |

# Скилы для claude.ai: 144 zip

Каждый zip это один скил: внутри папка со SKILL.md, всё проверено (name, description, формат YAML).

## Как загрузить
claude.ai → Настройки → Возможности (Capabilities) → Скилы (Skills) → «Загрузить скил» → выбрать один zip. По одному файлу за раз.
Грузить все 144 не нужно: начни с первых пятнадцати из списка ниже.

## 1. Самые полезные для Umbrahold (грузить первыми)
1. `threejs-scene-setup`: сцена, камера, рендер three.js
2. `threejs-materials-lighting`: материалы, свет, тени
3. `threejs-gltf-loading`: загрузка GLB/GLTF моделей (Meshy)
4. `performance-optimization`: FPS, лаги, телефоны
5. `rpg`: прокачка, предметы, квесты, баланс
6. `game-feel`: «сочность» ударов, тряска, отклик
7. `game-ui-ux`: интерфейс, HUD, меню на телефоне и ПК
8. `level-design`: локации, края мира, ведение игрока
9. `img2threejs`: модель three.js из картинки
10. `create-game-assets`: генерация ассетов
11. `procedural-gen`: процедурный мир (деревья, камни)
12. `save-systems`: сохранения
13. `audio-design`: звук и музыка
14. `camera-systems`: камера в 3D
15. `ponytail`: «минимальное изменение» при правках кода

## 2. Продвижение в Яндекс Играх / VK (маркетинг)
`marketing-plan`, `launch`, `aso` (карточка в каталоге), `onboarding` (первые минуты), `ab-testing`, `community-marketing`, `influencer-marketing`, `ad-creative`, `ads`, `analytics`, `churn-prevention` (удержание), `copywriting`, `social`, `video`, `pricing`, `paywalls`, `referrals`, `marketing-ideas`, `marketing-psychology`, `content-strategy`, `customer-research`, `competitors`, `competitor-profiling`, `public-relations`, `events`.

Остальные маркетинговые (больше для сайтов и B2B): `ai-seo`, `attribution`, `co-marketing`, `cold-email`, `copy-editing`, `cro`, `directory-submissions`, `emails`, `free-tools`, `image`, `lead-magnets`, `marketing-council`, `marketing-loops`, `offers`, `popups`, `product-marketing`, `programmatic-seo`, `prospecting`, `revops`, `sales-enablement`, `schema`, `seo-audit`, `signup`, `site-architecture`, `sms`.

## 3. Игровой дизайн и механики
`game-ai`, `ai-behavior-trees-utility-ai`, `dialogue-systems`, `input-systems`, `physics-tuning`, `shader-programming`, `roguelike`, `survival-crafting`, `tower-defense`, `card-game`, `puzzle`, `platformer`, `fps-shooter`, `visual-novel`, `prototype-fast`, `game-jam`, `router` (подбирает нужный игровой скил).

## 4. Работа с кодом и проверка
`verification-loop`, `tdd-workflow`, `eval-harness`, `coding-standards`, `frontend-patterns`, `backend-patterns`, `security-checklist`, `strategic-compact`, `continuous-learning`, `graphify`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help`, `clickhouse-io`, `project-guidelines-example`.

## 5. Публикация
`itch-publish`, `steam-publish`.

## 6. Другие движки (для Umbrahold не нужны)
Web 2D: `phaser-core`, `phaser-arcade-physics`, `pixijs-rendering`.
Godot: `godot-2d-movement`, `godot-3d-essentials`, `godot-animation`, `godot-audio`, `godot-csharp`, `godot-export`, `godot-gdscript`, `godot-gdscript-headless-testing`, `godot-multiplayer`, `godot-nodes-scenes`, `godot-physics`, `godot-resources`, `godot-shaders`, `godot-signals-groups`, `godot-tilemap`, `godot-ui-control`.
Unity: `unity-animation`, `unity-build-pipeline`, `unity-csharp-scripting`, `unity-input-system`, `unity-navmesh`, `unity-physics`, `unity-scriptableobjects`, `unity-tilemap-2d`.
Unreal: `unreal-behavior-trees`, `unreal-blueprints`, `unreal-cpp-gameplay`, `unreal-enhanced-input`, `unreal-niagara`, `unreal-packaging`.
Roblox: `roblox-characters`, `roblox-datastores`, `roblox-luau`, `roblox-networking`, `roblox-physics`, `roblox-studio-workflow`, `roblox-ui`.
Прочее: `bevy-ecs`, `love2d-core`, `pygame-core`.

## Откуда
Репозиторий github.com/iliafreedive-del/skills: игровой пак awesome-gamedev-agent-skills, ponytail, graphify, everything-claude-code, img2threejs и пак marketingskills (50 скилов). В `img2threejs` и `ponytail` лишние поля шапки перенесены в `metadata`, а описания везде переписаны в корректный YAML, чтобы claude.ai их принял. Сами тексты скилов не менялись.

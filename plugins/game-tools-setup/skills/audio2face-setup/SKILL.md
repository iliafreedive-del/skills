---
name: audio2face-setup
description: "Choose and set up NVIDIA Audio2Face-3D, AI models and tools that turn speech audio into 3D facial animation (lip-sync, emotion) via SDK, Maya plugin, Unreal Engine 5 plugin or NIM microservice. Use when the user wants talking characters, lip-sync from voice lines, or facial animation from audio."
license: MIT (this guide); see the component licenses below
---

# Audio2Face-3D setup

Audio2Face-3D is not a skill. It is a family of NVIDIA AI models and integrations that generate facial animation (jaw, tongue, eyes, skin, blendshape weights) from audio. It needs an NVIDIA GPU for good speed (the SDK has a CPU fallback). It does not run inside Claude; Claude can help install it and wire its output into a game.

Hub: https://github.com/NVIDIA/Audio2Face-3D

## Pick the component

| Need | Component | License |
| --- | --- | --- |
| Faces in Unreal Engine 5 (MetaHuman ready) | ACE Unreal plugin + Audio2Face-3D models plugin (UE 5.4 to 5.6) from developer.nvidia.com | MIT |
| Animate in Autodesk Maya, export FBX/keys | Maya ACE (github.com/NVIDIA/Maya-ACE) | MIT |
| Own engine or tool (C++), real-time | Audio2Face-3D SDK (github.com/NVIDIA/Audio2Face-3D-SDK) | MIT |
| Train a model on own data | Audio2Face-3D Training Framework | Apache-2.0 |
| Server for many clients (gRPC) | Audio2Face-3D NIM (build.nvidia.com/nvidia/audio2face-3d) | NVIDIA AI product terms |
| Pre-trained models (Mark, Claire, James, v3.0) | Hugging Face, NVIDIA org | NVIDIA Open Model License |
| Audio2Emotion models | Hugging Face | Custom: only with Audio2Face |

Check the model license before shipping a commercial game; the sample dataset is evaluation only.

## Browser games (three.js)

There is no web runtime. Bake offline instead:

1. Generate the animation in Maya ACE (or the SDK) from each voice line.
2. Export blendshape weights per frame (ARKit-style 52 shapes work well).
3. Load them in three.js as morph target animation on a glTF head with matching morph targets (`mesh.morphTargetInfluences`), synced to the audio's `currentTime`.
4. Keep clips short and compress the weight tracks (quantize to 8 bit, drop unused shapes) to keep download size small.

Pair with the gamedev plugin skills `threejs-gltf-loading`, `audio-design`, `dialogue-systems`.

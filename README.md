# Vanilla-RTX
Vanilla RTX Resource Pack for Minecraft with Ray Tracing.

⚠️ Windows 10/11 - Bedrock Edition +1.21.70 Only.  
⚠️ Dedicated DXR-capable hardware required.  
⚠️ **Important: To solve the issues with ray tracing in Minecarft 1.21.90, [follow this guide](https://github.com/Cubeir/Vanilla-RTX/issues/49#issuecomment-2994431940).** (Temporary)  
</br>
[![Discord](https://img.shields.io/discord/721377277480402985?style=flat-square&logo=discord&logoColor=F4E9D3&label=Discord&color=F4E9D3&cacheSeconds=3600)](https://discord.gg/A4wv4wwYud) 
![Repo Size](https://img.shields.io/github/repo-size/Cubeir/Vanilla-RTX?style=flat-square&color=F4E9D3&label=Repo%20Size&cacheSeconds=3600) 
![Last Commit](https://img.shields.io/github/last-commit/Cubeir/Vanilla-RTX?style=flat-square&color=F4E9D3&label=Last%20Commit&cacheSeconds=1800) 
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fminecraftrtx.net%2Findex&up_message=Online&up_color=F4E9D3&down_message=Temporarily%20Down&down_color=ED9E00&style=flat-square&logoSize=auto&label=Website%20Status&cacheSeconds=90&link=https%3A%2F%2Fminecraftrtx.net%2F)](https://minecraftrtx.net/index) 
[![Ko-Fi](https://img.shields.io/badge/-Support%20my%20work%20on%20Ko--Fi-F4E9D3?style=flat-square&logo=ko-fi&logoColor=F4E9D3&labelColor=555555)](https://ko-fi.com/cubeir)

## Description

This project aims to bring complete ray tracing support for Minecraft's default resources in a manner that seamlessly integerates with the game while maintaining a native look and feel.

- **[Vanilla RTX:](https://mcpedl.com/vanilla-rtx)** Uses 16x heightmaps with 192x normal maps generated based on height differences.  
- **[Vanilla RTX Normals:](https://mcpedl.com/vanilla-rtx-normals)** Features handcrafted 16x normal maps instead.
- Every possible vanilla block is supported (Creative, Education Edition, secret or unobtainable blocks, etc...)  
- All blocks feature highly detailed, unique material designs that remain consistent across different blocks made of the same material.
- Compatibility errors of vanilla resources with ray tracing are resolved through the Enhanced option as much as possible. (accessed from resource pack's settings)
- Related Projects:
  - **[Vanilla RTX Tuner](https://github.com/Cubeir/Vanilla-RTX-Tuner):** An installable tool that lets you customize fog, lighting, materials, and more in Vanilla RTX.
  - **Vanilla RTX Opus:** Composition of both Vanilla RTX & Vanilla RTX Normals. (Coming along soon!)
  - **[Chemistry RTX Extensions:](https://mcpedl.com/chemistry-rtx/)** Additional world-only packs to add ray tracing compatibility to content available under Minecraft: Education Edition toggle.
  - **[Vibrant Vanilla PBR:](https://mcpedl.com/vanilla-pbr)** A branch of Vanilla RTX for Vibrant Visuals graphics mode usable on a wider range of hardware.

Initial goal of this project was to create a fresh Bedrock Edition equivalent of [Vanilla Normals Renewed](https://github.com/Poudingue/Vanilla-Normals-Renewed). This effort later evolved into Vanilla RTX Normals.  
Vanilla RTX now strives to provide an ideal default Minecraft RTX experience for all Bedrock Edition players.  

## Images
![vanilla-rtx_chase-the-skies-main-cover-image_minecraft-rtx](https://github.com/user-attachments/assets/2443facc-c96f-4cb9-846f-38042dc7c1fe)
![vanilla-rtx_ice-king's-vault-ray-tracing-showcase-image_minecraft-rtx](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/974cf798-aea6-4723-89a8-49c911e19830)
![vanilla-rtx_colosseum-demo-showcase-image_minecraft-rtx](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/83bc172f-e0bc-4e1a-884d-7a8747f92163)
![vanilla-rtx_normals-wall-image_minecraft-rtx](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/7b621735-1e62-40d1-bfbd-a673556443d7)
![vanilla-rtx_room-lighting-image_minecraft-rtx](https://user-images.githubusercontent.com/75272685/222483572-42c3f0bf-9baf-4e2f-a751-bddedad80ab2.png)
![vanilla-rtx_mangrove-swamp-wild-update_minecraft](https://github.com/user-attachments/assets/4cbacc35-27e2-465b-8b4c-bab5ece9edef)
![vanilla-rtx-normals-stonecutter-design-example](https://github.com/user-attachments/assets/b91cea41-da90-418b-b87e-ece1c2317c10)
![vanilla-rtx_sculk-wild-update-deepdark_minecraft](https://github.com/user-attachments/assets/5ea09a8e-6416-46d6-a568-58270bbabaf5)

More at Vanilla RTX's [CurseForge](https://www.curseforge.com/minecraft-bedrock/texture-packs/vanilla-rtx/gallery) & [Website](https://minecraftrtx.net/gallery) gallery.
## Usage Tips
- For Installation: Each folder in this repository is a complete package. To import one, download and extract the whole repo, compress either of the folders `Vanilla RTX` or `Vanilla RTX Normals` into a `.zip` file, rename the `.zip` extension to `.mcpack`, and open in Minecraft or Minecraft Preview to import.

- It is recommended that you enable the pack in Global Resources instead of World resource packs, there's an issue in Minecraft that can create incomplete copies of resource pack's files when enabled in world settings.

- If you're experiencing performance issues, [disable Minecraft's VSync](https://youtu.be/CKK1VSbGGnk), you can keep VSync on in your graphics card's control panel. This also reduces input latency when compared to Minecraft's VSync.

- Activation issues: There is a problem that will keep Vanilla RTX from loading and could make the world appear glossy. To prevent this, ray tracing must be enabled before joining a world. However since Minecraft 1.21.60, ray tracing can only be initially toggled while in a world. You must first join any world, enable ray tracing (you may experience issues at first) then exit to the main menu and rejoin. Once ray tracing is enabled, do not turn it off to prevent this issue from occurring again, or [enable ray tracing via options.txt](https://www.youtube.com/watch?v=hNS1p4IYmJo&feature=youtu.be) instead before launching the game.  

For simplicity, use this [batch script](https://github.com/Cubeir/Vanilla-RTX/blob/master/LaunchMinecraftRTX.bat) which quickly activates ray tracing before launching Minecraft with an option to disable VSync. (Recommended while [MCPE-191513](https://bugs.mojang.com/browse/MCPE/issues/MCPE-191513) and [MCPE-121850](https://bugs.mojang.com/browse/MCPE/issues/MCPE-121850) persist).

- If you've encountered visual bugs (such as some textures exhibiting z-fighting issues, or entities with missing or black textures) try switching to Enhanced option included in Vanilla RTX (Normals). This enables various work-in-progress features and updates, which enhance visuals and work around some of ray tracing's technical issues with vanilla resources, but note that some of them may come with minor drawbacks or incompatibility with other resource packs/add-ons, they can also potentially break with future Minecraft updates due to use of undocumented features.
For an updated list of features [view this page](https://minecraftrtx.net/enhancements).

- The shortcut for toggling ray tracing while inside of a world is the semicolon key (;) on your keyboard, however it is a good practice to always keep ray tracing on and avoid dynamically toggling it, as it can cause a few glitches, such as jumbled player geometry or black entity textures.

- To ensure subpack changes are saved, you may need to apply the setting multiple times.

- Education Edition resources will only load if the pack is loaded in world settings.

- If textures fail to load or appear to have issues, make sure that world, server or realm resource packs are not overriding Vanilla RTX's files.



## Copyright
[View License](https://github.com/CubeIR/Vanilla-RTX/blob/master/LICENSE.txt) 

Reminder:  
Vanilla RTX and its derivative works are completely free to download and use. However be aware of unauthorized copies or versions of Vanilla RTX that may circulate, sometimes under different names and even for sale. These unauthorized copies may, at best, replicate the version available on this page.

Disclaimer:  
The license file linked above does not apply to any original Minecraft art resource.  
  
Please note that this pack relies on some of Minecraft's original art resources (found at [this github repository](https://aka.ms/resourcepacktemplate)) to function.
This is due to a game limitation where texture maps can only be called within the pack and once removed, the game stops defaulting to its own resources, contrary to the usual behavior of Minecraft texture packs. Consequently, Vanilla RTX unavoidably has to include a small part of base game's resources as referenced by ```texture_set.json``` files. As time passes this may result in outdated resources. Parity checks are performed on a regular basis with the pack adjusted accordingly.  
Large parts of vanilla resources also had to be modified for compatibility with ray tracing or to work around other technical issues or limitations without altering their original appearance. For instance, the Enhanced option which addresses a wide range of compatibility issues with Minecraft’s vanilla resources in ray tracing graphics mode, [learn more](https://minecraftrtx.net/enhancements).

### Credits
Created and maintained with ❤️‍🔥 by Cubeir — special thanks to:
EchoQuasar, Miriel, Big Plonk, FobidenNinja, nathanhillis420, Spikey, Giuseppe DiMarca, Jordan, David Sabrowsky, Cody Starr, ObliviousDraede, Dabadking, Spaceowl, Alexkillerk209, nattyhob, Rolando Dojer, Waffle, Willström, Ernesto cuellar, Bastha, Steve, Plugin, Jayssizle, Drackae, Pizza4001, nxsty, Irwin Montalvo Roach, Thomas Zeman, Azorawing, PotatoHour, Kittygamer123, UDJM_Phoenix, Lanaismymommy, StigFinnegan, TKbn, joanmrz, James Kelly, RJ Fajilan, spacetoker, Byrn, OmarVillegas, Jacob, Isttret, Superluminal, Travis Bishop, crungleDorf, ri, ObsydianX, Dylan, Kyo Don, Okapi, The_Asa_Games, GoldGamer 11 —— and to everyone who has supported this project in any way along the way.

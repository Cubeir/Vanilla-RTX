# Vanilla-RTX

Vanilla RTX Resource Pack for Minecraft with RTX.

⚠️ Windows 10/11 - Bedrock Edition +1.21.60 Only ⚠️

## Description

This project aims to bring complete ray tracing support for Minecraft's default resources in a manner that seamlessly integerates with the game while maintaining a native look and feel.

- **[Vanilla RTX:](https://github.com/Cubeir/Vanilla-RTX/tree/master/Vanilla-RTX)** Uses 16x heightmaps with 192x normal maps generated based on height differences.  
- **[Vanilla RTX Normals:](https://github.com/Cubeir/Vanilla-RTX/tree/master/Vanilla-RTX-Normals)** Features handcrafted 16x normal maps instead.
- Every possible vanilla block is supported (Creative, Education Edition, secret or unobtainable blocks, etc...)  
- All blocks feature highly detailed, unique material designs that remain consistent across different blocks made of the same material.
- **[Vanilla PBR:](https://github.com/Cubeir/Vanilla-RTX/tree/master/Vanilla-PBR)** A derivative of Vanilla RTX for Deferred Lighting graphics mode usable on a wider range of hardware.

Initial goal of this project was to create a fresh Bedrock Edition equivalent of [Vanilla Normals Renewed](https://github.com/Poudingue/Vanilla-Normals-Renewed). This effort later evolved into Vanilla RTX Normals.  
Vanilla RTX now strives to provide an ideal default Minecraft RTX experience for all Bedrock Edition players.  
  
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fminecraftrtx.net%2Findex&up_message=Online&up_color=F4E9D3&down_message=Temporarily%20Down&down_color=ED9E00&style=flat-square&logoSize=auto&label=Website%20Status&cacheSeconds=90&link=https%3A%2F%2Fminecraftrtx.net%2F)](https://minecraftrtx.net/index) 
[![Discord](https://img.shields.io/discord/721377277480402985?style=flat-square&logo=discord&logoColor=F4E9D3&label=Discord&color=F4E9D3&cacheSeconds=3600)](https://discord.gg/A4wv4wwYud) 
![Repo Size](https://img.shields.io/github/repo-size/Cubeir/Vanilla-RTX?style=flat-square&color=F4E9D3&label=Repo%20Size&cacheSeconds=3600) 
![Last Commit](https://img.shields.io/github/last-commit/Cubeir/Vanilla-RTX?style=flat-square&color=F4E9D3&label=Last%20Commit&cacheSeconds=1800) 
[![Patreon](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%3Fusername%3Dcubeir%26type%3Dpatrons&style=flat-square&color=F4E9D3&label=&labelColor=555555&logo=patreon&logoColor=F4E9D3)](https://patreon.com/cubeir)


## Images
![Vanilla RTX for Minecraft RTX - Cover Image](https://github.com/user-attachments/assets/6c6a8c3e-d74a-4a58-b9fc-840942a1e207)
![ice kings vault](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/974cf798-aea6-4723-89a8-49c911e19830)
![Minecraft with RTX Vanilla RTX](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/83bc172f-e0bc-4e1a-884d-7a8747f92163)
![Vanilla RTX Normals Wall](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/7b621735-1e62-40d1-bfbd-a673556443d7)
![Vanilla RTX image](https://user-images.githubusercontent.com/75272685/222483572-42c3f0bf-9baf-4e2f-a751-bddedad80ab2.png)
![Vanilla RTX Demo World](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/3ac5552d-0261-461b-ad26-ef6315dc2606)
More at [Vanilla RTX Gallery](http://minecraftrtx.net/gallery) and [MCPEDL Page](http://minecraftrtx.net/gallery)
## Usage Tips
- There is a problem that will keep Vanilla RTX from loading and could make the world appear glossy. To prevent this, ray tracing must be enabled before joining a world. However since Minecraft 1.21.60, ray tracing can only be initially toggled while in a world. So join any world, enable ray tracing (you may experience issues at first) then exit to the main menu and rejoin. Once enabled, do not turn ray tracing off to prevent this issue from occurring again, or [enable ray tracing via options.txt](https://www.youtube.com/watch?v=hNS1p4IYmJo&feature=youtu.be) instead before launching the game.
To simplify things, you can use this [batch script](https://github.com/Cubeir/Vanilla-RTX/blob/master/LaunchMinecraftRTX.bat) to quickly activate ray tracing before it launches Minecraft.

- If you've encountered visual bugs (such as some textures exhibiting z-fighting issues, or entities with missing or black textures) try switching to Enhanced option included in Vanilla RTX (Normals). This enables various work-in-progress features and updates, which enhance visuals and work around some of ray tracing's technical issues with vanilla resources, but note that some of them may come with minor drawbacks or incompatibility with other resource packs/add-ons, they can also potentially break with future Minecraft updates due to use of undocumented features.

- If you're experiencing low frame rate, [disable Minecraft's VSync](https://youtu.be/E-gANUpoMus?t=12), you can keep VSync on in your graphics card's control panel. This also reduces input latency when compared to Minecraft's VSync.

- The shortcut for toggling ray tracing while inside of a world is the semicolon key (;) on your keyboard, however it is a good practice to always keep ray tracing on and avoid dynamically toggling it, as it can cause a few glitches, such as messing up player geometry or black entity textures.

- It is recommended that you enable the pack in Global Resources instead of World resource packs, there's an issue in Minecraft that can create incomplete copies of resource pack's files when enabled in world settings.

- To ensure subpack changes are saved, you may need to apply the settings multiple times.

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
Parts of vanilla resources also had to be modified or converted for proper functioning with ray tracing or to work around other technical issues or limitations without altering their original appearance. For instance, the Enhanced option which addresses a wide range of compatibility issues with Minecraft’s vanilla resources in ray tracing graphics mode.

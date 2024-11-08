# Vanilla-RTX

Vanilla RTX Resource Pack for Minecraft with RTX.

⚠️ Windows 10/11 - Bedrock Edition +1.16.200 Only ⚠️

## Description

This project aims to bring complete ray tracing support for Minecraft's default resources with thoughtfully designed materials.  

Vanilla RTX uses 16x heightmaps (with 192x normal maps generated later based on height differences) Vanilla RTX Normals uses handcrafted 16x normal maps instead.  
Every possible vanilla block is supported (Creative, Education Edition, secret or unobtainable blocks, etc...)  
Everything is consistent & fine-tuned for Minecraft RTX.  

Initial goal of this project was having something similar to [Vanilla Normals Renewed](https://github.com/Poudingue/Vanilla-Normals-Renewed) for Bedrock Edition, which later became [Vanilla RTX Normals](https://github.com/Cubeir/Vanilla-RTX/tree/master/Vanilla-RTX-Normals). Vanilla RTX now strives to provide an ideal default Minecraft RTX experience for all Bedrock Edition players.


![GitHub repo size](https://img.shields.io/github/repo-size/CubeIR/Vanilla-RTX) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/CubeIR/Vanilla-RTX?style=flat) [![](https://dcbadge.vercel.app/api/server/A4wv4wwYud?style=flat)](https://discord.gg/A4wv4wwYud)
## Images
![Vanilla RTX Minecraft with RTX Cover Image](https://github.com/user-attachments/assets/d64f7bbe-8d2e-4ccb-b515-6ecf5e207200)
![ice kings vault](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/974cf798-aea6-4723-89a8-49c911e19830)
![Minecraft with RTX Vanilla RTX](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/83bc172f-e0bc-4e1a-884d-7a8747f92163)
![Vanilla RTX Normals Wall](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/7b621735-1e62-40d1-bfbd-a673556443d7)
![Vanilla RTX image](https://user-images.githubusercontent.com/75272685/222483572-42c3f0bf-9baf-4e2f-a751-bddedad80ab2.png)
![Vanilla RTX Demo World](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/3ac5552d-0261-461b-ad26-ef6315dc2606)
More screenshots at [this page](http://minecraftrtx.net/gallery).


## Usage Tips
- If you've encountered visual bugs (such as some textures exhibiting z-fighting issues, or entities with missing or black textures) consider switching to Experimental option included in Vanilla RTX (or Vanilla RTX Normals). This enables various work-in-progress features and updates, which enhance visuals and work around some of ray tracing's technical issues with vanilla resources, but please note that some of them may come with minor drawbacks, side effects, or cause minor incompatibility with other resource packs/add-ons, they can also be unstable and potentially break with future Minecraft updates due to use of undocumented features.

- If you're experiencing low frame rate, [disable Minecraft's VSync](https://youtu.be/E-gANUpoMus?t=12), you can keep VSync on in your graphics card control panel. This also reduces input latency when compared to Minecraft's VSync.

- There is an issue that will keep Vanilla RTX files from loading and might make the world fully glossy. To prevent this, always make sure ray tracing is enabled before you attempt joining a world. In other words, do not enable ray tracing while inside a world! Do it through the main menu instead.

- The shortcut for toggling ray tracing while inside of a world is the semicolon key ";" on your keyboard, however it is a good practice to always keep ray tracing on and avoid dynamically toggling it, as it can cause a few glitches, such as black entity textures.

- It is recommended that you enable the pack in Global Resources instead of World resource packs, there's an issue in Minecraft that can sometimes cause incomplete copies of resource pack files.

- To ensure your pack options or subpack changes are saved, you may need to apply the settings multiple times.

- Education Edition resources will only load if the pack is loaded in world settings.

- If textures appears broken or fail to load, make sure that server, world, or realm resource packs are not overriding Vanilla RTX's files.



## Copyright
[View License](https://github.com/CubeIR/Vanilla-RTX/blob/master/LICENSE.txt) 

Reminder:  
Vanilla RTX (Normals) is completely free download and use. However, be aware of unauthorized copies or versions of Vanilla RTX that may circulate, sometimes under different names and even for sale. These unauthorized copies may, at best, replicate the version available on this page.

Disclaimer:  
The license file linked above does not apply to any original Minecraft art resource.  

Please note that this pack relies on some of Minecraft's original art resources (found at [this github repository](https://github.com/Mojang/bedrock-samples/releases)) to function.
This is due to a game limitation where texture maps can only be called within the pack and once removed, the game stops defaulting to its own resources, contrary to the usual behavior of Minecraft texture packs. Consequently, Vanilla RTX unavoidably has to include a small part of base game's resources as referenced by texture_set.json files. As time passes this may result in outdated textures.  
Updates will include the latest texture changes to retain parity with vanilla textures and PBR textures will be updated accordingly. Parts of vanilla resources also had to be modified or converted for proper functioning with ray tracing or to work around other technical issues or limitations without altering their original appearance.  

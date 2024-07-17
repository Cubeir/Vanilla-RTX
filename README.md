# Vanilla-RTX

Vanilla RTX Resource Pack for Minecraft with RTX.

⚠️ Windows 10/11 - Bedrock Edition +1.16.200 Only ⚠️

## Description

Vanilla RTX aims to bring full ray tracing support for Minecraft's default resources while remaining completely faithful to all the different aspects and details of vanilla Minecraft.  

Vanilla RTX uses 16x heightmaps (192x normal maps are later generated based on height differences) Vanilla RTX Normals uses handmade 16x normal maps instead.  
Every possible vanilla block is supported (Creative, Education Edition, secret or unobtainable blocks, etc...)  
Everything is consistent & fine-tuned for Minecraft RTX.  

Initial goal of this project was having something similar to [Vanilla Normals Renewed](https://github.com/Poudingue/Vanilla-Normals-Renewed) for Bedrock Edition, which later became known as Vanilla RTX Normals. Vanilla RTX now strives to provide an ideal default Minecraft RTX experience for all Bedrock Edition players.


![GitHub repo size](https://img.shields.io/github/repo-size/CubeIR/Vanilla-RTX) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/CubeIR/Vanilla-RTX?style=flat) [![](https://dcbadge.vercel.app/api/server/A4wv4wwYud?style=flat)](https://discord.gg/A4wv4wwYud)
## Images
![Vanilla RTX for Minecraft RTX](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/32f8e0a7-1c9c-4da9-b9e9-9540203e20bf)
![ice kings vault](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/974cf798-aea6-4723-89a8-49c911e19830)
![Minecraft with RTX Vanilla RTX](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/83bc172f-e0bc-4e1a-884d-7a8747f92163)
![Vanilla RTX Normals Wall](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/7b621735-1e62-40d1-bfbd-a673556443d7)
![Vanilla RTX image](https://user-images.githubusercontent.com/75272685/222483572-42c3f0bf-9baf-4e2f-a751-bddedad80ab2.png)
![Vanilla RTX Demo World](https://github.com/CubeIR/Vanilla-RTX/assets/75272685/3ac5552d-0261-461b-ad26-ef6315dc2606)
For more information and screenshots visit [this page](http://minecraftrtx.net/).

## Copyright
[View License](https://github.com/CubeIR/Vanilla-RTX/blob/master/LICENSE.txt) 

Reminder:  
Vanilla RTX (Normals) is completely free download and use. However, be aware of unauthorized copies or versions of Vanilla RTX that may circulate, sometimes under different names and even for sale. These unauthorized copies may, at best, replicate the version available on this page.

Disclaimer:  
The license file linked above does not apply to Minecraft's original art resources.  

Please note that this pack relies on some of Minecraft's original art resources (found at [this github repository](https://github.com/Mojang/bedrock-samples/releases)) for proper functioning.
This is due to a game limitation where texture maps can only be called within the pack and once removed, the game stops defaulting to its own resources, contrary to the usual behavior of Minecraft texture packs. Consequently, Vanilla RTX unavoidably has to include a small part of base game's resources as referenced by texture_set.jsons. This may rarely result in outdated textures.  
  
Updates will include the latest texture changes to retain parity with vanilla textures, and PBR textures will be updated accordingly. A number of resources also had to be edited or converted to function properly with ray tracing, without altering their original appearance.

## Tips
- If you're experiencing low frame rates, [disable Minecraft's VSync](https://youtu.be/E-gANUpoMus?t=12), you can keep VSync on in your graphics card control panel. This also reduces input latency when compared to Minecraft's VSync.

- There is an issue that will keep Vanilla RTX files from loading and might make the world fully glossy. To prevent this, always make sure ray tracing is enabled before you attempt joining a world. In other words, do not enable ray tracing while inside a world! Do it through the main menu instead. It is a good practice to always keep ray tracing on and avoid dynamically toggling it, as it can cause a few other glitches.

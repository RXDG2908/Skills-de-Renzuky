# minecraft-skills

Claude Code plugin — Minecraft modding skills for Forge, NeoForge, GregTech Modern, NeoGradle, and Bedrock GameTest.

## Install

```bash
/plugins install mrquentin/minecraft-skills
```

Or add as a marketplace in `~/.claude/settings.json`:

```json
"extraKnownMarketplaces": {
  "mrquentin": {
    "source": {
      "source": "github",
      "repo": "mrquentin/minecraft-skills"
    }
  }
}
```

Then install the plugin:

```bash
/plugins install minecraft-skills@mrquentin
```

## Skills

| Skill | Trigger |
|-------|---------|
| **minecraft-forge** | Creating or debugging a Minecraft Forge mod (1.18–1.20.x) |
| **minecraft-neoforge** | Creating or debugging a NeoForge mod (1.20.1, 1.21.x+) |
| **neogradle** | Configuring ModDevGradle or NeoGradle build setup |
| **gtceu-addon** | Building a GregTech CEu Modern addon (Forge 1.20.1) |
| **minecraft-gametest** | Writing Minecraft Bedrock GameTest framework tests |

## Skills detail

### minecraft-forge
Covers DeferredRegister, event buses (game + mod), sided logic, SimpleChannel networking, datagen, ForgeConfigSpec, capabilities, and migration patterns for Forge 1.18–1.20.x.

### minecraft-neoforge
Covers ModDevGradle setup, constructor-injected IEventBus, DeferredRegister typed helpers, parallel mod bus, CustomPacketPayload networking (1.21+), data attachments, DataComponentType, access transformers, and full Forge→NeoForge migration table.

### neogradle
Covers ModDevGradle vs NeoGradle selection, full DSL reference for both plugins, run configuration, access transformers, jar-in-jar, Parchment mappings, multi-project setups, and CI/CD optimizations.

### gtceu-addon
Covers Material.Builder API, machine system (MetaMachine, tiered + multiblock), recipe system (GTRecipeType, GTRecipeBuilder), KubeJS integration, and a Mixin/AT last-resort policy with mandatory justification.

### minecraft-gametest
Covers Bedrock GameTest project setup, manifest.json, test registration API, assertion methods, simulated players, structure creation, all `/gametest` commands, and test organization guidelines.

## License

MIT

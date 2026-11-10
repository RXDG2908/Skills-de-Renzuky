---
name: Minecraft Forge Mod Development
description: This skill should be used when the user wants to create, modify, or debug a Minecraft mod using MinecraftForge (not NeoForge). Covers project setup via MDK, DeferredRegister, event buses, sided logic, networking with SimpleChannel, data generation, config system, capabilities, and inter-mod compatibility for Forge 1.18–1.20.x.
version: 1.0.0
---

# Minecraft Forge Mod Development

You are an expert Minecraft Forge mod developer. You target the Forge loader specifically (not NeoForge — use the neoforge skill for that). You write modern, data-driven, event-driven mods that follow current Forge conventions.

## Core Protocols

### 1. Always Fetch Fresh Documentation

Forge API changes between versions. Before writing registration, networking, or datagen code:

- **Forge docs (version-specific)**: `https://docs.minecraftforge.net/en/<MC_VERSION>/`
  - Replace `<MC_VERSION>` with e.g. `1.20.x`, `1.19.x`, `1.18.x`
  - Always confirm the exact version with the user before fetching
- **Forge MDK (starting point)**: `https://github.com/MinecraftForge/MinecraftForge` → check branch for version
- **Forge javadoc**: `https://javadoc.minecraftforge.net/`
- **Community wiki**: `https://forge.gemwire.uk/wiki/` (supplements official docs)

See `references/forge-links.md` for curated links.

DO NOT assume API signatures from memory — fetch source or docs for the target version first.

### 2. Project Setup (MDK)

Download MDK from `https://files.minecraftforge.net/` for the target MC + Forge version.

**Key `build.gradle` fields:**
```groovy
version = "${mc_version}-${mod_version}"
group = 'com.yourname.modid'

minecraft {
    mappings channel: 'official', version: '<mc_version>'
    runs {
        client { workingDirectory project.file('run') }
        server { workingDirectory project.file('run') }
        data {
            args '--mod', 'modid', '--all',
                 '--output', file('src/generated/resources/'),
                 '--existing', file('src/main/resources/')
        }
    }
}

dependencies {
    minecraft "net.minecraftforge:forge:${mc_version}-${forge_version}"
}
```

**`gradle.properties`:**
```properties
mc_version=1.20.1
forge_version=47.2.0
mod_version=1.0.0
```

**Gradle tasks:**
```bash
./gradlew genIntellijRuns   # Set up IDE run configs
./gradlew runClient         # Launch game client
./gradlew runServer         # Launch dedicated server
./gradlew runData           # Generate data (recipes, tags, models)
./gradlew build             # Build JAR
```

**`mods.toml`** (`src/main/resources/META-INF/`):
```toml
modLoader = "javafml"
loaderVersion = "[47,)"
license = "MIT"

[[mods]]
modId = "modid"
version = "${file.jarVersion}"
displayName = "My Mod"

[[dependencies.modid]]
    modId = "forge"
    mandatory = true
    versionRange = "[47,)"
    ordering = "NONE"
    side = "BOTH"

[[dependencies.modid]]
    modId = "minecraft"
    mandatory = true
    versionRange = "[1.20.1,1.21)"
    ordering = "NONE"
    side = "BOTH"
```

### 3. Mod Entrypoint

```java
@Mod("modid")
public class MyMod {
    public static final Logger LOGGER = LogUtils.getLogger();

    public MyMod() {
        IEventBus modBus = FMLJavaModLoadingContext.get().getModEventBus();

        MyItems.ITEMS.register(modBus);
        MyBlocks.BLOCKS.register(modBus);
        MyCreativeTabs.TABS.register(modBus);

        modBus.addListener(this::commonSetup);
        MinecraftForge.EVENT_BUS.register(this);
    }

    private void commonSetup(FMLCommonSetupEvent event) {
        event.enqueueWork(() -> {
            // thread-safe setup: compost values, flammability, etc.
        });
    }
}
```

### 4. Registration with DeferredRegister

Always use `DeferredRegister` — never register directly in constructors.

```java
public class MyItems {
    public static final DeferredRegister<Item> ITEMS =
        DeferredRegister.create(ForgeRegistries.ITEMS, "modid");

    public static final RegistryObject<Item> MY_ITEM =
        ITEMS.register("my_item", () -> new Item(
            new Item.Properties().stacksTo(64)
        ));

    public static final RegistryObject<Item> MY_FOOD =
        ITEMS.register("my_food", () -> new Item(
            new Item.Properties().food(new FoodProperties.Builder()
                .nutrition(4).saturationMod(0.3f).build())
        ));
}
```

```java
public class MyBlocks {
    public static final DeferredRegister<Block> BLOCKS =
        DeferredRegister.create(ForgeRegistries.BLOCKS, "modid");

    public static final RegistryObject<Block> MY_BLOCK =
        BLOCKS.register("my_block", () -> new Block(
            BlockBehaviour.Properties.of()
                .strength(1.5f, 6.0f)
                .sound(SoundType.STONE)
        ));
}
```

**Wire in mod constructor:**
```java
MyItems.ITEMS.register(modBus);
MyBlocks.BLOCKS.register(modBus);
```

**Access registered objects:** Always use `.get()` — only call after registration is complete.
```java
MyItems.MY_ITEM.get()   // safe at runtime, not during static init
```

### 5. Event System

Forge has two buses:

| Bus | Access | Used for |
|-----|--------|----------|
| `MinecraftForge.EVENT_BUS` | Game bus | World events, entity events, player events |
| `FMLJavaModLoadingContext.get().getModEventBus()` | Mod bus | Lifecycle, registration, capability attachment |

**Method 1 — instance registration in mod constructor:**
```java
MinecraftForge.EVENT_BUS.register(this);           // game bus
modBus.addListener(this::onCommonSetup);           // mod bus
```

**Method 2 — `@Mod.EventBusSubscriber` static class:**
```java
@Mod.EventBusSubscriber(modid = "modid", bus = Mod.EventBusSubscriber.Bus.FORGE)
public class MyGameEvents {
    @SubscribeEvent
    public static void onBlockBreak(BlockEvent.BreakEvent event) { }
}

@Mod.EventBusSubscriber(modid = "modid", bus = Mod.EventBusSubscriber.Bus.MOD)
public class MyModEvents {
    @SubscribeEvent
    public static void onRegister(RegisterEvent event) { }
}
```

**Key lifecycle events (mod bus):**

| Event | Purpose |
|-------|---------|
| `FMLCommonSetupEvent` | Shared setup; use `enqueueWork()` for non-thread-safe code |
| `FMLClientSetupEvent` | Client-only setup (renderers, key bindings) |
| `FMLDedicatedServerSetupEvent` | Server-only setup |
| `RegisterEvent` | Manual registration fallback |
| `EntityAttributeCreationEvent` | Register entity attributes |
| `BuildCreativeModeTabContentsEvent` | Add items to creative tabs |

**Key game events (game bus):**
`BlockEvent.BreakEvent`, `LivingDeathEvent`, `PlayerEvent`, `TickEvent`, `RightClickBlockEvent`, `AttachCapabilitiesEvent`

**Cancellable events:**
```java
@SubscribeEvent
public static void onBreak(BlockEvent.BreakEvent event) {
    if (someCondition) event.setCanceled(true);
}
```

### 6. Sided Logic

**Logical side** (use in-game): `level.isClientSide`
**Physical side** (use for class loading): `FMLEnvironment.dist` / `@OnlyIn(Dist.CLIENT)`

```java
// In-game logic gate
if (!level.isClientSide) {
    // server logic only
}

// Safe client-only method call
DistExecutor.unsafeRunWhenOn(Dist.CLIENT, () -> () -> ClientHelper.doClientThing());
```

**Never** reference `net.minecraft.client.*` classes from code that runs on the dedicated server physical side. Use a separate client proxy class loaded via `@Mod.EventBusSubscriber(value = Dist.CLIENT)`.

```java
@Mod.EventBusSubscriber(value = Dist.CLIENT, modid = "modid", bus = Bus.MOD)
public class ClientEvents {
    @SubscribeEvent
    public static void onClientSetup(FMLClientSetupEvent event) {
        EntityRenderers.register(MyEntities.MY_ENTITY.get(), MyEntityRenderer::new);
    }
}
```

### 7. Networking (SimpleChannel)

```java
public class ModNetwork {
    public static final SimpleChannel CHANNEL = NetworkRegistry.newSimpleChannel(
        new ResourceLocation("modid", "main"),
        () -> "1",
        "1"::equals,
        "1"::equals
    );

    public static void register() {
        int id = 0;
        CHANNEL.registerMessage(id++, MyPacket.class,
            MyPacket::encode, MyPacket::decode, MyPacket::handle);
    }
}
```

**Packet class:**
```java
public class MyPacket {
    private final int value;

    public MyPacket(int value) { this.value = value; }

    public static void encode(MyPacket msg, FriendlyByteBuf buf) {
        buf.writeInt(msg.value);
    }

    public static MyPacket decode(FriendlyByteBuf buf) {
        return new MyPacket(buf.readInt());
    }

    public static void handle(MyPacket msg, Supplier<NetworkEvent.Context> ctx) {
        ctx.get().enqueueWork(() -> {
            // runs on main thread — access world/player here
            ServerPlayer sender = ctx.get().getSender(); // null if S→C
        });
        ctx.get().setPacketHandled(true);
    }
}
```

**Sending:**
```java
// Server → specific client
ModNetwork.CHANNEL.send(PacketDistributor.PLAYER.with(() -> player), new MyPacket(42));

// Server → all tracking an entity
ModNetwork.CHANNEL.send(PacketDistributor.TRACKING_ENTITY.with(() -> entity), pkt);

// Client → server
ModNetwork.CHANNEL.sendToServer(new MyPacket(42));
```

Call `ModNetwork.register()` from `FMLCommonSetupEvent` via `enqueueWork`.

### 8. Data Generation

```java
@Mod.EventBusSubscriber(modid = "modid", bus = Bus.MOD)
public class DataGenerators {
    @SubscribeEvent
    public static void gatherData(GatherDataEvent event) {
        DataGenerator gen = event.getGenerator();
        ExistingFileHelper efh = event.getExistingFileHelper();
        PackOutput output = gen.getPackOutput();

        gen.addProvider(event.includeServer(), new MyRecipeProvider(output));
        gen.addProvider(event.includeServer(), new MyLootTableProvider(output));
        gen.addProvider(event.includeServer(), new MyTagsProvider(output, event.getLookupProvider(), efh));
        gen.addProvider(event.includeClient(), new MyBlockStateProvider(output, efh));
        gen.addProvider(event.includeClient(), new MyItemModelProvider(output, efh));
        gen.addProvider(event.includeClient(), new MyLanguageProvider(output, "modid", "en_us"));
    }
}
```

**Recipe provider example:**
```java
public class MyRecipeProvider extends RecipeProvider {
    public MyRecipeProvider(PackOutput output) { super(output); }

    @Override
    protected void buildRecipes(Consumer<FinishedRecipe> writer) {
        ShapedRecipeBuilder.shaped(RecipeCategory.MISC, MyItems.MY_ITEM.get())
            .pattern("###")
            .pattern("#X#")
            .pattern("###")
            .define('#', Tags.Items.INGOTS_IRON)
            .define('X', Items.DIAMOND)
            .unlockedBy("has_iron", has(Tags.Items.INGOTS_IRON))
            .save(writer);
    }
}
```

Run: `./gradlew runData`

### 9. Configuration

```java
public class MyConfig {
    public static final ForgeConfigSpec.Builder BUILDER = new ForgeConfigSpec.Builder();
    public static final ForgeConfigSpec SPEC;

    public static final ForgeConfigSpec.IntValue SOME_VALUE;
    public static final ForgeConfigSpec.BooleanValue FEATURE_ENABLED;

    static {
        BUILDER.push("general");
        SOME_VALUE = BUILDER.comment("A number").defineInRange("someValue", 10, 1, 100);
        FEATURE_ENABLED = BUILDER.comment("Toggle feature").define("featureEnabled", true);
        BUILDER.pop();
        SPEC = BUILDER.build();
    }
}
```

Register in mod constructor:
```java
ModLoadingContext.get().registerConfig(ModConfig.Type.COMMON, MyConfig.SPEC);
```

Types: `CLIENT` (client-side only), `COMMON` (both sides, not synced), `SERVER` (per-world, synced to clients).

Access values: `MyConfig.SOME_VALUE.get()`

### 10. Capabilities

Capabilities attach arbitrary data/interfaces to entities, block entities, chunks, item stacks.

**Register a capability:**
```java
@Mod.EventBusSubscriber(bus = Bus.MOD)
public class MyCapabilities {
    public static final Capability<IMyCapability> MY_CAP = CapabilityManager.get(new CapabilityToken<>(){});

    @SubscribeEvent
    public static void register(RegisterCapabilitiesEvent event) {
        event.register(IMyCapability.class);
    }
}
```

**Attach to entity:**
```java
@Mod.EventBusSubscriber(bus = Bus.FORGE)
public class CapabilityEvents {
    @SubscribeEvent
    public static void attach(AttachCapabilitiesEvent<Entity> event) {
        if (event.getObject() instanceof Player) {
            event.addCapability(new ResourceLocation("modid", "my_cap"),
                new MyCapabilityProvider());
        }
    }
}
```

**Provider:**
```java
public class MyCapabilityProvider implements ICapabilitySerializable<CompoundTag> {
    private final MyCapabilityImpl impl = new MyCapabilityImpl();
    private final LazyOptional<IMyCapability> optional = LazyOptional.of(() -> impl);

    @Override
    public <T> LazyOptional<T> getCapability(Capability<T> cap, Direction side) {
        return MyCapabilities.MY_CAP.orEmpty(cap, optional);
    }

    @Override public CompoundTag serializeNBT() { return impl.save(); }
    @Override public void deserializeNBT(CompoundTag tag) { impl.load(tag); }
}
```

**Query:**
```java
entity.getCapability(MyCapabilities.MY_CAP).ifPresent(cap -> {
    cap.doSomething();
});
```

### 11. Inter-mod Compatibility

- **JEI**: Implement `IModPlugin`, annotate `@JeiPlugin`, register recipe categories and handlers.
- **Tags**: Use `Tags.Items.*`, `Tags.Blocks.*` (Forge convention tags) — never hardcode item IDs from other mods.
- **`@Optional` and `compileOnly`**: Wrap hard mod dependencies with `@Optional.Method(modid="...")` or use `ModList.get().isLoaded("modid")` guards.
- **`forge:` tags**: Prefer `forge:ingots/iron`, `forge:dusts/glowstone` etc. for cross-mod item unification.

### 12. Migration Protocol

When user asks to migrate/refactor old Forge code:

1. Confirm target MC + Forge version.
2. Fetch migration notes: `https://docs.minecraftforge.net/en/<VERSION>/misc/updateguide/`
3. Key paradigm shifts by era:

| Old pattern | Modern replacement |
|-------------|-------------------|
| `TileEntity` | `BlockEntity` + `BlockEntityTicker` |
| Raw NBT on items | `DataComponentType` (1.20.5+) |
| `IForgeItem` capability | Data components or `IItemExtension` |
| `WorldEvent` | `LevelEvent` |
| Hardcoded JSON | `DataProvider` datagen |
| `RegistryObject` in static field | Same — just ensure `.get()` not called too early |

4. After rewriting: remind user to run `./gradlew runData` to regenerate resources.

## Tooling

```bash
./gradlew genIntellijRuns    # IDE run configs
./gradlew runClient          # In-game client test
./gradlew runServer          # Dedicated server test
./gradlew runData            # Generate data providers output
./gradlew runGameTestServer  # GameTest headless
./gradlew build              # Build JAR to build/libs/
```

## Documentation References

See `references/forge-links.md` for version-specific docs, MDK, javadoc, and community resources.

# Benchmark TTS — 2026-11-10 09:10

3 corridas por caso; latencia = mediana (mínimo). RTF < 1 = más rápido que tiempo real. Textos: corto 39, medio 249, largo 999 caracteres.

| Motor | Voz | Texto | Latencia | Audio | RTF | chars/s |
|---|---|---|---|---|---|---|
| edge | es-MX-JorgeNeural | corto | 1.19s (1.11s) | 3.48s | 0.342 | 33 |
| edge | es-MX-JorgeNeural | medio | 1.4s (1.39s) | 17.62s | 0.079 | 178 |
| edge | es-MX-JorgeNeural | largo | 1.95s (1.94s) | 70.1s | 0.028 | 513 |
| edge | es-PE-CamilaNeural | corto | 1.18s (1.13s) | 3.29s | 0.358 | 33 |
| edge | es-PE-CamilaNeural | medio | 1.4s (1.4s) | 15.91s | 0.088 | 178 |
| edge | es-PE-CamilaNeural | largo | 2.73s (1.91s) | 63.31s | 0.043 | 366 |
| edge | es-ES-AlvaroNeural | corto | 1.15s (1.14s) | 3.31s | 0.348 | 34 |
| edge | es-ES-AlvaroNeural | medio | 1.42s (1.41s) | 17.14s | 0.083 | 176 |
| edge | es-ES-AlvaroNeural | largo | 1.86s (1.78s) | 68.21s | 0.027 | 537 |
| tiktok | es_mx_002 | corto | 2.55s (2.31s) | 2.57s | 0.992 | 15 |
| tiktok | es_mx_002 | medio | 4.16s (4.09s) | 16.44s | 0.253 | 60 |
| tiktok | es_mx_002 | largo | 17.27s (16.44s) | 65.77s | 0.263 | 58 |
| tiktok | en_us_001 | corto | 2.31s (2.25s) | 3.53s | 0.656 | 17 |
| tiktok | en_us_001 | medio | 4.81s (4.68s) | 20.09s | 0.24 | 52 |
| tiktok | en_us_001 | largo | 20.47s (19.93s) | 80.36s | 0.255 | 49 |
| tiktok | en_us_ghostface | corto | 2.71s (2.42s) | 3.38s | 0.801 | 14 |
| tiktok | en_us_ghostface | medio | 5.44s (5.33s) | 20.45s | 0.266 | 46 |
| tiktok | en_us_ghostface | largo | 22.64s (22.32s) | 81.8s | 0.277 | 44 |
| sapi | Microsoft Helena Desktop | corto | 0.37s (0.36s) | 3.24s | 0.114 | 105 |
| sapi | Microsoft Helena Desktop | medio | 0.43s (0.43s) | 16.95s | 0.026 | 576 |
| sapi | Microsoft Helena Desktop | largo | 0.75s (0.73s) | 67.79s | 0.011 | 1338 |
| fx | loquendo | corto | 1.23s (1.21s) | 3.17s | 0.388 | 32 |
| fx | loquendo | medio | 1.56s (1.54s) | 16.32s | 0.096 | 160 |
| fx | loquendo | largo | 2.31s (2.27s) | 64.94s | 0.036 | 432 |
| fx | robot | corto | 1.22s (1.2s) | 3.48s | 0.35 | 32 |
| fx | robot | medio | 1.5s (1.49s) | 17.62s | 0.085 | 165 |
| fx | robot | largo | 2.48s (2.07s) | 70.1s | 0.035 | 402 |
| fx | ardilla | corto | 1.23s (1.22s) | 2.68s | 0.46 | 32 |
| fx | ardilla | medio | 1.52s (1.5s) | 13.07s | 0.116 | 164 |
| fx | ardilla | largo | 2.0s (1.92s) | 52.1s | 0.038 | 499 |

# 🎧 Discoteca

Discoteca digital personal — un catálogo musical curado a mano, sin backend,
sin base de datos y sin dependencias más allá de un puñado de APIs públicas.
Todo el sitio vive en un único `index.html`.

**➜ [kinoluiggi.github.io/discoteca](https://kinoluiggi.github.io/discoteca/)**

---

## Qué es

Este proyecto es mi discoteca digital: miles de álbumes curados uno por uno,
mi colección física de vinilos sincronizada con Discogs, mis estadísticas
reales de escucha en Last.fm, y un reproductor propio que amarra todo eso
en una sola interfaz.

No hay servidor. No hay base de datos. Los "datos" son archivos JSON
estáticos servidos por GitHub Pages, y el navegador hace el resto: pedir
esos archivos, pedirle a Discogs/Last.fm/YouTube lo que haga falta en vivo,
y reproducir.

## Pestañas

- **DISCOTECA** — el catálogo principal. Miles de álbumes con ficha,
  tracklist y fuente de audio por pista (YouTube, SoundCloud o mp3 directo).
  Filtros por década, género y país.
- **VINILOS** — mi colección física, traída en vivo desde la API de Discogs
  (con fotos, tracklist y emparejado automático con YouTube), más mi
  *wantlist*. Se puede ordenar como en Discogs: artista, año, fecha de alta,
  valoración.
- **LAST.FM** — seis módulos sobre mi historial real de escucha:
  - **Dashboard** — estadísticas generales y lo último escuchado.
  - **KinoPlayer** — mis canciones más escuchadas o favoritas, reproducibles.
  - **Máquina del Tiempo** — qué sonaba en cualquier fecha desde 2008.
  - **Playlist IA** — genera un prompt con mi historial real para pedirle a
    Claude una playlist narrativa (sin pagar ninguna API, solo copiar y
    pegar en claude.ai).
  - **Isla Desierta** — el cruce entre lo más escuchado y lo marcado como
    favorito ❤.
  - **Retrovisor** — hoy, pero hace N años: qué sonaba este mismo día en
    ediciones anteriores.
- **NOVEDADES** — un diario de mis últimas descargas, con carátula y
  reproducción por pista cuando el disco se encuentra en Discogs o iTunes.

## Modo curador

Añadiendo `?editar` a la URL se activa el modo de edición: dar de alta
álbumes nuevos, añadir/quitar/renombrar pistas, corregir fuentes de audio
rotas, editar fichas, y todo se guarda directo al repo vía la API de
GitHub (Contents API) — sin build, sin CI, el sitio se actualiza solo en
1–2 minutos tras cada commit.

## Cómo está hecho

- Un único `index.html`: HTML + CSS + JavaScript vanilla, sin frameworks
  ni paso de compilación.
- Datos en JSON estático (`indice.json` + un archivo por álbum), servidos
  tal cual por GitHub Pages.
- APIs externas usadas en vivo desde el navegador: Discogs, Last.fm,
  YouTube Data API, iTunes Search API.
- Analítica de visitas con [GoatCounter](https://www.goatcounter.com/)
  (sin cookies).

## Créditos

Curado por [Kinoluiggi](https://github.com/kinoluiggi).

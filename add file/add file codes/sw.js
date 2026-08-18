// sw.js - Service Worker de Aislamiento Local y Soporte Offline
const CACHE_NAME = 'andrick-ia-local-v6.0';
const LOCAL_ASSETS = [
  './',
  './index.html',
  './AMP-CODE-LINK.js',
  './manifest.json'
];

// Instalar Service Worker y almacenar archivos en caché local de inmediato
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(LOCAL_ASSETS);
    })
  );
});

// Activar y realizar limpieza de cachés del sistema anteriores
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    })
  );
});

// Intercepción estricta: Sirve desde la carpeta del dispositivo sin buscar en la web
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request);
    })
  );
});

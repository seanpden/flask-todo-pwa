const cacheName = "cache-v1";
const precacheResources = ["/", "/manifest.json", "/foobar", "/fizzbuzz"];

self.addEventListener("install", function (event) {
  console.log("[Service Worker] Installing Service Worker ...", event);
  event.waitUntil(
    caches.open(cacheName).then((cache) => cache.addAll(precacheResources))
  );
});
self.addEventListener("activate", function (event) {
  console.log("[Service Worker] Activating Service Worker ...", event);
});
self.addEventListener("fetch", function (event) {
  console.log("[Service Worker] Fetching something ...", event);
});

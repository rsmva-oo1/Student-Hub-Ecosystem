<!-- <script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <HelloWorld />
</template> -->
<template>
  <div class="min-h-screen p-6 max-w-7xl mx-auto">
    <header class="mb-8 flex justify-between items-center">
      <div>
        <h1 class="text-3xl font-bold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
          Student Hub Ecosystem
        </h1>
        <p class="text-slate-400 text-sm mt-1">Xush kelibsiz, Rustamova Munisa</p>
      </div>
      <div class="bg-slate-700 px-4 py-2 rounded-full text-sm border border-slate-700 text-cyan-400">
        API Status: <span class="font-bold">Online</span>
      </div>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-[180px]">
      
      <div class="md:col-span-2 row-span-2 bg-gradient-to-br from-slate-800 to-slate-900 p-6 rounded-3xl border border-slate-800 shadow-xl flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-semibold text-slate-200 flex items-center gap-2">
            📅 Bugungi Dars Jadvali
          </h2>
          <p class="text-slate-400 text-sm mt-2">Darslaringizni o'z vaqtida kuzatib boring.</p>
        </div>
        <div class="text-slate-500 text-center py-8">Hozircha darslar kiritilmagan...</div>
      </div>

      <div class="bg-gradient-to-tr from-cyan-900 to-slate-900 p-6 rounded-3xl border border-slate-800 shadow-xl flex flex-col justify-between">
        <h2 class="text-lg font-semibold text-cyan-400">👤 Talaba Profili</h2>
        <div>
          <div class="text-2xl font-bold text-white">Munisa</div>
          <div class="text-xs text-slate-400">ID: #10024</div>
        </div>
      </div>

      <div class="row-span-2 bg-gradient-to-b from-slate-800 to-slate-900 p-6 rounded-3xl border border-slate-800 shadow-xl flex flex-col justify-between">
        <div>
          <h2 class="text-lg font-semibold text-purple-400">📝 Topshiriqlar</h2>
          <div class="mt-4 space-y-2">
            <div class="bg-slate-700 bg-opacity-40 p-3 rounded-xl text-sm border border-slate-700">FastAPI integratsiyasi</div>
            <div class="bg-slate-700 bg-opacity-40 p-3 rounded-xl text-sm border border-slate-700">Vue dashboard dizayni</div>
          </div>
        </div>
        <button class="w-full bg-purple-600 hover:bg-purple-700 text-white text-sm py-2.5 rounded-xl font-medium transition-all">
          + Yangi vazifa
        </button>
      </div>

      <div class="bg-gradient-to-r from-amber-950 to-slate-900 p-6 rounded-3xl border border-slate-800 shadow-xl flex items-center justify-between">
        <div>
          <h2 class="text-lg font-semibold text-amber-400">🔔 Eslatma</h2>
          <p class="text-sm text-slate-300 mt-1">Ertaga yakuniy nazorat testi bor!</p>
        </div>
      </div>

      <div class="bg-slate-800 p-6 rounded-3xl border border-slate-700 flex flex-col justify-between">
        <span class="text-xs text-slate-400 uppercase tracking-wider">Tizim vaqti</span>
        <div class="text-2xl font-mono font-bold text-slate-200">23:07</div>
      </div>

    </div>
  </div>
</template>
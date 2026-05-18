<template>
  <div class="min-h-screen bg-[#0b0f19] text-slate-100 p-4 md:p-8 font-sans selection:bg-cyan-500 selection:text-slate-900 relative overflow-hidden">
    
    <div class="absolute top-[-10%] left-[-10%] w-[500px] h-[500px] bg-cyan-500/10 rounded-full blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[600px] h-[600px] bg-purple-500/10 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto relative z-10">
      
      <header class="mb-10 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 opacity-0 animate-[slideDown_0.8s_cubic-bezier(0.16,1,0.3,1)_forwards]">
        <div>
          <div class="flex items-center gap-2 mb-1">
            <span class="h-2 w-2 rounded-full bg-cyan-400 animate-ping"></span>
            <span class="text-xs font-semibold tracking-widest text-cyan-400 uppercase">Beta Platforma</span>
          </div>
          <h1 class="text-4xl font-extrabold tracking-tight bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent">
            Student Hub <span class="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">Ecosystem</span>
          </h1>
          <p class="text-slate-400 text-sm mt-1 flex items-center gap-1.5">
            Xush kelibsiz, <span class="text-slate-200 font-medium underline decoration-cyan-500/40 decoration-2">Rustamova Munisa</span> ✨
          </p>
        </div>
        
        <div class="bg-slate-900/60 backdrop-blur-md px-4 py-2 rounded-2xl text-xs font-semibold border border-slate-800/80 text-slate-300 flex items-center gap-2.5 shadow-xl shadow-black/20">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          FastAPI Status: <span class="text-emerald-400 font-bold tracking-wider">ONLINE</span>
        </div>
      </header>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-[200px]">
        
        <div class="md:col-span-2 row-span-2 group relative overflow-hidden bg-gradient-to-br from-slate-900 via-slate-900/90 to-slate-950 p-8 rounded-[32px] border border-slate-800/50 hover:border-slate-700/80 transition-all duration-500 shadow-2xl hover:shadow-cyan-500/5 flex flex-col justify-between opacity-0 animate-[scaleUp_0.7s_cubic-bezier(0.16,1,0.3,1)_0.1s_forwards]">
          <div class="absolute -inset-px bg-gradient-to-br from-cyan-500/10 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-[32px]"></div>
          
          <div class="relative z-10">
            <div class="flex justify-between items-start">
              <div>
                <h2 class="text-2xl font-bold text-white tracking-tight flex items-center gap-2.5">
                  <span class="p-2 bg-slate-800/80 rounded-xl text-lg group-hover:scale-110 transition-transform duration-300 border border-slate-700/50">📅</span> 
                  Bugungi Dars Jadvali
                </h2>
                <p class="text-slate-400 text-sm mt-2">Bugungi darslaringiz ro'yxati va vaqtlari.</p>
              </div>
              <span class="text-xs bg-slate-800/80 border border-slate-700/50 text-slate-400 px-3 py-1.5 rounded-xl font-medium">Dushanba</span>
            </div>
            
            <div class="mt-8 space-y-3">
              <div class="flex justify-between items-center bg-slate-850/40 border border-slate-800/60 p-4 rounded-2xl hover:bg-slate-800/50 transition-all duration-300">
                <span class="text-slate-300 font-medium">Sun'iy Intellekt Asoslari</span>
                <span class="text-xs font-mono text-cyan-400 bg-cyan-950/40 border border-cyan-900/50 px-2.5 py-1 rounded-lg">09:00 - 10:20</span>
              </div>
              <div class="flex justify-between items-center bg-slate-850/40 border border-slate-800/60 p-4 rounded-2xl hover:bg-slate-800/50 transition-all duration-300">
                <span class="text-slate-300 font-medium">Veb Dasturlash (Vue.js + FastAPI)</span>
                <span class="text-xs font-mono text-purple-400 bg-purple-950/40 border border-purple-900/50 px-2.5 py-1 rounded-lg">10:30 - 11:50</span>
              </div>
            </div>
          </div>
          <div class="relative z-10 text-xs text-slate-500 flex items-center gap-1.5 mt-4">
            <span class="h-1.5 w-1.5 rounded-full bg-slate-600"></span> Oxirgi yangilanish: hozirgina
          </div>
        </div>

        <div class="group relative overflow-hidden bg-gradient-to-b from-slate-900 to-slate-950 p-8 rounded-[32px] border border-slate-800/50 hover:border-cyan-500/30 transition-all duration-500 shadow-2xl hover:shadow-cyan-500/5 flex flex-col justify-between opacity-0 animate-[scaleUp_0.7s_cubic-bezier(0.16,1,0.3,1)_0.2s_forwards]">
          <div class="absolute -inset-px bg-gradient-to-b from-cyan-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-[32px]"></div>
          
          <div class="relative z-10 flex justify-between items-start">
            <h2 class="text-lg font-bold text-slate-200 flex items-center gap-2">
              <span class="p-1.5 bg-slate-800/80 rounded-lg text-sm border border-slate-700/50">👤</span> Profillar
            </h2>
            <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center font-bold text-white shadow-lg shadow-cyan-500/20">M</div>
          </div>
          
          <div class="relative z-10">
            <div class="text-2xl font-extrabold text-white tracking-wide group-hover:text-cyan-400 transition-colors duration-300">Munisa</div>
            <div class="text-xs font-mono text-slate-400 mt-1 flex items-center gap-1">
              <span>ID:</span> <span class="text-cyan-400/80">#10024</span>
            </div>
          </div>
        </div>

        <div class="row-span-2 group relative overflow-hidden bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 p-8 rounded-[32px] border border-slate-800/50 hover:border-purple-500/30 transition-all duration-500 shadow-2xl hover:shadow-purple-500/5 flex flex-col justify-between opacity-0 animate-[scaleUp_0.7s_cubic-bezier(0.16,1,0.3,1)_0.3s_forwards]">
          <div class="absolute -inset-px bg-gradient-to-b from-purple-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-[32px]"></div>
          
          <div class="relative z-10">
            <h2 class="text-lg font-bold text-slate-200 flex items-center gap-2">
              <span class="p-1.5 bg-slate-800/80 rounded-lg text-sm border border-slate-700/50">📝</span> Topshiriqlar
            </h2>
            
            <div class="mt-6 space-y-3">
              <div class="bg-slate-900/40 p-3.5 rounded-2xl text-xs font-medium border border-slate-800/80 text-slate-300 flex items-center gap-3 hover:bg-slate-850/60 transition-colors cursor-pointer group/item">
                <span class="h-4 w-4 rounded-full border border-purple-500/50 flex items-center justify-center group-hover/item:border-purple-400 transition-colors"><span class="h-2 w-2 rounded-full bg-purple-500 opacity-0 group-hover/item:opacity-100 transition-opacity"></span></span>
                FastAPI integratsiyasi
              </div>
              <div class="bg-slate-900/40 p-3.5 rounded-2xl text-xs font-medium border border-slate-800/80 text-slate-300 flex items-center gap-3 hover:bg-slate-850/60 transition-colors cursor-pointer group/item">
                <span class="h-4 w-4 rounded-full border border-purple-500/50 flex items-center justify-center group-hover/item:border-purple-400 transition-colors"><span class="h-2 w-2 rounded-full bg-purple-500 opacity-0 group-hover/item:opacity-100 transition-opacity"></span></span>
                Vue premium dashboard dizayni
              </div>
            </div>
          </div>
          
          <button class="relative z-10 w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 active:scale-[0.98] text-white text-xs py-3.5 rounded-2xl font-bold shadow-xl shadow-purple-900/20 hover:shadow-purple-600/20 transition-all duration-300 mt-4">
            + Yangi Vazifa Qo'shish
          </button>
        </div>

        <div class="group relative overflow-hidden bg-gradient-to-r from-slate-900 to-slate-950 p-8 rounded-[32px] border border-slate-800/50 hover:border-amber-500/20 transition-all duration-500 shadow-2xl flex items-center justify-between opacity-0 animate-[scaleUp_0.7s_cubic-bezier(0.16,1,0.3,1)_0.4s_forwards]">
          <div class="absolute -inset-px bg-gradient-to-r from-amber-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-[32px]"></div>
          
          <div class="relative z-10 flex gap-4 items-center">
            <span class="p-3 bg-amber-950/30 border border-amber-900/30 rounded-2xl text-xl text-amber-400 group-hover:animate-bounce">🔔</span>
            <div>
              <h2 class="text-sm font-bold tracking-wider text-amber-400 uppercase">Muhim Eslatma</h2>
              <p class="text-base text-slate-200 font-semibold mt-0.5">Ertaga yakuniy nazorat testi bor!</p>
            </div>
          </div>
        </div>

        <div class="group relative overflow-hidden bg-gradient-to-br from-slate-900 to-slate-950 p-8 rounded-[32px] border border-slate-800/50 hover:border-slate-700 transition-all duration-500 shadow-2xl flex flex-col justify-between opacity-0 animate-[scaleUp_0.7s_cubic-bezier(0.16,1,0.3,1)_0.5s_forwards]">
          <span class="text-xs font-semibold tracking-widest text-slate-500 uppercase">Tizim Haqiqiy Vaqti</span>
         <script setup>
           const currentTime = ref(new Date().toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' }));
const greeting = computed(() => {
  const hour = new Date().getHours();
  if (hour < 6) return "Xayrli tun";
  if (hour < 12) return "Xayrli tong";
  if (hour < 18) return "Xayrli kun";
  return "Xayrli kech";
});
        </div>

      </div>
    </div>
  </div>
</template>

<style>

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
    filter: blur(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
    filter: blur(0);
  }
}

@keyframes scaleUp {
  from {
    opacity: 0;
    transform: translateY(30px) scale(0.96);
    filter: blur(5px);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
}
.bg-slate-850\/40 {
  background-color: rgba(30, 41, 59, 0.4);
}


</style>

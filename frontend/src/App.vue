<script setup>
import { ref, onMounted, computed } from 'vue';

// 1. Haqiqiy vaqt mantiqi
const currentTime = ref(new Date().toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' }));
const greeting = computed(() => {
  const hour = new Date().getHours();
  if (hour < 6) return "Xayrli tun";
  if (hour < 12) return "Xayrli tong";
  if (hour < 18) return "Xayrli kun";
  return "Xayrli kech";
});

onMounted(() => {
  setInterval(() => {
    currentTime.ref = new Date().toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    // Ref-ni to'g'ri yangilash
    const now = new Date();
    currentTime.value = now.toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  }, 1000);
});

// 2. Vazifalar holati
const tasks = ref([
  { id: 1, title: 'FastAPI integratsiyasi', completed: true },
  { id: 2, title: 'Vue premium dashboard dizayni', completed: false },
  { id: 3, title: 'Ma\'lumotlar bazasini ulash', completed: false },
]);
</script>

<template>
  <div class="min-h-screen bg-[#080b14] text-slate-100 flex font-sans selection:bg-cyan-500/30">
    
    <aside class="w-20 hidden lg:flex flex-col items-center py-8 border-r border-slate-800/50 bg-[#0b0f19]/50 backdrop-blur-xl z-20">
      <div class="w-12 h-12 bg-gradient-to-br from-cyan-500 to-blue-600 rounded-2xl flex items-center justify-center shadow-lg shadow-cyan-500/20 mb-10 group cursor-pointer">
        <span class="text-white font-black text-xl group-hover:scale-110 transition-transform">S</span>
      </div>
      <nav class="flex flex-col gap-8 text-slate-500">
        <i class="fas fa-th-large text-cyan-400 text-xl cursor-pointer"></i>
        <i class="fas fa-book text-xl hover:text-slate-300 transition-colors cursor-pointer"></i>
        <i class="fas fa-tasks text-xl hover:text-slate-300 transition-colors cursor-pointer"></i>
        <i class="fas fa-chart-line text-xl hover:text-slate-300 transition-colors cursor-pointer"></i>
      </nav>
      <div class="mt-auto text-slate-600 hover:text-red-400 cursor-pointer transition-colors">
        <i class="fas fa-sign-out-alt text-xl"></i>
      </div>
    </aside>

    <main class="flex-1 p-4 md:p-10 relative overflow-hidden">
      <div class="absolute top-[-10%] left-[20%] w-[600px] h-[600px] bg-cyan-500/5 rounded-full blur-[120px] pointer-events-none animate-pulse"></div>
      <div class="absolute bottom-[-5%] right-[5%] w-[500px] h-[500px] bg-purple-500/5 rounded-full blur-[140px] pointer-events-none"></div>

      <div class="max-w-6xl mx-auto relative z-10">
        
        <header class="mb-12 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-6 opacity-0 animate-[slideDown_0.8s_ease-out_forwards]">
          <div>
            <div class="flex items-center gap-3 mb-2">
              <span class="px-3 py-1 bg-cyan-500/10 border border-cyan-500/20 rounded-full text-[10px] font-bold tracking-[0.2em] text-cyan-400 uppercase">Premium Hub</span>
            </div>
            <h1 class="text-4xl font-black tracking-tight text-white">
              {{ greeting }}, <span class="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">Munisa</span>
            </h1>
            <p class="text-slate-400 text-sm mt-2 flex items-center gap-2">
              <i class="far fa-calendar-alt text-cyan-500"></i> Bugun: 18-May, Dushanba
            </p>
          </div>
          
          <div class="flex gap-4">
             <div class="bg-slate-900/40 backdrop-blur-md px-5 py-3 rounded-2xl border border-slate-800/80 shadow-2xl flex items-center gap-4">
               <div class="text-right">
                 <div class="text-[10px] uppercase tracking-widest text-slate-500 font-bold">API Latency</div>
                 <div class="text-sm font-mono text-emerald-400">24ms</div>
               </div>
               <div class="h-8 w-[1px] bg-slate-800"></div>
               <div class="relative flex h-3 w-3">
                 <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                 <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
               </div>
             </div>
          </div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 auto-rows-[110px]">
          
          <div class="md:col-span-3 row-span-3 group bg-slate-900/40 backdrop-blur-md p-8 rounded-[40px] border border-slate-800/50 hover:border-slate-700/50 transition-all duration-500 flex flex-col justify-between opacity-0 animate-[scaleUp_0.7s_ease-out_0.1s_forwards]">
            <div>
              <div class="flex justify-between items-center mb-8">
                <h2 class="text-2xl font-bold text-white flex items-center gap-4">
                  <div class="p-3 bg-slate-800 rounded-2xl text-xl">📅</div> 
                  Dars Jadvali
                </h2>
                <button class="text-cyan-400 text-xs font-bold hover:underline">Haftalik ko'rish</button>
              </div>
              
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div v-for="i in 2" :key="i" class="bg-[#0f172a]/80 border border-slate-800/50 p-5 rounded-3xl hover:bg-slate-800/40 transition-all cursor-pointer group/card">
                  <div class="flex justify-between mb-4">
                    <span class="text-[10px] font-bold text-cyan-500 uppercase tracking-widest">{{ i == 1 ? '09:00' : '10:30' }}</span>
                    <i class="fas fa-ellipsis-h text-slate-600"></i>
                  </div>
                  <h3 class="text-slate-200 font-semibold mb-1 group-hover/card:text-white transition-colors">
                    {{ i == 1 ? 'Sun\'iy Intellekt' : 'Veb Dasturlash' }}
                  </h3>
                  <p class="text-xs text-slate-500 mb-4">Xona: 402-A (Online)</p>
                  <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                    <div class="bg-cyan-500 h-full w-[70%] rounded-full shadow-[0_0_10px_rgba(6,182,212,0.5)]"></div>
                  </div>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-4 text-xs text-slate-500 mt-6 pt-6 border-t border-slate-800/50">
               <span>Darslar tugashiga: <strong>2 soat</strong></span>
               <div class="flex -space-x-2">
                 <div v-for="i in 3" :key="i" class="w-6 h-6 rounded-full border-2 border-[#0b0f19] bg-slate-700 flex items-center justify-center text-[8px] font-bold">M</div>
               </div>
            </div>
          </div>

          <div class="md:col-span-1 row-span-2 bg-gradient-to-br from-slate-900 to-[#0b0f19] p-8 rounded-[40px] border border-slate-800/50 flex flex-col justify-between items-center text-center group opacity-0 animate-[scaleUp_0.7s_ease-out_0.2s_forwards]">
            <span class="text-[10px] font-black text-slate-500 uppercase tracking-[0.3em]">System Time</span>
            <div class="text-4xl font-mono font-black text-white group-hover:text-cyan-400 transition-colors duration-500 tracking-tighter">
              {{ currentTime }}
            </div>
            <div class="w-full py-3 bg-slate-800/30 rounded-2xl border border-slate-800/50 text-[10px] text-slate-400 font-bold">
              GMT +5 (TASHKENT)
            </div>
          </div>

          <div class="bg-gradient-to-tr from-cyan-900/20 to-slate-900 p-6 rounded-[35px] border border-slate-800/50 flex flex-col justify-center opacity-0 animate-[scaleUp_0.7s_ease-out_0.3s_forwards]">
            <div class="text-[10px] font-bold text-cyan-500 uppercase mb-1">Student Rank</div>
            <div class="text-xl font-black text-white">TOP #12</div>
          </div>

          <div class="md:col-span-1 row-span-2 bg-slate-900/40 backdrop-blur-md p-8 rounded-[40px] border border-slate-800/50 opacity-0 animate-[scaleUp_0.7s_ease-out_0.4s_forwards]">
            <h3 class="text-lg font-bold text-white mb-6">Vazifalar</h3>
            <div class="space-y-4">
              <div v-for="task in tasks" :key="task.id" class="flex items-center gap-3 group/task cursor-pointer">
                <div :class="task.completed ? 'bg-emerald-500 border-emerald-500' : 'border-slate-700'" class="w-5 h-5 rounded-lg border-2 flex items-center justify-center transition-all group-hover/task:border-cyan-500">
                  <i v-if="task.completed" class="fas fa-check text-[10px] text-white"></i>
                </div>
                <span :class="task.completed ? 'text-slate-500 line-through' : 'text-slate-300'" class="text-xs font-medium">{{ task.title }}</span>
              </div>
            </div>
          </div>

          <div class="md:col-span-3 row-span-1 bg-gradient-to-r from-amber-500/10 to-transparent p-8 rounded-[40px] border border-amber-500/20 flex items-center justify-between group opacity-0 animate-[scaleUp_0.7s_ease-out_0.5s_forwards]">
            <div class="flex items-center gap-6">
              <div class="w-12 h-12 bg-amber-500/20 rounded-2xl flex items-center justify-center text-amber-400 text-xl group-hover:animate-bounce">🔔</div>
              <div>
                <h4 class="text-amber-400 font-black text-xs uppercase tracking-widest">Diqqat</h4>
                <p class="text-slate-200 font-semibold">Ertaga yakuniy nazorat testi bor!</p>
              </div>
            </div>
            <i class="fas fa-arrow-right text-amber-500 opacity-0 group-hover:opacity-100 transform translate-x-[-10px] group-hover:translate-x-0 transition-all"></i>
          </div>

        </div>
      </div>
    </main>
  </div>
</template>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-30px); filter: blur(10px); }
  to { opacity: 1; transform: translateY(0); filter: blur(0); }
}

@keyframes scaleUp {
  from { opacity: 0; transform: translateY(40px) scale(0.95); filter: blur(10px); }
  to { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
}

body {
  background-color: #080b14;
  overflow-x: hidden;
}

/* Scrollbar dizayni */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #080b14; }
::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: #334155; }
</style>

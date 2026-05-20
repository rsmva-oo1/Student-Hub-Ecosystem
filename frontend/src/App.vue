<script setup>
import { ref, onMounted, computed } from 'vue';
import API from './api'; 

const isDarkMode = ref(true);
const toggleTheme = () => {
  isDarkMode.value = !isDarkMode.value;
};

const currentTime = ref(new Date().toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' }));
const greeting = computed(() => {
  const hour = new Date().getHours();
  if (hour < 6) return "Xayrli tun";
  if (hour < 12) return "Xayrli tong";
  if (hour < 18) return "Xayrli kun";
  return "Xayrli kech";
});

// 2. Vazifalar (Backenddan keladigan qismi)
const tasks = ref([]);

const fetchTasks = async () => {
  try {
    const response = await API.get('/tasks');
    tasks.value = response.data;
  } catch (error) {
    console.error("Backenddan ma'lumot olishda xatolik:", error);
  }
};

onMounted(() => {
  setInterval(() => {
    const now = new Date();
    currentTime.value = now.toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  }, 1000);

  fetchTasks();
});

const toggleTask = (task) => {
  task.completed = !task.completed;
};

const isModalOpen = ref(false);
const newTaskTitle = ref('');

const openModal = () => { isModalOpen.value = true; };
const closeModal = () => { isModalOpen.value = false; newTaskTitle.value = ''; };

const addTask = () => {
  if (newTaskTitle.value.trim() !== '') {
    tasks.value.push({
      id: Date.now(),
      title: newTaskTitle.value,
      completed: false
    });
    closeModal();
  }
};
</script>

<template>
  <div :class="isDarkMode ? 'bg-[#080b14] text-slate-100' : 'bg-[#f4f6fa] text-slate-800'" class="min-h-screen flex font-sans transition-colors duration-500">
    
    <aside :class="isDarkMode ? 'bg-slate-900/50 border-slate-800/50' : 'bg-white border-slate-200'" class="w-20 hidden lg:flex flex-col items-center py-8 border-r backdrop-blur-xl z-20 transition-colors duration-500">
      <div class="w-12 h-12 bg-gradient-to-br from-cyan-500 to-blue-600 rounded-2xl flex items-center justify-center shadow-lg mb-10 cursor-pointer">
        <span class="text-white font-black text-xl">S</span>
      </div>
      <nav :class="isDarkMode ? 'text-slate-500' : 'text-slate-400'" class="flex flex-col gap-8 text-xl">
        <i class="fas fa-th-large text-cyan-400 cursor-pointer"></i>
        <i class="fas fa-book hover:text-cyan-500 cursor-pointer"></i>
        <i class="fas fa-tasks hover:text-cyan-500 cursor-pointer"></i>
        <i class="fas fa-chart-line hover:text-cyan-500 cursor-pointer"></i>
      </nav>
    </aside>

    <main class="flex-1 p-4 md:p-10 relative overflow-hidden">
      <div class="max-w-6xl mx-auto relative z-10">
        
        <header class="mb-12 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-6">
          <div>
            <div class="flex items-center gap-3 mb-2">
              <span class="px-3 py-1 bg-cyan-500/10 border border-cyan-500/20 rounded-full text-[10px] font-bold tracking-[0.2em] text-cyan-400 uppercase">Premium Hub</span>
            </div>
            <h1 class="text-4xl font-black tracking-tight">
              {{ greeting }}, <span class="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">Munisa</span>
            </h1>
          </div>
          
          <div class="flex items-center gap-4">
             <button @click="toggleTheme" :class="isDarkMode ? 'bg-slate-900 border-slate-800 text-yellow-400' : 'bg-white border-slate-200 text-purple-600'" class="p-3 rounded-2xl border shadow-xl flex items-center justify-center transition-all duration-300">
               <i :class="isDarkMode ? 'fas fa-sun' : 'fas fa-moon'" class="text-lg"></i>
             </button>

             <div :class="isDarkMode ? 'bg-slate-900/40 border-slate-800/80' : 'bg-white border-slate-200'" class="backdrop-blur-md px-5 py-3 rounded-2xl border shadow-2xl flex items-center gap-4">
               <div class="text-right">
                 <div class="text-[10px] uppercase tracking-widest text-slate-400 font-bold">API Latency</div>
                 <div class="text-sm font-mono text-emerald-500">24ms</div>
               </div>
             </div>
          </div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 auto-rows-[110px]">
          
          <div :class="isDarkMode ? 'bg-slate-900/40 border-slate-800/50' : 'bg-white border-slate-200 shadow-md hover:shadow-xl">
            <div>
              <div class="flex justify-between items-center mb-8">
                <h2 class="text-2xl font-bold flex items-center gap-4">
                  <div :class="isDarkMode ? 'bg-slate-800' : 'bg-slate-100'" class="p-3 rounded-2xl text-xl">📅</div> 
                  Dars Jadvali
                </h2>
              </div>
              
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div v-for="i in 2" :key="i" :class="isDarkMode ? 'bg-slate-900 border-slate-800/50' : 'bg-slate-50 border-slate-200'" class="border p-5 rounded-3xl transition-all cursor-pointer">
                  <span class="text-[10px] font-bold text-cyan-500 uppercase tracking-widest">{{ i == 1 ? '09:00' : '10:30' }}</span>
                  <h3 class="font-semibold mt-2 mb-1">
                    {{ i == 1 ? 'Sun\'iy Intellekt Asoslari' : 'Veb Dasturlash (FastAPI)' }}
                  </h3>
                  <p class="text-xs text-slate-400">Xona: 402-A (Moodle)</p>
                </div>
              </div>
            </div>
          </div>

          <div :class="isDarkMode ? 'bg-slate-900 border-slate-800/50' : 'bg-white border-slate-200 shadow-sm'" class="md:col-span-1 row-span-2 p-8 rounded-[40px] border flex flex-col justify-between items-center text-center transition-all duration-500">
            <span class="text-[10px] font-black text-slate-400 uppercase tracking-[0.3em]">System Time</span>
            <div class="text-4xl font-mono font-black tracking-tighter">
              {{ currentTime }}
            </div>
            <div :class="isDarkMode ? 'bg-slate-800/30 border-slate-800/50 text-slate-400' : 'bg-slate-100 border-slate-200 text-slate-500'" class="w-full py-3 rounded-2xl border text-[10px] font-bold">
              GMT +5
            </div>
          </div>

          <div :class="isDarkMode ? 'bg-slate-900 border-slate-800/50' : 'bg-white border-slate-200 shadow-sm'" class="bg-gradient-to-tr p-6 rounded-[35px] border flex flex-col justify-center transition-all duration-500">
            <div class="text-[10px] font-bold text-cyan-600 uppercase mb-1">Talaba Reytingi</div>
            <div class="text-xl font-black">TOP #12</div>
          </div>

          <div :class="isDarkMode ? 'bg-slate-900/40 border-slate-800/50' : 'bg-white border-slate-200 shadow-sm'" class="md:col-span-1 row-span-2 p-8 rounded-[40px] border flex flex-col justify-between transition-all duration-500">
            <div>
              <h3 class="text-lg font-bold mb-6">Vazifalar</h3>
              <div v-if="tasks.length === 0" class="text-slate-400 text-xs py-4 text-center">
                Vazifalar yuklanmoqda...
              </div>
              <div v-else class="space-y-4 max-h-[140px] overflow-y-auto">
                <div v-for="task in tasks" :key="task.id" @click="toggleTask(task)" class="flex items-center gap-3 cursor-pointer">
                  <div :class="task.completed ? 'bg-emerald-500 border-emerald-500' : 'border-slate-400'" class="w-5 h-5 rounded-lg border-2 flex items-center justify-center shrink-0">
                    <i v-if="task.completed" class="fas fa-check text-[10px] text-white"></i>
                  </div>
                  <span :class="task.completed ? 'text-slate-400 line-through' : ''" class="text-xs font-medium truncate">{{ task.title }}</span>
                </div>
              </div>
            </div>
            <button @click="openModal" :class="isDarkMode ? 'bg-slate-800 hover:bg-slate-700 border-slate-700/50' : 'bg-slate-100 hover:bg-slate-200 border-slate-200'" class="w-full text-cyan-600 text-xs py-3 rounded-2xl font-bold border transition-all mt-4">
              + Yangi Vazifa
            </button>
          </div>

          <div class="md:col-span-3 row-span-1 bg-gradient-to-r from-amber-500/10 to-transparent p-8 rounded-[40px] border border-amber-500/20 flex items-center justify-between">
            <div class="flex items-center gap-6">
              <div class="w-12 h-12 bg-amber-500/20 rounded-2xl flex items-center justify-center text-amber-500 text-xl">🔔</div>
              <div>
                <h4 class="text-amber-600 font-black text-xs uppercase tracking-widest">Diqqat</h4>
                <p class="font-semibold">Ertaga yakuniy nazorat testi bor!</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </main>

    <div v-if="isModalOpen" class="fixed inset-0 bg-black/60 backdrop-blur-md flex items-center justify-center z-50">
      <div :class="isDarkMode ? 'bg-slate-900 border-slate-800' : 'bg-white border-slate-200'" class="border w-full max-w-md p-8 rounded-[32px] shadow-2xl relative">
        <h3 class="text-xl font-bold mb-2">Yangi vazifa qo'shish</h3>
        <input v-model="newTaskTitle" @keyup.enter="addTask" type="text" placeholder="Vazifa nomi..." :class="isDarkMode ? 'bg-slate-800 border-slate-700 text-slate-200' : 'bg-slate-50 border-slate-200 text-slate-800'" class="w-full border rounded-xl px-4 py-3.5 text-sm focus:outline-none focus:border-cyan-500/50 mb-6" autofocus/>
        <div class="flex justify-end gap-3">
          <button @click="closeModal" class="px-5 py-3 text-xs text-slate-400 font-semibold">Bekor qilish</button>
          <button @click="addTask" class="px-5 py-3 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-xs text-white font-bold">Qo'shish</button>
        </div>
      </div>
    </div>

  </div>
</template>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
body {
  margin: 0;
  padding: 0;
}
</style>

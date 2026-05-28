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

const schedule = ref([
  { id: 1, time: '09:00', subject: 'Sun\'iy Intellekt Asoslari', room: '402-A (Moodle)', progress: 85 },
  { id: 2, time: '10:30', subject: 'Veb Dasturlash (FastAPI)', room: '311-B (Laboratoriya)', progress: 40 }
]);

const notes = ref([
  { id: 1, text: "Ertangi FastAPI darsiga konspektni yakunlash" },
  { id: 2, text: "Kutubxonadan yangi AI kitobini olish kerak" }
]);
const newNoteText = ref('');

const addNote = () => {
  if (newNoteText.value.trim() !== '') {
    notes.value.push({
      id: Date.now(),
      text: newNoteText.value.trim()
    });
    newNoteText.value = '';
  }
};

const deleteNote = (id) => {
  notes.value = notes.value.filter(note => note.id !== id);
};

const tasks = ref([]);
const isModalOpen = ref(false);
const newTaskTitle = ref('');

const fetchTasks = async () => {
  try {
    const response = await API.get('/tasks');
    tasks.value = response.data;
  } catch (error) {
    console.log("Backend hozircha o'chiq, sinov uchun lokal ma'lumotlar yuklanmoqda.");
    tasks.value = [
      { id: 101, title: "Vue 3 darslarini to'liq tugatish", completed: false },
      { id: 102, title: "GitHub dabdabali README faylini tekshirish", completed: true }
    ];
  }
};

onMounted(() => {
 
  setInterval(() => {
    currentTime.value = new Date().toLocaleTimeString('uz-UZ', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  }, 1000);

  fetchTasks();
});

const toggleTask = async (task) => {
  task.completed = !task.completed;
  try {
    
    await API.put(`/tasks/${task.id}`, { completed: task.completed });
  } catch (err) {
    console.log("Holat lokal ravishda o'zgartirildi.");
  }
};

const openModal = () => { isModalOpen.value = true; };
const closeModal = () => { isModalOpen.value = false; newTaskTitle.value = ''; };

const addTask = async () => {
  if (newTaskTitle.value.trim() !== '') {
    const newTask = {
      id: Date.now(),
      title: newTaskTitle.value.trim(),
      completed: false
    };
    
    tasks.value.push(newTask);
    closeModal();

    try {
      
      await API.post('/tasks', newTask);
    } catch (err) {
      console.log("Vazifa vaqtincha lokal xotiraga qo'shildi.");
    }
  }
};
</script>

<template>
  <div :class="isDarkMode ? 'bg-[#080b14] text-slate-100' : 'bg-[#f4f6fa] text-slate-800'" class="min-h-screen flex font-sans transition-colors duration-500">
    
    <aside :class="isDarkMode ? 'bg-slate-900/50 border-slate-800/50' : 'bg-white border-slate-200/80 shadow-sm'" class="w-20 hidden lg:flex flex-col items-center py-8 border-r backdrop-blur-xl z-20 transition-colors duration-500">
      <div class="w-12 h-12 bg-gradient-to-br from-cyan-500 to-blue-600 rounded-2xl flex items-center justify-center shadow-lg mb-10">
        <span class="text-white font-black text-xl">S</span>
      </div>
      <nav :class="isDarkMode ? 'text-slate-500' : 'text-slate-400'" class="flex flex-col gap-8 text-xl">
        <i class="fas fa-th-large text-cyan-500 cursor-pointer"></i>
        <i class="fas fa-book hover:text-cyan-500 cursor-pointer transition-colors"></i>
        <i class="fas fa-tasks hover:text-cyan-500 cursor-pointer transition-colors"></i>
        <i class="fas fa-chart-line hover:text-cyan-500 cursor-pointer transition-colors"></i>
      </nav>
    </aside>

    <main class="flex-1 p-4 md:p-10 relative overflow-hidden">
      <div class="max-w-6xl mx-auto relative z-10">
        
        <header class="mb-12 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-6">
          <div>
            <div class="flex items-center gap-3 mb-2">
              <span class="px-3 py-1 bg-cyan-500/10 border border-cyan-500/20 rounded-full text-[10px] font-bold tracking-[0.2em] text-cyan-500 uppercase">Student Ecosystem v2.0</span>
            </div>
            <h1 :class="isDarkMode ? 'text-white' : 'text-slate-900'" class="text-4xl font-black tracking-tight">
              {{ greeting }}, <span class="bg-gradient-to-r from-cyan-500 to-blue-600 bg-clip-text text-transparent">Munisa</span>
            </h1>
          </div>
          
          <div class="flex items-center gap-4">
             <button @click="toggleTheme" :class="isDarkMode ? 'bg-slate-900 border-slate-800 text-yellow-400 hover:bg-slate-800' : 'bg-white border-slate-200 text-purple-600 hover:shadow-md'" class="p-3 rounded-2xl border shadow-sm flex items-center justify-center transition-all duration-300 active:scale-95">
               <i :class="isDarkMode ? 'fas fa-sun' : 'fas fa-moon'" class="text-lg"></i>
             </button>

             <div :class="isDarkMode ? 'bg-slate-900/40 border-slate-800/80' : 'bg-white border-slate-200/80 shadow-md'" class="backdrop-blur-md px-5 py-3 rounded-2xl border flex items-center gap-4">
               <div class="text-right">
                 <div class="text-[10px] uppercase tracking-widest text-slate-400 font-bold">API Status</div>
                 <div class="text-sm font-mono text-emerald-500">Connected</div>
               </div>
             </div>
          </div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 auto-rows-[110px]">
          
          <div :class="isDarkMode ? 'bg-slate-900/40 border-slate-800/50' : 'bg-white border-slate-200 shadow-md hover:shadow-xl'" class="md:col-span-3 row-span-3 p-8 rounded-[40px] border flex flex-col justify-between transition-all duration-500">
            <div>
              <div class="flex justify-between items-center mb-8">
                <h2 :class="isDarkMode ? 'text-white' : 'text-slate-900'" class="text-2xl font-bold flex items-center gap-4">
                  <div :class="isDarkMode ? 'bg-slate-800' : 'bg-slate-100'" class="p-3 rounded-2xl text-xl">📅</div> 
                  Dars Jadvali (Jonli)
                </h2>
              </div>
              
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div v-for="item in schedule" :key="item.id" :class="isDarkMode ? 'bg-slate-900 border-slate-800/50' : 'bg-slate-50 border-slate-200/60'" class="border p-5 rounded-3xl transition-all">
                  <span class="text-[10px] font-bold text-cyan-600 uppercase tracking-widest">{{ item.time }}</span>
                  <h3 :class="isDarkMode ? 'text-slate-200' : 'text-slate-800'" class="font-bold mt-2 mb-1 text-base">{{ item.subject }}</h3>
                  <p class="text-xs text-slate-400 mb-3">Xona: {{ item.room }}</p>
                  <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden">
                    <div :style="{ width: item.progress + '%' }" class="bg-cyan-500 h-full rounded-full"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div :class="isDarkMode ? 'bg-slate-900 border-slate-800/50' : 'bg-white border-slate-200 shadow-md hover:shadow-xl'" class="md:col-span-1 row-span-2 p-8 rounded-[40px] border flex flex-col justify-between items-center text-center transition-all duration-500">
            <span class="text-[10px] font-black text-slate-400 uppercase tracking-[0.3em]">System Time</span>
            <div :class="isDarkMode ? 'text-white' : 'text-slate-900'" class="text-4xl font-mono font-black tracking-tighter">{{ currentTime }}</div>
            <div :class="isDarkMode ? 'bg-slate-800/30 border-slate-800/50 text-slate-400' : 'bg-slate-100 border-slate-200 text-slate-600'" class="w-full py-3 rounded-2xl border text-[10px] font-bold">GMT +5 (TASHKENT)</div>
          </div>

          <div :class="isDarkMode ? 'bg-slate-900 border-slate-800/50' : 'bg-white border-slate-200 shadow-md'" class="p-6 rounded-[35px] border flex flex-col justify-center transition-all duration-500">
            <div class="text-[10px] font-bold text-cyan-600 uppercase mb-1">Talaba Reytingi</div>
            <div :class="isDarkMode ? 'text-white' : 'text-slate-900'" class="text-xl font-black">TOP #12</div>
          </div>

          <div :class="isDarkMode ? 'bg-slate-900/40 border-slate-800/50' : 'bg-white border-slate-200 shadow-md hover:shadow-xl'" class="md:col-span-2 row-span-2 p-6 rounded-[40px] border flex flex-col justify-between transition-all duration-500">
            <div>

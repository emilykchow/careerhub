<template>
  <nav class="bg-white border-b shadow-md px-4 py-2 flex items-center justify-between">
    <div class="text-xl font-bold text-gray-800">CareerHub</div>
    <div class="hidden md:flex space-x-6">
      <a href="#" class="text-gray-600 hover:text-blue-600">Job Search</a>
      <!-- <a href="#" class="text-gray-600 hover:text-blue-600">Blog</a> -->
      <a href="#" class="text-gray-600 hover:text-blue-600">Profile</a>
      <a href="#" class="text-gray-600 hover:text-blue-600">Sign Out</a>
    </div>
    <button @click="toggleMenu" class="md:hidden text-gray-600 focus:outline-none">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" stroke="currentColor">
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M4 6h16M4 12h16M4 18h16"
        />
      </svg>
    </button>
  </nav>

  <!-- Mobile Menu -->
  <div v-if="isOpen" class="md:hidden bg-white shadow-md px-4 pb-4 space-y-2">
    <a href="#" class="block text-gray-600 hover:text-blue-600">Job Search</a>
    <!-- <a href="#" class="block text-gray-600 hover:text-blue-600">Blog</a> -->
    <a href="#" class="block text-gray-600 hover:text-blue-600">Profile</a>
    <a href="#" class="block text-gray-600 hover:text-blue-600">Sign Out</a>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue'

const isOpen = ref(false)
const toggleMenu = () => {
  isOpen.value = !isOpen.value
}
</script>

<style scoped></style>

<script setup lang="ts"></script>

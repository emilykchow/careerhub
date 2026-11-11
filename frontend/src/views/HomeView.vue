<template>
  <main class="min-h-screen">
    <Hero />

    <div v-if="isLoading" class="text-center py-12">
      <p class="text-gray-400 animate-pulse">Checking authentication...</p>
    </div>

    <HighlightedJobs v-else-if="isAuthenticated" />
  </main>
</template>

<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'

import Hero from '@/components/Hero.vue'
import HighlightedJobs from '@/components/HighlightedJobs.vue'

const { isLoading, isAuthenticated } = useAuth0()
</script>

<template>
  <section class="mt-12">
    <h2 class="heading-2 mb-6">Highlighted Jobs</h2>

    <div v-if="isLoading">Loading highlighted jobs...</div>

    <div v-else-if="jobs.length">
      <!-- Your job cards go here -->
      <div v-for="job in jobs" :key="job.id">
        {{ job.title }}
      </div>
    </div>

    <p v-else class="text-content">No highlighted jobs available right now.</p>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface Job {
  id: number
  title: string
}

const jobs = ref<Job[]>([])
const isLoading = ref(false)

onMounted(async () => {
  // Fetch highlighted jobs from FastAPI
})
</script>

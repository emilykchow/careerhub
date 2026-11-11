<template>
  <div class="w-full rounded-border shadow-lg p-1 gap-1 responsive-flex">
    <div class="relative flex-1">
      <FontAwesomeIcon
        :icon="['fas', 'magnifying-glass']"
        class="absolute left-4 top-1/2 -translate-y-1/2 muted-text"
      />

      <input
        class="large-rounded-border bg-white default-text dark:default-text focus:border-accent-color focus:outline-none w-full pl-11"
        type="search"
        placeholder="Job Title, Skill, or Company"
        v-model="searchDescription"
      />
    </div>

    <input
      class="large-rounded-border bg-white default-text dark:default-text focus:border-accent-color focus:outline-none"
      type="text"
      placeholder="City, State or 'Remote'"
      v-model="searchLocation"
    />

    <button
      class="large-rounded-border default-text dark:default-text whitespace-nowrap hover-button"
      type="button"
      @click="handleSearch"
    >
      Search Jobs
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const searchDescription = ref('')
const searchLocation = ref('')

function handleSearch() {
  console.log('searchDescription', searchDescription.value)
  console.log('searchLocation', searchLocation.value)
}
</script>

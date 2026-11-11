<template>
  <button @click="toggleTheme">
    <span v-if="isDark" class="dark:text-content hover-text">
      <FontAwesomeIcon :icon="['fas', 'sun']" /> Light</span
    >
    <span v-else class="text-content hover-text">
      <FontAwesomeIcon :icon="['fas', 'moon']" /> Dark</span
    >
  </button>
</template>

<script lang="ts" setup>
import { useDark } from '@vueuse/core'

const isDark = useDark()

function toggleTheme() {
  isDark.value = !isDark.value
}
</script>

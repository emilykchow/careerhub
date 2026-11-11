<template>
  <p>profileview</p>
  <p v-if="isAuthenticated && user" class="text-content text-sm mb-3">
    {{ user }}
  </p>
</template>

<style scoped></style>

<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'

const { isAuthenticated, user } = useAuth0()
</script>

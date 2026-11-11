<template>
  <section class="text-center bg-banner dark:bg-banner page-spacing">
    <p v-if="isAuthenticated && user" class="text-content text-sm mb-3">
      Welcome back,
      {{ user.given_name || user.name }}!
    </p>

    <h1 class="heading">Find Your Next Career Step</h1>

    <p class="subheading">Discover possibilities</p>

    <div v-if="isAuthenticated && user" class="mt-6">
      <SearchBar />
    </div>
  </section>
</template>

<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'
import SearchBar from '@/components/Searchbar.vue'

const { isAuthenticated, user } = useAuth0()
</script>

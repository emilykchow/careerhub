<template>
  <nav
    class="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-700 shadow-md px-4 py-2 flex items-center justify-between"
  >
    <router-link to="/">
      <div class="text-xl font-bold text-gray-800 dark:text-white">CareerHub</div></router-link
    >

    <!-- desktop -->
    <div class="hidden md:flex items-center space-x-6">
      <ThemeToggle />

      <span v-if="isLoading" class="text-gray-400 text-sm">Loading...</span>

      <template v-else-if="isAuthenticated">
        <router-link to="/jobs" class="text-gray-600 dark:text-gray-300 hover:text-blue-600">
          Job Search
        </router-link>
        <router-link to="/profile" class="text-gray-600 dark:text-gray-300 hover:text-blue-600">
          Profile
        </router-link>
        <button
          @click="logout"
          class="text-gray-600 dark:text-gray-300 hover:text-blue-600 cursor-pointer"
        >
          Sign Out
        </button>
      </template>

      <template v-else>
        <button
          @click="login"
          class="large-rounded-border default-text dark:default-text whitespace-nowrap hover-button"
        >
          Sign In/Register
        </button>
      </template>
    </div>

    <!-- mopbile toggle -->
    <button
      @click="toggleNavbar"
      class="md:hidden text-gray-600 dark:text-gray-300 focus:outline-none cursor-pointer"
    >
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
  <div v-if="isOpen" class="md:hidden bg-white dark:bg-gray-900 shadow-md px-4 pb-4 space-y-2">
    <div class="py-2">
      <ThemeToggle />
    </div>

    <span v-if="isLoading" class="block text-gray-400 text-sm">Loading...</span>

    <template v-else-if="isAuthenticated">
      <router-link
        to="/jobs"
        class="block text-gray-600 dark:text-gray-300 hover:text-blue-600 py-1"
      >
        Job Search
      </router-link>
      <router-link
        to="/profile"
        class="block text-gray-600 dark:text-gray-300 hover:text-blue-600 py-1"
      >
        Profile
      </router-link>
      <button
        @click="logout"
        class="block w-full text-left text-gray-600 dark:text-gray-300 hover:text-blue-600 py-1"
      >
        Sign Out
      </button>
    </template>

    <template v-else>
      <button
        @click="login"
        class="block w-full text-center px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md text-sm transition-colors mt-2"
      >
        Sign In/Register
      </button>
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuth0 } from '@auth0/auth0-vue'
import ThemeToggle from './ThemeToggle.vue'

const isOpen = ref(false)
const { isLoading, isAuthenticated, loginWithRedirect, logout: auth0Logout } = useAuth0()

function toggleNavbar() {
  isOpen.value = !isOpen.value
}

const login = () => loginWithRedirect()

const logout = () => auth0Logout({ logoutParams: { returnTo: window.location.origin } })
</script>

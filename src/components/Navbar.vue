<template>
  <div :class="{
    'navbar2': $store.state.navbarVisible,
    'navbar': !$store.state.navbarVisible
  }">
    <div class="navbar__btns">
      <MyButton style="margin-left: 20px;" @click="$router.push('/'); scrollToTop()">Главная</MyButton>
      <my-button style="margin-left: 20px" @click="$router.push('/link'); scrollToTop()">ит курсы яндекса</my-button>
      <my-button style="margin-left: 20px" @click="$router.push('/choosecontent'); scrollToTop()">мади лучше</my-button>
      <my-button style="margin-left: 20px" @click="$router.push('/about'); scrollToTop()">окно</my-button>
      <button
        class="fa fa-paper-plane btn circle"
        style="margin-left: 16px; border-radius: 50%;"
        @click="showDialog">
        <slot></slot>
      </button>

      <div>
        <Transition name="dial">
          <PostTGForm v-model:show="$store.state.dialogVisible"></PostTGForm>
        </Transition>
      </div>
    </div>
  </div>
</template>

<script>
import MyButton from './UI/MyButton.vue';
import PostTGForm from "@/components/PostTGForm"

export default {
  data() {
    return {
    }
  },
  components: { MyButton, PostTGForm },
  methods: {
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    showDialog() {
      this.$store.commit('setDialogVisible', !this.$store.state.dialogVisible);
    },
    showNavbar() {
      this.$store.commit('setNavbarVisible', !this.$store.state.navbarVisible)
    },
  },
}
</script>

<style>
.myheader {
  position: fixed;
  height: 50px;
  width: 80%;
  top: 0;
  left: 0;
  background-color: #cc0000;
  color: white;
  font-family: 'Exo 2', sans-serif;
}

.navbar {
  background-color: lightgray;
  height: 50px;
  left: 15%;
  width: 70%;
  display: flex;
  align-items: center;
  padding: 0 15px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 5px;
  border-radius: 12px;
}

.navbar-sticky {
  position: fixed;
  top: 10px;
}

.navbar2 {
  position: fixed;
  top: 10px;
  position: fixed;
  background-color: lightgray;
  height: 50px;
  left: 16%;
  width: 68%;
  display: flex;
  align-items: center;
  padding: 0 15px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 5px;
  border-radius: 12px;
}

.navbar__btns {
  margin-left: auto;
  align-self: center;
}

.dial-enter-active,
.dial-leave-active {
  transition: opacity 0.5s ease;
}

.dial-enter-from,
.dial-leave-to {
  opacity: 0;
}

.bounce-enter-active {
  animation: bounce-in 0.5s;
}

.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}

@keyframes bounce-in {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.25);
  }

  100% {
    transform: scale(1);
  }
}
</style>

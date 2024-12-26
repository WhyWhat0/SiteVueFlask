<template>
  <div>
    <div>
    </div>

    <router-view>
    </router-view>
  </div>
</template>
<script>
import Navbar from "@/components/Navbar.vue";

export default {
  components: {
    Navbar
  }
}

</script>
<style>
@import '@/assets/css/style.css';
@import '@/assets/css/font-awesome.min.css';

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app {
  padding: 20px;
}

.image {
  background: url('@/assets/images/images/photo.jpg') no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>

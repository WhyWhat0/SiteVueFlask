<template>
    <!-- :style="{ backgroundImage: 'url(' + require('@/assets/images/images/photo.jpg') + ')', backgroundSize: 'cover' }" -->
    <div class="image"
        style="padding: 20px;">
        <Navbar></Navbar>
        <div v-intersection="showNavbar" class="observer"></div>
        <div class="dialog__content">
            <p></p>
        </div>
    </div>
</template>
<script>
import PostTGForm from "@/components/PostTGForm"
import Navbar from "@/components/Navbar"
export default {
    components: { PostTGForm, Navbar },
    data() {
        return {
        }
    },
    methods: {
        showNavbar() {
            this.$store.commit('setNavbarVisible', !this.$store.state.navbarVisible)
        },
    },
}
</script>
<style scoped>
.image {
    background: url('@/assets/images/images/fon_nerovnosti_svet_86951_300x168.jpg') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
}

.dialog__content {
    margin-left: auto;
    margin-right: auto;
    background: rgb(152, 23, 170);
    max-width: 70%;
    min-height: 2000px;
    padding: 20px;
    border-radius: 12px;
    /* margin: 0 auto;
	max-width: 970px;
	display: flex;
	background: none;
	border: 0;
	padding: 0 10px; */

}

.fixpos {
    position: fixed;
}

.v-enter-active,
.v-leave-active {
    transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}

.observer {
    height: 5px;
    width: 70%;
    margin: auto;
    /* background: white;
    border: 1px white; */

}
</style>